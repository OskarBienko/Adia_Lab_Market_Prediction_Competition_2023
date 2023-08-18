## ADIA Lab Market Prediction Competition 2023

**The cross-section forecast problem**

The problem of directly predicting asset price returns is a fascinating albeit considerably hard problem in finance nowadays. For this reason, alternative prediction problems have surged in an attempt to circumvent these modelling difficulties, and still obtain predictions with tradeable potential. One of the most interesting alternatives is the problem of identifying the relative ordering in performance of an investment vehicle, in the cross-section of a pool or subset of them. This is the cross-section forecast problem. In this setting, we track a pool of investment vehicles that is generally obtained through some rule (for example S&P 500 tracks the performance of the 500 largest companies in the US) at different dates. This pool is typically known as the universe within the financial argot, and can be viewed as an object of study by itself. The challenge of this competition is to identify/sort/rank from best to worst, the performance of all elements of the universe at each given date. The signal for this problem is future performance remapped to the interval [-1,1], but our scoring function for the competition takes into account just the predicted vs true ranking of values, using Spearman's rank correlation.

To illustrate a bit further the interesting use cases of this problem, we can imagine an investment strategy that is long on the best performing element of the universe, and short on the worst performing one. In this setting, no matter the direction of the market, is still possible to obtain positive returns (or to minimize losses).

The dataset presented to the competitors is an obfuscated version of high-quality market data. Therefore, details such as the nature of each investment vehicle, the frequency at which dates are measured (although it is given that it is constant interval) and the definition of each feature, are not available.

----


**Competition phases and format**

This competition is focused on forecasting and has two phases. The first is the submission phase where participants can submit and test their models. The second phase, which is automatic, involves running the models against unobserved live market data.

Submission phase - 12 weeks:
In the first phase, participants are required to submit either a Python notebook (.ipynb) or Python script (.py) file. This file should contain the necessary code to build, load, or update their models trained on the data. Participants can either use static models, trained only once on the initial training set, or dynamic models that update or retrain themselves on the unseen data.

Out-of-Sample phase - 12 weeks:
In the second phase, also called Out-of-Sample (OOS), the participant's code will be automatically run by the platform on live market data and evaluated. In this phase, the participants won't be able to modify their code.

Why the two-phase approach?
* Only the performance on Out-of-Sample data will be taken into account.
* Reproducibility of the winning solution is ensured.
* Participants won't be able to exploit data leaks.

----

**My take**

Even after the submission phase, sharing the data is prohibited, thus I uploaded only the notebooks and python files:

* exploratory_data_analysis.ipynb - this file was provided by the Organizer and I did a little bit of code refactoring.