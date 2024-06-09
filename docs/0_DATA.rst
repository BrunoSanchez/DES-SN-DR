############################################
0 - DATA: Transient light curves from DES-SN
############################################


Overview
========

The light-curves are produced using the Scene Modelling Photometry pipeline described in `Brout et al. 2019a`_ and `Sanchez et al. 2024`_ (in prep.).

The full set of light-curves will be released after acceptance of `Sanchez et al. 2024`_ (in prep.) currently in collaboration wide review.

Content datasets
----------------

We provide light-curves in 4 different directories:

* ``DES-SN5YR_DESDR``: The SMP light curve dataset from DES 5YR
* ``DES-SN5YR_DESDR_specz``: The subset of SMP light curves with a host spectroscopic redshift
* ``DES-SN5YR_DESDR_HD``: Hubble Diagram 
* ``DES-SN5YR_DESDR_DIFFIMG``: The DIFFIMG, with PSF forced photometry over the entire dataset

Data Format
===========

The light curve files are provided in standard FITS_ format following the SNANA_ convention. 
The data is split in  ``HEAD.FITS`` files, just for the header information, and ``PHOT.FITS`` files containing the actual light curve measurements.

``HEAD`` file 
-------------

The ``HEAD`` file contains tabular information for all transient events and it stores the ``SNID`` that uniquely identifies the event.
This integer type variable can be used to find the event light-curve and it is shared among all files in DES-SN5YR.

.. table:: ``HEAD`` File Column variables

    +-------------------------------+------------------------------------------------------+
    | Variable name                 | Description                                          |
    +===============================+======================================================+
    | ``SNID``                      | integer or character ID                              |
    +-------------------------------+------------------------------------------------------+
    | ``FAKE``                      | 0=real data, 1=fake overlaid on image, 2=SNANA sim,  |
    +-------------------------------+------------------------------------------------------+
    | ``RA,DEC``                    | sky coordinates (degrees)                            |
    +-------------------------------+------------------------------------------------------+
    | ``SNTYPE``                    | integer type assigned by survey (e.g., SPEC type)    |
    +-------------------------------+------------------------------------------------------+
    | ``NOBS``                      | number of obs (all bands)                            |
    +-------------------------------+------------------------------------------------------+
    | ``PTROBS_MIN``                | pointer to 1st light curve obs in PHOT file          |
    +-------------------------------+------------------------------------------------------+
    | ``PTROBS_MAX``                | pointer to last light curve obs                      |
    +-------------------------------+------------------------------------------------------+
    | ``MWEBV[_ERR]``               | E(B-V) for Milky way                                 |
    +-------------------------------+------------------------------------------------------+
    | ``REDSHIFT_HELIO[_ERR]``      | best heliocentric redshift;                          |
    |                               | zSpec if available; else zPhot; else -9              |
    +-------------------------------+------------------------------------------------------+
    | ``REDSHIFT_FINAL[_ERR]``      | best CMB redshift (no VPEC correction)               |
    +-------------------------------+------------------------------------------------------+
    | ``VPEC_[ERR]``                | pec velocity (km/sec) and error on correction        |
    +-------------------------------+------------------------------------------------------+
    | ``PEAKMJD``                   | approx PEAKMJD; useful to init light curve fit       |
    +-------------------------------+------------------------------------------------------+
    | ``MJD_TRIGGER``               | MJD when survey trigger is satisfied                 |
    +-------------------------------+------------------------------------------------------+
    | ``MJD_DETECT_FIRST``          | MJD of first detection                               |
    +-------------------------------+------------------------------------------------------+
    | ``MJD_DETECT_LAST``           | MJD of last detection                                |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_SB_FLUXCAL_[band]`` | Surface brightness mag at SN location                |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_NMATCH``            | number of host matches with DDLR < 4                 |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_NMATCH2``           | number of host matches with DDLR < 7                 |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_OBJID``             | integer id of host (long long int)                   |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_RA``                | R.A. (deg) for center of host                        |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_DEC``               | declination (deg) for center of host                 |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_SNSEP``             | transient-host separation, arcsec                    |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_DDLR``              | SN-host sep in distance-light-radii (d_DLR)          |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_SPECZ[_ERR]``       | zSpec of host (-9 -> not available)                  |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_PHOTOZ[_ERR]``      | zphot (mean of PDF); -9 -> not available             |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_ZPHOT_Q[PPP]``      | redshift containing PPP percent of zPDF prob         |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_LOGMASS[_ERR]``     | logmass and error                                    |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_LOGSFR[_ERR]``      | log(star formation rate) and error                   |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_MAG_[band]``        | Host Magnitudes for band=u,g,r,i,z,Y                 |
    +-------------------------------+------------------------------------------------------+
    | ``HOSTGAL_MAGERR_[band]``     | Host magnitude error.                                |
    +-------------------------------+------------------------------------------------------+
    | **Additional variables for simulated data.**                                         |
    +-------------------------------+------------------------------------------------------+
    | ``SIM_TYPE_INDEX``            | true integer transient type (e.g., 1 for SNIa)       |
    +-------------------------------+------------------------------------------------------+
    | ``SIM_[SSS]``                 | true sim property SSS                                |
    +-------------------------------+------------------------------------------------------+

.. note:: ``HOSTGAL_`` quantities
    
    - Each ``HOSTGAL_{}`` has ``HOSTGAL2_{}`` for 2nd host-match; 
    - -999 indicates no 2nd host; else values are filled.
    - First listed host has smallest DDLR and may not be the true host   

.. note:: Using data from the `HOSTGAL` quantities:

    Please cite `Kelsey et al. 2023`_ and `Wiseman et al. 2020`_.



``PHOT`` file
-------------

The ``PHOT`` file contains the light curve measurements, with all written sequentially to the ``PHOT``-tables, and pointers in the ``HEAD`` file (see ``PTROBS_MIN`` and ``PTROBS_MAX``) are used to select the appropriate rows from the PHOT table. To help catch pointer mistakes, ``MJD = -777`` is written after each light curve to clearly indicate the end of it.

.. table:: ``PHOT`` file variable columns

    
    +-------------------------------+------------------------------------------------------+
    | Variable name                 | Description                                          |
    +===============================+======================================================+
    | ``MJD``                       | Float, Modified Julian Day (MJD).                    |
    +-------------------------------+------------------------------------------------------+
    | ``BAND``                      | String indicating DES bandpass filter. (g, r, i, z)  |
    +-------------------------------+------------------------------------------------------+
    | ``CCDNUM``                    | CCD or detector number                               |
    +-------------------------------+------------------------------------------------------+
    | ``IMGNUM``                    | DES Image number identifier; e.g. exposure number,   |
    |                               | or visit id                                          |
    +-------------------------------+------------------------------------------------------+
    | ``FIELD``                     | DES-SN survey field name. (SHALLOW, DEEP)            |
    |                               | (E1, E2, E3, S1, S2, X1, X2, X3, C1, C2)             |
    +-------------------------------+------------------------------------------------------+
    | ``PHOTFLAG``                  | bit-mask of information (check data README)          |
    +-------------------------------+------------------------------------------------------+
    | ``PHOTPROB``                  | float metric; e.g, RealBogus score, chi2, ...        |
    +-------------------------------+------------------------------------------------------+
    | ``FLUXCAL``                   | calibrated flux : mag = 27.5 - 2.5*log10(FLUXCAL)    |
    +-------------------------------+------------------------------------------------------+
    | ``FLUXCALERR``                | Poisson uncertainty on FLUXCAL; sky+galaxy+source    |
    +-------------------------------+------------------------------------------------------+
    | ``PSF_SIG1``                  | PSF Gauss sigma, pixels                              |
    +-------------------------------+------------------------------------------------------+
    | ``SKY_SIG``                   | sky noise (ADU/pixel)                                |
    +-------------------------------+------------------------------------------------------+
    | ``SKY_SIG_T``                 | template sky noise (for DIFFIMG, not for SMP)        |
    +-------------------------------+------------------------------------------------------+
    | ``ZEROPT``                    | image zero point                                     |
    +-------------------------------+------------------------------------------------------+
    | ``GAIN``                      | N_photoelectron/ADU                                  |
    +-------------------------------+------------------------------------------------------+
    | ``XPIX``                      | x-locaton on CCD (pixels)                            |
    +-------------------------------+------------------------------------------------------+
    | ``YPIX``                      | y-locaton on CCD (pixels)                            |
    +-------------------------------+------------------------------------------------------+
    | **Additional variables for simulated data.**                                         |
    +-------------------------------+------------------------------------------------------+
    | ``SIM_MAGOBS``                | true model mag                                       |
    +-------------------------------+------------------------------------------------------+

...........

.. include:: _static/links.rst

