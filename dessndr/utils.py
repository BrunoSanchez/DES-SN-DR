#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  utils.py
#
#  Copyright 2022 bruno <bruno.sanchez@duke.edu>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import gzip
import logging

import numpy as np
import pandas as pd

from astropy.table import Table


logger = logging.getLogger(__name__)

# =============================================================================
# Reading functions
# =============================================================================

def read_lcplot(filename):
    """Reads a LCPLOT file. It takes a path and returns a table.

    Parameters
    ----------
    - filename: data filename

    Returns
    -------
    - table: Pandas.DataFrame, containg data
    """

    config = {
        'sep': '\s+',
        'comment': '#'
    }

    if filename.endswith('.gz'):
        config['compression'] = 'gzip'
    
    return pd.read_csv(filename,  **config)



def open_fitres(filename):
    """Reads a FITRES file. It takes a path and returns a table.

    Parameters
    ----------
    - filename: data filename

    Returns
    -------
    - table: Pandas.DataFrame, containg data
    """
    names, startrow = get_names_rows(filename)
    config = {
        'header': None,
        'skiprows': startrow,
        'names': names,
        'delim_whitespace': True,
    }
    return pd.read_csv(filename,  **config)


def get_names_rows(filename):
    """Takes in a FITRES file and outputs the variable names and startline
    for the data

    Parameters
    ----------
    - filename: data filename

    Returns
    -------
    - names: column names for table
    - startrow: starting row
    """

    with open(filename) as fp:
        comment = False
        for i, line in enumerate(fp):
            if line.startswith('# '):
                comment = True
                line = line.lstrip('# ')
            if line.startswith('VARNAMES:'):
                line = line.replace(',', ' ')
                line = line.replace('\n', '')
                names = line.split()
            elif line.startswith('SN') and not comment:
                startrow = i
                break

    return names, startrow


def read_dump(filename):
    names, startrow = get_names_rows(filename)
    config = {
        'header': None,
        'skiprows': startrow,
        'names': names,
        'delim_whitespace': True,
        'skip_blank_lines': True,
        'error_bad_lines': False,
        'comment': '#'
    }
    return pd.read_csv(filename, **config)


def read_alldump(filename):
    with open(filename) as f:
        lines = f.readlines()
    rows = []
    for aline in lines:
        if 'NVAR' in aline:
            nvar = int(aline.strip('NVAR:'))
        elif 'VARNAMES:' in aline:
            row = aline.strip('VARNAMES:')
            colnames = row.split()
        elif 'SN:' in aline:
            row = aline.strip('SN:').split()
            datarow = {}
            for data, col in zip(row, colnames):
                datarow[col] = data
            rows.append(datarow)
    return pd.DataFrame(rows)


def read_lc_merge(filepath):
    tab = read_alldump(filepath)
    types = {
        'CID':        'str',
        'ZCMB':       'float',
        'SIM_PKMJD':  'float',
        'SIM_c':      'float',
        'SIM_x1':     'float',
        'SIM_mB':     'float',
        'FOUND_FLAG': 'int',
    }
    return tab.astype(types, copy=True)


def get_names_rows_lcdat(filename):
    """Takes in a DAT file and outputs the variable names and startline
    for the data

    Parameters
    ----------
    - filename: data filename

    Returns
    -------
    - names: column names for table
    - startrow: starting row
    """
    if filename.endswith('.gz'):
        open_function = lambda ff: gzip.open(ff, mode='rt')
    else:
        open_function = open
    with open_function(filename) as fp:
        for i, line in enumerate(fp):
            if line.startswith('VARNAMES:') or line.startswith('VARLIST:'):
                line = line.replace(',', ' ')
                line = line.replace('\n', '')
                names = line.split()
            elif line.startswith('OBS:'):
                startrow = i
                break

    return names, startrow


def open_lcdat(filename):
    """Reads a DAT file. It takes a path and returns a table.

    Parameters
    ----------
    - filename: data filename

    Returns
    -------
    - table: Pandas.DataFrame, containg data
    """
    names, startrow = get_names_rows_lcdat(filename)
    config = {
        'header': None,
        'skiprows': startrow,
        'names': names,
        'delim_whitespace': True,
    }
    return pd.read_csv(filename,  **config)


class PhotFITS(object):
    """Class for reading SNANA photometry tables in FITS format

    Parameters
    ----------
    - version: [str] data version name. It is the prefix to the _HEAD and _PHOT
                filenames

    Attributes
    ----------
    - dump_head: [astropy.table.Table] the header of photometry table
    - dump_phot: [astropy.table.Table] the photometry table data
    - head_df: [pandas.DataFrame] the header in Pandas format
    - phot_df: [pandas.DataFrame] the photometry table in Pandas format
    - cid_recs: [numpy.ndarray] the array of CIDs present in the data

    Methods
    -------
    - get_lc(cid: str): [None, pandas.DataFrame] returns a lightcurve
    - phot_table: -property- [pandas.DataFrame] returns the photometry df
    - get_lcs(cidlist: list, tuple): [pandas.DataFrame] returns a
            data frame with the photometry for a list of cids

    """
    def __init__(self, version):

        self.dump_head = Table.read(f'{version}_HEAD.FITS.gz')
        self.dump_phot = Table.read(f'{version}_PHOT.FITS.gz')

        self.head_df = self.dump_head.to_pandas()
        self.head_df['SNID'] = self.head_df['SNID'].astype(int)

        self.phot_df = self.dump_phot.to_pandas()
        self.phot_df['BAND'] = self.phot_df.BAND.astype(str)
        self.phot_df['FIELD'] = self.phot_df.FIELD.astype(str)
        self.phot_df['MAG'] = -2.5 * np.log10(self.phot_df.FLUXCAL) + 27.5

        self.cid_recs = np.array(self.head_df.SNID.values, dtype=int)

    def get_lc(self, cid):
        if cid in self.cid_recs:
            imin = self.head_df.PTROBS_MIN.values[self.cid_recs==cid][0]
            imax = self.head_df.PTROBS_MAX.values[self.cid_recs==cid][0]

            lc = self.phot_df[imin:imax].copy()
        else:
            logger.info(f"""CID {cid} not in records""")
            return None
        return lc

    @property
    def phot_table(self):
        return self.phot_df

    def get_lcs(self, cidlist: list):
        lcs = []
        for acid in cidlist:
            anlc = self.get_lc(acid)
            if anlc is not None:
                anlc['CID'] = anlc
                lcs.append(anlc)
            else:
                continue

        try:
            lcs = pd.concat(lcs)
            return lcs
        except ValueError:
            return None

    def query_cids(self, cids):
        if not isinstance(cids, list):
            cids = [cids]
    
        query_result = {}
        for cid in cids:
            if cid in self.cid_recs:
                query_result[cid] = dict(
                    self.head_df.iloc[np.where(self.cid_recs==cid)]
                )
            
        return query_result 
    