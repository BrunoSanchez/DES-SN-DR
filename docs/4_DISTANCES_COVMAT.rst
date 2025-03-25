######################################################
4 - DISTANCES_COVMAT: Distances and Covariance matrix
######################################################

Overview
========
We provide two Hubble diagrams, one including only the essential information for cosmology (``DES-SN5YR_HD.csv``) and one including additional metadata (``DES-SN5YR_HD+MetaData.csv``).

Using the metadata, SN distances are calculated as:

:math:`\mu=-2.5 \log_{10} (x_0) + \alpha x_1 - \beta c \pm \gamma/2 - \rm{biasCor}_\mu - M_{0\mathrm{avg}}`

Hubble Diagram
==============

The released tables include parameters for the SNIa SALT3 fit, and additional metadata as well.

.. note:: Additional parameter availability

    The distance information is provided only for the events that fall into our Hubble Diagram, and thus only these events have additional parameters (such as SALT3 fitted parameters) in the release.

Data Format
-----------

``DES-SN5YR_HD.csv`` Column definitions

- ``CID`` - Candidate ID
- ``IDSURVEY`` - ``{10:'DES', 61:'CFA1', 62:'CFA2', 63:'CFA3S', 64:'CFA3K' ,65:'CFA4p2', 66:'CFA4p3', 150:'FOUND'}``
- ``zHD`` - Hubble Diagram Redshift (with CMB and ``VPEC`` corrections)
- ``zCMB`` - CMB Corrected Redshift
- ``zHEL`` - Heliocentric Redshift
- ``MU`` - SN distances
- ``MUERR_FINAL`` - SN distance uncertainties (renormalized for BEAMS prob of being core-collapse)

``DES-SN5YR_HD+MetaData.csv`` Additional column definitions

..

- ``CIDint`` - Candidate ID integer (same as ``CID`` except for those starting with letters e.g. ``sn2000aa``)
- ``TYPE`` - Type of supernova, 1=Type Ia (everything in this file is 1)

..

- ``PROB_SNNV19`` - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from `Vincenzi et al. 2019`_ (Nominal)
- ``PROB_SNNDESCC`` - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from `Jones et al. 2017`_
- ``PROB_SNNJ17`` - Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from DES data
- ``PROB_SCONE`` - Prob of being Ia from SCONE trained on sims generated using core-collapse templates `Vincenzi et al. 2019`_
- ``PROB_SNIRFV19`` - Prob of being Ia from SNIRF trained on sims generated using core-collapse templates from `Vincenzi et al. 2019`_
- ``PROBCC_BEAMS`` - BEAMS Prob of being core-collapse (see eq. 6 in `Vincenzi et al. 2024`_)

..

- ``c`` - SALT3 color
- ``cERR`` - SALT3 color uncertainty
- ``x1`` - SALT3 stretch
- ``x1ERR`` - SALT3 stretch uncertainty
- ``mB`` - SALT3 uncorrected brightness
- ``mBERR`` - SALT3 uncorrected brightness uncertainty
- ``x0`` - SALT3 light curve amplitude where :math:`m_x = -2.5\mathrm{log}_{10}(x0)` used in the modified Tripp equation
- ``x0ERR`` - SALT3 light curve amplitude uncertainty

..

- ``COV_x1_c`` - SALT3 fit covariance between ``x1`` and ``c``
- ``COV_x1_x0`` - SALT3 fit covariance between ``x1`` and ``x0``
- ``COV_c_x0`` - SALT3 fit covariance between ``c`` and ``x0``

..

- ``HOST_RA`` - Host Galaxy RA
- ``HOST_DEC`` - Host Galaxy DEC
- ``HOST_ANGSEP`` - Angular separation between SN and host [arcsec]
- ``HOST_DDLR`` - Directional light radius distance between SN and host (dimentionless)
- ``HOST_ZSPEC`` - Host spectroscopic redshift (heliocentric frame, same as zHEL).
- ``HOST_ZSPECERR`` - Uncertainty in host spectroscopic redshift.
- ``VPEC`` - Peculiar velocity [km/s]
- ``VPECERR`` - Peculiar velocity uncertainty [km/s]
- ``MWEBV`` - Milky Way E(B-V)
- ``HOST_LOGMASS`` - Host Galaxy Log Stellar Mass
- ``HOST_LOGMASS_ERR`` - Uncertainty in Host Galaxy Log Stellar Mass
- ``HOST_COLOR`` - Host Galaxy rest-frame :math:`u-r` color
- ``HOST_COLOR_ERR`` - Uncertainty in Host Galaxy rest-frame u-r color

..

- ``PKMJD`` - Fit Peak Date
- ``PKMJDERR``  - Fit Peak Date Uncertainty
- ``NDOF`` - Number of degrees of freedom in SALT3 fit
- ``FITCHI2`` - SALT3 fit chi squared
- ``FITPROB`` - SNANA Fitprob
- ``biasCor_mu`` - Bias correction applied to brightness :math:`m_b`
.. - ``biasCorErr_mu``  - Uncertainty on bias correction applied to brightness :math:`m_b`
- ``biasCor_mu_COVSCALE`` - Reduction in uncertainty due to selection effects (multiplicative)
- ``biasCor_mu_COVADD``  - Uncertainty floor as given by the intrinsic scatter model (quadrature)


Global Parameters
=================

.. note:: Note, these global parameters are determined from the likelihood analysis of all the SNe on the Hubble diagram.

- :math:`\alpha =  0.16087 \pm 0.00152`
- :math:`\beta = 3.11780 \pm 0.03530`
- :math:`\gamma = 0.03754 \pm 0.00798`
- :math:`M_{0~\mathrm{avg}} = -29.95821`



Covariance matrices
===================

Statistical and Stat+Systematic
-------------------------------

The Statistical and Stat+Systematic Covariance matrices (both 1829 x 1829 matrices) are provided in
- ``STATONLY.txt.gz``
- ``STAT+SYS.txt.gz`` (all systematics)

Single-systematic cov matrix are also available in ``SingleSYS_CovMatrix`` folder.

Single-systematic covariance matrices
-------------------------------------

List and definition of Single-systematic covariance matrix:

- ``BS20`` : Nominal vs BS20 scatter model
- ``P21SYS1`` : Nominal vs realization 1 from MCMC dust model fitting code
- ``P21SYS2`` : Nominal vs realization 2 from MCMC dust model fitting code
- ``P21SYS3`` : Nominal vs realization 3 from MCMC dust model fitting code
- ``W22_AGE`` : Nominal vs modelling approach described by `Wiseman et al. 2022`_
- ``P21_HOSTCOLOR`` : Nominal vs dust-based approach dividing between red and blue galaxies
- ``MWEBV`` : Systematics asociated with Milky Way extinction amplitude
- ``MWCOLORLAW`` : Systematics asociated with Milky Way extinction color law
- ``CALIBplusSALT3`` : Systematics associated with calibration and LC modelling (see ``2_LCFIT_MODEL/SALT3.DES5YR-SYS``)
- ``CALSPEC`` : Systematics associated with calibration of CalSpec standard stars
- ``ZSHIFT`` : Systematic redshift shift
- ``MASSLOC`` : Systematic associated to 0.3 dex shift in mass step location
- ``ALPHAEVOL`` : Systematic associated with alpha redshift evolution
- ``BETAEVOL`` : Systematic associated with beta redshift evolution
- ``GAMMAEVOL`` : Systematic associated with gamma redshift evolution
- ``SNNtraining`` : SuperNNova trained on V19 templates vs different training simulations
- ``SNIRF`` : SuperNNova classification vs SNIRF classification
- ``SCONE`` : SuperNNova classification vs SCONE classification
- ``CClikelihood`` : Simulation-based modelling of core-collpase likelihood vs polynomial
- ``FIXAB`` : Systematic associated with fixing alpha and beta parameters
- ``SIGINT_MODEL`` : Systematic associated with color-independent modelling of sigma_int
- ``SVAHOSTLIB`` : Nominal Host library vs Host library built using DES Science Verification data
- ``HOSTEFFshift`` : Nominal DES spec redshift efficiency vs efficiency curve shifted by 0.2 mag
- ``VPEC`` : Systematic associated with pec velocity corrections



.. .. table:: Global parameters

..     +-----------------------------+-----------------------------+
..     | Parameter                   |                       Value |
..     +=============================+=============================+
..     | :math:`\alpha`              | :math:`0.16087 \pm 0.00152` |
..     +-----------------------------+-----------------------------+
..     | :math:`\beta`               | :math:`3.11780 \pm 0.03530` |
..     +-----------------------------+-----------------------------+
..     | :math:`\gamma`              | :math:`0.03754 \pm 0.00798` |
..     +-----------------------------+-----------------------------+
..     | :math:`M_{0~\mathrm{avg}}`  |                   -29.95821 |
..     +-----------------------------+-----------------------------+



...........

.. include:: _static/links.rst
