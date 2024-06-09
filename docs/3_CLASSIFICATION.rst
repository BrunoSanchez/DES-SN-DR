################################################
3 - CLASSIFICATION: Classification probabilities
################################################

Overview
========

DES used 3 classifiers to select Type Ia Supernovae. 
Here are released the probabilities of the 1635 used SNIa for the DES-SN5YR Hubble Diagram.

Classifiers
===========

We made use of the following classifiers:

- **SuperNNova**
  
  - References
  
    - `Moller et al. 2019`_
    - `Moller et al. 2022`_ 
    - `Möller et al. 2024`_
  
  - Documentation: `SuperNNova`_

- **SCONE**

  - References

    - `Qu et al. 2021`_

  - Documentation: `SCONE`_

- **SNIRF**

  - Documentation: `SNIRF`_

Classifier agreement
--------------------

.. image:: _static/images/classifier_agreement.png
   :height: 300
.. :width: 200
.. image:: _static/images/training_sample_comparison.png
   :align: right
   :height: 300
.. :width: 200

Release Format
==============

Probabilities with classifiers that use Redshift information
------------------------------------------------------------

A ``csv`` file is released with the candidate ID (``CID``) as the single event identifier, in combination with the probabilities.

Column definitions
^^^^^^^^^^^^^^^^^^

- ``PROB_SNNV19`` (*) - Probability of being Ia from ``SuperNNova`` trained on sims generated using core-collapse templates from `Vincenzi et al. 2019`_ (*Nominal*)
- ``PROB_SNNDESCC`` - Probability of being Ia from ``SuperNNova`` trained on sims generated using core-collapse templates from `Jones et al. 2017`_
- ``PROB_SNNJ17`` - Probability of being Ia from ``SuperNNova`` trained on sims generated using core-collapse templates from DES data
- ``PROB_SCONE`` - Probability of being Ia from ``SCONE`` trained on sims generated using core-collapse templates `Vincenzi et al. 2019`_
- ``PROB_SNIRFV19`` - Probability of being Ia from ``SNIRF`` trained on sims generated using core-collapse templates from `Vincenzi et al. 2019`_
- ``PROBCC_BEAMS`` - BEAMS Probability of being core-collapse (see eq. 6 in `Vincenzi et al. 2024`_)

(*) ``PROB_SNNV19`` is our Nominal

Probabilities of being SN Ia using only light-curves (no redshift information)
------------------------------------------------------------------------------

We also release the classification from `Möller et al. 2024`_ that does not use redshift information. 

This is in a ``csv`` file again with the candidate ID (``CID``) as the single event identifier, in combination with the probabilities.

Column definitions
^^^^^^^^^^^^^^^^^^
- ``PROB_SNN_noz_singlemodel``: Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from Vincenzi et al 2019. This model uses only light-curves for classification, no redshift information. (*Nominal: single model*)
- ``PROB_SNN_noz_ensemble``: Prob of being Ia from SuperNNova trained on sims generated using core-collapse templates from Vincenzi et al 2019. This model uses only light-curves for classification, no redshift information. These probabilities are an average of 5 independet models (*Ensemble*).

...........

.. include:: _static/links.rst
