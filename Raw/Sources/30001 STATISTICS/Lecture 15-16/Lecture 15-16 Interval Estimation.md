---
course: Statistics
course_code: "30001"
tags:
  - "source"
  - course_30001
Links:
Title: "INTERVAL ESTIMATION"
Reference: "Course Material"
Created: 2026-05-18
Processed: false
---


# INTERVAL ESTIMATION

## From point estimate to interval estimate

**(READING)**

- **Parameter: θ.** Measurable **population** characteristic (e.g. mean, **μ** )

- Based on n random i.i.d. draws from X , X1, X2, … , Xn:

- **Point Estimator:** θ\hat{P} . **Statistic, ,** θ\hat{P} = f X1, … , Xn , used to **estimate θ** (e.g. \bar{X} is an estimator of **μ** ).

- **Point Estimate:** θ\hat{\beta}_0 **. Realisation of** θ\hat{P} in relation to  a sample θ\hat{\beta}_0 = f(x1, … , xn) .

- =

- **Problem:** Prob \hat{θ} **θ** is null if \hat{θ}_{i}s a continuous r.v., or it is unknown ( **θ** is not known). **Solution:**

- **Confidence interval:** (θ\hat{P} 1, θ\hat{P} 2) . **Random interval** whose extremes are **two statistics** θ\hat{P} 1 = f1(X1, … , Xn) and θ\hat{P} 2 = f2(X1, … , Xn) , used to **estimate θ** , built in such a way that Prob \hat{θ}_{1} ≤ θ ≤\hat{θ}_{2} = 1 −α with 0 ≤α≤1 chosen a priori. This interval is called a 100 1 −α% **confidence interval** and it is clearly random, as its extremes depend on the **random variables** X1, … , Xn .

- **Interval estimate:** \hat{θ}_{1}, \hat{θ}_{2} realisation of the interval given a specific sample x1, … , xn: \hat{θ}_{1} = f1(x1, … , xn) and θ\hat{\beta}_0 2 = f2(x1, … , xn) .

## From point estimate to interval estimate

**(READING)**

The uncertainty associated with a point estimate is due to the sampling variability, i.e. to the different results that can be obtained based on the different samples that can be drawn from a population. This uncertainty can be quantified by the standard error of the estimator, and also depends on its distribution.

The idea behind confidence intervals is to build an estimator that **explicitly incorporates** this uncertainty.

In many **cases,** and specifically in **all the cases that we will take into account** , the interval an estimator can be obtained by adding and subtracting from an (appropriate) **point estimator** amount called the **margin of error (ME)** , which in turn depends on the **standard error** and on the **distribution of** the estimator

## From point estimate to interval estimate

**(READING)**

Consider the case where one wants to estimate the mean, **μ** , of a **population** X

Population distribution ?

**Parameter (unknown): μ**

Distribution of the estimator, here the X . sample mean,(\bar{X})

Estimates obtained based on different samples (realisations of \bar{X} ): typically different from the parameter, even when they are concentrated around it with high probability!

The estimated interval is built around the point estimate, taking into account the dispersion of the estimates around the parameter!

## Confidence interval: general concepts

**(READING)**

Building a confidence interval

Point estimator ± Margin of error

Point Estimator ± (Reliability Factor)(Standard Error)

- The - **reliability factor** depends on the **required confidence level** , (1 - ), and on the

- **distribution of** the point estimator, and – given the standard error – controls (determines) the width of the interval.

- - - If the confidence level (1 – ) is high, i.e. if the probability that the interval (estimator) contains the parameter of interest is high, the width of the interval will be larger.

- Indeed, the interval ( - ; - ) contains the parameter with probability 1, while a point estimator will cover the parameter with probability 0 (if the point estimator is a continuous r.v.).

- There is therefore a **trade-off** between the precision of the interval (the greater the smaller the interval width) and the confidence level.

## The confidence level

**(READING)**

The confidence level - **(1 –** )

- Probability that the **random** confidence interval contains the unknown parameter

- It can also be seen as the **proportion** of samples (out of all those that can be drawn from the population) leading to interval **estimates** containing the parameter.

- The interval estimate built based on a **specific** sample may or may not contain the parameter (and it is not possible to state which of the two situations occurs, because the parameter is unknown). Thus, **it makes no sense to associate any probability with the actual interval estimate**

## The confidence level: frequentist interpretation

**(READING)**

## Parameter of interest

For each possible sample, an interval is obtained based on an appropriately chosen statistic (estimator)

- The (1 - )x100% of the intervals (estimates) contains the parameter - The ( )x100% of the intervals do not contain the parameter

## Interval Estimates

For a specific interval (calculated from one specific sample) **we cannot know whether or not** - **contain the it contains the parameter. However, if we know that** (1 – )x100% of intervals - _**level**_ that the observed interval is one of those **parameter, we can be** _**confident at the**_ (1 – ) including the parameter **!**

# Interval estimation Confidence intervals for the mean

## Confidence interval for μ:** σ **(2) known

We want to estimate the mean, **μ** , of a **population** X having **known variance,** σ(2) . Assume that

- X has **normal distribution**

- **or** the sample  is large enough, so that the **central limit theorem can be** applied.

X−\bar{μ}_{I}n such cases X~N(μ, \bar{σ}(2) /n ) and consequently n(~N(0, 1)() ) σ/

- We use the notation of the book indicating with _z_ - /2 the percentile of order (1 - - /2)

## Confidence interval for μ:** σ **(2) known

**Interval estimation of the mean, μ, of a population** X **with known variance,** σ(2) **.** Case where X is normal or the sample is large enough (central limit theorem). Given any value of α it is:

The interval **estimator** for - **μ** at the level (1 - )x100% is:

σ X z **The interval is obtained by subtracting and adding to**(\bar{X}) **the margin of error ME=** α/2 n(, ) given by the product between the **reliability factor** , z (depending on the distribution of the α/2 (standardised) estimator and on the confidence level), and the **standard error** of \bar{X} .

## Rstudio: CI.mean()

The function **`CI.mean()`** in package **`UBStats`** allows to determine the confidence interval for the expected value of a population:

```
CI.mean(x, sigma=NULL, conf.level=0.95, digits=2, data)
```

## where:

- **`x`** is a **numeric** vector or the name of one of the columns of the dataframe specified in **`data`**

- **`sigma`** is the value of the standard deviation, **if known**

- **`conf_level`** is the confidence level (0.95 by default)

- **`digits`** is the number of decimals used to round off the reported statistics

## Hands on: estimation of μ with** σ **(2) known

To assess the efficiency of a call centre, a survey is conducted on a random sample of **300** calls received in one week (dataframe **`CallCenter.P`** in **`Lesson 14-16_Data.Rdata`** ) for which, among other things, information on the duration (in seconds) of the conversation ( **`TimeTalk`** ) is collected. It is **assumed** that the conversation duration has a standard deviation = 150 sec. **Determine the 99% confidence interval for the average conversation duration.**

```
library(UBStats)
CI.mean(x=TimeTalk,sigma=150,conf.level = 0.99,data=CallCenter.P)
```

**`> CI.mean(x=TimeTalk,sigma=150,conf.level = 0.99,data=CallCenter.P) Confidence interval for the mean Confidence level: 0.99`** _(Note that the function can also be used to_ **`Variance: known`**

_

**[Note that the function can also be used to obtain the point estimate and the standard error of the estimator)**
._

```
n   xbar sigma_X   SE  Lower  Upper
300 254.37     150 8.66 232.07 276.68
```

_The function reports the number of available data, the sample mean, the standard deviation (in this case known), the standard error of the estimator (also obtained in the last lesson) and the lower and upper limits of the interval estimate_

## Hands on: estimation of μ with** σ **(2) known

To assess the efficiency of a call centre, a survey is conducted on a random sample of **300** calls received in one week (dataframe **`CallCenter.P`** in **`Lesson 14-16_Data.Rdata`** ) for which, among other things, information on the duration (in seconds) of the conversation ( **`TimeTalk`** ) is collected. The conversation duration is **assumed to** have a standard deviation = 150 sec **.**

```
Confidence interval for the mean
Confidence level: 0.99
Variance: known
n   xbar sigma   SE  Lower  Upper
300 254.37   150 8.66 232.07 276.68
```

**Can we conclude that the average talk time is between 232.07 and 276.68 with probability 0.99?**

No, because the observed interval **is not random,** so it either contains **μ** or it does not. We can, however, say that 99% of the intervals built around the sample mean contain **μ** ; hence we can quantify the confidence level (or trust) associated with the interval as 99%, defined as the % of interval estimates that contain the parameter.

## Hands on: estimation of μ with** σ **(2) known / CI width

**How to obtain a 99% confidence interval for the average conversation time with width 20?** The length of the confidence interval for the mean in the case of known variance is **2ME= 2** z n σ/ α/2

Given the confidence level and the variance of the population, the only quantity on which one can act to reduce the width of the interval is the sample size. For the width of the interval to be 20, it is necessary that **ME=10** , i.e. that:

- **`# sample size needed to obtain ci of width 10`**

- **`z_alpha_2 <- qnorm(0.995)`**

- **`z_alpha_2`**

- **`(1) 2.575829`**

- **`(z_alpha_2*150/10)^2`** _A sample of size higher than or equal to_ _**1493** should be drawn._

- **`(1) 1492.852`**

## Confidence interval for μ:** σ **(2) known / CI width

α **Determination of the sample size needed to guarantee a CI at level 1 – with a given margin of error, ME (or, equivalently, with a given width, 2ME).**

For the margin of error to be at **most ME (or, equivalently, for the interval width to be at most 2ME),** it is necessary to select a sample with size:

Clearly, the result should be rounded up to the next integer!

This result holds even when the distribution is not normal, as **long as the resulting size is big enough to ensure the applicability of the central limit theorem (otherwise the distribution of the sample mean would not be normal)**

## Confidence interval for μ (pop. Normal):** σ **(2) not known

**Interval estimation of the mean, μ, of a normally distributed population** X **with variance** σ(2) **unknown**

The confidence interval for - **μ** at level (1 – )x100% is:

**Since the variance is unknown, the extremes of the interval are not known!!!** It would seem natural to **substitute to** σ **its estimate** , based on the sample variance , S= S(2) However, **the distribution of** \bar{X} when replacing S to σ **is no longer normal (and therefore the percentile used,** z **, is not appropriate here)** ! α/2 The following result is valid, yet: if the population has a **normal** distribution **,** the statistic

X−\bar{μ}_{T} **=** n S/

has a known distribution, specifically a _**Student’s t**_ distribution with ( n – 1) **degrees of freedom, denoted by** _**t**_ n –1

## Student’s** _**t**_ **distribution

Replacing - **(2)** with the sample variance, S(2) , increases the uncertainty that characterises \bar{X} , since also S(2) varies from sample to sample. The _**Student's t**_ distribution is bell-shaped and centred at **0,** and depends on a single parameter, ν , called **degrees of freedom** , which influences its variability **As the degrees of freedom increase,** _**Student’s t**_ **converges to the standard normal**

## Confidence interval for μ (pop. Normal):** σ **(2) not known

**Interval estimate for the mean, μ, of a normally distributed population with variance,** σ(2) **, unknown** Following the same procedure as in the case where the variance is known and the distribution of the standardised sample mean is a standard normal, when the population distribution is normal and the variance unknown, the confidence interval for **μ** at the (1 – - )x100% level is:

**The interval is obtained by subtracting and adding to the point estimator,** \bar{X} **, the margin of** s **error ME=** t n−1,α/2 n(, given by the product between the ) **(reliability factor)**(, )(t)(n−1,α/2) **(–)**( which ) depends on the distribution of the estimator (standardised using the square root of the sample **–** variance) and on the confidence level and the **estimate of the standard error** of \bar{X} .

* We use the notation of the book indicating with the percentile of order (1 – - /2)

## Rstudio: CI.mean(), pt(), qt()

The function **`CI.mean()`** in package **`UBStats`** allows to determine the confidence interval for the expected value even when the variance is unknown. The syntax is as seen for the case with known variance, except that the argument **`sigma`** should not be specified.

```
CI.mean(x, conf.level=0.95, digits=2, data)
```

It is also worth introducing the functions available in R to determine the **cumulative probabilities** and the **percentiles** of a Student’s _**t**_ distribution:

## `pt(q, df)`** and **`qt(p, df)`

similar to the functions **`pnorm()`** and **`qnorm()`** calculating probabilities and percentiles of a normal distribution, where:

- **`df`**: degrees of freedom

- **`q`**: (numerical) value at which the cumulative probability has to be calculated. The function **`pt()`** calculates F **`q`** = Prob(tdf ≤ **`q`** ) (i.e. the area below the density curve of the Student’s _**t**_ distribution up to **`q`** )

- **`p:`** order of the **percentile** . The **`qt()`** function calculates the value at which the cumulative probability is **`p`** , i.e. the value t **`df,1- p`** such that F t **`df,1−p`** = Prob tdf ≤ t **`df,1−p`** = **`p`** .

## Hands on: estimation of μ (pop. Normal) with** σ **(2) not known

It is of interest to estimate the average number of customers who visit a shop on weekdays, in order to assess whether it would be worthwhile to hire staff permanently or to increase the number of staff members only at weekends. It is assumed that the number of customers on a weekday has a normal distribution. For a period with no special events, the number of customers on a random sample of weekdays in each week is monitored, for a total of n **= 15** 2 observations. σ xi =2755, σ xi = 585203 are observed. **95% confidence interval for the average number of customers during a weekday?**

```
> n <-15
```

1 \bar{X} 2 2 **`> sum_x <- 2755`** s(2) = i −nx n−1 \sumx **`> sum_x2 <- 585203 > xbar <- sum_x/n > s2_X <- (sum_x2-n*xbar^2)/(n-1) > t_14_alpha_2 <- qt(0.975,df=14)`** \bar{s}_{c}i x∓t **`> ME <- t_14_alpha_2*sqrt(s2_X/n)`** 0.95 μ= 14,0.025 15 **`> c((xbar-ME),(xbar+ME)) (1) 142.0142 225.3191`**

## Hands on: estimated μ (pop. Normal) with** σ **(2) not known

It is of interest to estimate the average number of customers who visit a shop on weekdays, in order to assess whether it would be worthwhile to hire staff permanently or to increase the number of staff members only at weekends. It is assumed that the number of customers on a weekday has a normal distribution. For a period with no special events, the number of customers on a random sample of weekdays in each week is monitored, for a total of n **= 15** 2 observations. σ xi =2755, σ xi = 585203 are observed.

```
> c((xbar-ME),(xbar+ME))
(1) 142.0142 225.3191
```

n **? Is it possible to control the width of the confidence interval acting on** Both t and s and on n _**.**_ depend on the **extracted sample** It is therefore not possible to n−1,α/2 guarantee that an interval will have a specific width, because that will depend on the sample that will be actually extracted and on the resulting variance estimate, which might differ from the actual one. An result can be obtained the same n approximate using percentile (as increases, the percentile decreases) and the current estimate s , which may, however, differ greatly from that estimated from another sample of bigger size.

## Confidence interval for μ (non-normal pop.):** σ **(2) not known

**Suppose it is not possible to assume that the distribution is normal. Is it possible to obtain confidence intervals for μ in the case when the variance is unknown?**

- If n X is big enough, for the central limit theorem,(\bar{X}) has an approximately normal distribution.

- However, the interval

ci \bar{x}∓z n 1−α μ= α/2σ/

cannot be used because its extremes depend on σ , which is not known

- However, the sample variance S(2) is an unbiased estimator for σ(2) , and it can be shown that its variance decreases as n increases; thus, when the sample is sufficiently large, variance estimates are concentrated around σ(2) .

In the case of large samples, one can then substitute s to σ to obtain the interval. σ(2) Statistical software usually build the interval as in the case of a normal population with unknown, thus using the percentile of the Student’s distribution, t , which is higher than n−1,α/2 z , in order to take into account the greater uncertainty due to the substitution of σ(2) with its α/2 n estimate (the two percentiles are however similar when is high):

ci x∓t\bar{s}_{n}≅ x∓z\bar{s}_{n} 1−α μ= n−1,α/2 / α/2 /

## Hands on: estimated μ (pop. not Normal) with** σ **(2) not known

The dataframe **`Insurance`** (in **`Lesson 14-16_Data.Rdata`** ) contains information on reimbursements ( **`refunds`** , in dollars) for healthcare costs to (unrelated) subscribers with different socio-demographic characteristics, including the number of **`children`** . **What is the 95% confidence interval of the average repayment to childless subscribers?** Since no assumptions were made about the distribution of reimbursement in the population, the interval can only be determined if the sample size is sufficiently large

```
> refund.nochild <-Insurance$refund(Insurance$children==0) # data

> length(refund.nochild) # sample width

(1) 574
```

- **`# no need to specify 'date' as x is a vector`**

```
> CI.mean(x=refund.nochild,conf.level=0.95)
Confidence interval for the mean
Confidence level: 0.95
Variance: unknown
```

```
n     xbars_Xse    Lower    Upper
Normal.Approx 574 12365.98 12023.29 501.84 11382.38 13349.57
Student-t     574 12365.98 12023.29 501.84 11380.30 13351.65
```

_The function reports number of data, sample mean, estimated standard deviation and standard error, and the interval’s limits calculated using both normal and Student’s_ _**t** percentiles_

## Interval estimation

**Confidence intervals for the proportion**

## Confidence interval for the proportion

When one is interested in estimating the proportion, p , of cases with a certain characteristic in the population, the confidence interval can be built based on the sample proportion, P\hat{P} , i.e. the sample mean of Bernoullian r.v.’s indicating success or failure for the sample units. n **When the sample size, , is sufficiently large** , by the central limit theorem:

The variance of P\hat{P} depends on p but, as in the case of a non-normal population with unknown variance, one can estimate the variance by substituting p with the sample proportion, getting:

. **Note that the percentile of the standardised normal distribution is used here**

## Rstudio: CI.prop()

The function **`CI.prop()`** in package **`UBStats`** allows to determine the confidence interval for the proportion of 'successes' in a population. The syntax is very similar to that of function **`CI.mean()`**

```
CI.prop(x, success=NULL, conf.level=0.95, digits=2, data)
```

## where:

- **`x`**: name of a vector or factor or one of the columns of the dataframe specified in **`data`**

- **`success x`** is to be considered a success. It can be omitted if: allows you to define which value of

- **`x`** is a binary vector (values 0/1; in this case it is assumed that 1 indicates a success) or a logical

- vector (values **`TRUE/FALSE`** ; in this case it is assumed that **`TRUE`** indicates a success)

- **`conf_level`** is the confidence level (0.95 by default)

- **`digits`** is the number of decimals used to round off the reported statistics

Note that the function does not check whether the conditions needed to build the interval (e.g. sample width) are satisfied

## Hands on: estimating the proportion

Consider the data on the calls to a call centre in the dataframe **`CallCenter.` P** (in **`Lesson 1416_Data.Rdata`** ) with particular reference to the reason for the contact ( **`Topic`** ) and to the duration in seconds of the conversation ( **`TimeTalking`** )

**Estimate the proportion of telephone calls concerning the contract** ( **`Topic="Contract related"`** ), p **, with a 90% confidence interval.**

In order to determine the interval, the sample must be sufficiently large

```
> CI.prop(x=Topic, success="Contract related",
+         conf.level=0.9,data=CallCenter.P)
```

```
Confidence interval for the proportion
Confidence level: 0.9
n pbar  s_X   se Lower Upper
300 0.27 0.45 0.03  0.23  0.32
```

_The function reports the sample size (sufficient to allow the application of the central limit theorem), the sample frequency, the estimated standard deviation and standard error, and the limits of the interval_

## Hands on: estimating the proportion

Consider the data on the calls to a call centre in the **`CallCenter.` P** dataframe (in **`Lesson 1416_Data.Rdata`** ) with particular reference to the reason for the contact ( **`Topic`** ) and to the duration in seconds of the conversation ( **`TimeTalking`** )

**Estimate the proportion of telephone calls lasting more than 6 minutes** , p **, with a 90% confidence interval.**

In order to determine the interval, the sample must be sufficiently large

```
> long.length<-CallCenter.P$TimeTalk>(6*60) # data extraction

```

```
> # In this case, it is not necessary to specify the success argument

> # as the vector long.length is logical

```

```
> CI.prop(x=long.length,conf.level=0.9)
```

```
Confidence interval for the proportion
Confidence level: 0.9
```

```
n pbar  s_X   se Lower Upper
300 0.27 0.45 0.03  0.23  0.32
```

## Hands on: proportion estimation / CI width

**Is it possible to obtain a 90% confidence interval with width at most 0.05 for the proportion of phone calls lasting more than 6 minutes?**

We want to obtain an interval with semi-width ME=0.025.

given the confidence level, **ME** depends on n **and also** on \hat{p} , which **depends on the drawn sample** .

Consider the function . p 1−p We note that it reaches its maximum when =0.5. Thus: p zα/2 \hat{p}(1−\hat{p})/n≤zα/2 0. 5(2) /n Adopting a **conservative** approach, we can determine n by considering the **maximum value of the standard error**

p

## Hands on: proportion estimation / CI amplitude

# Is it possible to obtain a 90% confidence interval with width at most 0.05 for the proportion of phone calls lasting more than 6 minutes?

We want to obtain an interval with semi-width ME=0.025; using a conservative approach we choose n such that:

2 z **0.5**(2) **0.5**(2) α/2 z ≤ **0.025** →n≥ α/2 n **0.025**(2)

- **`# sample width to obtain ci of width <=0.05`**

**`> z_alpha_2 <- qnorm(0.95) > z_alpha_2`** _A sample sized 1083 or more guarantees a 90% CI with a width_ **`(1) 1.644854`** _of 0.05,_ _**whatever the sample frequency of the extracted**_ n _**sample is** (because we obtained based on the frequency to_ **`> (z_alpha_2*0.5/0.025)^2`** _which the maximum standard error corresponds)_ **`(1) 1082.217`**

## Confidence interval for proportion/ CI width

α **Determination of the sample size needed to guarantee a CI for the proportion at level  1 – with a given margin of error, ME (or, equivalently, with a given width 2ME).** Using a conservative approach, for the margin of error to be at **most ME (or, equivalently for the width of the interval to be at most 2ME),** it is necessary to select a sample with size: 2 z **0.5**(2) α 2 / n≥ **ME**(2)

Clearly the result should be rounded up to the next integer!

## Interval estimation Confidence intervals for the difference between means

## Confidence interval for the difference between means

As already seen with reference to point estimation, in many applications we are interested in comparing the means of two populations

**The parameter of interest is the difference between the means of the two populations,** μX −μY In this case, the confidence interval will be built around the **unbiased** point estimator ( X−(\bar{X}) \bar{Y} ). The reliability factor and the standard error of the estimator depend on **the relationships between the samples and on the assumptions on the distributions of the populations.**

## CI for difference between means, independent samples

In the case of **independent** samples, the sample means \bar{X} and \bar{Y} are **independent** and thus **uncorrelated**: the **variance** of the estimator (X−(\bar{X}) Y)(\bar{X}) thus results:

2 2 σ σ X Y Var(X−(\bar{X}) \bar{Y} ) = Var(\bar{X} ) + Var(\bar{Y} ) = + n n X Y

Moreover, since \bar{X} and \bar{Y} **are independent, in the case when**

- The two populations X and Y have normal **distribution**

- **or** the samples are sufficiently large, so that the **central limit theorem** can be applied. one has that:

Following the same procedure as for building the confidence interval for the mean:

2 2 σ σ X Y = ci X−(\bar{X}) 1−α μX −μY (\bar{x}−\bar{y}) ∓zα/2 (\bar{x}−\bar{y}) ∓zα/2∙SE((\bar{X}) Y) nX(+) nY(=)

## CI for the difference between means, independent samples

**rare** . The case when both the variances are known is very 2 2 2 - If the **unknown** variances are assumed to be **equal** , σX = σY = σ , the common variance is estimated using the so-called **pooled corrected sample variance:**

- If the **unknown** variances are assumed to be **different** , the standard error of (X−(\bar{X}) \bar{Y} ) is 2 2 estimated by replacing σX and σY with the sample variances obtained from the two 2 2 samples, SX and SY . The confidence intervals built (under appropriate assumptions) in the two cases have different margins of error, due both (obviously) to different standard error estimates and to different reliability factors (percentiles).

## CI for difference between means, independent samples

If X and Y have **normal** distributions, and their variances are assumed to be **equal**:

− − X−\bar{Y} ((\bar{X}) ) (μX μY) has a Student's _**t**_ distribution with ( nX + nY −2) degrees of freedom. 2 2 S S pooled pooled ~~+~~ nX nY

Thus, using the usual procedure, the confidence interval (estimate) is:

_It can also be used without assuming normality if the samples are sufficiently large (_ _**same considerations on normal vs. Student's t as for** interval for non-normal population with unknown variance)!_

If X and Y have **normal** distributions (or the samples **are** sufficiently large) with **different** variances, 2 2 the interval is built using the estimates sX and sY ; in this case, the reliability factor is still the percentile of a Student's _**t,**_ but with a different number of degrees of freedom (the interval in this case will only be obtained with R*)

* Refer to the textbook if you are interested to a more detailed discussion on the topic

## Rstudio: CI.diffmean() for independent samples

The function **`CI.`** diffmean **`()`** in package **`UBStats`** allows to determine the confidence interval for the difference between means. In the case of **independent** samples, intervals can be built in two alternative ways

## Samples contained in two separate vectors

**`CI.diffmean(x, y, type="independent", sigma.x=NULL, sigma.y=NULL, conf.level=0.95, digits=2, data)`** where:

-: name of two **numeric** **`date.`** The function

- **`x,y`** vectors possibly names of two variables in determines the CI for **`μ_x-μ_y`**

- **`type="independent"`**: specifies that the samples are independent (default) and not paired (case where **`type="paired"`** must be indicated, as we shall see later)

- **`sigma.x,sigma.y:`** allow standard deviations to be specified, if **known** ; in the case of known and equal variances, it is sufficient to specify only one of the two arguments

- **`conf_level`** is the confidence level (0.95 by default)

- **`digits`** is the number of decimals used to round off the reported statistics

_Note: the function does not check whether the conditions necessary for the determination of the interval (e.g. sample size, type of samples, paired or independent) are fulfilled_

## Rstudio: CI.diffmean() for independent samples

The function **`CI.`** diffmean **`()`** in package **`UBStats`** allows to determine the confidence interval for the difference between means. In the case of **independent** samples, intervals can be built in two alternative ways

## Samples obtained based on a 2-level vector

```
CI.diffmean(x, by, type="independent", sigma.by=NULL,
```

- **`conf.level=0.95, digits=2, data)`** where:

- **`x,by`**: vectors of **equal length** ordered in such a way that their elements refer to the same unit **;** **`x`** is the name of a **numeric** vector **while** **`by`** is the name of a vector **that takes only two values,** **`by1`** ≺ **`by2`** (considering standard, alphabetical, numeric or order of levels in a factor); possibly **`x`** and/or **`by`** can be the names of variables in **`date.`** The function determines the CI for **`μ_by1-μ_by2`**

- **`type="independent"`**: specifies that samples are independent (default)

- **`x`**

- **`sigma.by:`** vector containing the standard deviations in the two groups (see manual*).

- **`conf_level`** is the confidence level (0.95 by default)

- **`digits`** is the number of decimals used to round off the reported statistics

- _Note: the function does not check whether the conditions necessary for determining the interval (e.g. sample width, type of samples - paired or independent) are met_

* In the case of known variances we suggest using the **`x,y`** approach

## Hands on: difference between means, independent samples

The dataframe **`Insurance`** (in **`Lesson 14-16_Data.Rdata`** ) contains information on reimbursements ( **`refunds`** , in dollars) for healthcare costs to subscribers (unrelated) with different socio-demographic characteristics ( **`age, sex, bmi, children, smoker, region`** ). **Estimate the difference in the average amount of expenditure reimbursed to smokers and nonsmokers using a 99% confidence interval, assuming that the variances are equal** The two samples are **independent** as the subscribers have no links one to each other

```

# approach based on x,y

# extraction of data of interest

refund.smoke <- Insurance$refund(Insurance$smoker=="yes)
refund.nosmoke<-Insurance$refund(Insurance$smoker=="no").
```

```

# no need to specify type, as independent=default

CI.diffmean(x=refund.smoke,y=refund.nosmoke,conf.level=0.99,digits=1)

# approach based on x,by

CI.diffmean(x=refund,by=smoker, conf.level=0.99,digits=1,data=Insurance)
```

## Hands on: difference between means, independent samples

**`> # Approach based on x,y > CI.diffmean(x=refund.smoke,y=refund.nosmoke,conf.level=0.99,digits=1) Confidence interval for μ_x-μ_y Samples: independent`** _The results show that with 99% confidence the average_ **`Confidence level: 0.99`** _reimbursement to smokers is greater, as all confidence interval_ **`Variances: unknown`** _values are positive, regardless of assumptions and approximations,_ **`x = refund.smoke`** _and the mean difference is estimated to be between 22310 and_ **`y = refund.nosmoke`** _24921 (if variances are equal)_ **`Unknown variances assumed to be equal n_x n_y xbar ybar xbar-ybar s_X s_Y se   Lower   Upper Normal.Approx 274 1064 32050.2 8434.3     23616 11541.5 5993.8 506.1 22312.4 24919.5 Student-t     274 1064 32050.2 8434.3     23616 11541.5 5993.8 506.1 22310.5 24921.4 Unknown variances assumed to be different n_x n_y xbar ybar xbar-ybar s_X s_Y se   Lower   Upper Normal.Approx 274 1064 32050.2 8434.3     23616 11541.5 5993.8 721.1 21758.6 25473.3 Student-t     274 1064 32050.2 8434.3     23616 11541.5 5993.8 721.1 21747.2 25484.7`** ^qt0lth
*(See also: [[Lecture 15-16 Interval Estimation with FULL NOTES#^pbfw5w]])*

_The function reports the intervals built both assuming that the unknown variances are equal and that they are different. We note different standard error estimates in the two cases and a slightly wider interval in the case of unknown variances. Under both assumptions, both an interval obtained using the normal approximation and an interval obtained using Student's_ _**t** are reported, which are practically identical, as the percentiles of the two distributions are almost identical given the high sample sizes._

## Hands on: difference between means, independent samples

**`> CI.diffmean(x=refund.smoke,y=refund.nosmoke,conf.level=0.99,digits=1) Confidence interval for μ_x-μ_y Samples: independent Confidence level: 0.99` Comparison of syntax based on** **`x,y` and syntax** **`Variances: unknown` based on** **`x,by`** _**(output selected: attention limited**_ **`x = refund.smoke`** _**to case of equal variances)**_ **`y = refund.nosmoke`**

**`Unknown variances assumed to be equal n_x n_y xbar ybar xbar-ybar s_X s_Y se    Lower   Upper Normal.Approx 274 1064 32050.2 8434.3     23616 11541.5 5993.8 506.1 22312.4 24919.5 Student-t     274 1064 32050.2 8434.3     23616 11541.5 5993.8 506.1 22310.5 24921.4 > # approach based on x,by > CI.diffmean(x=refund,by=smoker,conf.level=0.99,digits=1,data=Insurance) Confidence interval for μ_x-μ_y`** _The results are the same regardless of the syntax, but the signs of_ **`Samples: independent Confidence level: 0.99`** _the intervals are opposite because in the second case we cannot_ **`Variances: unknown`** _control the order (unless we create a factor by reordering the_ **`x = refund|smoker=no`** _levels)_ **`y = refund|smoker=yes`**

```
Unknown variances assumed to be equal
n_xn_yxbarybarxbar-ybars_Xs_Yse    Lower    Upper
Normal.Approx1064 274 8434.3 32050.2    -23616 5993.8 11541.5 506.1 -24919.5 -22312.4
Student-t     1064 274 8434.3 32050.2    -23616 5993.8 11541.5 506.1 -24921.4 -22310.5
```

## Hands on: difference between means, independent samples

The dataframe **`Insurance`** (in **`Lesson 14-16_Data.Rdata`** ) contains information on reimbursements ( **`refunds`** , in dollars) for healthcare costs to subscribers (unrelated) with different socio-demographic characteristics ( **`age, sex, bmi, children, smoker, region`** ). **Estimate the difference in the average amount of expenditure reimbursed to smokers and nonsmokers** _**without children**_ **using a 99% confidence interval** The two samples are **independent** as the subscribers are not related to each other

```

# extraction of data of interest

refund.smoke <- Insurance$refund(Insurance$smoker=="yes" &
Insurance$children==0)
refund.nosmoke<-Insurance$refund(Insurance$smoker=="no" &
Insurance$children==0)
CI.diffmean(x=refund.smoke,y=refund.nosmoke,
type="independent",conf.level=0.99)
```

## Hands on: difference between means, independent samples

**`> CI.diffmean(x=refund.smoke,y=refund.nosmoke, +             type="independent",conf.level=0.99) Confidence interval for μ_x-μ_y Samples: independent`** _The results show that with 99% confidence the average_ **`Confidence level: 0.99 Variances: unknown`** _reimbursement to smokers is also higher in the sub-population of_ **`x = refund.smoke`** _childless subjects, as all values of the confidence interval are_ **`y = refund.nosmoke`** _positive, regardless of assumptions and approximations_

## `Unknown variances assumed to be equal`

```
n_x n_y    xbar   ybar xbar-ybar     s_X    s_Y    se   Lower   Upper
Normal.Approx 115 459 31341.4 7611.8   23729.6 11596.7 5858.5 768.3 21750.5 25708.6
Student-t     115 459 31341.4 7611.8   23729.6 11596.7 5858.5 768.3 21743.9 25715.2
Unknown variances assumed to be different
```

```
n_x n_y    xbar   ybar xbar-ybar     s_X    s_Y     se   Lower   Upper
Normal.Approx 115 459 31341.4 7611.8   23729.6 11596.7 5858.5 1115.4 20856.4 26602.7
Student-t     115 459 31341.4 7611.8   23729.6 11596.7 5858.5 1115.4 20813.3 26645.9
```

_The standard errors calculated assuming equal or different unknown variances differ from each other; the differences between the intervals are not marked, even if the interval calculated assuming unknown variances is slightly wider. Given the sample sizes, the percentiles of the standard normal and of the Student’s_ _**t** distribution - and consequently the obtained intervals - are substantially the same_

## Hands on: difference between means, independent samples

Consider data on the calls to a call centre in the **`CallCenter.` P** dataframe (in **`Lesson 1416_Data.Rdata`** ) with particular reference to the reason for the contact ( **`Topic`** ) and the duration in seconds of the conversation ( **`TimeTalking`** )

**Estimate with a 95% confidence interval the difference between the average talk time of contractrelated and payment-related calls (** **`Topic="Contract related"` and** **`Topic="Payment related"` ), under the assumption that the variances are equal, and assuming first that they are known and equal to 22500 seconds(2) and then that they are unknown**

```

# Extract the data of interest

```

```
talk.contract<-CallCenter.P$TimeTalk(CallCenter.P$Topic=="Contract related").
talk.payment<-CallCenter.P$TimeTalk(CallCenter.P$Topic=="Payment related").
CI.diffmean(x=talk.contract,y=talk.payment,sigma.x=sqrt(22500),
type="independent",conf.level=0.95,digits=1)
CI.diffmean(x=talk.contract,y=talk.payment,type="independent",
conf.level= 0.95,digits=1)
```

## Hands on: difference between means, independent samples

**95% confidence interval the difference between the average talk time of contract-related and payment-related calls (** **`Topic="Contract related"` and** **`"Payment related"` ), under the assumption that the variances are equal, assuming first that they are known and equal to 22500 seconds(2) and then that they are unknown**

```
Confidence interval for μ_x-μ_y
Samples: independent
Confidence level: 0.95
Variances: known
x = talk.contract
y = talk.payment
n_x n_y  xbar ybar xbar-ybar sigma_X sigma_Y   SE Lower Upper
82  80 233.1  257     -23.9      150    150 23.6 -70.1  22.3
```

```
Confidence interval for μ_x-μ_y
Samples: independent
Confidence level: 0.95
Variances: unknown
x = talk.contract
y = talk.payment
```

_The interval built without assuming that the variances are known is wider. However, in both cases we conclude (with 95% confidence) that the difference between the means can be positive or negative, despite a negative point estimate, regardless of the assumptions on the variances_

```
Unknown variances assumed to be equal
```

```
n_x n_y  xbar ybar xbar-ybar   s_X   s_Y   se Lower Upper
Normal.Approx  82  80 233.1  257     -23.9 175.4 152.9 25.9 -74.6  26.8
Student-t      82  80 233.1  257     -23.9 175.4 152.9 25.9 -75.0  27.2
```

## CI for difference between means, paired samples

In the case of **paired samples** of size n , two measurements Xi and Yi are available for each sample unit; the differences Di = Xi −Yi can therefore be considered as measurements on the r.v. D= X−Y on n sample units.

In this case, the variance of the sample mean of the differences, \bar{D} **=** X−(\bar{X}) \bar{Y} is: \bar{X} 2 Var σ D= Var(D)/n= D /n 2 2 = Var X+ Var Y−2Cov σ +σ −2σ X−Y/n= (Var X, Y) /n= ( X Y XY) /n X e Y are Assuming that **jointly normal** (or that the **sample size is sufficiently large** ), the statistic \bar{D} has a **normal** distribution **and** the confidence interval for is μX −μY = ci \bar{d}∓z ∙σ n= \bar{d}∓z 1−α μX −μY α/2 D/ α/2 ∙SE(\bar{D}) where \bar{d} **=** \bar{x}−\bar{y}_{i}s the sample mean of the realisations of the differences d1, … , dn

## CI for difference between means, paired samples

The variance of the differences (and/or the variances of the two populations and their covariance) is seldom known, and the variance of \bar{D} **=** X−(\bar{X}) \bar{Y} must be estimated - as we have seen when dealing with point estimation - with the **corrected sample variance:**

Since \bar{D} is a sample mean, in the case of a **normal** distribution, the confidence interval for ( μX −μY ) is obtained exactly as the interval for the mean of a normal population with unknown variance:

If the population is not normal, but the sample is large enough, so that the central linit theorem applies, it is possible to use the interval based on the percentile of the standard normal or on the percentile of the Student’s distribution, in order to account for the 2 σ uncertainty associated with the estimate of D

## Rstudio: CI.diffmean() for paired samples

The function **`CI.`** diffmean **`()`** in package **`UBStats`** allows to determine the confidence interval for the difference between means of **paired** samples, with the following syntax:

```
CI.diffmean(x, y, type="paired", sigma.d=NULL, conf.level=0.95,
digits=2, date)
```

## where:

-: name of two **numeric** vectors ordered so that their elements refer to the same unit or names

- **`x,y`** of two numeric columns in the dataframe specified in **`date`**

- **`type="paired"`**: specifies that the samples are paired

- **`sigma.d:`** allows the standard deviation of the **difference** to be specified, if **known**

- **`conf_level`** is the confidence level (0.95 by default)

- **`digits`** is the number of decimals used to round off the reported statistics

_Remark: the function does not check whether the conditions necessary for determining the interval (e.g. sample width, type of samples - paired or independent) are met_

## Hands on: difference between means, paired samples

A clinical study conducted on 44 patients with high (bad) cholesterol levels to evaluate the efficacy of a cholesterol-lowering drug reported the following results:

Cholesterol level at the beginning of treatment: \bar{x}_{i}ni = 155; sini 19.9 Cholesterol level at 8 weeks: \bar{x}_{8}w = 122; s8w = 24.5, sini,8w = 23.4 **Estimate the average reduction in cholesterol level following treatment using a 90% confidence interval**

The sample is not particularly large, although the distribution of the sample mean can be approximated by a normal one already for samples of size 30

```
> xbar_ini <- 155
> s_ini <- 19.9
> xbar_8w <- 122
> s_8w <- 24.5
> cov_ini_8w <- 23.4
> n <- 44
```

```
> mean_ini_8w <- xbar_ini-xbar_8w # difference between averages

> se_diff <- sqrt(s_ini^2+s_8w^2-2*cov_ini_8w)/sqrt(n)
> t_43_alpha_2<-qt(0.95,df=43)
> ME<-t_43_alpha_2*se_diff
> c((mean_ini_8w-ME),(mean_ini_8w+ME))
(1) 25.19095 40.80905
```

## Hands on: difference between means, paired samples

The dataframe **`Fatalities_US`** (in **`Lesson 13_Data.Rdata`** ) contains data on the number of **`Accidents`** (per 100,000 inhabitants) registered in 48 US states. General information on states is available (unemployment rate, % of drivers aged between 15 and 24, **`YoungDrivers`** ), besides the number of accidents at night ( **`Night`** ) and due to alcohol ( **`Alcohol`** ). To fight alcohol-related accidents, an awareness-raising campaign was carried out, following which a new survey of the number of such accidents (per 100,000 inhabitants, **`AlcoholPostCampaign`** ) was collected. **Evaluate the reduction in the average number of alcohol-related accidents as a result of the campaign using a 95% confidence interval.**

```
> CI.diffmean(x=Alcohol,y=AlcoholPostCampaign, type="paired",
```

```
+             conf.level=0.95,data=Fatalities_US)
Confidence interval for μ_x-μ_y
Samples: paired
Confidence level: 0.95
Variance: unknown
x = Alcohol
```

_Based on these results, we can conclude (with 95% confidence) that the average number of alcoholrelated accidents decreased after the campaign_

```
y = AlcoholPostCampaign
```

```
n xbar ybar d=xbar-ybar  s_D   se Lower Upper
Normal.Approx 48 7.47 6.18        1.28 2.31 0.33  0.63  1.93
Student-t     48 7.47 6.18        1.28 2.31 0.33  0.61  1.95
```

# Interval estimation Confidence intervals for the difference between proportions

## Confidence interval for the difference between proportions

As already seen with reference to point estimation, in many applications we are interested in comparing the proportions of a certain phenomenon in two populations

**Population 1**

**Population 2**

X1, … , XnX sample of size nX , iid Y1, … , YnY sample of  size nY iid X distributed according to a Bernoulli of Y distributed according to a Bernoulli parameter pX (i.e. X takes on a value of 1 parameter pY (i.e. Y takes on a value of 1 or 0 or 0 depending on whether a success is depending on whether a success is observed = observed or not, and pX proportion of or not, and pY = proportion of successes in the successes in the population), with population), with E X= pX and Var X= pX(1− pX ) E Y= pY and Var Y= pY(1− pY ) \hat{P}_{X} = (X1+ … + XnX)/nX **= sample** P\hat{Y} = (Y1+ … + YnY)/nY = **sample proportion of successes proportion of successes**

**The parameter of interest is the difference between the proportions in the two populations,** pX −pY

## Confidence interval for the difference between proportions

The point estimator for the difference between the proportions in two populations is the −\hat{P} difference between the proportions in the two samples, P\hat{P} X PY In the case of **independent samples,** we have seen that:

−\hat{P} P P is **never** _and_ Var(\hat{P} X Y ) known (it depends on pX pY ), but it can be estimated by replacing pX and pY with the observed sample proportions.

**If the samples are large enough, by the central limit theorem we have:**

. **Note that the percentile of the standardised normal distribution is used here**

## Rstudio: CI.diffprop() for independent samples

The function **`CI.diffprop()`** in package **`UBStats`** allows to determine the confidence interval for the difference between the proportions of ‘successes' in two independent populations. Again, it is possible to use the syntax based on two vectors **`x,y`** or the syntax based on **a vector** **`x`** partitioned on the **basis of a 2-level vector** **`by`** . In the **first case**:

```
CI.diffprop(x, y, success.x=NULL, success.y=NULL,
```

```
conf.level=0.95, digits=2,data)
```

## where:

-: name of two vectors or factors or two variables in **`data`**: the interval is built for

- **`x,y p_x-p_y`**

- define the values of **`x`** and to be taken as success in the two

- **`success.x,success.y: y`** samples. They can be omitted (in one or both cases) if **`x`** or **`y`** are binary (values 0/1; in this case it is assumed that 1 indicates a success) or logical (values **`TRUE/FALSE`** ; in this case it is assumed that **`TRUE`** indicates a success). If success is encoded in the same way in the two samples, it is sufficient to specify only one of the two arguments

- **`conf_level`** is the confidence level (0.95 by default)

- **`digits`** is the number of decimals used to round off the reported statistics

_Note that the function does not check whether the conditions necessary for determining the interval (e.g. sample width) are satisfied_

## Rstudio: CI.diffprop() for independent samples

The function **`CI.diffprop()`** in package **`UBStats`** allows to determine the confidence interval for the difference between the proportions of 'successes' in two independent populations.

**In the case of vector** **`x` partitioned on the basis of a 2-level vector** **`by`:**

**`CI.diffprop(x, by, success.x=NULL, conf.level=0.95, digits=2,data)`** where:

- **`x,by`**: vectors (or factors) with the same length ordered so that their elements refer to the same unit. **`x`** is the name of a vector/factor, **`by`** is the name of a two-level vector/factor with two values/levels **`by1`** ≺ **`by2`** (possibly **`x`** and/or **`by`** can be the names of variables in **`data`** ). In this case, the function calculates the interval for **`p_by1-p_by2`**

- **`success.x:`** defines the values of **`x`** to be taken as success. It can be omitted when **`x`** is binary

- (values 0/1; in this case, 1 is assumed to indicate success) or logical (values **`TRUE/FALSE`** ; in this case, **`TRUE`** is assumed to indicate success).

- **`conf_level`** is the confidence level (0.95 by default)

- **`digits`** is the number of decimals used to round off the reported statistics

_Note that the function does not check whether the conditions necessary for determining the interval (e.g. sample width) are satisfied_

## Hands on: difference between proportions

The dataframe **`Banner`** (in **`Lesson 14-16_Data.Rdata)`** contains information on two alternative banners (A and B) shown to users of a social network. It is of interest to compare the Click-Through Rate (CTR) of the two banners, i.e. the ratio between the number of clicks on each banner and the number of banner views served by the ad server (impressions). The variable **`Click`** indicates for each user who viewed a banner whether they clicked ( **`Yes)`** or not ( **`No`** ). **Build a 90% confidence interval for the difference between the CTRs**

```

# syntax x,y

# define data vectors

banner_A<-Banner$Click(Banner$Banner=="A")
banner_B<-Banner$Click(Banner$Banner=="B")
```

```
CI.diffprop(x=banner_A,y=banner_B,success.x="Yes",
conf.level=0.90,digits=4)
```

```

# syntax x,by

```

```
CI.diffprop(x=Click,y=Banner,success.x="Yes",conf.level=0.90,
digits=4,data=Banner)
```

## Hands on: difference between proportions

```
> CI.diffprop(x=banner_A,y=banner_B,success.x="Yes",
+             conf.level=0.90,digits=4)
```

```
Warning:
Only 'success.x' is specified; 'success.y' set equal to 'success.x'.
Confidence interval for p_x-p_y
Confidence level: 0.9
x:banner_A = Yes
y:banner_B = Yes
n_x  n_y phat_x phat_y phat_x-phat_y    s_X    s_Y     se   Lower Upper
2364 2323 0.1929  0.263       -0.0701 0.3946 0.4403 0.0122 -0.0902 -0.05
>
> CI.diffprop(x=Click,by=Banner,success.x="Yes",
+             conf.level=0.90,digits=4,data=Banner)
Confidence interval for p_x-p_y
Confidence level: 0.9
x:Click = Yes | Banner = A
y:Click = Yes | Banner = B
n_x  n_y phat_x phat_y phat_x-phat_y    s_X    s_Y     se   Lower Upper
2364 2323 0.1929  0.263       -0.0701 0.3946 0.4403 0.0122 -0.0902 -0.05
```

## What considerations?

## Recap: averages and differences between averages

- _In the case of unknown variance(s) for large samples the approximation is_ _**normal** , but one can_

_use Student's_ _**t** to widen the interval and thus account for the uncertainty associated with estimating the variance(s)_

## Recap: proportion and difference between proportions

## Related Notes
- [[Lecture 15-16 Interval Estimation with FULL NOTES]]
- [[Lecture 13-14 Slides Point estimation with FULL NOTES]]
- [[Lecture 13-14 Slides Point estimation]]