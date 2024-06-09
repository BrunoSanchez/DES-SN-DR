#################################################################
6 - DCR_CORRECTIONS: Wavelength-dependent Atmospheric Corrections
#################################################################

Overview
========

We release the photometric corrections due to wavelength-dependent atmospheric effects (DCR and wavelength-dependent seeing) applied to our SNe Ia  (`Lee & Acevedo et al. 2023`_).

For the ``SHAPE`` effect, the flux ratio values in the look-up tables can be translated to the ``SHAPE`` magnitude corrections. 
For the ``COORD`` effect, the user can start from the altitude shifts vs. `g-i` values of stars and calculate the ``COORD`` magnitude corrections. Please calculate the ``MAGCOR`` values following the tutorial and use them (not the table ``MAGCOR_COORD`` values) for the ``COORD`` magnitude corrections. 

More details on the conversion from the relevant tables to the SHAPE and COORD magnitude corrections can be found in the :doc:`../tutorial/05-LambdaDependentCorrections`

Data Format
===========

For ``COORD`` & ``SHAPE``
-------------------------

- Magnitude Corrections table: ``DCRADJ_MAGCOR_v220929.csv`` contains all the magnitude corrections (both COORD and SHAPE) to be added to the uncorrected (SALT2 or SALT3) magnitudes

..

- ``CID`` - Candidate ID
- ``EXPNUM`` - Exposure Number
- ``MAG_MODEL_g`` - Model `g` band magnitude
- ``MAG_MODEL_i`` - Model `i` band magnitude
- ``AIRMASS`` - Air Mass
- ``PSF_FWHM_ASEC`` - PSF FWHM in arcseconds
- ``MAGCOR_COORD`` - Magnitude corrections (COORD) to be added to the uncorrected magnitudes
- ``MAGCOR_SHAPE`` - Magnitude corrections (SHAPE) to be added to the uncorrected magnitudes
- ``RADEG`` & ``DECDEG`` - Right Acension (RA) and Declination (DEC) of SN in the given exposure in degrees
- ``BAND`` - Band (filter) of the observation
- ``SNR`` - S/N of the SN
- ``dRA`` & ``dDEC`` - DCR altitude shift converted to RA and DEC coordinates
- ``ddRA`` & ``ddDEC`` - DCR altitude shift in RA and DEC with respect to the S/N weighted average coordinate
- ``ADJOFF`` - Total offset with respect to the S/N weighted average coordinate

For COORD only
--------------

- DCR Coordinate table: ``DCR_dictionary.csv`` contains the altitude shifts vs. `g-i` magnitude
  
..

- ``SLOPE_ALT`` - slope of altitude `Alt` vs. `g-i` color
- ``YINT_ALT`` - y-intercept of altitude `Alt` vs. `g-i`` color

..

- ``mmag_vs_fracpsf_Moffat3.txt`` contains the magnitude offset by the astrometric offset in fractions of the PSF size for a Moffat PSF.
- ``DCR_coord_table.csv`` contains the ``MAGCOR_DCR`` (COORD) by CID and exposure number but is not necessary for the calculations. 


For SHAPE only
--------------

- Wavelength-dependent corrections lookup table: 
 - Flux ratio values for the `g` and `r` bands by `g-i`, Air Mass, and PSF FWHM.
  - ``flux_ratio_values_g_table_DCR_shape.npy`` 
  - ``flux_ratio_values_r_table_DCR_shape.npy``
 - `g-i` values, Air MAss, and PSF FWHM (in arcseconds). 
  - ``g_table_DCR_shape_xyz_columns.npy``
  - ``r_table_DCR_shape_xyz_columns.npy``

...........

.. include:: _static/links.rst

