###############################################
1 - SIMULATIONS: The DES-SN5YR mock simulations
###############################################

Overview
========

We present 25 mocks of the DES-SN5YR sample.
These simulations have been mainly used for testing and validation of our cosmological analysis.


Simulation parameters
---------------------

.. table:: Input Cosmology

    +-----------------------------+----------------+
    | Parameter                   |          Value |
    +=============================+================+
    | :math:`H_0`                 |           70.0 |
    +-----------------------------+----------------+
    | :math:`\Omega_{\Lambda}`    |          0.685 |
    +-----------------------------+----------------+
    | :math:`\Omega_{M}`          |          0.315 |
    +-----------------------------+----------------+
    | :math:`w_0`                 |           -1.0 |
    +-----------------------------+----------------+
    | :math:`w_a`                 |              0 |
    +-----------------------------+----------------+


Efficiencies and selection Functions
------------------------------------

- DES detection efficiency from `Kessler et al. 2019`_.
- DES spectroscopic redshift efficiency from `Vincenzi et al. 2022`_.
- Host Library was built from DES deep coadds by `Qu et al. 2024`_.

Simulation contents released 
============================

The folders ``SNIa_SIMULATIONS`` contain SNe Ia:

- SED model is the SALT3 model provided in ``2_LCFIT_MODEL``
- Details on the SN Ia rates, intrinsic scatter and populations are in Sec. 4.2 of `Vincenzi et al. 2024`_.

The folders ``SNnonIa_SIMULATIONS`` contain non Ia SNe generated using the templates by `Vincenzi et al. 2019`_.

- SED model are presented by `Vincenzi et al. 2019`_ and `Vincenzi et al. 2022`_.
- Details on the SN Ia rates, intrinsic scatter and populations are in Sec. 4.3 of `Vincenzi et al. 2024`_.


.. note:: The data format of the simulations is identical to the format given in the :doc:`0-DATA <0_DATA>` page.

Reproduce the simulations
=========================

The PIPPIN_ input files used to generate the mocks are available in the folder: ``7_PIPPIN_FILES`` (:file:`D5yr_sim_nominal.yml`).
All the auxiliary files needed to generate the simulations are also available within `SNANA ROOT Data`_.


References
----------

The main references that describe the assumptions and inputs used to generate these mocks are presented by `Kessler et al. 2019`_, `Vincenzi et al. 2022`_, `Qu et al. 2024`_, `Vincenzi et al. 2024`_.

...........

.. include:: _static/links.rst
