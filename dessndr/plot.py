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
from copy import copy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


oldParams = copy(plt.rcParams)
#print(oldParams)

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 16}

matplotlib.rc('font', **font)

FLTCOLORS = {}
FLTCOLORS['u'] = '#ac53b9ff'
FLTCOLORS['g'] = '#3995e4ff'
FLTCOLORS['r'] = '#51bc64ff'
FLTCOLORS['i'] = '#2a7f13ff'
FLTCOLORS['z'] = '#ffc627ff'
FLTCOLORS['y'] = '#e43939ff'

FLTLIST = ('g', 'r', 'i', 'z')



def plot_sn_light_curve(df, 
        mjd_col='MJD', flux_col='FLUXCAL', flux_err_col='FLUXCALERR', 
        band_col='BAND', ax=None, CID=None, 
        *args, **kwargs
    ):
    """
    Plots a Supernova light curve from a DataFrame with error bars.

    Parameters:
    - df: pandas DataFrame containing the photometry data
    - mjd_col: str, name of the column for Modified Julian Date (default: 'MJD')
    - flux_col: str, name of the column for Flux (default: 'FLUX')
    - flux_err_col: str, name of the column for Flux Uncertainty (default: 'FLUX_ERR')
    - band_col: str, name of the column for Band (default: 'BAND')
    - CID: int, candidate ID in DES

    Returns:
    - A plot of the light curve with error bars.
    """
    if ax is None:
        fig, ax = plt.subplots(*args, **kwargs)

    # Group the data by the BAND column
    grouped = df.groupby(band_col)

    # Loop through each group (each band) and plot the light curve with error bars
    for band, group in grouped:
        color = FLTCOLORS[band.strip()]
        ax.errorbar(
            group[mjd_col], group[flux_col], 
            yerr=group[flux_err_col], fmt='o', linestyle='', color=color,
            label=f'{band}')
    
    # Set plot labels and title
    ax.set_xlabel('MJD')
    ax.set_ylabel('Flux')
    suffix = ''
    if CID is not None: 
        suffix = "CID: %s"%CID 
    
    ax.set_title('Supernova Light Curve'+suffix)
    plt.legend()
    plt.tight_layout()
    return fig, ax


def plot_lcplot(lcplot_data, cid=None):
    if cid is None:
        raise ValueError

    fig, ax = plt.subplots(figsize=(8, 6))
    for aband in FLTLIST:
        df = lcplot_data[lcplot_data.SNID==cid]
        df_band = df[df.BAND==aband]
        df_band_data = df_band[df_band.DATA_MODEL==1]
        df_band_model = df_band[df_band.DATA_MODEL==0]
        ax.errorbar(
            df_band_data.PHASE, df_band_data.FLUXCAL, df_band_data.FLUXCALERR, 
            marker='o', color=FLTCOLORS[aband], label=aband+' DATA')
        ax.plot(df_band_model.PHASE, df_band_model.FLUXCAL, 
                '--', color=FLTCOLORS[aband],label=aband+' MODEL')
    
    ax.set_title(f'SN CID: {cid} | chi2/dof={np.sum(df[df.DATA_MODEL==1].CHI2)/np.sum(df.DATA_MODEL==1):.3f}') 
    ax.set_xlim(-25, 75)
    yscale = (np.min(df.FLUXCAL-2*df.FLUXCALERR.mean()), 
              np.max(df.FLUXCAL+2*df.FLUXCALERR.mean()))
    ax.set_ylim(*yscale)
    ax.set_xlabel('PHASE')
    ax.set_ylabel('FLUXCAL')
    plt.legend()
    plt.tight_layout()
    return fig, ax
