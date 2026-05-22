---
course: Statistics
course_code: "30001"
tags:
  - "source"
  - course_30001
Links:
Title: "Lecture 13-14 Slides Point estimation"
Reference: "Course Material"
Created: 2026-05-18
Processed: false
---


## POINT ESTIMATION

## Covered so far...

**(READING)**

- Descriptive statistics: description of the characteristics of a set of observations with reference to a specific variable. Observations might consist of a **sample** or of the **entire** .

- **population**

- Measures of (central or non-central) tendency and dispersion, calculation of the frequency with which values of a variable are observed; calculation of measures summarizing the extent of the relationship between two variables (correlation and covariance)

- Random variables: description of the outcome of a **random** sampling of a unit from a population with **known** characteristics **.**

- It is not possible to know with certainty what the observed result will be for a randomly drawn unit: a random variable describes the probabilities with which specific values are observed, as well as the characteristics of the population (e.g. expected value and variance)

- draws from the **same**

- In the case of repeated **independent** population, it is not possible to know with certainty what the values of the calculated statistics (e.g. the mean) will be. However, we have seen that for some statistics it is possible to assess aspects of their probability distribution (expected value and variance, probability of observing specific values) and - in some cases (normal distribution or central limit theorem) - their distribution is known.

## Inference

**(READING)**

**Inferential** statistics concerns the procedures required to make **extrapolations** on **parameters** of a population X from **statistics** (e.g. the sample mean) calculated for a simple random sample X1, X2, … , Xn extracted from X

- **Estimation** of a parameter

- **Point** estimation: a single value

- **Interval** estimation: a range of values

- **Hypothesis testing** for a parameter: assess which of two possible hypotheses is more supported by sample results

## Point estimation: parameter, estimator, estimate

With reference to point estimation, it is fundamental to distinguish between:

- **Parameter: θ.** Measurable characteristic of the **population with reference to a r.v.** X Examples of parameters are the mean, **μ** , or the standard deviation, **σ** , of the population, or the proportion p of cases with a certain characteristic in the population.

- **Estimator:** θ\hat{P} . **Statistic** used to **estimate θ** . θ\hat{P} is a function of the outcome of (simple) random sample of n i. i. d. draws X1, … , Xn distributed as X , i.e. θ\hat{P} = f(X1, … , Xn) . Since the realisations of X1, … , Xn are **random,** θ\hat{P} is a **r.v.** describing the realisations of θ\hat{P} with respect X . to all the samples that can be extracted from

For example, the sample mean \bar{X} = ((X1 + ⋯+ Xn)/n ) is a possible estimator of the population mean, **μ** . Note that until a sample is actually drawn, \bar{X} is a random variable, whose realisation is not known a priori.

- **Estimate:** θ\hat{\beta}_0 θ\hat{P} **. Sample realisation of an estimator** calculated from the specific sample

actually drawn, x1, … , xn .

For example, extracting a **specific** sample of size 10 from X , ( **1, 0.5, 2.5, 4, 3.5, 6, 7, 8, 8.5, 9** ) the realisation of \bar{X} is \bar{x} = 5 .

## Point estimation: parameter, estimator, estimate

Examples. We are interested in assessing a master’s degree with reference to the placement of graduates. A simple random sample of 200 graduates one year after graduation is  drawn.

- **What is the monthly salary a generic graduate can expect?**

- X **= monthly salary of a randomly selected graduate**

- **Parameter of interest: population average,** - **, calculated on all graduates**

- **Estimator: sample mean (random variable)**

- **What is the (squared) expected deviation around the average salary?**

- X **= monthly salary of a randomly selected graduate** - - (2) **Parameter of interest: population variance,** - **Estimator: sample variance (random variable)**

- **What percentage of graduates found a job within 6 months of graduation?** - X **= Bernoulli r.v. indicating whether a graduate found (1) or not (0) work within 6 months** - **Parameter of interest: proportion of graduates who found a job within 6 months, p** - **Estimator: sample success rate,** P\hat{P} **(random variable, average of** X1, X2, … , X200 **)**

## Point estimatation: parameter, estimator, estimate

**(READING)**

Unlike when we considered extractions from a population described by a r.v. with **known** parameters, in the inferential case the characteristics of the population are **not** known. The inference will necessarily have to be based on the specific estimate corresponding to a specific sample extracted from the population.

However, to assess the reliability of the inferential procedure, we can ask ourselves:

- What is the **expected value** of the **estimator we decide to use to estimate a certain parameter?** Does it coincide with the parameter of interest or not?

- What is the dispersion of the **estimates** around the parameter of interest? Can we expect realisations of the estimator far away from the parameter of interest? And with what probability? With what probability will we extract a sample that yields estimates very far from the parameter?

**We will assess the reliability of the inferential process by choosing the estimator with the best properties. However, given the estimate calculated from a specific sample, we will not be able to make any assessment, especially with respect to how close (if close at all!) this estimate is to the value of the parameter (which is unknown).**

## Properties of estimators: unbiasedness

A point estimator \hat{θ} n based on a (simple random) sample of n units is said to be **unbiased** for a parameter θ if its expected value coincides with the parameter itself, for any value of n and θ:

\hat{E} θn = θ for any value of n and θ

If an estimator \hat{θ} n is **biased** for a parameter θ , its **bias** is defined by

A **biased** estimator for a parameter θ , is said to be **asymptotically unbiased** if, as the sample size increases, the bias is reduced:

lim \hat{θ}_{n} = 0 or equivalently lim \hat{θ}_{n} = θ n→∞(D) n→∞(E)

## Standard error of an unbiased estimator

For a generic **unbiased** estimator \hat{θ} for a parameter θ , i.e. such that E(θ)(\hat{P}) = θ:

The **variance of an unbiased estimator is the expected squared deviation** of **the estimator** from **the parameter of interest** (as the expected value of the estimator is the parameter itself). **The standard deviation of an unbiased estimator** is called **standard error of the estimator** . The variance (and the standard error) of an unbiased estimator provides information on the **reliability** of the estimator.

Among all the unbiased estimators for a certain parameter, the one with the smallest **variance (or standard error)** will be preferable, as it guarantees the **greatest concentration of estimates around the parameter.**

## Estimator for the population mean

Given a population described by a r.v. X, we are typically interested in is its **mean** (or expected = value) E(X) μ . A ‘natural’ (or intuitive) estimator for μ based on an i.i.d. random sample X1, X2, … , Xn , is the **sample mean** \bar{X} .

As we have already seen, **whatever the distribution of** X is, the following hold **:**

\bar{X} - the expected value of \bar{X} is: E X= E X1 + ⋯+ E Xn /n= n∙μ / n= μ therefore \bar{X} is an **unbiased estimator for** μ

- The variance of \bar{X} is: Var \bar{X}= Var X1/n+ ⋯+ Var Xn/n= n∙σ(2) / n(2) = σ(2) / n with σ(2) = Var(X) and therefore its standard error is SE\bar{X} = σ(2) / n . As n increases, the dispersion of **estimates** around μ decreases!

In addition

- It can be shown that given n , \bar{X} is the unbiased estimator with **minimum variance (the most** _**efficient**_ **)**

- If X is normally distributed, the **distribution** of \bar{X} is also **normal;** the same applies, whatever the distribution of X , if n is sufficiently high (central limit theorem).

## Estimator for the population variance

Note that the variance of \bar{X} σ(2) depends on the variance of the population, which **is typically unknown.** To estimate σ(2) one can use the **sample variance** S(2):

n −(\bar{X}) X X ( i )(2) S(2) = \sum n−1 i=1

It can be shown that:

The sample variance S(2) is an **unbiased estimator** E(S(2) ) = σ(2) **for** σ(2) **whatever the distribution of** X

The so-called **unadjusted** sample variance:

n −(\bar{X}) X X ( i )(2) \hat{S}(2) = \sum n i=1

n−1 S(2) is characterised by: E((\hat{P}) ) = n(σ)(2)

\hat{S}(2) is a **biased estimator for** σ(2) , but it is **asymptotically unbiased**

## Hands on: estimating the population mean

To assess the efficiency of a call centre, a survey is conducted on a random sample of **300** calls received in a week (dataframe **`CallCenter.P`** *): the day and time of each call, the reason for the contact ( **`Topic`** ), the duration (in seconds) of the wait ( **`TimeWaiting`** ) and of the conversation ( **`TimeTalk`** ) are recorded. Customers are also contacted in order to record whether they are satisfied with the service ( **`Satisfaction`** ) and whether or not their problem has been resolved ( **`Solved`** ). The conversation duration is assumed to have a standard deviation of 150 sec.

**Determine the estimate of the average conversation duration. What is the standard error of the estimator used and what is its interpretation?**

- **`xbar <- mean(CallCenter.P$TimeTalk) # no missing values`**

- **`xbar`**

- **`(1) 254.3733`**

_Estimate of the population mean duration_

- **`sigmaX <- 150 # standard deviation assumed known > n <- nrow(CallCenter.P) # no  missing values`**

- **`SE_Xbar <- sigmaX/sqrt(n)`**

- **`SE_Xbar`**

_The standard error represents the_ _**expected deviation** of a_ _**generic** estimate from_ **`(1) 8.660254`** _the population mean duration_

- This dataframe and all the other used below are in file **`Lesson 13-14_Data.Rdata`**

## Hands on: estimating the population mea\bar{n} \bar{X} **“Since the standard error is** SEX **= 8.66 and** x **= 254.3733 we can conclude that the expected deviation between the population mean,** μ **, and 254.3733 is 8.66”. Comments** ?

The statement is false: **8.66** is the deviation from of a and not of a **expected** μ **generic specific** estimate! We cannot exclude higher or lower deviations: **8.66** is only a **summary** of the deviations characterising the estimates calculated on **all** possible samples.

To further clarify this fundamental aspect, remember that since n =300, \bar{X} has a distribution that can be **approximated** by a normal (central limit theorem):

X~N(\bar{X} - **, σ(2)** /300) = N( - **, 8.66(2)** )

The standard error measures the **dispersion** of the **estimates** . obtained based on all the possible samples around μ

_We cannot rule out that the estimate obtained based on the specific available sample (254.3733) is far from_ μ _. What we can say though is that the probability to draw a sample leading to an estimate close to_ μ _is higher than the probability to draw a sample leading to an estimate far from_ μ _. The lower the standard error of the estimator the higher the probability of estimates close to_ μ _._

**μ**

## Hands on: estimating the population mean

**How to obtain an estimator with a lower standard error? What effects on estimation?** By increasing the sample size the standard error of \bar{X} decreases.

**What is the sample size required to reduce the standard error to a maximum of 5 seconds?** For the standard error of the sample mean to be at most 5, we must have:

**Assume that a sample of size 900 is drawn leading to an estimate equal to 7.24. “** _**Since 7.24 is based upon a larger sample (900) such estimate is more reliable than the estimate, 8.66, based on a sample of size 300**_ **”. Comments?**

Surely the standard error of the estimatore based upon a larger sample is smaller. Therefore the concentration of the possible estimates around μ will be higher and the probability of estimates far from μ lower. Nonetheless, we cannot draw any conclusions about a **specific estimate** , because it might be that the larger sample contains some extreme or outlying cases and the smaller sample contains very “central” observations

## Hands on: estimating the population mean

**How would your assessment of the standard error of** \bar{X} **and of the sample size needed to have a standard error lower than 5 change if** σ **(2) was not known?** It is not possible to answer precisely as in the case when the variance is known. Even so, it is possible to **estimate** σ(2) using the sample variance, S(2) ; the **estimate** of the standard error based on the available sample is: se\bar{X} = s(2) /n

- **`n <- nrow(CallCenter.P)`**

- **`s2_X <- var(CallCenter.P$TimeTalk) # estimate of the variance`**

- **`s2_X`**

- **`(1) 28445.97`**

- **`se_Xbar <- sqrt(s2_X/n) # estimate of the standard error > se_Xbar`** _Note that the estimated variance based on the sample (and the estimated_ **`(1) 9.737552`** _standard error) is larger than the one assumed before,_ σ(2) = 150(2) =22500

Based on such estimate we can approximate the sample size needed to reduce the standard error using n≥s(2) / **5**(2):

- **`s2_X/25 (1) 1137.839`**

- _Based on this result, a sample sized at least_ _**1138** should be drawn. As a precaution, it is best to consider the highest value obtained by using the highest variance for the calculations_

## RStudio: a note on missing values

**(OPTIONAL)**

**For the sake of completeness, we consider the case when the dataset contains missing values, using the data in the** **`CallCenter.R.NoMiss` and** **`CallCenter.R.Miss` dataframes**

- **`CallCenter.R.NoMiss$TimeWaiting`**

- **`(1) 15 35 90 70 51 58 118 38 99 124 113 86`**

- **`CallCenter.R.Miss$TimeWaiting # missing value (1) 15 35 90 70 51 58 118 38 99 124 113 86 NA > mean(CallCenter.R.NoMiss$TimeWaiting)`**

- **`(1) 74.75`**

- **`mean(CallCenter.R.Miss$TimeWaiting,na.rm=T)`**

- **`(1) 74.75`**

- **`var(CallCenter.R.NoMiss$TimeWaiting)`**

- **`var(CallCenter.R.Miss$TimeWaiting,na.rm=T)`**

- **`(1) 1279.477`**

- **`# However:`**

- **`nrow(CallCenter.R.NoMiss)`**

- **`(1) 12`**

_When there are missing values, the number of rows in the dataframe (or the length of a data vector)_ _**does not coincide with the number of instances! Note: We will derive the standard error of the estimators using the functions in UBStats for confidence intervals (introduced in the next lessons), which exclude missing values from the calculations!**_

- **`nrow(CallCenter.R.Miss) # the number of rows includes the missing value!`**

- **`(1) 13`**

- **`complete.cases(CallCenter.R.Miss$TimeWaiting) # not NA`**

- **`(1) TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE FALSE`**

- **`n.Miss<-sum(complete.cases(CallCenter.R.Miss$TimeWaiting))`**

- **`n.Miss`**

- **`(1) 12`**

* In the exam, datasets will not have NAs i.e. missing values

## Estimator for the population proportion

Another parameter one is typically interested in is the **proportion** p **of cases in a population that exhibit a characteristic (coded as 'success’)** , estimated on the basis of a simple random sample of n units, by measuring the r.v. X1, … , Xn indicating for each unit whether a success was observed (1) or not (0).

To estimate p we use the **sample proportion** P\hat{P} .

- the r.v. X1, … , Xn are i.i.d. according to a Bernoulli distribution with parameter p , and P\hat{P} is therefore their **sample mean.** From the properties of the sample mean we have:

- \hat{P}

- E P= E X= p

\hat{P}_{i}s an **unbiased estimator for** p ,

- Var \hat{P}= Var(X)/n = p(1−p) /n

The variance of P\hat{P} ( **never known** ) is smaller the larger the sample

- If n P is sufficiently high, the distribution of\hat{P} can be approximated by a normal distribution \hat{P}

- \hat{P}≈N(p, p(1−p)/n ). Note that the variance of is not known (but it can be estimated by substituting pwith its estimate).

## Hands on: estimating the population proportion

The dataframe **`CallCenter.P`** includes, among others, a variable ( **`Solved`** ) indicating whether the customer’s problem has been solved.

**Estimate the proportion** p **of problems solved, and the standard error of the estimator.**

```
> table(CallCenter.P$Solved)
```

```

```

```
27 273
```

Success in this case is coded as **`Y`** ! The estimate of p is (there are no missing values)

\hat{p} **=273/300=0.91**

\hat{V}_{a}r with its P= p(1−p) /n is not known (it depends on p ) but it can be estimated by substituting p estimate. Thus, the estimate of the standard error i\hat{s} \hat{s}_{e}\hat{P} = p∙(1− p)/n= **0.91∙(1−0.91)/300** = **0.0165**

## What can you conclude about the parameter?

We **cannot** conclude that p is close to 0.91, the expected deviation from p of a generic estimate is very low, and –  given the approximately normal distribution of P\hat{P} (high sample size, central limit and estimates far from theorem) – estimates are very concentrated around p p are unlikely, though not impossible.

* Syntax for the calculations using R in the script

## Estimator for the difference between means (and proportions)

In many applications we are interested in evaluating the differences between the averages of two populations

- Cholesterol-lowering drug

- Comparison of average cholesterol levels at the start of the treatment and after a certain period of treatment

- Comparison of average cholesterol levels in patients treated with two different drugs

- Gender gap: comparison of average salary levels for men and women in the same position

- Marketing campaigns

- Average expenditure before and after a sales campaign

- Comparison of the percentage of customers clicking on two different banners

- Comparison of the percentage of users opening the link to an ad posted on different social media (e.g. facebook, instagram)

## Estimators for the difference between means

## Problem setting:

**The parameter of interest is the difference between the means of the two populations** μX −μY

## Estimators for the difference between means

To estimate the difference between the means of two populations described by two r.v. X and Y on the basis of two samples X1, … , XnX and Y1, … , YnY, it is natural to use the estimator: \bar{X}−\bar{Y}. **Whatever the distribution of** X and Y we have:

- X−(\bar{X})

- E((\bar{X}) Y) = E(X) −E((\bar{X}) Y) =(\bar{X}) μX −μY

- X−(\bar{X}) is therefore an **unbiased estimator for**

- ((\bar{X}) Y) μX −μY

- The variance, and thus the standard error, of the estimator **depends on the relationships between the two populations (and thus between the samples drawn from them) and on the assumptions on the joint distribution of di** X **and** Y **!**

- The **distribution** of X−(\bar{X}) \bar{Y} also depends on the relationship between X and Y and on their joint distribution. In general, with **large** samples the distribution of the sample means can be approximated with a **normal** (even if the variances are not known). However, some clarifications are necessary - especially for **small** samples; we will discuss about this when knowing the distributions of the estimators will be of crucial importance.

## Estimators for the difference between means

We deal with two specific cases:

- **Independent** samples. We are interested in comparing the means of two populations on the basis of samples, **possibly of different sizes,** drawn **independently** (e.g. average wages for men and women, profitability of customers reached by different marketing campaigns, sales volumes in restructured and non-restructured stores,…). This is the case where the two samples are made up of different statistical units, so that it makes sense to assume that the results observed on one sample are in no way linked to the results observed on the other.

- **Paired same** samples. In this case, the two samples represent two measurements from the **statistical units.** For example, the same variable is measured at different times, or under different conditions (e.g. the average amount spent by a customer before and after a promotional campaign, or at different times of the year). Thus, the two samples have the **same size** and are **paired** in the sense that two measurements are available for the same **unit.**

## Estimator for the difference between means: independent samples

In the case of **independent** samples, the sample averages \bar{X} and \bar{Y} are **independent** and thus **uncorrelated,** and the **variance** of the estimator (X−(\bar{X}) Y)(\bar{X}) is:

The case where both variances are known is very rare.

- If the variances **are not known** and are assumed to be **different** , Var(X−(\bar{X}) \bar{Y} ) is estimated by 2 2 2 2 replacing σX and σY with the sample variances obtained from the two samples, SX and SY . 2 2 2 - If the two **unknown** variances are **assumed equal,** so that σX = σY = σ , the common variance is estimated using the so-called **pooled sample variance:**

## Estimators for the difference between means: paired samples

In the case of **paired samples** of size n , two measurements are available for each sample unit: Xi and Yi ; the differences Di = Xi −Yi can therefore be considered as n measurements from the r.v. D= X−Y .

\bar{D} **=** X−(\bar{X}) \bar{Y} **.** One can then refer to the sample mean of the differences,

- Clearly E(D) = \bar{μ} D= E(X−(\bar{X}) \bar{Y} ) = μX −μY ,

- As for the variance of \bar{D} , by the properties of the sample mean we have that:

Var \bar{D}= σ2 Var(D)/n= D /n

Using the properties of linear combinations of r.v. we have that

2 2 = Var D= Var X−Y= Var X+ Var Y−2Cov(X, Y) σX +σY −2σXY

In this case, it is very rare to assume that the variance of D= X−Y is known, as it would 2 be necessary to make assumptions directly on the variance of differences, σD , **or** on the variances of X and Y **and** on their covariance (or correlation)

## Estimators for the difference between means: paired samples

To **estimate** the variance of \bar{D} **=** X−(\bar{X}) \bar{Y} it is possible to proceed in the same way as for the sample mean, and use the **sample variance** calculated on the differences:

which is clearly related to the variances and sample covariance of the two samples:

## Hands on: estimating the difference between means

The dataframe **`Insurance`** (in **`Lesson 13_Data.Rdata`** ) contains information on reimbursements ( **`refunds`** , in $) for healthcare expenses to (unrelated) subscribers with different socio-demographic characteristics ( **`age, sex, bmi -`** body mass index – **`children, smoker, region`** ).

**Estimate the difference in the average amount of expenditure reimbursed to smokers and nonsmokers,** _**limiting attention to those who do not have children**_ **.**

The two samples are **independent** as the subscribers have no links to each other

- **`# extraction of the two samples`**

- **`refund.smoke <- Insurance$refund(Insurance$smoker=="yes" & + Insurance$children==0)`**

- **`refund.nosmoke <- Insurance$refund(Insurance$smoker=="no" & + Insurance$children==0)`**

- **`mean_x <- mean(refund.smoke)`**

- **`mean_y <- mean(refund.nosmoke)`**

- **`mean_x_y <- mean_x-mean_y`**

- **`mean_x_y`**

```
(1) 23729.57
```

_The average amount reimbursed to smokers is higher. Obviously, there could be other factors that influence spending and that could be 'controlled for', but overall there is a difference between the two means_

## Hands on: estimating the difference between means

The dataframe **`Insurance`** contains information on reimbursements ( **`refunds`** , in $) for healthcare expenses to subscribers (unrelated) with different socio-demographic characteristics ( **`age, sex, bmi -`** body mass index – **`children, smoker, region`** ).

**Estimate the standard error of the estimator of the difference in the average amount of expenditure reimbursed to smokers and non-smokers,** _**limiting attention to those who do not have children**_ **.**

- **`nx<-length(refund.smoke) # no missing values! > ny<-length(refund.nosmoke)`**

- **`var_x<-var(refund.smoke)`**

- **`var_y<-var(refund.nosmoke)`**

- 2 2

- **`> # S2_pooled`** n −1 s 2 X X + (nY −1)sY

- s =

- **`> var_pooled<-((nx-1)*var_x+(ny-1)*var_y)/(nx+ny-2)`** Pool **`> var_pooled`** nX + nY −2 **`(1) 54284441`** 2 2

- s s

- s\bar{e} \bar{X} = Pool + Pool X−Y

- **`> se_x_y<-sqrt(var_pooled*((1/nx)+(1/ny)))`** n n X Y

- **`> se_x_y (1) 768.3133`**

* Please refer to the R script for details on the intermediate results

## Hands on: estimating the difference between means

A clinical study conducted on 44 patients with high (bad) cholesterol levels to evaluate the efficacy of a cholesterol-lowering drug reported the following results:

Cholesterol level at start of treatment: \bar{x}_{i}ni = 155; sini = 19.9 Cholesterol level at 8 weeks: \bar{x}_{8}w = 122; s8w = 24.5, sini,8w = 23.4

**Estimate the average reduction in cholesterol level following treatment. Standard error?** The two samples are **paired**: they relate to two measurements on the same individual

We obtain the estimate of the difference between means and the estimate of the std error from the available sample statistics. If we had the data for each patient, we could determine them from the differences between the data on cholesterol levels before and after treatment for each patient! _**Estimate of the difference between means**_ **:**

\bar{x} −\bar{x} = 155 −122 = 33 ini 8w

_**Estimate of the variance of the difference,**_ D= Xini −X8w 2 2 2 s = s + s −2s = 19.9(2) + 24.5(2) −2 ∙23.4 = 949. 46 D ini 8w ini,8w _**Estimate of the standard error of the difference between sample means,**_ D=(\bar{X}) \bar{X} ini − \bar{X} 8w 2 se = s 949.46 \bar{X}_{i}ni−\bar{X}_{8}w D/n= /44 = 4. 645281 The expected deviation of a generic estimate of the difference between means is about 4.65.

* Syntax for calculations using R in the script

## Hands on: estimate and estimator of difference between means

The dataframe **`Fatalities_US`** contains data on the number of accidents (per 100,000 inhabitants) registered in 48 US states ( **`Accidents`** ). General information on the states is available (unemployment rate, % of drivers aged between 15 and 24, **`YoungDrivers`** ), besides the number of accidents at night ( **`Night`** ) and due to alcohol ( **`Alcohol`** ). In order to fight alcohol-related accidents, an awareness-raising campaign was carried out, following which a new survey of the number of such accidents (per 100,000 inhabitants, **`AlcoholPostCampaign`** ) was collected for each state. **Assess the drop in the average number of alcohol-related accidents after the campaign.** The two samples are **paired**: they refer to observations of the same state before and after the campaign.

- **`diff <- Fatalities_US$Alcohol-Fatalities_US$AlcoholPostCampaign > mean_d <- mean(diff)`**

- **`se_diff <- sd(diff)/sqrt(length(diff)) # estimate of standard error`**

- **`mean_d`**

- **`(1) 1.281191`**

- **`se_diff`**

- **`(1) 0.3328564`**

_Check on the R script that the same result is obtained from the aggregated statistics_

## Estimators for the difference between proportions

Problem setting: we are interested in comparing the proportions of a certain phenomenon in two different populations

## Population 1

## Population 2

X1, … , XnX i.i.d sample of size nX from X Y1, … , YnX i.i.d sample of size nY from Y distributed according to a Bernoulli with distributed according to a Bernoulli with parameter pX (i.e. X takes 1 or 0 depending on parameter pY (i.e. Y takes 1 or 0 depending on whether a success is observed or not, and pX = whether a success is observed or not, and pY = proportion of successes in the population), proportion of successes in the population), with E X= pX and Var X= pX(1− pX ) with E Y= pY and Var Y= pY(1− pY ) \hat{P}_{X} = (X1+ … + XnX)/nX **= sample** \hat{P}_{Y} = (Y1+ … + YnY)/nY = **sample proportion of successes proportion of successes**

**The parameter of interest is the difference between the proportions in the two populations:** pX −pY

## Estimators for the difference between proportions

**To estimate the difference between the proportions in two populations, it is quite natural to** To estimate the difference between the proportions of 'successes' in two populations, it is natural to use the estimator **propose the estimator where and are the sample averages of two samples whose units have** P\hat{P} −P\hat{P} where P\hat{P} and P\hat{P} X Y X Y are the sample means of two samples whose units have Bernoulli distributions with parameters **Bernoulli distributions with parameters and respectively.** pX and pY respectively. **For the properties of sample averages: For the properties of sample means:**

- \hat{P}

- **??** P − P\hat{P} P P - E(P\hat{P} X PY) = E(P\hat{P} X) −E(P\hat{P} Y) = E(X) −E(Y) = pX −pY E(\hat{P} X Y) = E(\hat{P} X) −E(\hat{P} Y) = pX −pY is therefore an −\hat{P} **unbiased estimator for** P P is therefore an **unbiased estimator for**

- (\hat{P} X Y) pX −pY

- The variance of the estimator **depends on the relationships between** X **and** Y **. In the case of independent samples:**\hat{P})

−(\hat{P}) Var(P(\hat{P}) X PY ) _is unknown (it depends on_ pX and pY _), but can be estimated by replacing_ and _with their_ pX pY _estimates, i.e. the observed sample proportions._

## Hands on: estimating the difference between proportions

In order to determine which of two banners, A or B, is more effective, users of a social network are shown one of the two banners chosen at random. We are interested in the Click-Through Rate (CTR) of the two banners, i.e. the ratio between the number of clicks on each banner and the number of banner views served by the ad server (impressions). Banner A is viewed by 2364 users and generates 456 clicks. Banner B is viewed by 2323 users and generates 611 clicks. **Estimation of the difference between the CTRs? Standard error of the estimator?** The CTR is the sample proportion of clicks on impressions; the standard error of the estimator can be **estimated** as the two experiments and thus the two samples are independent. _**Estimates of the two proportions and of their difference:**_ \hat{p}_{A} = 456/2364 = 0.1929 ; \hat{p}_{B} = 611/2323 = 0.263 ; \hat{p}_{A} −\hat{p}_{B} = 0. 1929−0. 263= −0. 0701 _**Estimates of the variances of the sample proportions,**_ P\hat{P} A _**e**_ P\hat{P} B, \hat{V}_{a}r(P\hat{P} A ) = 0.1929 ∙(1 −0.1929)/2364 = 0.000066 \hat{V}_{a}r(P\hat{P} B ) = 0.263 ∙(1 −0.263)/2323 = 0.000083 _**Estimate of the standard error of the difference between the two sample proportions,**_ P\hat{P} A _**e**_ P\hat{P} B, \hat{s}_{e}P\hat{A}−P\hat{B} = Var(P\hat{P} A ) + Var((\hat{P}) P\hat{P} B ) = 0. 000066+ 0. 000083= 0. 0122 ^xbgh8w
*(See also: [[Lecture 13-14 Slides Point estimation with FULL NOTES#^sa7vty]])*

- Syntax for calculations using R and using dati in a dataframe ( **`Banner`** ) in the script

## Recap

## From point estimate to interval estimate

**(READING)**

**Point estimation:** sample data is used to determine a **single value** to estimate an unknown population parameter.

In general, a point estimator coincides with the parameter of interest with zero probability! It is virtually impossible for a sample to provide an estimate that coincides with the parameter and –  even if it did – this would not be known. With reference to a point estimator, it is always **necessary to provide information on its standard error in** . **order to correctly convey the dispersion of estimates around the parameter** We may be interested in proposing estimators that **'incorporate' information about the dispersion around the parameter** , as well as in somehow **controlling the probability that** . **the estimator 'covers' the parameter of interest**

**Interval estimation:** sample data are used to determine an **interval estimator** (whose extremes are functions of the sample observations) that contains an unknown population parameter with **a certain probability**

## Related Notes
- [[Lecture 13-14 Slides Point estimation with FULL NOTES]]
- [[Lecture 15-16 Interval Estimation]]
- [[Lecture 15-16 Interval Estimation with FULL NOTES]]