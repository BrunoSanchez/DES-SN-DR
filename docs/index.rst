========================================
Dark Energy Survey Supernova Program 5YR
========================================

.. topic:: The DES Supernova Program 5-year Data release.
   
   The Dark Energy Survey Supernova Program (DES-SN) consisted on 5 years of observations using the Dark Energy Survey instrument, finding Type Ia Supernovae up to cosmological redshifts :math:`z>1.1`.

   This is the **full public data release** of DES-SN (DES-SN5YR) containing all data products used to compute the cosmological result from the full 5 years of photometrically classified supernovae (SNe) combined with a sample of low-redshift SNe. 

   **Instructions to download the full data release and its accompanying python utility package can be found below.**


.. Overview of DES-SN 5-year Data release 
.. ======================================

.. 0 - DATA
..   Transient light curves from DES-SN, measured with DIFFIMG and SMP photometry pipelines, and also including SALT3 model fitted curves.

.. 1 - Simulations
..   DES mocks used for testing and validation of the DES cosmological pipeline. 

.. 2 - LCFIT_MODEL
..   The trained   used in DES-SN5YR cosmological analysis.

.. 3 - CLASSIFICATION
..   Classification probabilities for the DES SNe used in the DES-SN5YR cosmological analysis.

.. 4 - DISTANCES_COVMAT
..   Distances and Hubble Diagram, global SN sample parameters :math:`\alpha, \beta, \gamma, M_0`, and Statistical and Systematic covariance matrices.

.. 5 - Cosmology
..   Likelihood used, and obtained chains from CosmoMC_  and emcee_ 

.. 6 - DCR_CORRECTIONS
..   The Wavelength-dependent photometrical corrections to our observed transients

.. 7 - PIPPIN_FILES
..   The PIPPIN_ input files for reproducing the cosmological SNIa analysis. 
  

Detailed description of release Contents
========================================

.. toctree::
  :maxdepth: 2

  0_DATA
  1_SIMULATIONS
  2_LCFIT_MODEL
  3_CLASSIFICATION
  4_DISTANCES_COVMAT
  5_COSMOLOGY
  6_DCR_CORRECTIONS
  7_PIPPIN_FILES


The DES-SN5YR utility package 
=============================

We release basic utilities for using this data. To install this package simply clone this github repo and install locally. This is also one way to obtain the full dataset.

Installation
------------

.. code-block:: bash

  git clone https://github.com/BrunoSanchez/DES-SN-DR.git
  cd DES-SN-DR
  python -m pip install -e .


Acquiring the Full Release dataset
----------------------------------

.. code-block:: bash
   
  downloaddessndr <dest_dir>


After this, in order to find your dataset globally in your system you should set up the environment variables

.. code-block:: bash

  export DES5YRDR_DATA_ROOT='<dest_dir>'
  export DES5YRDR_DATA='<dest_dir>/DES-SN5YR'


Examples of use of this Data Release
====================================

We provide some Jupyter Notebooks with examples to load and read this data, and produce some example figures. These are in the ``docs/tutorial`` directory, or in the Tutorial section on [readthedocs](https://desdrtest.readthedocs.io).

This package provides some utilities that can be imported in a Python session as


.. code-block:: python

  >>> from dessndr import utils, data
  >>> phot = utils.PhotFITS(os.path.join(data.DES5YRDR_DATA, '0_DATA/DES-SN5YR_DES'))
  >>> lc = phot.get_lc(phot.cid_recs[0]))


DES 5YR Tutorials 
-----------------

.. toctree:: 
   :maxdepth: 1

   tutorial/01-load_data
   tutorial/02-load_lcplot
   tutorial/03-Classification
   tutorial/04-HubbleDiagram
   tutorial/05-LambdaDependentCorrections
   tutorial/06-Cosmology-DESSN5YR_Flat_wCDM


Used Public cosmology Codes  
===========================
 - PIPPIN_
 - CosmoSIS_
 - MontePython_
 - Cobaya_
 - CosmoMC_ 
 - emcee_ 

Using this Data 
===============

Please always obtain the data from our official download links. 

.. note:: Version tags
  Always Check the tag versions to verify you are using the latest version of our data files.


Download the .zip from Zenodo
-----------------------------

Download directly from our Zenodo release page (click in the badge):

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.12720778.svg
  :target: https://doi.org/10.5281/zenodo.12720778



Or get it straight from a terminal with: 


.. code-block:: bash

  wget https://zenodo.org/records/12720778/files/DES-SN5YR-1.2.zip?download=1


Clone DES-SN5YR Git repository
------------------------------

.. code-block:: bash

  git clone https://github.com/des-science/DES-SN5YR
  
Aknowledge authorship of DES-SN5YR
==================================

.. note:: Please cite these references in order to give credit to the rightful authors.


 - `DES Collaboration 2024`_ - The Dark Energy Survey: Cosmology Results With ~1500 New High-redshift Type Ia Supernovae Using The Full 5-year Dataset 
 - `Vincenzi et al. 2024`_ - The Dark Energy Survey Supernova Program: Cosmological Analysis and Systematic Uncertainties 
 - `Sanchez et al. 2024`_ - Light curves and data release for the full Dark Energy Survey Supernova Program
 - `Möller et al. 2024`_ - The Dark Energy Survey 5-year photometrically classified type Ia supernovae without host-galaxy redshifts 
 - `Lee & Acevedo et al. 2023`_ - The Dark Energy Survey Supernova Program: Corrections on Photometry Due to Wavelength-dependent Atmospheric Effects 
 - `Kelsey et al. 2023`_ - Concerning colour: The effect of environment on type Ia supernova colour in the dark energy survey
 - `Wiseman et al. 2020`_ - Supernova host galaxies in the dark energy survey: I. Deep coadds, photometry, and stellar masses


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`


.. include:: _static/links.rst


