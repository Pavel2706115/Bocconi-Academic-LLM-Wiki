---
course: Statistics
course_code: "30001"
tags:
  - "source"
  - course_30001
Links:
Title: "RANDOM VARIABLES AND THEIR COMBINATIONS"
Reference: "Course Material"
Created: 2026-05-18
Processed: true
---


# RANDOM VARIABLES AND THEIR COMBINATIONS

## Motivation: the statistical inference problem

**(READING)**

The statistical inference problem arises when one is interested in evaluating measures that describe (or summarize) the characteristics of an **entire population** , called _**parameters**_ , but collecting data on all units of the population is _**prohibitively**_ expensive (cost or time), _**difficult**_ or **even** _**impossible.**_ This is the case, for example, when the population is very large (all companies operating in Europe) or not fully defined or accessible (all the people who purchased a certain brand’s products or who were exposed to an advertising message). In such cases, it may be necessary or convenient to collect data only on a **random sample** of units drawn from the population and to infer about population _**parameters**_ based on the sample summary measures calculated on observed data, called _**statistics**_ .

## Motivation: the statistical inference problem

**(READING)**

When inferring a **population parameter** from a **statistic** calculated from a **sample** of size n, it is crucial to assess the **reliability** of this generalization and the **risk associated with it** . Therefore one must appropriately **quantify the uncertainty** inherent to the fact that inference is **one** based upon only of the samples that could have been drawn from the population.

Thus, one must evaluate the relationship between the **parameter** of interest and the distribution of the considered **statistic** calculated based on **all the possible samples** of size n that can be drawn from the population, in order to quantify, for example, the dispersion of the **statistic** around the **parameter** and the consequent uncertainty of the inferential process.

In order to make such an assessment, we will first consider the case when it is possible to make assumptions about the population (or better _about the distribution of a variable of interest in the population_ ) and examine:

- The distribution of statistics based on simple random samples drawn from the population - The relationship between the characteristics of this distribution and the parameter of interest Specifically, we consider **random variables* (r.v.)** to describe the outcome of drawing a sample from a population

- **(*) The formal definition of a random variable was introduced in the Mathematics 2 course.**

# Random variables (r.v.) Discrete and continuous random variables

##

## Discrete r.v.: introduction (see notes)

A company is interested to the number of exposures to an advertising message on a social network (during a pre-specified time period) for subjects in a specific segment (for example, subjects with a certain age class). Below are results observed during a marketing campaign on 1500 subjects.

|.|.|**Consider**X**= nr of exposures for a****_generic_ subject. What can be said about_subject but only to assess the probability of observing each possible value._**|
|---|---|---|
|**Exposures**|**Counts**|**Consider**X**= nr of exposures for a****_generic_ subject. What can be said about_subject but only to assess the probability of observing each possible value._**|
|**0**|**525**|
|**1**|**450**|
|**2**|**300**|
|**3**|**150**|
|**4**|**75**|
|**Total**|**1500**|
|

**Consider** X **= nr of exposures for a** _**generic**_ **subject. What can be said about** X **?**

**What is the probability that a generic subject did not visualize the advertising message?** _Probability of drawing one of the subjects who did not visualize the message Since the subjects who did not visualize the message are 525 out of a total of 1500:_ Pr **(** X **= 0) = 525/1500 = 0.35**

## Discrete r.v.: probability function (see notes)

Number of exposures to an advertising message on a social network (during a pre-specified time period) for subjects in a specific segment; campaign targeting 1500 individuals.

|**r.v.**X**= nr of exposures for a randomly chosen subject.probabily**function of a random number assigns a probability to each value x: 035 = 0|
|---|---|---|---|---|
|**Exposures**|**Counts**|
|**0**|**525**|
|**1**|**450**|
|**2**|**300**|
|035 = 0|
|**3**|**150**|
|PX x= . x 0.30 x= 1 0.20 x= 2 0.10 x= 3 0.05 x= 4 0 altrove|
|**4**|**75**|
|**Total**|**1500**|

The probability function describes the **population** , that is, the characteristics of a generic population element with respect to X. In this case, the probability of observing each value is equal to the frequency of the value in the population.

## Discrete r.v.: probability function, expected value (see notes)

The company is about to launch a new marketing campaign aimed at all the subjects in the **assumes** target segment, and that the probability of exposures to the advertising message is . **the same observed in the previous “pilot” campaign**

**What is the probability function of** the **r.v.** X _**=**_ **“** _**number of exposures to the ad for a generic subject”?**_

|**_bject”?_**|
|---|---|---|
|0.35|x= 0|_The probability function describes the outcome of a single_|
|0.30|x= 1|_"random sampling" from the population, based on the_|
|PX x= 0.20 0.10|x= 2 x= 3|**_assumptions_** _made about the number of exposures to the ad_ _based on past experience._|
|0.05|x= 4|
|0|otℎerwise|

## What is the expected number of exposures for a generic subject?

_To determine the_ _**expected value** of  the r.v._ X _it is necessary to consider the values that can be observed for a generic subject, weighted by their probability of occurrence!_

- - - - - E X= 0.35 0 + 0.30 1 + 0.2 2 + 0.1 3 + 0.05 4 = 1.2

## Discrete r.v.: probability function and variance (see notes)

The company is about to launch a new marketing campaign aimed at all the subjects in the **assumes** target segment, and that the probability of exposures to the advertising message is . **the same observed in the previous “pilot” campaign**

## **r.v.** X _**=**_ **“** _**number of exposures to the ads for a generic subject”**_

0.35 x= 0 0.30 x= 1 0.20 x= 2 E X= 1.2 P x= X 0.10 x= 3 0.05 x= 4 0 otℎerwise **Expected quadratic deviation from** E X **of the number of exposures for generic subject** _? Again, it is necessary to consider the values of quadratic deviations that can be observed on a generic client and weight them by their associated probability!_ Var X= 0 −1.2(2) ∙0.35 + 1 −1.2(2) ∙0.3 + 2 −1.2(2) ∙0.2 + 3 −1.2(2) ∙0.1 + 4 −1.2(2) ∙0.05 = 1.36

## Discrete r.v.: probability and cumulative distribution function

A **discrete** random variable X can take only a **countable number of distinct values Probability function** of X: assigns to each value x the probability that X is equal to x:

P X x= Prob(X= x)

_Probability to observe on a unit randomly selected from a_ x _on_ X _population the value_

This function has the following properties:

- 0 ≤P x≤ 1    for each x X

σx PX x= 1

**The cumulative distribution function** of X associates to each x the probability that X is x: less than or equal to

F ≤ X x= Prob(X x)

_Probability to observe on a unit randomly selected from a_ X x _. population a value on at most equal to_

## Discrete r.v.: expected value and variance (see notes)

For random variables, we are also interested in calculating some summary measures, such as the **expected value** and the **variance.**

**Expected value** E xP X(x) X= μ = \sum x **Variance: expected quadratic deviation of the values of** X **from the expected value** Var X= σ(2) = E(2) X−μ = E(X(2) ) −μ(2)

**Note:** If the probability function exactly reflects the composition of the population, **the expected value and the variance will coincide with the population mean and variance!**

## Discrete r.v.: the Bernoulli distribution (see notes)

A company assumes that the number of exposures to an advertising message on a social network for a generic subject is characterized by the following probability function.

It is generally assumed that an ad is more effective when subjects **Exposures Probability 0 0.35** are exposed to it at least 3 times (useful frequency). **1 0.30 What is the probability function of the r.v.** X **indicating (1/0) 2 0.20 whether a subject will be exposed to the ad for a “useful” 3 0.10 number of times? 4 0.05** = Prob X 0 = 0.35 + 0.30 + 0.2 = 0.85 **Total 1.00** = Prob X 1 = 0.10 + 0.05 = 0.15 0.85 x= 0 x= 0, 1 P 0.15 x= 1 P X X 0 otℎerwise x= \{(0.15)(x)((1 −0.15))(1−x) 0 otℎerwise x= \{ **Bernoulli ’s r.v.:** for a subject randomly selected from the population, X describes whether _success_ X= 1 X= 0 (an event coded as) a (case when ) or a _failure_ (when ) occurs.

## Discrete r.v.: the Bernoulli distribution

A company assumes that the number of exposures to an advertising message on a social network for a generic subject is characterized by the following probability function. **The r.v.** X **indicating (1/0) whether a subject will be exposed to the ad for a “useful” number of times has a Bernoulli distribution characterised by a probability of success equal to = 0.15** p

0.85 x= 0 x= 0, 1 P 0.15 x= 1 P X X 0 otℎerwise x= \{(0.15)(x)((1 −0.15))(1−x) 0 otℎerwise x= \{

**Expected value and variance?** - - E X= 0.85 0 + 0.15 1 = 0.15 = p Var X= 0 −0.15(2) ∙0.85 + 1 −0.15(2) ∙0.15 = = 0.15(2) ∙0.85 + 0.85(2) ∙0.15 = 0.15 ∙0.85 ∙ 0.15 + 0.85 = 0.15 ∙0.85 = 0.1275 = p 1−p

## Discrete r.v.: the Bernoulli distribution (see notes)

**A Bernoulli's r.v. is characterized by the parameter** p **(indicating the probability of observing a success, i.e., the proportion of successes in the population) has a probability distribution:** (1 −p) x= 0 x= 0, 1 P x= 1 X p 0 otℎerwise = \{(p)(x)((1 −p))(1−x) 0 otℎerwise x= \{ **Expected value and variance of** X~Bernoulli p: E X= 1 −p∙0 + p∙1 = p Var X= 0 −p(2) (1 −p) + 1 −p(2) p= p−p(2) = p 1 −p

## Continuous r.v.: notable distributions

Defining a density function that adequately describes the population (based on past experience or on the researcher’s assumptions) can be complicated. Theoretical models have been developed to describe some typical situations

Uniform r.v.                         Normal r.v.                     Chi-squared r.v.

These distributions depend on **parameters** that act on their **shape so as** to **fit the assumed** characteristics of the population’s distribution

## Continuous r.v.: the normal distribution

## The two and **σ(2)** determine the characteristics of the distribution **parameters μ**

## μ

## Features:

- Bell-shaped and symmetrical

- Centered on the mean **μ** (=median)

- The amount of spread depends on the standard deviation, **σ**

- As **μ** and **σ** vary, we get a large collection of density functions

**σ=8** Changes in **μ** (keeping constant **σ** ) shift the **μ =16** distribution without **μ=5 μ=24** changing its shape **σ μ=16 σ=5** Changes in (keeping constant **μ** ) affect the dispersion and **σ=8** concentration of values around the mean **σ=24**

## Rstudio: pnorm() and qnorm() - normal distribution

**The cumulative distribution function of a normal r.v.** cannot be calculated **manually** by integrating the density function.

The functions **pnorm()** and **qnorm()** available in R allow to determine the **cumulative distribution function** and the **percentiles** of a normal distribution, respectively. To simplify the syntax as much as possible, we will use the functions in this way:

**pnorm(q, mean=0, sd=1)**

**qnorm(p, mean=0, sd=1)**

## Where:

- **mean** and **sd** (with default values 0 and 1) allow to specify the parameters of the distribution

- **q** is the numeric value at which you want to calculate the cumulative distribution function of a normal distribution with the specified parameters. Thus, the function **pnorm()** calculates F **`q`** = Prob(X≤ **`q`** ) (i.e., the area under the normal density curve up to **q** )

- **p** indicates the order of the **percentile** to be calculated, i.e., the value at which the cumulative distribution function of a normal distribution with the specified parameters is equal to **p** . Thus, the function **qnorm()** calculates x **`1−p`** (*) i.e., the value such that F x **`1−p`** = Prob X≤ x **`1−p`** = **p** .

* The notation x **`1−p`** to indicate the percentile of order **`p`** is as used in the textbook

## Hands-on exercises: the normal distribution

**Suppose** the income of freelancers working in a particular industry and region over the past year has a normal distribution with a mean of 71K and a variance of 324K(2)

## A professional declares an income of 20K. What considerations?

**> sqrt(324) # sd**

**(1) 18**

- **# probability that income is less than 20K:**

- **pnorm(20,mean=71,sd=18)**

**(1) 0.002303266**

_The reported income is exceptionally low: only the 0.23% of the population is expected to have an income less than 20K_

## What is the probability that the income is between 20K and 80K?

**> pnorm(80,mean=71,sd=18)- pnorm(20,mean=71,sd=18)**

**(1) 0.6891592**

## What is the probability that the income is greater than 90K?

**> 1-pnorm(90,mean=71,sd=18)**

**(1) 0.1455857**

## Hands-on exercises: the normal distribution

# What is the interval including the 90% of the most common incomes?

**> c(qnorm(0.05,mean=71,sd=18), qnorm(0.95,mean=71,sd=18)) (1) 41.39263 100.6074**

**Declaring an income exceeded only by the 10% of the population qualifies for a certain type of tax relief. What is the minimum income threshold for such relief?**

**> qnorm(0.9,mean=71,sd=18)**

**(1) 94.06793**

**The revenue office decides to systematically assess professionals who declared an income below the lowest 5% of income values. What income threshold triggers the tax assessment?**

**> qnorm(0.05,mean=71,sd=18) (1) 41.39263**

**There is a** _**risk**_ **of having a tax assessment if declaring an income below the threshold exceeded by the 70% of the population. What income threshold puts a professional at risk?**

**> qnorm(0.3,mean=71,sd=18)**

**(1) 61.56079**

# Random variables Linear transformation and standardization

##

##

## Expected value and variance of linear transformations of a r.v.

Consider a **linear transformation** of a **r.v.** X,  Y= a+ bX. Expected value and variance of Y are related to expected value and variance of X (μ and σ(2) ):

E Y= E a+ bX= a+ bE X= a+ bμ

Var Y= Var a+ bX= b(2) Var X= b(2) σ(2) →Sd ∙ σ Y= |b| ∙Sd X= |b|

In fact, referring for the sake of simplicity to a discrete r.v. (“proof” required), it is: = E (a+ bx)PX PX xPX x= a+ bE X a+ bμ Y= \sum (x) = a\sum x+ b\sum x x x 2 Var a+ bx− a+ bμ PX bx−bμ(2) PX(x) Y= \sum (x) = \sum x x = b(2)(2) P b(2) Var X = b(2) σ(2) x−μ X(x) = \sum x (same reasoning for a continuous r.v.)

## Expected value and variance of linear transformations of a r.v.

A company is considering whether to launch a new product with a unit selling price of $25. After considering several scenarios, the company expects to sell 300K units of the product, with an expected deviation of 90K units. The variable product cost per unit is assumed to be $15, while the fixed costs are expected to be $900K.

**What is the expected profit? What deviation do you expect from the expected profit?**

X **=** _**units sold**_

E X= 300K Sd X= 90K

Y **=** _**Profit**_ **=** X∙ 25−15−900K= 10X−900 E Y= E 10X−900= 10E X−900 = 3000 −900 = 2100K Sd Y= Sd 10X−900= 10Sd X= 900K

## Normal r.v.: linear transformation

For a given r.v. X with expected value and variance equal to μ and σ(2) , we saw that the linear transformation Y= a+ bX has expected value and variance:

E Y= E a+ bX= a+ bE X= a+ bμ Var Y= Var a+ bX= b(2) Var X= b(2) σ(2) →Sd Y= |b| ∙Sd X= |b| ∙σ

Nonetheless, it is not always possible to easily determine the probability or density distribution of Y based on the distribution of X. Even so, in the **particular case** of a **normally** distributed r.v. X , with expected value μ and variance σ(2 ) , any linear transformation of X has a **normal distribution:**

X~N(μ, σ(2) ) → Y= a+ bX~N a+ bμ, b(2) σ(2)

## Standardization of a r.v.

We consider a particular linear transformation of an r.v., called **standardization** . Given **any random variable** X, the **standardized variable** is:

X−μ Z= σ

The r.v. Z is defined based on the expected value and variance of X (indicated by μ and σ(2 ) ), and its expected value and variance are the following:

X E X μ ( ) μ − E Z= E σ(−) σ(=) σ σ(= 0) X 1 μ Var Z= Var(Var(X))(= 1) σ(−) σ(=) σ(2)

## Normal r.v.: standardization

We saw that for a  normally distributed r.v. X , with expected value μ and variance σ(2 ) **:** X~N(μ, σ(2) ) → Y= a+ bX~N a+ bμ, b(2) σ(2)

Therefore, the **standardized normal r.v.** has a normal distribution, with an expected value of 0 and a variance of 1, which is called the **standard normal** distribution.

X−μ X~N(μ, σ(2) ) → Z= σ(~N) 0,1

**Note that for a standardized normal distribution:** Prob Z≤0= **0.5** = Prob **=** Z≥0 **Prob Z≤0= ??0.5 Prob Z≥0** If **If** Prob **Prob** Z≤ **Z≤** z **z** = **= p** →Prob **→Prob** Z≤−z= **Z≤−z= 1   ???1 –– p p p** →Prob Z≥−z= **???** →Prob Z≥−z= **p**

**-** z **0** z

## Normal r.v.: standardization

Although normal distribution probabilities and percentiles can be easily computed with R, it is important to note that

X−μ x−μ x−μ X~N(μ, σ(2) ) → Prob X< x= Prob < = Prob Z< σ σ σ x **`1−`** −μ **`p`** → Prob X< x = → Prob Z< = Prob Z< z = **`p p 1−p 1−p`** σ

x **`1−`** −μ **`p`** → = z → x = μ + z σ **`1−p 1−p 1−p`** σ → x = μ − z σ **`1−p p`**

## Hands on: the standard normal distribution

Consider again the income of freelancers working in a particular industry and region over the past year, normally distributed with a mean of 71K and a variance of 324K(2)

## Probabily of income lower than 20K calculated using the original and the standard normal

**> pnorm(20,mean=71,sd=18)**

- **(1) 0.002303266**

- **pnorm((20-71)/18,mean=0,sd=1) # standardisation**

- **(1) 0.002303266**

## 90-th percentile calculated using the original and the standard normal

**> qnorm(0.9,mean=71,sd=18)**

- **(1) 94.06793**

- **71 + qnorm(0.9,mean=0,sd=1)*18**

- **(1) 94.06793**

## 10-th percentile calculated using the original and the standard normal

**> qnorm(0.1,mean=71,sd=18)**

- **(1) 47.93207**

- **71 + qnorm(0.1,mean=0,sd=1)*18**

- **(1) 47.93207**

- **71 - qnorm(0.9,mean=0,sd=1)*18**

**(1) 47.93207**

**Random variables Linear combinations of random variables**

## **Joint distribution of** _**two**_ **r.v.

**(READING)**

To study **linear combinations** of two **r.v.** we must briefly introduce the concept of **joint distribution.**

The **joint probability (or density) function** of **two r.v.** X and Y assigns a probability to each pair of values (or each pair of intervals in the continuous case): P XY x, y= Prob(X= x, Y= y) b d Prob a≤X≤b, c≤Y≤d = ׬ ׬ fXY xydxdy a c From these functions, the covariance between the two r.v., Cov X, Y , and their correlation, Corr X, Y , can be determined.

2 2 Specifically, given the expected values and variances of X(μX and σX) and Y (μY and σY): Cov X, Y= σXY = E X−μX (Y−μY)

σ XY

= Corr X, Y= ρXY σ σ X Y

## Bivariate normal distribution

**(READING)**

A particularly important joint density distribution is the **bivariate normal** distribution:

where z σ and z σ X = (x− μX)/ X Y = (y− μY)/ Y

**We will never go into the technical details of this**

**distribution** ; for our purposes, it is only important to note that if X and Y have a joint normal distribution, then we also have that:

## Independent r.v.

A fundamental concept  for the analysis of linear combinations of two r.v. is **independence**

Two r.v. X and Y are said to be independent if the **probability of observing certain values for one r.v. does not depend in any way on the values taken by the other r.v.** , so that: P X= xProb xP XY x, y= Prob X= x, Y= y= Prob Y= y= PX Y y

fXY x, y= fX xfY y

This means that the probability of jointly observing values of X and Y can be determined from the (marginal) distributions of the two r.v.

For our purposes, this result is relevant because when two r.v. are **independent** they are also **linearly independent** , that is:

Cov X, Y= Corr X, Y= 0

##

##

## Linear combinations of r.v.

Consider a **linear combination** of two r.v. X and Y _**:**_

aX+ bY 2 2 with E X= μX, Var X= σX, E Y= μY, Var Y= σY and Cov(X, Y)= σXY. The **expected value** and the **variance** of the linear combination are: E aX+ bY= aμX + bμY 2 2 2 Var aX+ bY= a(2) σ + b σ + 2abσ X Y XY _**IfIf**_ X X and and YY _**are independentare independent,?**_ σXY = 0 _**and**_ Var aX+ bY= a(2) σ2X + b2σ2Y

The **distribution of** (aX+ bY) depends on the joint distribution of the two r.v. In the **special case** where X and Y have a **joint normal** distribution it is: 2 2 2 (aX+ bY) ~N(aμX + bμY, a(2) σX + b σY + 2abσXY) And therefore, in the case of **independence:** 2 2 2 (aX+ bY) ~N(aμX + bμY, a(2) σX + b σY)

## Linear combinations of r.v.

**(OPTIONAL)**

A production process consists of 3 phases, A, B and C. The durations (in minutes) of phases A 2 and B are two r.v., TA (μA=10 and σA=1) and TB (μB=16 and σB =2), which are correlated, with ρAB=0.2. The duration of phase C is fixed and it’s 4 minutes. **Expected value and standard deviation of the overall duration of the production process?** The overall duration is T= TA + TB + 4 (the last phase has a fixed duration, not random) **Expected value:** E TA + TB + 4 = μA + μB + 4 = 10 + 16 + 4 = 30 **Variance:** Var T + T + 4 = Var T + T = σ2 + σ2 + 2σ A B A B A B AB Cov TA, TB = σAB = ρABσAσB = 0.2 ∙1 ∙2 = 0.4 →Var T + T + 4 = 1 + 4 + 2 ∙0.4 = 5. 8 A B

**If** TA **and** TB **are assumed to be jointly normally distributed, what is the probability that the total duration of the process is between 25 and 35 minutes?**

**> pnorm(35,mean=30,sd=sqrt(5.8))- pnorm(25,mean=30,sd=sqrt(5.8)) (1) 0.9621187**

# Random variables Sum and mean of i.i.d. random variables Central Limit Theorem

## Sum and mean of i.i.d. r.v.

An important case is when, given a r.v. X with expected value μ and variance σ(2) , we consider n r.v. X1, X2, … , Xn with the following properties:

- They are **independent** (and consequently all the pairs Xi **,** Xk have **covariance** equal to 0)

- Thay all have the **same distribution as** X That is, X1, X2, … , Xn are **independent** and **identically distributed** ( **i.i.d.** ) as X.

n units from the **same** This is the case, for example, when we consider **randomly selected population** (with replacement, i.e. assuming to repeatedly draw from the entire population) and each of them describes the ( **random** ) result of the selection.

Consider two particular **linear combinations** of the n r.v. X1, X2, … , Xn, their **sum** and their **mean:**

**Sum:** S= X +X 1 2 + ⋯+ Xn

**Mean:**(\bar{X}) X= ( X1 + X2 + ⋯+ Xn)/n= S/n

## Sum and mean of i.i.d. r.v.: expected value and variance

If the r.v. X1, X2, … , Xn are n **r.v. i.i.d.** as a r.v. X, with expected value μ and variance σ(2) (for X **sum** and their **mean** are example, the outcomes of independent observations on ), their . r.v. whose expected values and variances can be determined from μandσ(2 )

**Sum:** S= X1 + ⋯+ Xn _**All the**_ Xi _**have the same expected value**_ μ _**and the same variance**_ σ(2) _**;**_ **→ E S=** ?E X1 + ⋯+ E Xn = nμ _**the covariances are zeros as they are independent.**_

- **→ Var S=** ?Var X + ⋯+ Var X = nσ(2) 1 n

**Mean:**(\bar{X}) X= ( X1 + ⋯+ Xn)/n= S/n

**\bar{X} → E X=** ?E X1/n+ ⋯+ E Xn/n= n∙μ/ n= μ

**→ Var \bar{X}=** ?Var X1/n+ ⋯+ Var Xn/n= n∙σ(2) / n(2) = σ(2) / n

## Sum and mean of i.i.d. r.v.: distribution

Even if it is possible to determine the **expected value** and **variance of the sum and of the mean of** n **i.i.d. r.v.** X1, X2, … , Xn **, it is not always possible to determine their probability (or density) functions. However:**

- **The sum and mean of** n **normally distributed i.i.d. r.v.** X1, X2, … , Xn, have **normal distribution** , with mean and variance obtained as described above:

X1, X2, … , Xn **i.i.d.** X ~N(μ, σ(2) )

- S= (X1 +X2 + ⋯+ Xn)~N(nμ, nσ(2) ) X= (\bar{X} 1 +X2 + ⋯+ Xn)/n ~N(μ, σ(2) /n)

- **Central Limit Theorem:** For **sufficiently** large n, the distributions of the **sum** and of the **mean** of n **r.v.** X1, X2, … , Xn **i.i.d.** as a r.v. X  can be _**approximated**_ by the **normal distribution** (with expected value and variance as above), **whatever the distribution of** X **.**

## Sum and mean of i.i.d. r.v.

A company assumes that the amount spent on its products by a customer in a generic shop where a promotion is running has an average of 22€ and a standard deviation of 9 € . Assume that exactly 80 customers take advantage of the promotion. **Obtain the probability that the average amount spent by the 80 clients is higher than 25** € **, specifying whether and what assumptions are needed to obtain it.**

It is possible to determine the required probability without specific assumptions, because the hypothesized number of clients is high enough to apply the central limit theorem and **=** approximate the distribution of the mean as follows, X~N(μ, \bar{σ}(2) /80) N(22, 9(2) /80). **> 1-pnorm(25,mean=22,sd=9/sqrt(80)) (1) 0.0014**

**What is the total amount spent by the 80 clients that the company can expect to be exceeded with probability 0.9?**

**> qnorm(0.1,mean=22*80,sd=9*sqrt(80))**

**(1) 1656.837**

## Sum and mean of i.i.d. r.v.

The daily electricity consumption of a generic household at a given time of year is assumed . to be normally distributed with a mean of 48 Kwh and a variance of 16Kwh(2) **What is the probability that the average daily consumption of 5 households is greater than 50Kwh?** \bar{X} **=** ~~X~N(μ, σ~~(2) ~~/n)~~ N(48,16/5) ^y2zdkv

**> 1-pnorm(50,mean=48,sd=sqrt(16/5)) (1) 0.1317762**

**How much electricity is needed to meet the daily electricity demand of 10 households with a probability of at least 0.95? =** We are looking for the 95-th percentile of S~N(nμ, nσ(2) ) N(480,160). **> qnorm(0.95,mean=480,sd=sqrt(160)) (1) 500.8059**

**Is it possible to determine the required quantities if normality is not assumed?**

No: the number of cases is too small to apply the Central Limit Theorem

## Sum and mean of i.i.d. r.v.: Bernoulli distribution

Consider n **r.v.** X1, X2, … , Xn that are **i.i.d.** as X~Bernoulli p whose parameter is the _**success**_ E: probability of observing a in a population, with X= p, Var X= p 1 −p S= X **= number of successes** 1 + X2 + ⋯+ Xn \hat{P}= (X1 + X2 + ⋯+ Xn)/n= **proportion of successes**

For sufficiently large n (typically higher than 30*) the distribution of S and P\hat{P} can be approximated by a normal distribution, that is

and\hat{P} S≈N(np, np 1−p) P≈N(p, p 1−p/n)

n=5mean=0.125 n=10mean=0.125 n=30mean=0.125 n=100mean=0.125 Distribution of P\hat{P} for var=0.021875 var=0.0109375 var=0.0036458 var=0.0010938 increasing values of n, given p=0.125

* When p is very small or very high, some authors suggest to verify whether np 1−p> 5

## Sum and mean of i.i.d. r.v.: Bernoulli distribution

A company installs surveillance cameras and estimates that the 15% of the installed cameras require post-installation work for changes. **Based on the orders received, 50 cameras will be installed next month. What is the probability that the percentage of cameras requiring postinstallation work will be higher than 25%?** The r.v. describing whether a random camera will require a second intervention is: X~Bernoulli(p= 0.15); E X= 0. 15; Var X= 0. 15∙0. 85= 0. 1275 The r.v.’s describing whether each of the 50 installed cameras will require a second intervention, X1, X2, … , X50, are **iid as** X The % of cameras (out of the 50 installed) that require further intervention is: \hat{P}=(X1 + X2 + … +X50)/50

Since the sample size is sufficiently large, the distribution of P\hat{P} (which is the sample mean of a sample from a Bernoulli population) can be approximated by a normal distribution.

**> 1-pnorm(0.25,mean=0.15,sd=sqrt(0.15*(1-0.15)/50)) (1) 0.02383519**

## Related Notes
- [[Statistics_Formula_Sheet_Bocconi]]
- [[Lesson 7 Slides with NOTES]]
- [[Lecture 13-14 Slides Point estimation with FULL NOTES]]