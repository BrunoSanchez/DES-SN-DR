#######################################
5 - COSMOLOGY: SN likelihood and chains
#######################################

Overview
========

We release the `CosmoSIS`_ sampling chains for DES-SN5YR, and the likelihood used.


Likelihood
==========

The Likelihood file is ``SN_only_cosmosis_likelihood.py``
Use this with distances and cov matrixes in folder ``4_DISTANCES_COVMAT``.

Chains
======

The ``chains`` folder includes all the *cosmosis/emcee* chains (see file header) for the four cosmological models tested in our analysis:

- Flat :math:`\Lambda\rm{CDM}` (``flcdm`` sub-folder)
- :math:`\Lambda\rm{CDM}` (``lcdm`` sub-folder)
- Flat :math:`w\rm{CDM}`(``wlcdm`` sub-folder)
- Flat :math:`w_0 w_a \rm{CDM}` (``w0wacdm`` sub-folder)
  
And for the different probes combination

- DES-SN only
- DES-SN + CMB (from Planck Collaboration et al. 2020)
- DES-SN + BAO and 3x2pt
- DES-SN + BAO and 3x2pt + CMB

...........

.. include:: _static/links.rst

