# DES-SN 5YR DR Associated Software package
[![Documentation Status](https://readthedocs.org/projects/des-sn-dr/badge/?version=latest)](https://des-sn-dr.readthedocs.io/en/latest/?badge=latest)

## The Dark Energy Survey Supernova 5YR Cosmological analysis and Data Release

This repo contains the documentation and associated software package from the Dark Energy Survey Supernova Program 5-Year results.

Please check our [ReadTheDocs](https://des-sn-dr.readthedocs.org) for all details on contents and ancillary data description.



## The DES-SN5YR utility package 

We release basic utilities for using this data. To install this package simply clone this github repo and install locally. This is also one way to obtain the full dataset.

### Installation

```console
$ git clone https://github.com/BrunoSanchez/DESSN5YR_TESTDR.git
$ cd DESSN5YR_TESTDR
$ pip install -e .
```
<!-- $ git clone https://github.com/des-science/DES-SN5YR_DataRelease.git -->

### Acquiring the Full Release dataset

```console
$ downloaddessndr <dest_dir>
```

After this, in order to find your dataset globally in your system you should set up the environment variables

```console
$ export DES5YRDR_DATA_ROOT='<dest_dir>'
$ export DES5YRDR_DATA='<dest_dir>/DES-SN5YR'
```

## Contents of the Data Release

 - **0_DATA**: The light-curves produced using the Scene Modelling Photometry pipeline descibre in Brout et al. 2019a and Sanchez et al. 2024 (in prep.).

 - **1_SIMULATIONS:** DES Monte Carlo simulation mocks used for testing and validation of the DES cosmological pipeline.

 - **2_LCFIT_MODEL:** The SALT3 model used for the Nominal DES-SN5YR cosmological analysis

 - **3_CLASSIFICATION:** The classification probabilities for the 1635 DES SNe.
  
 - **4_DISTANCES_COVMAT:**
   - Data vector with redshifts (zHD) and distance modulii (MU) for the 1829 SNe (194 low-z + 1635 DES).
   - STAT only covariance matrix
   - STAT+SYST covariance matrix
   - Single systematic covariance matrices 

 - **7_PIPPIN_FILES:** This folder includes the pippin input files needed to reproduce DES simulations and cosmological analysis.

### Examples of use of this Data Release

We provide some Jupyter Notebooks with examples to load and read this data, and produce some example figures. These are in the ``docs/tutorial`` directory, or in the Tutorial section on [ReadTheDocs](https://des-sn-dr.readthedocs.org).

This package provides some utilities that can be imported in a Python session as


```python
>>> from dessndr import utils, data
>>> phot = utils.PhotFITS(os.path.join(data.DES5YRDR_DATA, '0_DATA/DES-SN5YR_DES'))
>>> lc = phot.get_lc(phot.cid_recs[0]))
```


## References and citing this work

> The Dark Energy Survey: Cosmology Results With ~1500 New High-redshift Type Ia Supernovae Using The Full 5-year Dataset. JOURNAL NUMBER. [DES Collaboration (2024).](https://ui.adsabs.harvard.edu/link_gateway/2024arXiv240102929D/doi:10.48550/arXiv.2401.02929)

> The Dark Energy Survey Supernova Program: Cosmological Analysis and Systematic Uncertainties JOURNAL NUMBER. [Vincenzi et al (2024).](https://ui.adsabs.harvard.edu/link_gateway/2024arXiv240102945V/doi:10.48550/arXiv.2401.02945) 

> Light curve and ancillary data release for the full Dark Energy Survey Supernova Program. JOURNAL NUMBER. [Sánchez et al (2024)](...)

**Please, for the full documentation refer to [ReadTheDocs](https://des-sn-dr.readthedocs.org).**
