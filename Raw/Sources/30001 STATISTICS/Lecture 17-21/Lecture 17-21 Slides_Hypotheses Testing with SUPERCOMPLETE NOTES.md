---
course: "Statistics"
course_code: "30001"
tags:
  - "source"
  - course_30001
Title: "Hypothesis testing Test on the mean"
Reference: "Course Material"
Created: 2026-05-18
Processed: true---

## HYPOTHESIS TESTING

## Hypothesis testing: introduction

**(READING)**

on a Hypothesis **(statistical) testing**: procedure for assessing whether a given **hypothesis population parameter θ** is **supported by** the **available empirical evidence.**

A **statistical hypothesis** is a statement about a measurable characteristic of a population, i.e. it is a statement about a the **parameter θ of a population** described by a r.v. 𝑿 (or about the a number of parameters of several populations)

- Hypotheses on a population mean or the proportion of cases with a certain characteristic

- Simple hypothesis: **μ** = 350 / specifies a single value for the parameter

- One-sided composite hypothesis: 𝒑 ≥ 0.6 / specifies a set of values for the parameter

- Hypotheses about the difference between the means or proportions of two populations

- Simple hypothesis: 𝛍𝑿 = 𝛍𝒀 or 𝛍𝑿 −𝛍𝒀 = 0

- One-sided composite hypothesis: 𝛍𝑿 ≤𝛍𝒀 or 𝛍𝑿 −𝛍𝒀 ≤ 0

- Bilateral composite hypothesis: 𝒑𝑿 ≠𝒑𝒀 o 𝒑𝑿 −𝒑𝒀 - 0

- Hypotheses on the relationship between two variables

- Simple hypothesis: the correlation between two variables in the population is 0

- Simple hypothesis: two qualitative variables are independent in the population

## Hypothesis testing: introduction

**(READING)**

Note that we will **never be able to determine whether a hypothesis about θ is** _**true**_ **or** _**false**_ , because **the true value of θ is unknown** and hypothesis testing is based on a **specific sample** drawn from the population.

Hypothesis testing **does not allow to conclude** whether a **hypothesis is true or false** . It is rather a procedure for **assessing whether or not** the observations in the random sample, 𝑋1, 𝑋2, … , 𝑋𝑛 , drawn from the population **support a hypothesis on θ .**

To determine whether or not the empirical evidence supports a hypothesis about **θ ,** hypothesis testing contrasts **two mutually exclusive hypotheses concerning θ** and assesses whether the observed sample realisation is more favourable to one hypothesis or to the other.

## Null and alternative hypothesis

**(READING)**

We contrast two hypotheses, called the **null hypothesis** and the **alternative hypothesis** . We will illustrate later how to choose the role of two hypotheses, but we anticipate that: **H0:** _**null**_ **hypothesis.** It describes a standard situation, the **status quo** with respect to which a difference or effect can be identified. It is the hypothesis **held to be true unless empirical evidence is clearly against it** (i.e. **H0** is held to be true until proven otherwise). **H0** can be simple (e.g. **θ = θ 0** ) or composite, but must **always** specify at least one value for the parameter (e.g. **θ ≤θ 0** or **θ ≥θ 0** , but not **θ < θ 0 or θ > θ 0** or **θ** - **θ 0)**

**H1** _**: alternative**_ **hypothesis.** It is typically the **hypothesis one is interested in proving** and represents the 'novelty' that **contrasts** the 'status quo' described by the **null hypothesis** . **H 1** can be of any type (simple or composite - either unilateral or bilateral)

**H0** and **H1 cannot overlap** , and together they define the set of values that the researcher considers plausible for the parameter, so that on the basis of the empirical evidence one only has to discriminate between the values for **θ** defined by **H0** and **H1** .

## Null and alternative hypothesis / scheme

**(READING)**

**=** Statistical hypotheses can be **simple** (specifying a single value, e.g. **θ θ 0** ) or **composite unilateral θ < θ or** (specifying a range of values for the parameter), and the latter can be (e.g. **0 θ ≤θ 0 ) or bilateral** ( **θ** - **θ ) 0**

**H0** may be simple or composite but must . always **include at least one specific value** Then **H0: θ ≤θ 0** or **H0: θ ≥θ 0** but not **H0: θ < θ 0** or **H0: θ** - **θ 0**

## Statistical test, test statistic, and rejection region

**(READING)**

A **statistical test** is a procedure for contrasting two hypotheses **H0** and **H1** and assessing, on the basis of the empirical evidence, whether to trust one hypothesis or the other, i.e. whether to - Accept (or fail to reject) **H0** (and thus reject **H1** ) or - Reject **H0** (and thus accept **H1)**

= A **statistical H H test statistic** 𝛉(෡) test for testing two hypotheses **0** and **1** is typically based on a 𝑓 𝑿1, … , 𝑿𝑛 . **The distribution of** 𝛉(෡) **depends on θ , and it is fully determined if θ is known** . A test based on the **test statistic** 𝛉(෡) defines a **rejection** (or **critical** ) **region.** The rejection region includes all the samples corresponding to realisations of 𝛉(෡) , i.e. 𝝑(෡) = 𝑓 𝑥1, … , 𝑥𝑛 , that are unfavourable to **H0** and thus lead to **rejecting H0** in favour of **H1** .Defining the rejection region implies defining an **acceptance** region. This region includes all the samples leading to realisations 𝝑(෡) = 𝑓 𝑥1, … , 𝑥𝑛 that are favourable to **H0** (thus leading to not rejecting **H0** and rejecting **H1** )

## Statistical test: Type I and Type II Errors

𝛉 are with The inferential problem arises because typically some realisations of(෡) **compatible** both the hypotheses being compared. No test to discriminate between two hypotheses **H0** and **H1** is therefore error-free, because hypothesis testing relies on **a sample** ! - Concluding in favour of a hypothesis, e.g. **H0** (resp. **H1** ) **does not imply** that **H0** (resp. **H1** ) **is true and H1** (resp. **H1** ) is **false** . We can only say that on the basis of the sample it seems more appropriate to work under the assumption that **H0** (resp. **H1** ) is true rather than false. - It is crucial to assess the risks associated with the decision made on the basis of a certain test (in the light of the empirical evidence, i.e. the observed sample). The following situations may arise:

|**State of nature** **(never known as** 𝛉**is not known)**|**Statistical decision(based on a sample)**|**Statistical decision(based on a sample)**|
|---|---|---|
|**Reject H0**|**Fail to reject H0**|
|**H0 is true**|**Type I error**|**_Correct decision_**|
|**H1 is true**|**_Correct decision_**|**Type II error**|

## Statistical test: Probability of Type I and Type II errors

Let us consider the possible errors that characterise a decision based on a statistical test (that is, based on the empirical evidence, i.e. the observed sample):

|**State of nature**|**Statistical decision(based on a sample)**|**Statistical decision(based on a sample)**|
|---|---|---|
|**Reject H0**|**Fail to reject H0**|
|**H0 is true**|**Type I error**|**_Correct decision_**|
|**H1 is true**|**_Correct decision_**|**Type IIerror**|

. **Type I error:** Reject the null hypothesis when it is true, **R|H0**

- We denote by ( **significance level of the test** ) the **probability** of committing a error of the first kind, - = Pr( **R|H0** ), or rather the **maximum probability of** committing an error of the first type when **θ** is one of the values specified by **H0** .

. **Type II error**: Fail to reject the null hypothesis when it is false, **A|H1**

We denote by - the probability of committing an error of the second kind, - = Pr( **A|H1** ), or rather the probability of committing an error of the second type when **θ** is one of the values specified by **H1** . The probability of correctly rejecting **H0** , Pr( **R|H1** ) = **1 -** - is called the **power of the test.**

## Statistical test: Probability of Type I and Type II errors

It would be desirable to construct a test that simultaneously minimises the probability of type I **.** and type II error

However, for a _**given sample size,** there is_ a trade-off between the two types of error: **a reduction in the probability of incurring one error leads to an increase in the probability of incurring the other error.**

are This problem is solved by considering that **the two types of errors typically** not equally serious. The severity of an error clearly depends on who is doing the hypothesis test, but by **convention the error of the type I error** is considered **more serious** .

Therefore, we set the null hypothesis ( **H0** ) so that the most serious error is **to reject such hypothesis when it is true** . The other hypothesis is set as alternative hypothesis ( **H1** ). This is why **H0** is the status quo, which it is convenient to take as true unless there is strong empirical evidence against it. This is also the reason why some authors prefer using “fail to reject **H0** ” or “don’t reject **H0** ” rather than “accept **H0** ”: indeed we are **conservative** towards **H0** , and therefore not rejecting **H0** indicates that the empirical evidence against it is not strong enough to reject it, and not that the empirical evidence supports it.

## Construction of a statistical test

**(READING)**

**To test two hypotheses concerning a parameter θ**

- One chooses as null hypothesis the one that is most problematic to reject when it is true

- A **test statistic** is chosen (typically a _point estimator of the parameter on which we are conducting the hypothesis test_ )

- Since the type I error (rejecting **H0** when true) is the most serious, one needs to specify what is the risk they are willing to take in terms of the probability of committing an error of the - - first type (significance level, , i.e. maximum probability of committing an error of the first type corresponding to values of **θ** specified by **H0** ; typical values for - are 0.1, 0.05, 0.025, 0.01, or 0.001 in the case of being very conservative towards **H0)**

- - - Among all the tests with significance level , the test with the lowest probability of committing an error of the second type is chosen ( - , evaluated at the values of **θ** specified by **H1)**

- All the tests introduced in the following slides have this property. (Note that the tests are presented intuitively, and without illustrating their optimality properties).

# Hypothesis testing Test on the mean

## The problem

. **Let us review the described procedure with a practical example** The average profitability (in appropriate units) ~~of a company's customers is 15.~~ A promotional campaign is being considered which should lead to increase the average profitability. The variance of the profitability is 170 and it is assumed not to change post-campaign.

Because of its costs, the campaign is considered to be **effective only if** the average profitability rises from 15 to 21. T ~~o decide whether or not to launch the promotional campaign, a pilot~~ survey is carried out on a random sample of 50 customers. **Parameter of interest?**

**after μ = profitability the campaign Hypotheses compared?**

We are interested in assessing whether the promotional campaign is effective or not, i.e. whether:

**μ = 21 (effective campaign, the average profitability increases) or**

**μ = 15 (ineffective campaign: the average profitability pre and post campaign are equal).**

## Null and alternative hypothesis

**Identification of null and alternative hypotheses** Contrasted hypotheses: **μ = 21 (effective campaign) and μ = 15 (ineffective campaign).** The two possible errors that can be made using a statistical test are: **(Reject μ = 21 21 | μ = 21 ) = (Fail to reject μ = 15 | μ = 21)** → **lose the opportunity of an effective campaign (Accept μ = 21 | μ = 15) = (Reject μ = 15 | μ = 15)** → **launch an ineffective campaign** The first error concerns **missed earnings** while the second concerns **an economic loss (more serious).**

Assume **μ = 15 (status quo) unless the empirical evidence is clearly against this assumption and supports the hypothesis that the campaign is indeed effective So:**

**H = 15 and H = 21 0: μ 1: μ**

## The test statistic

**Identification of the test statistic and its distribution** To build a **statistical test,** it is necessary to identify a **test statistic whose distribution depends on the parameter being inferred and which is fully determined if that parameter is known**

Being interested in making inferences about the expected value, **μ** , it is natural to discriminate between the two hypotheses based on the **sample mean.**

No assumptions were made about the distribution of profitability; however, the sample size is sufficiently large (50) to approximate the distribution of 𝑿(ഥ) with a normal distribution. Regardless the assumptions about the distribution of profitability, we have:

ഥ ഥ 𝑿~𝓝( **μ** , 𝛔(𝟐) /𝒏)→ 𝑿~𝓝( **μ** , 𝟏𝟕𝟎/𝟓𝟎)= 𝓝( **μ** , 𝟑. 𝟒)

as the variance is assumed to be known and equal to 170 both pre and post campaign. Note that the distribution of the test statistic is **completely known** , except for the parameter **μ** , which has to be tested.

## The test statistic

**Test statistic and its distribution** Test statistic: 𝑿~𝓝((ഥ) **μ** , 𝟏𝟕𝟎/𝟓𝟎) = 𝓝( **μ** , 𝟑. 𝟒)

The distribution of 𝑿(ഥ) describes the realisations of 𝑿(ഥ) , ഥ𝒙, calculated based on all possible 𝑿. samples that can be drawn from Under the assumption that **μ** is equal to a **specific** value, the distribution of 𝑿(ഥ) is fully known, and it is therefore possible to assess the probability of observing sample realisations in specific intervals

## Sample realisations and statistical decision-making

Let us consider the two hypotheses **H0: μ = μ 0 = 15 vs H1: μ = μ 1 = 21** on the **parameter μ** , and the distributions of the **test statistic,** 𝑿(ഥ) , under the two hypotheses

𝑿ഥ **=** 𝑿ഥ **= |( μ μ 0) |( μ μ 1) μ 0 = 15 μ 1 = 21**

To build a test for **H vs H** we need to **0 1** establish which sample realisations of 𝑿(ഥ) **H .** should lead to the rejection of **0** To do so, we consider the ‘distance’ of the realisations from what we expect to observe when **H is true** and we establish **when the 0 em irical evidence is too** ‘far’ **from H to be p 0 considered favourable to it, i.e. when it is unlikely that the observed sample was drawn from a population with** 𝛍 **=** 𝛍 **0 and it should be considered more likely that the observed sample was drawn from a = population with μ μ 1**

## Sample realisations and statistical decision-making

Let us consider the two hypotheses **H0: μ = μ 0 = 15 vs H1: μ = μ 1 = 21** on the **parameter μ** , and the distributions of the **test statistic,** 𝑿(ഥ) , under the two hypotheses

𝑿ഥ **=** 𝑿ഥ **= |( μ μ 0) |( μ μ 1)**

Whice sample realisations of 𝑿(ഥ) are 'far' from **H ? 0**

Note that **having defined the alternative hypothesis for H0:** 𝛍 **=** 𝛍 **0 = 15** allows to identify **which sample realisations are 'critical' for H0** , i.e. more **favourable to H1 than to H . 0**

**These are those far from H0** _**in the direction towards**_ **H . 1**

**μ 0 = 15 μ 1 = 21**

**We must build a one-sided right-tailed test, where 'right-tailed' refers to the critical tail of H0** i.e. that in the direction of **H1 .**

## Sample realisations and statistical decision-making

Let us consider the two hypotheses **H0: μ = μ 0 = 15 vs H1: μ = μ 1 = 21** on the **parameter μ** , and the distributions of the **test statistic,** 𝑿(ഥ) , under the two hypotheses

𝑿ഥ **=** 𝑿ഥ **= |( μ μ 0) |( μ μ 1) μ 0 = 15 μ 1 = 21** ഥ 𝒙 *** Don’t Reject H0 Reject H0**

Which sample realisations of 𝑿(ഥ) should be considered 'too far' from **H ? 0**

It is necessary to define a **rejection region** based on a **critical value** ഥ𝒙 ***** that determines for which **values of** ഥ𝒙 **the null hypothesis H0 should be rejected.**

**In this case, it is reasonable to reject H0 when the value of** ഥ𝒙 **is** _**extreme**_ **under H0 in the direction of H 1 Rejection region:** 𝒙>ഥ ഥ𝒙 *****

**How to choose** ഥ𝒙 ***?**

## Type I Error, Type II Error and their probability

Let us consider the two hypotheses **H0: μ = μ 0 = 15 vs H1: μ = μ 1 = 21** on the **parameter μ** , and the distributions of the **test statistic,** 𝑿(ഥ) , under the two hypotheses

𝑿ഥ **=** 𝑿ഥ **= In this case |( μ μ 0) |( μ μ 1) Rejection region:** 𝒙>ഥ ഥ𝒙 *** Probabilities of type I and type II errors?** - ***** 𝑿> ഥ𝒙 **=** = Pr((ഥ) ***** | **μ μ 0** ) ഥ - ***** = Pr(𝑿≤(ഥ) 𝒙 ***** | **μ = μ 1** ) ***** - Note that changing the rejection region by - ***** ഥ𝒙𝒙 ***** moving in one direction or the other reduces the probability of incurring one error **μ 0 = 15 μ 1 = 21** but increases the probability of incurring the ഥ 𝒙 ***** other error. **Don’t Reject H0 Reject H0**

Note that changing the rejection region by ഥ𝒙𝒙 ***** moving in one direction or the other reduces the probability of incurring one error but increases the probability of incurring the other error.

- **Building the rejection region given**

**H = vs H = = 21** on the Let us consider the two hypotheses **0: μ μ 0 = 15 1: μ μ 1 parameter μ Since we cannot minimise both errors, we define a rejection region that guarantees a** - **given probability of committing the type I error (which is considered more serious)**

𝑿ഥ **=** 𝑿ഥ **= |( μ μ 0) |( μ μ 1) The critical value** ഥ𝒙 *** must be chosen in such a wa that y $$$P(Reject H0 | H0 is true) =**$$$ Pr(𝑿>(ഥ) ഥ𝒙 ***** | **μ = μ 0** ) **=** - ഥ This condition is met when 𝒙 ***** is the 1 - - percentile of order ( ) of the distribution of 𝑿(ഥ) **under H0 ,** 𝑿(ഥ) **|( μ = μ 0)** ~𝓝( **μ0** , 𝛔(𝟐) / - 𝒏 )= 𝓝(𝟏𝟓, 𝟑. 𝟒) 𝟎 ഥ𝒙 **=** ഥ𝒙 **μ 0 = 15 μ 1 = 21 *** 𝛂 ഥ𝒙 𝛂(𝟎) **Don’t Reject H0 Reject H0**

## Rejection region

Test for **H = 15 vs H = 21. 0: μ 1: μ**

= **Rejection region:** ഥ𝒙> ഥ𝒙𝛂(𝟎) **with** ഥ𝒙𝛂(𝟎) percentile of order (1 - - ) of 𝓝( **μ0** , 𝛔(𝟐) /𝒏 ) = 𝓝(𝟏𝟓, 𝟑. 𝟒) By the relationship between the percentiles of a normal distribution and those of a standardised normal distribution we have:

= ∙ = = ∙ ഥ𝒙𝛂(𝟎) **μ 0** +𝒛𝛂 𝛔(𝟐) /𝒏 **μ 0** +𝒛𝛂 ∙𝑺𝑬(𝑿)(ഥ) **15** +𝒛𝛂 𝟑. 𝟒 Thus, we can define the **rejection region** as **:** ഥ𝒙> **15** + 𝒛𝛂 ∙ 𝟑. 𝟒 - **=0.01? What is the rejection region if you set**

- **# Only for verification**

- **qnorm(0.99,mean=15,sd=sqrt(3.4)) # percentile of order 0.99 under H0 (1) 19.28957**

→ **Rejection region:** ഥ𝒙> 𝟏𝟗. 𝟐𝟗 _We reject_ **H0** _, and we conclude in favour of the hypothesis that the campaign is effective if the sample drawn has a sample mean greater than 19.29_

- **# We will use this:**

- **z_01<-qnorm(0.99)**

- **x_0_alpha<-15+z_01*sqrt(3.4)**

- **x_0_alpha**

- **(1) 19.28957**

## Probability of type II error

Test with - **=** 0.01 the hypotheses **H0: μ = 15 vs H1: μ = 21;
- Rejection region:** ഥ𝒙> 𝟏𝟗. 𝟐𝟗

~~**What probability of not lau**~~ **nching the campaign when in fact it would have been effective?** We want to calculate the probability of **concluding** (on the basis of the test) **that the campaign is ineffective** when in fact it would have ensured the **required average profitability, i.e. 21.** This is the **probability of committing a type II error, and consists of failing to reject H0 (the campaign does not increase average profitability) when it is false (and H1 is true):** ഥ 𝛃= 𝑃 𝑿≤𝟏𝟗. 𝟐𝟗 **μ** = 𝟐𝟏= 𝑷(𝒁≤(𝟏𝟗. 𝟐𝟗−𝟐𝟏)/ 𝟑. 𝟒))

**> beta<-pnorm(19.29,mean=21,sd=sqrt(3.4))**

- **beta<-pnorm((19.29-21)/sqrt(3.4))**

- **beta<-pnorm((x_0_alpha-21)/sqrt(3.4)) # we will use this**

- **beta (1) 0.1768052**

- _=0.01 In order to control the probability of launching an ineffective campaign_ ( ) _we face a much higher probability of making the mistake of not organising an effective campaign_

## Hypotheses and empirical evidence

Test with - **=** 0.01 the hypotheses **H0: μ = 15 vs H1: μ = 21;
- Rejection region:** ഥ𝒙> 𝟏𝟗. 𝟐𝟗

~~**A sample of 50 customers is offered the promotion and (aft**~~ **er an appropriate observation period) a** ~~**n average profitability of 17.9 was found.**~~ **What is the decision?** The observed sample mean is greater than 15, but it **does not** fall into the rejection region. ~~Thus,~~ ~~**H**~~ **0** ~~is not rejected: there is insufficient empirical evidence to conclude that the promotion~~ would guarantee an average profitability of 21 (i.e. the observed sample mean, 17.9 is more compatible with **H0** than with **H1** , given the chosen significance level)

**Consider the statement: "The probability that the decision (based on the observed sample) not to reject H0 - i.e. not to launch the campaign - is wrong is 0.1768 (that is,** - **)"** The statement is false because is unknown and it which of the two **μ is not possible to know** hypotheses is actually true. The mentioned probability **does not** refer to the decision made on the basis of a **specific** sample (the observed one), **but** to the decision made on the basis of a **generic sample.** - **can be interpreted as the % of samples with sample means wrongly** - **! leading to not reject H0. Similar interpretation for**

## Interpretation of significance level

Whether a **decision** on **H0** is correct depends on whether the **actual H0** is true. This is **unknown** because the true value of the parameter of interest is unknown. It is not possible to assign a **:** - and **cannot** probability to the correctness of a specific decision - **be seen as probabilities that a** _**specific decision**_ is incorrect.

Let us assume that **H0** is true, and consider the rejection region of the test and the decisions made on the basis of the sample **means** of all the samples that can be drawn from the population

- The (1 - )x100% of the sample means are in the acceptance region, thus correctly leading not to **reject H0** - The ( )x100% of the sample means leads to the erroneous rejection of **H0**

## Observed significance level (p-value)

We have seen that the **rejection region of a test** is defined on the basis of the significance level set by the researcher.

- Note that setting is equivalent to establishing which sample realisations should be considered as 'extreme' under the null hypothesis (in the direction of the alternative), i.e. so extreme as to be considered 'anomalous' under the null hypothesis.

Another popular way to test hypotheses, implemented by statistical software, is based on the so-called **p-value** (also called observed significance level). **as** Specifically, the p-value is the probability of observing a value of the test statistic that is **extreme** (in the direction of the alternative hypothesis) **or more extreme than** the observed realisation under the assumption that the null hypothesis is true. The p-value is the probability of extracting a sample from the population - under the null hypothesis - that is less favourable to the null hypothesis than the one actually observed.

## Observed significance level (p-value)

Test with - =0.01 to test **H0: μ = 15 vs H1: μ = 21;
- Rejection region:** ഥ𝒙> 𝟏𝟗. 𝟐𝟗 **Sample mean of the drawn sample:** ഥ𝒙 **= 17.9. Determine the p-value.**

𝑿ഥ **=** 𝑿ഥ **= |( μ μ 0) |( μ μ 1)**

**The 'critical tail' for H is the one in the 0 direction of H1 (here, the right tail). Thus the most extreme values (i.e. sample means) are those greater than** ഥ **the observed sample mean,** 𝒙 **= 17.9. The p-value is** 𝑿> 𝟏𝟕. 𝟗 = 𝟏𝟓= 𝑷((ഥ) **μ** = 𝑷(𝒁> (𝟏𝟕. 𝟗−𝟏𝟓)/ 𝟑. 𝟒)

**μ 0 = 15 = 17.9 μ 1 = 21**

**> pvalue<-1-pnorm(17.9,mean=15,sd=sqrt(3.4)) > pvalue<-1-pnorm((17.9-15)/sqrt(3.4)) > pvalue**

**(1) 0.05788884**

## Observed significance level (p-value)

Test with - =0.01 to test **H0: μ = 15 vs H1: μ = 21;
- Rejection region:** ഥ𝒙> 𝟏𝟗. 𝟐𝟗. **Sample mean of the drawn sample: = 17.9; p-value=0.05789** ~~The p-value~~ ~~**quantifies how**~~ ~~_**extreme**_~~ ~~**the observed sample is under H**~~ **0 (in the direction of H1** ) while - actually indicates the 'anomaly level' the researcher is willing to accept. **-** - A - **high p-value** - in particular **greater than** indicates that the observed sample is not particularly anomalous and is in any case less extreme than the threshold defined on the basis of - **. H** It indicates that the empirical evidence **supports H0** more than **1** - A **less than** - **low p-value** - in particular - indicates that it is very unlikely (or at least more - **H** unlikely than what is tolerable on the basis of ) to extract a sample less favourable to **0** than the one observed, given a population whose parameter (here the mean) is the one **H H** . specified by **0** ! It therefore leads to reject **0**

The **p-value** is the **smallest significance level** at which **H0** can be **rejected.** In our example any significance level smaller than **0.05789** leads to not reject **H0** (as the p-value will be greater than - - ). Therefore, even if one builds a test with greater than 0.01 (as long as it is smaller than 0.05789), the observed sample would not lead to reject **H0**

## Observed significance level (p-value)

- **Statistical hypothesis testing can also be conducted using the p-value instead of the critical region:**

- The realisation of the test statistic given the observed sample is calculated.

- The p-value is calculated (i.e., **assuming H0 is true** , the probability of observing a realisation more extreme than the one observed, or the probability of drawing from the population a sample less favourable to **H0** than the observed one)

- The p-value is compared with the significance level,

- - **H** If the p-value < , we reject **0**

- If the p-value - - , we do not reject **H0**

This approach is the one **usually implemented by statistical software,** because it avoids the - definition of a rejection region based on a specific value of , and provides a result that allows a decision to be made on the basis of the desired value of - , whatever it may be, as well as to **H .** assess how extreme the sample is under **0**

On the other hand, the rejection region approach is more suitable when a test with the same level of - has to be applied repeatedly based on different samples (e.g. in quality control).

## Extension to composite hypotheses

- How does the test (the rejection region) **with significance level** change when we consider the hypotheses **H0: μ ≤ μ 0 and H1: μ = μ 1 (i.e. if H0 is composite rather than simple)** ?

ഥ ഥ ഥ𝑿 **|( μ = μ '0 )** 𝑿 **|( μ = μ ) 0** 𝑿 **|( μ = μ ) 1**

The rejection region shape **does not change: rejection region:** ഥ𝒙> ഥ𝒙 *** The critical** tail is still the **right tail:** very **high** ഥ values of 𝒙 still **point to H1** and lead to the **. rejection of H0**

ഥ Furthermore, for any 𝒙 ***, we note that if we consider ' μ 0 < μ 0**

**μ 0 = 15 μ 1 = 21**

𝑿> ഥ𝒙 *** =** 𝑿> ഥ𝒙 *** =** 𝑷((ഥ) **| μ μ’ 0** ) < 𝑷((ഥ) **| μ μ 0** ) **Thus most critical value for H μ 0 is the 0 as it is the one 'closest' to H . 1**

**The probability of incurring a type I error (as well as the p-value) is highest when μ = μ 0! Thus, the rejection region and the critical value are the same as those used to test H0: μ = μ 0 vs H1: μ = μ 1**

## Extension to composite hypotheses

- How does the test (the rejection region) **with significance level** change when we consider the hypotheses **H0: μ ≤ μ 0 and H1: μ > μ 0 (i.e. if both H0 and H1 are composite)** ?

ഥ𝑿 **= |( μ μ 0)**

Here **H1** does not specify any value for - **; even so, the shape of the rejection region depends on the relationship between H0 and H1!** The rejection region’s **does not change Rejection region:** 𝒙>ഥ ഥ𝒙 ***** ഥ very **high** values of 𝒙 still **point to H1** and lead to the **rejection of H0**

**μ 0 = 15**

**The value of** ഥ𝒙 *** is based on H0 , on the direction of H1, and on the most critical value for H0, which is the one 'closest' to H1, that is still μ 0! Thus, the test is identical to that built to verify H = = 0: μ μ 0 vs H1: μ μ 1 > μ 0**

## One-sided left-tailed test: Efficiency of a call centre

The Average Handling Time (AHT), which is used to assess the efficiency of call centres, refers to the average total time taken by an operator to handle a user’s call, including the time needed to perform all necessary tasks after the call is closed. In a call centre, the average AHT of the operators (in a certain time slot on a weekday) is 10 minutes, with a standard deviation σ=3 minutes. One wants to assess whether a course for training operators is effective and leads to a reduction of the average AHT to less than 8 minutes. Given its costs, the course is initially given to 50 operators: an average AHT of 7.05 minutes is recorded (over an appropriate observation period). Would you recommend to proceed and give the course to all the operators (assume that σ does not change after the course)? **Hypotheses compared?** We are interested in assessing whether the training course is effective or not, i.e. whether: **μ < 8 (effective course: average AHT is below the minimum desired threshold) μ ≥ 8 (ineffective course: the average AHT is greater than or equal to the minimum desired threshold)**

## One-sided left-tailed test: null and alternative hypothesis

**Identification of null and alternative hypotheses** Contrasted hypotheses: **μ < 8 (effective course) and μ ≥ 8 (ineffective course).** The two possible errors that can be made using a statistical test are: **(Reject μ < 8 | < μ < 8 ) = (Fail to reject μ ≥ 8 | μ < 8)** → **miss the opportunity for effective training (Accept μ < 8 | μ ≥ 8)** ) **= (Reject μ ≥ 8 8 | μ ≥ 8)** → **invest in ineffective training**

The company is only interested in investing in the course if it is effective, given the costs, so the most serious mistake is the second one **.**

Assume **μ ≥ 8 unless the empirical evidence is clearly against this assumption and supports the hypothesis that the training course is indeed effective So:**

**H0: μ ≥ 8 and H1: μ < 8**

## One-sided left-tailed test: rejection region

We want to test the two **composite** hypotheses **H0: μ ≥ 8 vs H1: μ < 8** .

ഥ𝑿 **= |( μ μ 0)**

In this case, the **critical tail for the null hypothesis is the left tail.** The shape of the rejection region **is: Rejection region:** 𝒙<ഥ ഥ𝒙 ***** relatively **small** values **of** ഥ𝒙 will lead to **lean towards H1** and **reject H0.**

**μ 0 = 8**

**The determination of** ഥ𝒙 *** is based on H0, on the direction of H1, and on the most critical value for H0, that is the one 'closest' to H1, which is . μ=8 0**

## One-sided left-tailed test: rejection region

We want to test the two **composite** hypotheses **H0: μ ≥ 8 vs H1: μ < 8** . **Which rejection** - **? region set, given the significance level**

**The critical value** ഥ𝒙 *** is chosen such that the maximum $$$P(Reject H0|H0 is true)$$$** ഥ **=** Pr(𝑿≤(ഥ) 𝒙 ***** | **μ = μ 0** ) **=** - This condition is met when ഥ ഥ 𝟎 𝒙 **=** 𝒙 ***** 𝟏−𝛂

- of the distribution of the percentile of order ഥ 𝑿 **when with μ=μ 0**

ഥ 𝑿 **|( μ = μ 0)** ~𝓝( **μ0** , 𝛔(𝟐) /𝒏 )= 𝓝(𝟖, 𝟗/𝟓𝟎) (remember that σ=3 and 𝑛=50).

- **One-sided left-tailed test: rejection region at level**

Test for **H0: μ ≥ 8 vs H1: μ < 8.**

𝟎 𝟎 = **Rejection region:** ഥ𝒙> ഥ𝒙𝟏−𝛂 **with** ഥ𝒙𝟏−𝛂 percentile of order - of a 𝓝(𝟖, 𝟗/𝟓𝟎 ) For the relationship with the percentiles of the standardised normal we have: 𝟎 ഥ𝒙𝟏−𝛂 = **μ 0** +𝒛𝟏−𝛂 ∙ 𝛔(𝟐) /𝒏= **μ 0** −𝒛𝛂 ∙ 𝛔(𝟐) /𝒏 = **μ 0** −𝒛𝛂 ∙𝑺𝑬(𝑿) =(ഥ) 𝟖 −𝒛𝛂 ∙ 𝟗/𝟓𝟎 It is convenient to write the **rejection region** as **:** ഥ𝒙< 𝟖 −𝒛𝛂 ∙ 𝟗/𝟓𝟎 **=** - **0.025? What rejection region if you set**

- **# only for verification**

- **qnorm(0.025,mean=8,sd=sqrt(9/50)) # percentile of N|H0 (1) 7.168458**

- **# percentiles N(0,1)**

**> z_975<-qnorm(0.025) # -1.959964 > z_025<-qnorm(0.975) # 1.959964 > # We will use this**

- **x_0_alpha<-8-z_025*sqrt(9/50)# same value**

→ **Rejection region:**

_We reject_ **H0** _if the drawn sample has a sample mean of less than 7.168_

- **x_0_alpha**

- **(1) 7.168458**

## One-sided left-tailed test: Statistical decision and p-value

Test with - **=** 0.025 to verify **H0: μ ≥ 8 vs H1: μ < 8;
- Rejection region:** ഥ𝒙< 𝟕. 𝟏𝟔𝟖 **The average AHT after the course for the 50 selected operators is 7.05. What decision?** The observed sample mean is less than 7.168 and thus falls into the rejection region. Therefore we reject **H0** and conclude **at level 0.025** that the course is effective (i.e. the observed sample mean, 7.04 is more compatible with **H1** than with **H0** , given the chosen significance level) **What is the p-value of the sample realisation? What considerations?** The p-value is the probability of observing a sample realisation more extreme than the observed one in the direction of **H1** under the hypothesis that **μ = μ 0** ; in our case it is 𝑷(𝑿< 𝟕. 𝟎𝟓(ഥ) **μ** = 𝟖= 𝑷(𝒁< (𝟕. 𝟎𝟓−𝟖)/ 𝟗/𝟓𝟎)

**> pvalue<-pnorm((7.05-8)/sqrt(9/50)) > pvalue (1) 0.01257238**

_**Obviously,** even on the basis of the p-value, we would reject_ **H0** _at the 0.025 level, because the sample realisation is more extreme than deemed acceptable. However, note that if one sets a significance level of 0.01 or 0.001, for example,_ **H0** _would not be rejected_

## Two-sided test: Bicycle lanes and PM10

**Ideally, the construction of cycle lanes should reduce traffic and pollution. However some argue that narrower carriageways will slow down traffic and have exactly the opposite effect.** Consider data on the level of PM10 in a busy London street, where the last section of a cycle path was completed in April 2016. ~~The average PM10 level measured in 2015 was 41,~~ with a variance of 207. We want to assess the impact of the cycle lane on the average PM10 level based on a sam ple of 30 measurements taken one month after the cycle lane was opened, assuming that the PM10 distribution is normal.

**How would you set up hypothesis testing?** We are interested in testing hypotheses concerning **μ** = average PM10 level one month after the opening of the cycle track. To determine which hypotheses to compare, we consider the error of **wrongly** concluding in favour of one of the two positions concerning the impact of the cycle track on the level of pollution to be the most serious.

**H** = **41** → **no effect 0: μ = μ 0** the cycle track has on the average PM10 level **H1: μ** ≠ **μ 0** → the cycle track has an effect (positive or negative) on the average PM10 level

## Two-sided test

= = **41 vs. H** ≠ **Testing the hypotheses H0: μ μ 0 1: μ μ 0** The test statistic is always 𝑿(ഥ) and 𝑿|(ഥ) **μ0** ~𝓝( **μ0** , **207/30** )= 𝓝( **41** , **6.9** )

ഥ𝑿| **μ0** ~𝓝( **41** , **6.9** ) **The sample realisations 'critical' for H0 are those far from H0** _**towards**_ **H1 Given the** _**two-sided**_ **structure of H1** , **H0** should be **rejected** if the **observed sample mean:** - is too **high** to be considered **consistent** with an average of **41** (so the empirical evidence supports the idea that the cycle track **increases average PM10 levels** );

**μ 0 = 41**

- is too **small** to be considered **consistent** with an average of **41** (so the empirical evidence supports the idea that the cycle track **decreases average PM10 levels)**

## Two-sided test: rejection region

# = = **41 vs. H** ≠ **Testing the hypotheses H0: μ μ 0 1: μ μ 0**

ഥ 𝑿| **μ0** ~𝓝( **41** , **6.9** ) In this case, **both tails are critical: it is reasonable to reject H0 when the value of** ഥ 𝑿| **μ0** ~𝓝( **41** , **6.9** ) **is** _**extreme**_ **under H0** _**in one of**_ **the directions indicated by H1 Rejection region:**

**μ 0 = 41** ഥ𝒙 ***** _**L**_ **Reject H0 Don’t Reject H0**

𝒙<ഥ ഥ𝒙 ***** or   𝒙>ഥ ഥ𝒙 ***** _**L U reasonably assuming that the two critical values are symmetrical with respect to**_ **μ 0** ഥ𝒙 ***** _**U**_

**How to choose** 𝒙ഥ ***** _**L**_ and 𝒙ഥ ***** _**U ?**_

**Reject H0**

## Two-sided test: rejection region

**Test the hypotheses H0: μ** = **μ 0** = **41 vs H1: μ** ≠ **μ 0 . Which rejection region given the** - **? significance level**

ഥ ഥ 𝒙 ***** and 𝒙 ***** _**L U**_ **must be chosen in such a way that $$$P(Reject H0 |H0 is true) =**$$$ Pr(𝑿<(ഥ) ഥ𝒙 ***** _**L**_ | **μ = μ 0** )+ Pr(𝑿>(ഥ) ഥ𝒙 ***** _**U**_ | **μ = μ 0** ) **=** - **Since the two directions** are **indifferent:** Pr(𝑿<(ഥ) ഥ𝒙 ***** _**L**_ | **μ = μ 0** ) **=** Pr(𝑿>(ഥ) ഥ𝒙 ***** _**U**_ | **μ = μ 0** ) **=** - **/2** This condition is ensured by the **percentiles of - order** - **/2** and (1 - **/2** ) of the distribution of 𝑿|(ഥ) **μ0** , which are conveniently expressed as: ഥ 𝟎 𝒙 = −𝒛 ∙ 𝛔(𝟐) 𝟏−𝛂/𝟐 **μ 0** 𝛂/𝟐 /𝒏 𝟎 ഥ𝒙𝛂/𝟐 = **μ 0** +𝒛𝛂/𝟐 ∙ 𝛔(𝟐) /𝒏

**Reject H0 Don’t Reject H0**

**Reject H0**

## Two-sided: fitting with confidence interval

# Test the hypotheses H0: μ** = **μ 0** = **41 vs H1: μ** ≠ **μ 0 . Which rejection region, given the** - **? significance level

ഥ 𝑿| **μ0** ~𝓝( **41** , **6.9** )

- **/2** - **/2 μ 0 = 41** 𝟎 𝟎 ഥ𝒙 ഥ𝒙 𝟏−𝛂/𝟐 𝛂/𝟐 **Reject H0 Don’t Reject H0 Reject H0**

**Note that the rejection region is** ഥ ഥ 𝒙< **μ0 –** _**z**_ - **/2** ∙ 𝛔(𝟐) /𝒏 **OR** 𝒙> **μ0 +** _**z**_ - **/2** ∙ 𝛔(𝟐) /𝒏 ∙ → **|** ഥ𝒙− **μ0 | >** _**z**_ - **/2** 𝛔(𝟐) /𝒏 **Thus the acceptance region for H0 is:** ഥ ∙ ∙ **μ0 –** _**z**_ - **/2** 𝛔(𝟐) /𝒏 **≤** 𝒙 **≤ μ0 +** _**z**_ - **/2** 𝛔(𝟐) /𝒏 ഥ ഥ **–** ∙ ∙ → 𝒙 _**z**_ - **/2** 𝛔(𝟐) /𝒏 **≤ μ0 ≤** 𝒙 **+** _**z**_ - **/2** 𝛔(𝟐) /𝒏 **The acceptance region coincides with the 1-** - **. We confidence interval at level ( ) for μ don’t** _**is included in the**_ **reject H0 if μ 0** - _**confidence interval at level**_ **(1- )** _**for**_ **μ**

- **Two-sided test: rejection region at level**

= = **41 vs H** ≠ **Build a test with significance level 0.05 for H0: μ μ 0 1: μ μ 0** (recall that 𝑿|(ഥ) **μ0** ~𝓝( **41** , **6.9** ))

𝟎 𝟎 **Rejection region:** ഥ𝒙< ഥ𝒙 **or** ഥ𝒙> ഥ𝒙 𝟏−𝛂/𝟐 𝛂/𝟐 which can be written using the percentiles of the standardised normal as:

𝛔(𝟐) ഥ𝒙< ∙ 𝛔(𝟐) **or** ഥ𝒙< ∙ **μ0** −𝒛𝛂/𝟐 /𝒏 **μ0** + 𝒛𝛂/𝟐 𝒏 → **|** ഥ𝒙− **μ0 |** > 𝒛𝛂/𝟐 𝛔(𝟐) /𝒏

- **z_025<-qnorm(0.975)**

> **> x_0_L_alpha_2<-41-z_025*sqrt(6.9)** _We reject_ **H0** _if the extracted sample has_ **> x_0_U_alpha_2<-41+z_025*sqrt(6.9)** ഥ𝒙 **< 35.8516** _or_ ഥ𝒙 **> 46.1484 > x_0_L_alpha_2**

> **(1) 35.8516** _or, equivalently when_ **> x_0_U_alpha_2 (1) 46.1484 |** ഥ𝒙− **41 | is greater than 5.1484**

- **(1) 46.1484**

- **z_025*sqrt(6.9)**

- **(1) 5.148404**

- **Two-sided test: rejection region at level**

**0.05 level test for H0: μ** = **μ 0** = **41 vs H1: μ** ≠ **μ 0** . Rejection region: **|** ഥ𝒙− **41 |** > **5.15 – – What is the probability to conclude based on the test that the cycle track has no effect on the average PM10 level (which therefore remains 41) when in fact it provides a 10% reduction?**

This is the probability of the test **failing to reject H0 when it is false,** when in fact the construction of the cycle path leads to a reduction in the average PM10 level from 41 to **36.9:** 𝑷(|𝑿−(ഥ) **41| ≤ 5.15 | μ = 36.9** ) = 𝑷( **41 – 5.15 ≤** 𝑿(ഥ) **≤ 41 + 5.15 | μ = 36.9** )

- **pnorm(41+5.15,mean=36.9,sd=sqrt(6.9))+    pnorm(41-5.15,mean=36.9,sd=sqrt(6.9)) (1) 0.655107**

- **Two-sided test: rejection region at level**

**0.05 level test for H0: μ** = **μ 0** = **41 vs H1: μ** ≠ **μ 0** . Rejection region: **|** ഥ𝒙− **41 |** > **5.15 For 30 measurements of PM10 taken one month after the opening of the cycle path, an average of 33.5 was recorded. What conclusions?**

**– Since (33.5-41)= 7.5 we reject H0 and conclude that the cycle track has an effect on the average PM10 level.** Such a **low** sample mean (thus extreme on the tail 'favourable' to the hypothesis **H1** that the cycle track leads to a reduction in the average PM10 level) is more likely due to a difference between and **41** . **μ**

**What is the p-value of the observed sample realisation?**

**H:** This is the probability of observing an even more extreme value than that observed under **0** 𝑷(|𝑿−(ഥ) **41 |** > **7.5 | μ = 41** ) = 𝑷(|𝒁 **|** > 𝟕. 𝟓 **/** 𝟔. 𝟗 ) = 𝟐𝑷(𝒁> 𝟕. 𝟓 **/** 𝟔. 𝟗 )

**> 2*(1-pnorm(41+7.5,mean=41,sd=sqrt(6.9))) (1) 0.004300957**

**> # We will use this: > 2*(1-pnorm(7.5/sqrt(6.9))) (1) 0.004300957**

The p-value is extremely low! The observed sample realisation would be definitely extreme/anomalous if indeed **μ** = **41**

## Test of level** - **on** _**n**_ 𝛔(𝟐) **known μ (Normal population or large ) -

## Test of level** - **on** _**n**_ 𝛔(𝟐) **unknown μ (Normal pop. or large ) -

In the case of a **normal population, if** the variance 𝛔(𝟐) is **unknown** , it could be reasonably 𝒔(𝟐) estimated by the sample variance, , but the percentiles **change.**

Indeed in **this case** the sample mean is **not a test statistic,** since 𝑿|(ഥ) **μ0** ~𝓝( **μ0** , 𝛔(𝟐) /𝒏); the distribution of the statistic under **H0** is not completely known  because it **depends on** 𝛔(𝟐) **, that is unknown!**

## However, as we discussed for confidence intervals:

(this is why, even when the variance is known, with “test statistic” we typically refer to the sample **.** mean standardized using its standard error)

When the **sample is large** , it is possible to use the **normal approximation also when the variance is unknown. Even so, statistical software typically use the percentiles of the Student’s** _**t**_ **distribution, in order to account for the further uncertainty due to the fact that the variance is estimated.**

## Test of level** - **on when** 𝛔(𝟐) **Student’s μ is unknown ( t)

## Rstudio: TEST.mean()

The **TEST.mean()** function in the **UBStats** package determines the p-value of a sample realisation given the hypotheses tested.

The syntax is very similar to that of the **CI.mean()** function:

**TEST.mean(x, sigma=NULL, mu0=0, alternative="two.sided", digits=2, data)**

- where:

- **x** is a **numeric** vector or the name of one of the columns of the dataframe specified in **data**

- **sigma** is the value of the standard deviation, **if known**

- **mu0** is the value of the mean under the null hypothesis (0 by default)

- **alternative** defines the type of test, specifying the direction of the alternative hypothesis: onesided left-tailed ( **alternative="less"** ), one-sided right-tailed ( **alternative="greater"** ) and two-sided ( **alternative="two.sided"** , default).

- **digits** is the number of decimals used to round the reported statistics

## Hands on: time on social

The time spent by users watching content posted on a social network - including advertisements - is an indicator of the platform’s potential for marketing purposes. One specific platform modified the algorithm selecting the displayed content in order to increase the average daily time on the platform compared to the  previous 34 minutes. The dataframe* **Time_Social** contains information on the time spent on the platform in a specific day ( **Time** , in minutes) by a sample of (active) users. **Based on the data collected, can you conclude that indeed the change in the algorithm led to an increase in the average time spent on the platform?**

**The null hypothesis** states **the status quo, H0: μ** = **34** while the alternative is the hypothesis we want to verify, **H1: μ** > **34. The sample size is sufficiently high.**

**> TEST.mean(x=Time,mu0=34,alternative="greater",data=Time_Social) Test hypotheses on mean**

**Variance: unknown**

**or Null hypothesis H0:** **`μ = 34 μ ≤ 34` Alternative hypothesis H1:** **`μ > 34` n xbar s_X se  stat p-value Normal.Approx 5976 35.6 7.82 0.1 15.87 <0.0001 Student-t     5976 35.6 7.82 0.1 15.87 <0.0001**

_The null hypothesis is rejected at any significance level set by the company: we conclude in favour of the hypothesis that the mean time has increased_

* All the dataframes used are in file **Lesson 17-21_Data.Rdata**

**Hypothesis testing Test on the difference between means**

## Test on the difference between means: test statistic

**To verify hypotheses on the difference between two populations’ means the test statistic is the difference between the sample means standardized or “studentized” under the null hypothesis depending on whether the standard error of the difference between the sample means, 𝑺𝑬** ഥ𝑿−ഥ𝒀ഥ𝑿−ഥ𝒀 **, is known or has to be estimated.**

**The expression of** 𝑺𝑬ഥ𝑿−ഥ𝒀 **depends** on the assumptions on the populations ( **independent or paired** ) and on their variance, that also determine the distribution of the test statistic and the percentile it has to be compared to (as seen for tests on the mean).

For a given **H0:** 𝛍𝑿 −𝛍𝒀 =  𝛅 **0** o **H0:** 𝛍𝑿−𝛍𝒀 ≤ 𝛅 **0** o **H0:** 𝛍𝑿 −𝛍𝒀 ≥ 𝛅 **0** , the test statistic is: 𝑿−((ഥ)) 𝛅 (((ഥ)) 𝒀) − **0** - Case of known variances (normal or large samples): ~𝓝(𝟎, 𝟏)

𝑿−((ഥ)) 𝛅 (((ഥ)) 𝒀) − **0** ~𝓝(𝟎, 𝟏) 𝑺𝑬 ഥ𝑿−ഥ𝒀 𝑿−(ഥ) 𝛅 ((ഥ) 𝒀) − **0** ෢ 𝑺𝑬 ഥ𝑿−ഥ𝒀

- Case of unknown variances:

In the case of **normal distributions (and of joint normal distribution for paired samples)** , the statistic has a Student’s _**t**_ distribution (with degrees of freedom depending on assumptions on populations and variances). In the case of **large samples** the distribution can be approximated by a – **normal** , but as seen in the case of tests on the population’s mean – the **Student’s** _**t**_ can also be used if one wants to account for the extra uncertainty due to the estimation of the variances.

## Test on the difference between means: test statistic

Expressions of standard errors and distibution of the test statistic in the different cases

* See the book for the df in the case of independent samples with unknown different variances

## Rstudio: TEST.diffmean() for independent samples

The **TEST.diffmean()** function - similar to the **CI.diffmean()** function - tests hypotheses on the difference between means. Two approaches can be used for **independent** samples. **: Samples stored in two distinct vectors: approach based on two vectors x, y**

**TEST.diffmean(x, y, type="independent", mdiff0=0, alternative="two.sided", sigma.x=NULL, sigma.y=NULL, var.test=FALSE, digits=2, data)** where:

-: names of two **numerical data.** The function

- **x,y** vectors possibly names of two variables in **-**

- tests hypotheses on **`μ_x μ_y`**

- **type="independent"**: specifies that the samples are independent (default) and not paired

- **sigma.x,sigma.y:** allow **standard deviations** to be specified, if **known** ; in the case of known and equal variances, it is sufficient to specify only one of the two inputs

- **mdiff0** is the value of the difference **`μ_x μ_y`** under the null hypothesis (0 by default) - **alternative** defines the type of test, and specifies the direction of the alternative hypothesis (one-sided left-tailed test, **"less",** or right-tailed, **"greater"** ; two-sided, **"two.sided"** ).

- **var.test** allows (by setting **var.test=TRUE** ) to test the hypothesis that the two (unknown) variances are equal (we do not go into the details of this test, we only comment on the output).

- **digits** is the number of decimals used to round the reported statistics

## Rstudio: TEST.diffmean() for independent samples

**(OPTIONAL)**

The **TEST.diffmean()** function - similar to the **CI.diffmean()** function - tests hypotheses on the difference between means. Two approaches can be used for **independent** samples. **Samples obtained by splitting a vector x based on a 2-levels vector, by:**

**TEST.diffmean(x, by, type="independent", mdiff0=0, alternative="two.sided", sigma.by=NULL, var.test=FALSE, digits=2, data)** where:

- **x,by**: two vectors with same **length** ordered so that their corresponding entries refer to the same **unit;**

**x** is the name of a **numeric vector** while **by** is the name of a vector **that takes only two values x by1 by2** (considering standard, alphabetical, numeric or level order in a factor). Possibly **-** and/or **by** can be the names of variables in **data.** The function tests hypotheses on **`μ_by1 μ_by2`**

- **type="independent"**: specifies that the samples are independent (default) and not paired

- **x**

- **sigma.by:** vector containing the standard deviations of in the two groups (see manual*).

- **mdiff0** is the value of the difference **`μ_by1 μ_by2`** under the null hypothesis (0 by default) - **alternative** , **var.test** , **digits** defined as before

* In the case of known variances we suggest using the **x,y** approach

## Rstudio: TEST.diffmean() for paired samples

The **TEST.diffmean()** function in the case of hypothesis testing for the difference between the means of **paired** samples has the following syntax:

**TEST.diffmean(x, y, type="paired", mdiff0=0, alternative="two.sided", sigma.d=NULL, digits=2, data)** where:

-: name of two **numeric** vectors ordered so that the elements refer to the same unit or names of

- **x,y -**

- two numeric columns in the dataframe specified in **data.** The function tests hypotheses on **`μ_x μ_y`**

- **type="paired"**: specifies that the samples are paired

- **sigma.d:** allows the standard deviation of the **difference** to be specified, if **known**

- **mdiff0** is the value of the difference **`μ_x μ_y`** established under the null hypothesis (0 by default)

- **alternative** , **digits** defined as for the case of independent samples

## Hands on: time on social

The dataframe **Time_Social** also includes information on the area where sampled users live. **On the basis of the data at hand, can you conclude that users in areas A and B are homogeneous with respect to the average time spent on the platform, or would you suggest adopting different algorithms for content selection for the two areas?** – **–** – **We are interested to test H0: μ A μ B = 0 (or H0: μ A** = **μ B or H0: μ B μ A = 0) vs H1: μ A μ B** - **0 (or H1: μ A** - **μ B o H0: μ B – μ A** - **0)**

The two samples are **independent**

**time.A<-Time_Social$Time(Time_Social$Area=="A") time.B<-Time_Social$Time(Time_Social$Area=="B")**

**# type not specified because type="independent" by default # approach based on x,y**

**> TEST.diffmean(x=time.A,y=time.B,mdiff0=0,alternative="two.sided")**

**# approach based on x,by: identical output as A "<" B**

**> TEST.diffmean(x=Time,by=Area,mdiff0=0,alternative="two.sided", data=Time_Social)**

Note that when **H0** states a specific difference between two means (for example, 0) and the – – alternative is **bilateral** it is indifferent to set **H0: μ A μ B =0** or **H0: μ B μ A =0**: only the **sign of the test statistic changes, but the statistical decision is the same (values on both tails are extreme)**

## Hands on: time on social

**> TEST.diffmean(x=time.A,y=time.B,mdiff0=0,alternative="two.sided") -** **`Test hypotheses on μ_x μ_y` Samples: independent Variances: unknown x = time.A y = time.B -** **`Null hypothesis H0: (μ_x μ_y) = 0` -** **`Alternative hypothesis H1: (μ_x μ_y) ≠ 0` Unknown variances assumed to be equal n_x  n_y  xbar  ybar xbar-ybar  s_X  s_Y  se  stat p-value Normal.Approx 3053 2923 35.39 35.83     -0.43 7.66 7.97 0.2 -2.13   0.033 Student-t     3053 2923 35.39 35.83     -0.43 7.66 7.97 0.2 -2.13   0.033 Unknown variances assumed to be different n_x  n_y  xbar  ybar xbar-ybar  s_X  s_Y  se  stat p-value Normal.Approx 3053 2923 35.39 35.83     -0.43 7.66 7.97 0.2 -2.13  0.0332 Student-t     3053 2923 35.39 35.83     -0.43 7.66 7.97 0.2 -2.13  0.0332**

_**The statistical decision depends on the significance level set. If**_ 𝛂 **> 0.033,** _**H0 is rejected, and we conclude that the mean time is different in the two areas, otherwise the null hypothesis of homogeneity between the two areas is not rejected. Note that the conclusion is the same irrespective of the assumptions on variances and distribution used.**_

* Please refer to the script for results based on the **x,by** syntax

## Hands on: time on social

**Comment on the statement: “Empirical evidence leads to the rejection of H 0 at the 0.05 level; therefore H0 is false with probability 0.05”**

The statement is false:

- concerns a decision made on the basis of a sample, on the quality of which we cannot draw any kind of conclusion. In particular, the sample could be one of those (5%) that leads to wrongly rejecting the null hypothesis (Type I error).

- In fact, we note that if one chooses a level of - **lower than 0.03, e.g. 0.01,** the null

- hypothesis would not be rejected.

- Furthermore, **H0** is either true or false and it makes no sense to associate a probability with

- a non-random event.

## Hands on: time on social

The dataframe **Time_Social** includes information about the activation of push notifications ( **Push** ). **Can we conclude that users with push notifications (Push="Yes") spend more time on the platform, assuming that the variances in the two groups of users are the same? – – We are interested to H0: μ Yes** ≤ **μ No** (or **μ Yes μ No** ≤ 0) vs **H1: μ Yes** > **μ No** (or **μ Yes μ No** > 0) and It is convenient to analyse into details the differences between the syntaxes based on **x,y x,by**

**# approach based on x,y time.yes<-Time_Social$Time(Time_Social$Push=="Yes") time.no<-Time_Social$Time(Time_Social$Push=="No") TEST.diffmean(x=time.yes,y=time.no,mdiff0=0,alternative="greater")**

**–** Note that **No** ≺ **Yes** ; therefore if the **x,by** syntax is used the hypotheses refer to **μ No μ Yes** , and to properly verify the considered hypotheses we need to set

**H0: μ No ≥ μ Yes** (or **μ No – μ Yes ≥** 0) vs **H1: μ No** < **μ Yes** (or **μ No – μ Yes** < 0)

**# approach based on x,by TEST.diffmean(x=Time,by=Push,mdiff0=0,alternative="less",data=Time_Social)** _**Be careful when using x,by with one-sided assumptions, as the order in the difference is the standard one (here alphabetical), and cannot be controlled unless a suitable factor is defined**_ **- We suggest using x,y with one-sided assumptions so that** **`μ_x μ_y` can be controlled**

## Hands on: time on social

**> TEST.diffmean(x=time.yes,y=time.no,mdiff0=0,alternative="greater") - Test hypotheses on** **`μ_x μ_y` Samples: independent Variances: unknown** 𝛂 **.** _**Based on the observed sample, we reject**_ **H00 x = time.yes**

_**The p-value is extremely low and lower than any standard level of**_ 𝛂 **.** _**Based on the observed sample, we reject**_ **H00** _**, concluding that users with or without push notifications spend a different time on average on the platform.**_

**y = time.no**

**- - Null hypothesis        H0: (** **`μ_x μ_y` ) = 0 or (** **`μ_x μ_y) ≤ 0` - Alternative hypothesis H1: (** **`μ_x μ_y` ) > 0**

**Unknown variances assumed to be equal**

**n_x  n_y  xbar  ybar xbar-ybar  s_X  s_Y  se  stat p-value Normal.Approx 2836 3140 37.15 34.21      2.94 7.81 7.56 0.2 14.78 <0.0001 Student-t     2836 3140 37.15 34.21      2.94 7.81 7.56 0.2 14.78 <0.0001**

**> TEST.diffmean(x=Time,by=Push,mdiff0=0,alternative="less",data=Time_Social) - Test hypotheses on** **`μ_x μ_y` Samples: independent Variances: unknown**

**x = Time|Push=No**

**y = Time|Push=Yes**

**- - Null hypothesis        H0: (** **`μ_x μ_y` ) = 0 or (** **`μ_x μ_y) ≥ 0` - Alternative hypothesis H1: (** **`μ_x μ_y` ) < 0**

**Unknown variances assumed to be equal**

**n_x  n_y  xbar  ybar xbar-ybar  s_X  s_Y  se   stat p-value Normal.Approx 3140 2836 34.21 37.15     -2.94 7.56 7.81 0.2 -14.78 <0.0001 Student-t     3140 2836 34.21 37.15     -2.94 7.56 7.81 0.2 -14.78 <0.0001**

## Hands on: software to improve productivity

A company is evaluating whether to switch to a new administration software to increase the average employees’ productivity. For the transition to the new software, it is deemed appropriate to organise training courses that are known to be effective. To organise the transition, the 130 employees of two departments (who can be considered as a representative random sample) are initially involved. The dataframe **Transition** contains information on the productivity of each employee with the old sw ( **Pre** ) and with the new one ( **Post** ) (after a certain period of use), and on the employees’ department ( **Department** ). **It is of interest to verify whether, as expected/desired, the employees average productivity increases with the new software, and in particular whether the average increase is greater than 6.5. Paired** samples: productivity of each employee with the old ( **Pre** ) and the new ( **Post** ) software Using a precautionary approach we set as null the hypothesis that the new software doesn’t increase the mean productivity as much as required and as alternative the hypothesis that the mean productivity increases more than required. The large sample size allows to test the hypotheses even without assuming joint normality ^yh1cau
*(See also: [[Lecture 17-21 Slides_Hypotheses Testing#^zbhy88]])*

**# it is necessary to specify type="paired" since by default # the function applies the test for independent samples TEST.diffmean(x=Post,y=Pre,mdiff0=6.5,type="paired", alternative="greater",data=Transition)**

## Hands on: software to improve productivity

**> TEST.diffmean(x=Post,y=Pre,mdiff0=6.5,type="paired", +               alternative="greater", data=Transition) - Test hypotheses on** **`μ_x μ_y` Samples: paired Variance: unknown**

**x = Post**

**y = Pre**

**- - Null hypothesis        H0: (** **`μ_x μ_y` ) = 6.5 or (** **`μ_x μ_y) ≤ 6.5` - Alternative hypothesis H1: (** **`μ_x μ_y` ) > 6.5 n  xbar  ybar dbar=xbar-ybar   s_D   se stat p-value Normal.Approx 130 57.39 47.95           9.44 12.69 1.11 2.64   0.004 Student-t     130 57.39 47.95           9.44 12.69 1.11 2.64   0.005**

## Based on the output above, how are the p-values determined?

𝟐 𝑷 𝒁> (ഥ𝒙−ഥ𝒚− 𝛅 **0** )/ 𝒔𝑫/𝒏= 𝑷 𝒁> (𝟓𝟕. 𝟑𝟗−𝟒𝟕. 𝟗𝟓− 𝟔. 𝟓)/ 𝟏𝟐. 𝟔𝟗/ 𝟏𝟑𝟎 𝟐 𝑷 𝒕𝟔𝟒 > (ഥ𝒙−ഥ𝒚− 𝛅 **0** )/ 𝒔𝑫/𝒏= 𝑷 𝒕𝟔𝟒 > (𝟓𝟕. 𝟑𝟗−𝟒𝟕. 𝟗𝟓− 𝟔. 𝟓)/ 𝟏𝟐. 𝟔𝟗/ 𝟏𝟑𝟎

**> 1-pnorm((57.39-47.95-6.5)/(12.69/sqrt(130)))**

**(1) 0.004126489**

- **1-pt((57.39-47.95-6.5)/(12.69/sqrt(130)),df=129) (1) 0.004636723**

## Hands on: software to improve productivity

**We are now interested in assessing whether there is a significant difference at level 0.001 between the averages of the productivity increase provided by the new software in the two departments. What conclusions?**

To test the hypotheses on the basis of the two **independent** samples **,** it is first necessary to define a new variable measuring the productivity increase for each employee and the two vectors with the data for the two groups of employees

We set as  null the hypothesis that the two groups of employees have equal mean performance, and as alternative the hypothesis that the group with medium-high ratings has a higher productivity increase.

**Transition$Improve<-Transition$Post-Transition$Pre Impr_1<-Transition$Improve(Transition$Department=="Dept1") Impr_2<-Transition$Improve(Transition$Department=="Dept2") TEST.diffmean(x=Impr_1,y=Impr_2,mdiff0=0,alternative="greater")**

An initial evaluation (results in the R script) shows that the p-values differ depending on the assumptions made about the equality of variances.

_Therefore we proceed to test the hypothesis that the two variances are equal at level 0.05_

## Hands on: software to improve productivity

**> TEST.diffmean(x=Impr_1,y=Impr_2,mdiff0=0,alternative="greater",var.test=T) Test hypotheses on** **`μ_` x -** **`μ_` y** _**Under the assumption that the variances are different,**_ **Samples: independent H0** _**we do not  reject**_ **0** _**at the significance level**_ **Variances: unknown** _**conclude that there is no difference between**_ **x = Impr_1** _**departments despite quite different means.**_ **y = Impr_2**

_**Under the assumption that the variances are different, we do not  reject**_ **H0** _**at the significance level**_ **0.001** _**and conclude that there is no difference between departments despite quite different means.**_

**x - x - Null hypothesis        H0: (** **`μ_ μ_` y) = 0 or (** **`μ_ μ_y) ≤ 0` x - Alternative hypothesis H1: (** **`μ_ μ_` y) > 0**

**Unknown variances assumed to be equal**

**n_x n_y  xbar ybar xbar-ybar  s_X   s_Y   se stat p-value Normal.Approx  96  34 11.51 3.59      7.92 11.2 14.87 2.44 3.24  0.0006 Student-t      96  34 11.51 3.59      7.92 11.2 14.87 2.44 3.24  0.0008 Unknown variances assumed to be different**

**n_x n_y  xbar ybar xbar-ybar  s_X   s_Y   se stat p-value Normal.Approx  96  34 11.51 3.59      7.92 11.2 14.87 2.79 2.83   0.002 Student-t      96  34 11.51 3.59      7.92 11.2 14.87 2.79 2.83   0.003 Levene test for homogeneity of variance x = Null hypothesis        H0:** **`σ2_ σ2_` y Alternative hypothesis H1:** **`σ2_x ≠ σ2_` y s2_x   s2_y F-stat df1 df2 p-value** _**We reject the assumption that the variances are**_ **125.39 221.16   5.82   1 128    0.02**

_**We reject the assumption that the variances are equal, at the 0.05 level**_

## Hands on: clinical trial

Clinical trials to test the efficacy of a (new) drug are typically conducted by randomly assigning patients to two groups: patients in one group receive a placebo, while patients in the other group are treated with the drug. The use of a (control) group receiving the placebo avoids the possible bias due to the fact that the very idea of being treated may have a positive effect. A clinical trial to test the efficacy of an asthma drug with reference to a specific clinical indicator is conducted by dividing patients into four groups: one group receives a placebo and the other three groups are given different dosages of the drug. Below are the results of the improvement observed in the clinical indicator at 13 weeks after the start of the trial

|**Placebo**|**Dosage:150mg**|**Dosage: 300 mg**|**Dosage: 600 mg**|
|---|---|---|---|---|
|**Number of subjects**|**42**|**44**|**49**|**44**|
|**Improvement: mean**|**0.06**|**0.16**|**0.21**|**0.26**|
|**Improvement: sd**|**0.48**|**0.35**|**0.37**|**0.41**|

## Hands on: clinical trial

**An experimental drug must be** _**statistically**_ **more effective than the placebo to be considered valid. How would you assess whether the drug with a specific dosage is significantly more effective than the placebo, assuming equal variances?** We want to test the difference between the means of improvement observed in patients treated with a certain dosage of the drug and in patients treated with the placebo. This is a test for the difference between means based on **independent** samples.

Denote by 𝛍𝑷 the mean improvement recorded for patients treated with the placebo and by 𝛍𝑭 the mean improvement recorded for patients treated with (a certain dosage of) the drug. The hypotheses to be tested are:

**H0:** 𝛍𝑭 −𝛍𝑷 ≤ **0** that is 𝛍𝑭 ≤𝛍𝑷, as well as 𝛍𝑷 −𝛍𝑭 ≥ **0** . The drug treatment 𝑭 (with a certain dosage) has a (mean) effect less than or equal to the placebo 𝑷

**H0:** 𝛍𝑭 −𝛍𝑷 > **0** that is 𝛍𝑭 > 𝛍𝑷, as well as 𝛍𝑷 −𝛍𝑭 < **0** . The drug treatment 𝑭 (with a certain dosage) has a (mean) effect higher than the placebo 𝑷

Note that there are different ways of writing the hypotheses, **which have no effect on the result obtained!!!**

## Hands on: clinical trial

𝛂 **for H: vs H: Rejection region at level 0** 𝛍𝑭 ≤𝛍𝑷 **1** 𝛍𝑭 > 𝛍𝑷 **Which test statistic?** The test statistic to verify the two hypotheses is the difference between the sample means, – ഥ𝑿𝑭 ഥ𝑿𝑷 (difference between the average improvement of drug-treated patients and the average improvement of placebo-treated patients), whose standard error depends on the - unknown - variances of the two sample means. Assuming that the variances are equal we use the **pooled** sample variance to **estimate** the (common) variance **. The rejection region is:**

_Note that the case of unknown variances cannot be analyzed in this course when only aggregated data are available because we only consider the case when raw data are available and use R to test hypotheses_

## Hands on: clinical trial

## **H: vs H: Rejection region at level 2.5% for 0** 𝛍𝑭 ≤𝛍𝑷 **1** 𝛍𝑭 > 𝛍𝑷 **for the 150mg dosage?** Based on the available information

|**Placebo**|**Dose:150mg**|
|---|---|---|
|**n. Cases**|**42**|**44**|
|**Mean**|**0.06**|**0.16**|
|**Sd**|**0.48**|**0.35**|

## We get:

𝟐 44 −1 0.35(2) + (42 −1)0.48(2) 𝒔 = = 𝟎. 𝟏𝟕𝟓𝟐 𝑃𝑜𝑜𝑙 44 + 42 −2 0.1752 0.1752 𝒔𝒆ഥ −ഥ = + = 𝟎. 𝟎𝟗𝟎𝟑 𝑿𝑭 𝑿𝑷 44 42 **> # percentile of the Student's t > qt(1-0.025,df=42+44-2) (1) 1.9886**

_It is_

– - ഥ𝒙𝑭 ഥ𝒙𝑷 = 0.1<1.9886 0.0903 = 0.1752 _, Or,  equivalently_

ഥ ഥ – (𝒙𝑭 𝒙𝑷)/0.0903 = 1.1074 < 1.9886 _Therefore_ _**, we don’t reject** H0 and conclude that the 150mg dosage has no significantly greater effect than placebo, at the 0.025 level_

* Syntax to determine these results using R is in the  script

## Hands on: clinical trial

## Test for **H0:** 𝛍𝑭 ≤𝛍𝑷 vs **H1:** 𝛍𝑭 > 𝛍𝑷 for **the 150mg dosage. What is the p-value?**

– ഥ𝒙 ഥ𝒙 0.1 𝑭 𝑷 𝑷 𝒕 > = 𝑷 𝒕 > 𝒕 > 1.1074 𝒏𝑷+𝒏𝑭−𝟐 ഥ ഥ 𝟒𝟐+𝟒𝟒−𝟐 𝟒𝟐+𝟒𝟒−𝟐 𝒔𝒆 − 0.0903(= 𝑷) 𝑿𝑭 𝑿𝑷

**> 1-pt(1.1074,df=42+44-2)**

**(1) 0.135641**

**What conclusions for the other dosages** ? _**At the 0.025 level only for the highest dosage H0 is rejected, concluding that there is a significant difference between drug and placebo.**_

_**Note that for the 300mg dosage  the p-value is higher than 0.025 although not extremely high, and H0 would be rejected at the 0.05 or 0.1 level.**_

|**Placebo **|**D:150mg **|**D:300mg **|**D: 600mg**|
|---|---|---|---|---|
|𝑛|**42**|**44**|**49**|**44**|
|ഥ𝒙|**0.06**|**0.16**|**0.21**|**0.26**|
|𝒔|**0.48**|**0.35**|**0.37**|**0.41**|
|ഥ𝒙𝑭−ഥ𝒙𝑷|**0.10**|**0.15**|**0.2**|
|𝒔𝒆ഥ𝑿~~𝑭~~−ഥ𝑿~~𝑷~~|**0.0903**|**0.0892**|**0.0961**|
|**(**ഥ𝒙𝑭−ഥ𝒙𝑷**)/**𝒔𝒆ഥ𝑿~~𝑭~~−ഥ𝑿~~𝑷~~|**1.1074**|**1.6816**|**2.0812**|
|𝒕𝒏~~𝑭~~+𝒏~~𝑷~~−𝟐,𝟎.𝟎𝟐𝟓|**1.9886**|**1.9867**|**1.9886**|
|**P-value**|**0.1371**|**0.0496**|**0.0217**|

_**Finally  note that for the 600mg dosage H0 would not be rejected if one was slightly more conservative towards H0, setting a lower**_ - **and** _**thus being prone to consider it to be true unless the difference between drug and placebo is extremely high.**_

# Hypothesis testing Test on proportion and on the difference between proportions

## Test for proportion

_The_ _**Churn**_ **rate** is the % of customers who cancel a contract or stop using the services provided by a company in a given time frame. Monitoring and preventing churn with customer retention strategies is crucial: the cost of **acquiring a new customer** is significantly higher than the cost of retaining an acquired customer. Moreover, retained customers are generally more profitable for the **.** company and ultimately more reliable (lower risk of churn)

A telecommunications company has a churn rate of **22%** on prepaid SIM cards. In order to retain customers who are considered - based on appropriate indicators - to be at high risk of churn, a promotional strategy is developed and applied to a sample of 150 customers, 29 of whom cancel their contracts anyway (within a certain deadline).

**Of the 150 customers on whom the promotional strategy was tested, 29 cancelled their contracts anyway. Can we say that on the basis of the sample result the strategy works?** The sample proportion of drop-outs is 𝒑ෝ = 29/150 = 0.193 < 0.22. This percentage is lower than the current one (assumed under **H0** ), however, we are considering . only one of the possible **samples of customers It is possible to observe a sample proportion lower than 0.22 even when H0 is true and the churn rate ensured by the promotional strategy is not really lower than 0.22.**

## Test for proportion

**To assess whether the promotional strategy is effective, a test should be run. How would you set up the hypothesis test to evaluate the strategy?**

The aim is to test whether 𝒑 **=** the proportion of drop-outs among customers who were offered the promotion, is lower or not than the current one, equal to 0.22.

Taking a conservative approach, we consider as most serious the error of concluding that the strategy is effective when in fact it is not.

Thus we set as null the hypothesis that the strategy under consideration is not effective, against the alternative hypothesis that it is effective:

**H:** - **0.22 0** 𝒑 **H: < 0.22 1** 𝒑

**How to build the rejection region?**

## Test for proportion: test statistic and its distribution

Test for **H:** - **0.22** vs **H: < 0.22 0** 𝒑 **1** 𝒑 To build a rejection region or to calculate the p-value of the observed sample realisation, we – must first identify a **test statistic** , which in this case - quite predictably is based on the sample 𝑷. proportion of successes,(෡)

**What is the distribution of 𝑷(෡) under H0** When the sample is **? sufficiently large** (the only case we will consider) 𝑷(෡) has a distribution which can be approximated by a normal, and ෡𝑷|(𝒑 **=** 𝒑 **0** ) ≈𝓝(𝒑 **0** , 𝒑 **0** ( **1–** 𝒑 **0** ) **/** 𝒏)

Note that in this **case, unlike in the previous ones** , under the null hypothesis both the **expected value** and the **variance** of the test statistic are known, since they depend on the parameter of interest, 𝒑!!! Clearly it is also possible to consider:

## Test for proportion: rejection region

Hypothesis test: **H0:** 𝒑 - **0.22** vs **H1:** 𝒑 **< 0.22** - **? Rejection region at level**

The **rejection region – based on the sample proportion,** ෝ𝒑 **– identifies the value of the sample proportion,** ෝ𝒑∗ that would lead to reject **H0** .

Using the same reasoning as in the previous cases, ෝ𝒑∗ must be such that: ෝ 𝑷(𝑷<(෡) 𝒑∗ **|** 𝒑 **=** 𝒑𝟎) = - **So** ෝ𝒑∗ **is the percentile of order** - of the distribution of 𝑷(෡) under the null hypothesis, and the rejection region can be written as:

𝟎 𝟎 = ∎ෝ𝒑< ෝ𝒑𝟏−𝛂 **con** ෝ𝒑𝟏−𝛂 percentile of order - of 𝓝(𝒑 **0** , 𝒑 **0** ( **1–** 𝒑 **0** ) **/** 𝒏)

∙ ∎ෝ𝒑< 𝒑 **0** −𝒛𝛂 𝒑 **0** ( **1–** 𝒑 **0** ) **/** 𝒏 by the relation between the percentiles of a normal distriution 𝒛 = −𝒛 and those of a standard normal distribution and considering that 𝟏−𝛂 𝛂 ෝ − 𝒑 𝒑 **0** _Note that for the extension to other cases (right-tail or two-tails test) the_ ∎ < −𝒛 𝛂 _same procedure illustrated for the test of the mean of a population_ 𝒑 **0** ( **1–** 𝒑 **0** ) **/** 𝒏

_Note that for the extension to other cases (right-tail or two-tails test) the same procedure illustrated for the test of the mean of a population (when the variance is known) can be adopted (properly modified)_

## Test for proportion: rejection region

Hypothesis test: **H0:** 𝒑 - **0.22** vs **H1:** 𝒑 **< 0.22 Should the observed sample proportion,** ෝ𝒑 **= 29/150 = 0.193, lead to reject H0 at level 0.025?**

- **# Verify different expressions**

- **qnorm(0.025,mean=0.22,sd= sqrt(0.22*(1-0.22)/150)) # percentile N|H0 (1) 0.153708**

- **0.22-qnorm(0.975)*sqrt(0.22*(1-0.22)/150) # relation with percentile N(0,1) (1) 0.153708**

- **qnorm(0.975) # percentile N(0,1)**

- **(1) 1.959964**

> ෝ −𝟎. 𝟐𝟐 𝒑

**Rejection region:** ෝ𝒑 < 𝟎. 𝟏𝟓𝟑𝟕 **or, equivalently,** < −𝟏. 𝟗𝟔 𝟎. 𝟐𝟐(𝟏−𝟎. 𝟐𝟐)/𝟏𝟓𝟎

_Since_ 0.193 > 0.1537 _and, equivalently_ (0.193 −0.22)/ 0.22(1 −0.22)/150 _=_ −0.798 > −1.06 _the null hypothesis cannot be rejected, and we should therefore conclude that the promotional strategy has not a significant effect (at level 2.5%) on the propensity to churn_

* Syntax to determine these results using R is in the  script

## Test for proportion: p-value

Test for **H:** - **0.22** vs **H: < 0.22 0** 𝒑 **1** 𝒑

**The sample proportion of drop-outs is = 29/150 = 0.193. What is the p-value of the observed sample realisation?**

p-value: probability of observing a more extreme sample proportion (wrt **H0** and in the direction of **H1** ) than the one observed on the extracted sample, assuming that **H0** is true. The p-value measures how unlikely the observed sample is under **H0** . In this case, it corresponds to the probability of observing a sample proportion less than 0.193 when the churn rate is 22%: ෡ ෡ 𝑷 𝑷< ෝ𝒑 **|** 𝒑 **=** 𝒑𝟎 = 𝑷(𝑷< **0.193 |** 𝒑 **= 0.22** )

**: Exploiting, as usual, the relation with the standardised normal, we can write**

**– –** 𝑷(𝒁< ( ෝ𝒑 𝒑𝟎 ) / 𝒑𝟎( **1−** 𝒑𝟎)/𝒏) = 𝑷(𝒁< ( **0.193 0.22** ) / **0.22** ( **1−0.22** )/ **150** )

**> pvalue<-pnorm((0.193-0.22)/sqrt(0.22*(1-0.22)/150)) > pvalue (1) 0.2123564**

## Test for proportion: p-value

Test for: **H:** - **0.22** vs **H: < 0.22 0** 𝒑 **1** 𝒑

**> pvalue<-pnorm((0.193-0.22)/sqrt(0.22*(1-0.22)/150))**

**> pvalue**

**(1) 0.2123564**

## What comments on the p-value?

The p-value of the observed realisation is 0.2119.  Thus, even when **H0** is true and _**p**_ **= 0.22 it is not unlikely at all to draw a sample characterised by a sample proportion less than or equal to 0.193.**

- Considering that the type I error is the most severe and that standard values of are typically low (i.e. 0.01, 0.025, 0.05, or 0.1 at most), **H0** should not be rejected and we conclude that the promotional strategy does not significantly reduce the churn rate. Note that the p-value allows conclude that the statistical decision would not change if a different level of significance was chosen.

## Rstudio: TEST.prop()

The **TEST.prop()** function in the **UBStats** package allows testing hypotheses on the proportion of ‘ successes ’ in a population. The syntax is very similar to that of the function **CI.prop()**

- **TEST.prop(x, success=NULL, p0=0, alternative="two.sided", digits=2, data)**

- where:

- **x**: name of a vector or factor or one of the columns of the dataframe specified in **data**

- **success**: allows to define which value of **x** is to be considered as a success. It can be omitted if **x** is a binary vector (values 0/1; in this case it is assumed that 1 indicates a success) or a logical

- vector (values **TRUE/FALSE** ; in this case it is assumed that **TRUE** indicates a success)

- **p0** is the value of the proportion established under the null hypothesis (0 by default)

- **alternative** defines the type of test, specifying the direction of the alternative hypothesis, as seen in the previous cases (possible values are **"less"** , **"greater"** and **"two.sided"** , the default value).

- **digits** is the number of decimals used to round the reported statistics

_Note that the function does not check whether the conditions necessary for determining the interval (e.g. sample size) are satisfied_

## Hands on: Bank customer analysis

According to some studies, banks and/or financial institutions lose an average of 25 to 30 per cent of their customers each year, often and mainly due to dissatisfaction with service and/or costs. A bank decides to conduct a survey on a sample of customers by collecting information on some sociodemographic characteristics and on the level of loyalty of the selected customers. The **Bank** dataframe contains the variable **FeesOK** , which detects whether the respondent considers ( **Yes)** or not ( **No)** the cost of maintaining a current account adequate or at least in line with the market. **Do you think the bank can conclude that the proportion of customers dissatisfied with costs is less than 25%?**

**> TEST.prop(x=FeesOK,success="No",p0=0.25,alternative="less",data=Bank) Test hypotheses on proportion**

**Null hypothesis** **`H0: p = 0.25 or p ≥ 0.25` Alternative hypothesis H1: p < 0.25 n phat s_X se stat p-value 1620 0.23 0.43 0.01 -2.3  0.0109**

α _The statistical decision depends on the chosen significance level . For example, at a level 0.001 or_ - _> 0.01 0.01 the null hypothesis cannot be rejected, whereas an opposite conclusion is reached if_

## Test for the difference between proportions

In many applications, we are interested in testing hypotheses concerning the **difference successes** The test statistic is based on the **between the proportions of ‘ ’ in two populations.** 𝑷(෡) − 𝑷(෡) . **difference between the sample proportions,** 𝑿 𝒀

= Therefore, given a null hypothesis **H0:** 𝒑𝑿 −𝒑𝒀 𝛅𝟎 vs a generic alternative hypothesis, it is **H** . necessary to determine the distribution of the test statistic under **0**

= The most typical case is when the null hypothesis is **H0:** 𝒑𝑿 −𝒑𝒀 𝟎, stating that 𝒑𝑿 and 𝒑𝒀 **have the same (unknown) value, which we denote by** 𝒑 **0 , so that H0:** 𝒑𝑿= 𝒑𝒀 = 𝒑 **0 Distribution ofDistribution of** under 𝑷(෡) 𝑿 − 𝑷(෡) **H ?** 𝒀 under **0 H0** ? When the samples are **sufficiently large** (the only case we −(෡) consider) and **are independent,** 𝑷(෡) 𝑿 𝑷𝒀 has a distribution that can be approximated by a normal distribution, and

= ∙ ෡𝑷|(𝒑𝑿 = 𝒑𝒀 𝒑 **0** ) ≈𝓝(𝟎, 𝒑 **0** ( **1** − 𝒑 **0** ) (𝟏/𝒏𝑿 + 𝟏/𝒏𝒀))

Where 𝒑 **0** is the (same) proportion of successes in the two populations. Since 𝒑 **0** is not known, it must be estimated!

## Test for the difference between proportions

= If 𝒑𝑿= 𝒑𝒀 𝒑 **0** , the two samples come from two populations with the same proportion of successes, 𝒑 **0** , and thus with the same Bernoulli distribution. To estimate 𝒑 **0** we consider the pooled proportion of successes, **calculated by merging the data** in the two samples:

−(෡) Thus (provided the samples are independent and sufficiently large) 𝑷(෡) 𝑿 𝑷𝒀 has a distribution that can be approximated by:

The rejection regions (and p-values) are obtained as seen for other cases using the percentile of this distribution (the shape of the rejection region clearly depends on the direction of **H1)** = In the case of **H0**: 𝒑𝑿 −𝒑𝒀 𝛅𝟎 the two proportions are different, and:

෡ ෡ 𝒑ෝ𝑿(𝟏− 𝒑ෝ𝑿) 𝒑ෝ𝒀(𝟏− 𝒑ෝ𝒀) 𝑷𝑿 − 𝑷𝒀 |( 𝒑𝑿 −𝒑𝒀 = 𝛅𝟎 ) ≈𝓝 𝛅𝟎, + 𝑛 𝑛 𝑋 𝑌

## Test on the difference between proportions: rejection region

A/B testing is used in online marketing to optimise campaigns and consists of proposing two versions (A or B) of the same design (homepage, banner) to different users and then testing which version performs better. A sample of users of a social network is shown one of two banners at random to compare their Click-Through Rate (CTR, ratio between the number of clicks on the banner and the number of views of the banner). Banner A, viewed by 2364 users, generates 456 clicks, while banner B, viewed by 2323 users, generates 611 clicks. **Rejection region at level** 𝛂? Using the same procedure described for other cases, the rejection region can be written as: ∎ **|** ෝ𝒑𝑿 −ෝ𝒑𝒀 **|** > 𝒛𝛂/𝟐 ∙𝒔𝒆𝟎= 𝒛𝛂/𝟐 ෝ𝒑𝟎(𝟏−ෝ𝒑𝟎) ∙(𝟏/𝒏𝑿 + 𝟏/𝒏𝒀 ) , with 𝒔𝒆𝟎 = 𝒔𝒆෡𝑷 −෡𝑷 = 𝟎 𝑿 𝒀|𝒑𝑿−𝒑𝒀 Or standardizing:

ෝ −ෝ 𝒑𝑿 𝒑𝒀 ∎ > 𝒛 𝛂/𝟐 𝒔𝒆 𝟎

## Hands on: A/B test

## Test at the 1% level whether the two banners perform equally well in terms of CTR

𝟎. 𝟐𝟐𝟕𝟕 ෝ𝒑𝟎 = (456 + 611)/(2364 + 2323) = 𝒔𝒆 = = = 𝟎. 𝟎𝟏𝟐𝟑 𝟎 Ƹ𝑝0(1 −Ƹ𝑝0) ∙(1/𝑛𝑋 + 1/𝑛𝑌 ) 0.2277(1 −0.2277) ∙(1/2364 + 1/2323 ) 𝒛 = 𝟐. 𝟓𝟕𝟔 𝟎.𝟗𝟗𝟓

ෝ ෝ ෝ ෝ − − > 2.576 ∙ 0.0123= **0.032 or** > 𝟐 **.576 Rejection region:** 𝒑𝑿 𝒑𝒀 𝒑𝑿 𝒑𝒀 /0.0123 _=_ 456/2364 − 611/2323 = /0.0123 = Ƹ𝑝𝑋 −Ƹ𝑝𝑌 |–  0.070 | > 𝟎. 𝟎𝟑𝟐 _or, equivalently,_ Ƹ𝑝𝑋 −Ƹ𝑝𝑌 5.6992 > 𝟐. 𝟓𝟕𝟔 _. We therefore reject H0: the two banners have different performances as for CTR._ **What is the p-value of the observed sample realisation? What conclusion based on it?** ෝ ෝ ෝ ෝ − − 𝟐𝑷 ෡𝑷 −෡𝑷 𝑿 𝒀 > |𝒑𝑿 𝒑𝒀| **|** 𝒑𝑿 = 𝒑𝒀 = 𝟐𝑷(𝒁> 𝒑𝑿 𝒑𝒀 /0.0123) = 𝟐𝑷(𝒁> 5.6992)

**> 2*(1-pnorm(5.6992))**

**(1) 1.203709e-08**

_The extremely low value of the p-value suggests that the null hypothesis would be rejected for any_ α _(reasonable) value of . Therefore we can conclude that, whatever the level of significance chosen by the researcher, the observed sample realisation leads to reject  the null hypothesis._

## * Syntax to determine these results using R is in the  script (data in dataframe **Banner** )

## Rstudio: TEST.diffprop()

The **TEST.diffprop()** function in the **UBStats** package allows testing hypotheses on the difference between the proportions of ‘ successes ’ in two populations. Again, since the test is based on independent samples, two approaches are possible.

**(x,y): TEST.diffprop(x, y, success.x = NULL, success.y = NULL, pdiff0=0, alternative="two.sided", digits=2, data)** where:

- **data.** The function tests

- **x,y**: name of two vectors or factors, possibly names of two variables in hypotheses on **p_x-p_y**

- **x** and

- **success.x,success.y:** specify the values of **y** to be considered success. They may be omitted if **`x`** or **y** are binary vectors (values 0/1; in this case 1 is assumed to indicate a success) or logical vectors (values **TRUE/FALSE** ; with **TRUE** indicating a success). If success is encoded in the same way in the two samples, it is sufficient to specify only one of the two arguments

- **pdiff0** is the value of the difference **p_x-p_y** under the null hypothesis (0 by default)

- **alternative** specifies the direction of the alternative hypothesis, as seen in the previous cases (possible values are **"less"** , **"greater"** and **"two.sided"** , the default value).

- **digits** is the number of decimals used to round the reported statistics

_Note that the function does not check whether the conditions necessary for determining the interval (e.g. sample size) are satisfied_

## Rstudio: TEST.diffprop()

**(OPTIONAL)**

The **TEST.diffprop()** function in the **UBStats** package allows testing hypotheses on the difference between the proportions of ‘ successes ’ in two populations. Again, since the test is based on independent samples, two approaches are possible.

**(x,by): TEST.diffprop(x, by, success.x = NULL, pdiff0=0,**

**"two.sided", digits=2, data)**

## where:

- **x,by**: vectors (or factors) with the same length ordered so that the elements refer to the same unit. **x is the name of a vector/factor** , **by** is the name of a two-level vector/factor with **by1** ≺ **by2** (possibly **x** and/or **by** can be the names of variables in **data** ). In this case, the function calculates the interval for **p_by1-p_by2**

- **success.x:** defines the value of **x** to be taken as success. It can be omitted if **`x`** is binary

- (values 0/1; in this case, 1 is assumed to indicate success) or logical (values **TRUE/FALSE** ; in this case, **TRUE is** assumed to indicate success).

- **alternative,digits** same as for the syntax based on **x,y**

_Note that the function does not check whether the conditions necessary for determining the interval (e.g. sample size) are satisfied_

## Hands on: Bank customer analysis

The dataframe **Bank** contains information on the variable **FeesOK** indicating whether the respondents consider ( **Yes)** or not ( **No)** the cost of maintaining a current account adequate and on the respondents’ sex ( **Sex** , assigned at birth)

## Can it be concluded that the proportion of dissatisfied customers differs depending on sex?

- **# approach based on x,y**

- **Fees.M<-Bank$FeesOK(Bank$Sex=="M")**

- **Fees.F<-Bank$FeesOK(Bank$Sex=="F")]**

- **TEST.diffprop(x=Fees.M,y=Fees.F,success.x="No",pdiff0=0) Warning:**

**Only 'success.x' is specified; 'success.y' set equal to 'success.x'.**

_**In this case, the null hypothesis cannot be rejected, and one should conclude that there is no significant difference unless**_ - _**= 0.1 is set.**_

**Test hypotheses on p_x-p_y x:Fees.M = No** _**is no significant difference unless**_ **y:Fees.F = No Null hypothesis H0: (p_x-p_y) = 0 Alternative hypothesis H1: (p_x-** **`p_y) ≠ 0` n_x n_y phat_x phat_y phat_x-phat_y s_X s_Y se_0  stat p-value 719 901   0.21   0.24         -0.04 0.4 0.43 0.02 -1.68  0.0939**

## Hands on: Bank customer analysis

- **# approach based on x,by**

- **TEST.diffprop(x=FeesOK,by=Sex,success.x="No",pdiff0=0,data=Bank) Test hypotheses on p_x-p_y**

**x:FeesOK = No | Sex = F**

- **y:FeesOK = No | Sex = M**

**Null hypothesis H0: (p_x-p_y) = 0 Alternative hypothesis H1: (p_x-** **`p_y) ≠ 0` n_x n_y phat_x phat_y phat_x-phat_y s_X s_Y se_0 stat p-value 901 719   0.24   0.21          0.04 0.43 0.4 0.02 1.68  0.0939**

In this case, being the test two-sided, no particular caution is needed when defining the difference in the null hypothesis; using this alternative approach, the p-value is the same, and what changes is only the sign of the test statistic, which is opposite to that of the statistic determined previously. This happens because the ordering of the levels of the variable **Sex** in **by** is F≺M , so the null hypothesis refers to **p_F-p_M** whereas in the previous case **p_M-p_F** was considered. Of course, things change a lot when the alternative is one-sided: we stress the importance of paying attention . to the standard ordering of levels when using the **x,by** approach

# Hypothesis testing Goodness of fit test and independence test

## Chi-square goodness of fit test

In order to optimise the performance of an e-commerce site, one wants to assess consumer preferences regarding four similar products of different brands, in order to determine which one is the most convenient to display first. For a certain period of time, the four products are presented to users interested in the product (search key). On a sample of 570 users who actually purchased the product, the following results are observed:

|Isit plausible that|**Brand1Brand4**|
|---|---|---|---|
|Determine, at the significance level- = **Number of consumers162** Pr :0.25 P1: 0.2 Ps = 0.15 PATO .25|
|is significantly different from the uniform distribution (under which the same % of consumers -|
|25% - prefer each brand).|

We indicate with 𝒑𝟏, 𝒑𝟐, 𝒑𝟑, 𝒑𝟒 the frequencies of the 𝟒 brands. We want to test: **H0:** 𝒑𝒌 = 𝒑𝒌𝟎 **= 0.25** for each 𝑘= 1,2,3,4 _of the considered variable is_ **H:** for at least one 𝑘 **1** 𝒑𝒌 ≠𝒑𝒌𝟎

_Note that under the null hypothesis, the distribution of the considered variable is_ _**fully specified** and does not depend on any unknown parameters_

## Chi-square goodness of fit test

In order to optimise the performance of an e-commerce site, one wants to assess consumer preferences regarding four similar products of different brands, in order to determine which one is the most convenient to display first. For a certain period of time, the four products are presented to users interested in the product (search key). On a sample of 570 users who actually purchased the product, the following results are observed:

## Chi-square goodness of fit test

**Comparison of observed frequency distribution with a ‘ theoretical ’ frequency distribution: the goodness-of-fit test.**

**Test H0:** 𝒑𝒌 = 𝒑𝒌𝟎 = **0.25 for** each 𝑘= 1,2,3,4 vs **H1:** 𝒑𝒌 ≠𝒑𝒌𝟎 for at least one 𝑘. Recall that to build a test, it is necessary to find a **test statistic** whose **distribution is known for any given value of the parameter of interest.**

In this case, a reasonable test statistic could be based on a comparison between the observed **H** . frequencies and the frequencies specified by the null hypothesis **0** Since the sample size is **relevant** in any hypothesis test, it is appropriate to base this comparison on the **observed absolute frequencies, which we denote** by 𝑶𝒌, and the expected - **frequencies** under **H0** , which we denote by 𝑬𝒌 = 𝒏 𝒑𝒌𝟎.

𝒏= **In the considered example the sample size is 570, and under the null hypothesis that each** 𝒑𝒌 = **0.25 the absolute frequencies should all be equal to 0.25** - **570 = 142.5.**

## Chi-square goodness of fit test: the test statistic

**In general, given a frequency distribution, to test the hypotheses H0:** 𝒑𝒌 = 𝒑𝒌𝟎 for each 𝑘= 1,2, … , 𝐾 vs **H1:** 𝒑𝒌 ≠𝒑𝒌𝟎 for at least one 𝑘 the observed absolute frequencies are compared with those expected under **H0**

|**Observed absolute frequencies, **𝑶𝒌|𝑶𝟏|𝑶𝟐|**....**|𝑶𝑲|
|---|---|---|---|---|
|**Expected absolute frequencies underH0,**𝑬𝒌|𝑬𝟏|𝑬𝟐|**....**|𝑬𝒌|

**Why this particular statistic?** The reason lies in the fact that **if** 𝑬𝒌 ≥ **5 for each** 𝒌, the statistic ො𝛘(𝟐) under **H0** has a **known** distribution and specifically a distribution called a **chi-square** with 𝐾−1 degrees of freedom (note: the degrees of freedom are 𝐾−1 because the sum of the frequencies is always 1, and therefore there are only 𝐾−1 frequencies ‘free’ to vary).

## Chi-square distribution

A random variable with a chi-square distribution can only assume **non-negative** values. The 𝜈 **chi-square distribution is right skewed,** and depends on a single parameter, , called degrees of freedom, which influences its shape.

## Chi-square goodness of fit test: rejection region

**Test the assumptions H0:** 𝒑𝒌 = 𝒑𝒌𝟎 for each 𝑘= 1,2, … , 𝐾 vs **H1:** 𝒑𝒌 ≠𝒑𝒌𝟎 for at least one 𝑘

**Critical tail for H ? 0** In this case, the **critical tail for H0 is the right tail**: very high values of the test statistic ො𝛘(𝟐) indicate a substantial difference between observed and expected absolute frequencies and thus statistical evidence favours the alternative hypothesis.

**Shape of the rejection region?** The shape of the rejection region **will be:** 𝟐 **Rejection region:** ොχ(𝟐) > ොχ∗ where, as usual, the critical value depends on the chosen significance level.

## Chi-square goodness of fit test: rejection region

**Test the assumptions H0:** 𝒑𝒌 = 𝒑𝒌𝟎 for each 𝑘= 1,2, … , 𝐾 vs **H1:** 𝒑𝒌 ≠𝒑𝒌𝟎 for at least one 𝑘

𝛘ො(𝟐) **|H0**

𝟐 **Which** ොχ∗ **given a level of significance,** - **?** The critical value must be chosen such that **$$$P(Reject H0 |H0 is true) =**$$$ Pr(ො𝛘(𝟐) > ොχ∗(𝟐) | **H0** ) **=** - 𝟐 This condition is fulfilled when ොχ∗ is the 1 - - of the distribution of percentile of order ො𝛘(𝟐) **under H0 , i.e.** 2 = ොχ∗(𝟐) χ𝐾−1,α 1 - - of a The percentile of order **chi-square distribution** with 𝐾−1 degrees of 𝟐 freedom, 𝛘𝑲−𝟏

## Rstudio: chisq.test, pchisq(), qchisq()

The **chisq.test()** function available in R allows you to apply the **goodness of fit test (with fully specified probabilities)** , using the syntax

## **chisq.test(x,p** )

## where:

- **x**: is a vector containing the absolute frequencies of the values taken by a variable. In the case of

- **raw** data, this distribution must first be determined using the function **table()** (an example is shown below)

- **p**: is the vector containing the **probabilities** assumed in **H0** . If not specified, it is assumed that the theoretical probabilities are all equal to each other.

It is also worth introducing the functions **pchisq(q, df)** and **qchisq(p,df)** available in R to determine the **distribution function** (or cumulative probability) and **percentiles** of a chi-square distribution with **df** degrees of freedom, respectively. As seen for other distributions, 𝟐 - **pchisq(q,df)** calculates Prob(𝛘 ≤ **`q`** ) (i.e. the area below the probability density function of **`df`** the 𝟐 𝛘 distribution, up to the value **`q`** ) **`df`**

𝟐 2 - of a distribution i.e. the value such **qchisq(p,df)** calculates the percentile of order **p** 𝛘 χ **`df df,1−p`** 𝟐 2 that Prob 𝛘 ≤χ = **p** . **`df df,1−p`**

## Chi-square goodness of fit test

**Test H0:** 𝒑𝒌 = 𝒑𝒌𝟎 = **0.25 for** each 𝑘= 1,2,3,4 vs **H1:** 𝒑𝒌 ≠𝒑𝒌𝟎 for at least one 𝑘. - **= 0.01? Rejection region at level** 2 2 - = 0.01 is: The rejection region at ොχ(2) > χ𝐾−1,α = χ3,0.01

**> qchisq(p=0.99,df=3)** → **Rejection region:** ොχ(2) > 𝟏𝟏. 𝟑𝟒𝟓 **(1) 11.34487**

## The sample results:

|**Brand1**|**Brand2**|**Brand3**|**Brand4**|
|---|---|---|---|---|
|**Observed absolute frequencies,**|**151**|**117**|**140**|**162**|
|**Expected absolute frequencies underH0, **𝑬𝒌|**142.5**|**142.5**|**142.5**|**142.5**|
|(𝑶𝒌−𝑬𝒌)𝟐/𝑬𝒌|**0.507**|**4.563**|**0.044**|**2.668**|

So ොχ(2) =0.507+4.563+0.044+2.668= **7.782. Conclusion?**

* Syntax to determine these results and the following using R is in the  script

## Chi-square goodness of fit test

**Test H0:** 𝒑𝒌 = 𝒑𝒌𝟎 = **0.25 for** each 𝑘= 1,2,3,4 vs **H1:** 𝒑𝒌 ≠𝒑𝒌𝟎 for at least one 𝑘. Rejection region at level - = 0.01 **:** ොχ(2) > 𝟏𝟏. 𝟑𝟒𝟓 = Sample value of the test statistic: ොχ(2) **7.782**

**p-value of** ොχ(2) **?**

## 2 **The p-value is** 𝑃(𝛘𝟑 > **7.782** )

**> 1-pchisq(7.782,df=3) (1) 0.05073865**: The p-value can be obtained easily using the function **chisq.test(x,p)**

**> chisq.test(x=c(151,117,140,162),p=c(0.25,0.25,0.25,0.25))**

**Chi-squared test for given probabilities**

**data: c(151, 117, 140, 162) X-squared = 7.7825, df = 3, p-value = 0.05073**

## Hands on: Bank customer analysis

Referring to the data on the customers of a bank, contained in the dataframe **Bank** , one is interested in testing whether or not the extracted sample reflects the composition of the customer population with regard to the education level:

Primary: 5%, High school: 28%, College: 17%, Graduate: 35%, Post-Graduate: 15%. **Assess whether the difference with the empirical distribution of the variable Education_Level is to be considered significant at the 0.01 level.**

**> table(Bank$Education_Level) Primary High School College Graduate Post-Graduate 56         389     267      526           159 > distr.table.x(x=Education_Level,data=Bank) Education_Level Count Prop Primary    56 0.04 High School   389 0.28 College   267 0.19 Graduate   526 0.38 Post-Graduate   159 0.11 TOTAL  1397 1.00** _education._

_The empirical distribution does not appear very different from the expected one. Note that a large number of customers (sample size n=1620) did not answer the question; thus the results will only be reliable if these customers do not have any particular characteristics with regard to the level of education._ _**In order to properly we need a test!**_

* Syntax to determine these results and the following using R is in the  script

## Hands on: Bank customer analysis

The function **chisq.test(x,p)** requires in input the vector **x** with the **empirical absolute frequencies** and the vector **p** with the expected proportions. In this case, therefore, it is not possible to apply the function directly to the data, and it is necessary to **obtain the frequency distribution to provide as input.**

**> table(Bank$Education_Level) Primary   High School   College   Graduate   Post-Graduate 56           389       267        526             159 > chisq.test(table(Bank$Education_Level),p=c(0.05,0.28,0.17,0.35,0.15))**

**Chi-squared test for given probabilities data: table(Bank$Education_Level) X-squared = 21.427, df = 4, p-value = 0.0002606**

_At the 0.01 level (but, indeed, for any of the values typically used), the null hypothesis that the distribution of educational level in the sample is the same as the theoretical hypothesis must be rejected. Indeed, when the sample size is large even small deviations can be considered as ‘ significant ’ and not related to chance or sample variability_

## Chi-square test of independence

The procedure used to test whether an empirical distribution is significantly different from a certain theoretical distribution can also be used to test the **independence between two (qualitative, or otherwise discrete) variables.**

For a sample of 165 customers in a certain segment who joined at least one marketing campaign, we consider the variables _Customer class_ (Silver, Gold, or Platinum depending on its profitability for the company) and _Number of marketing campaigns the customer has joined,_ resulting in the following table:

## How to assess whether the two variables are independent?

## Chi-square test of independence

In the analysis of contingency tables, we introduced intuitively the concept of independence between two variables, based on the comparison of conditional distributions. In this case*:

_Conditional distributions are different! However, at the_ _**inferential** level we are not interested in the empirical evidence as such, but rather in the possibility of_ _**making inferences about the population** ! The relevant question in this context is therefore:_ _**are the observed differences such that it can be inferred that the two variables are independent in the population? It is therefore necessary to find a test statistic to verify whether the two variables are independent**_

* Syntax in the R script

## Chi-square test of independence

## Analysis of customer class and number of joined marketing campaigns

|Observed under Ho|T value On:It , En = 3p . 41 = 8 .PT 165|**_Nr of_41**|Regardless of class 47/165 =0 . 245 Next to 1 campaign|
|---|---|---|---|---|---|---|
|E~~:~~|4 6 **Total165**|

The proportion of customers who joined 1 campaign - regardless of their class - is 41/165=0.248. If the number of campaigns had no **relation with the customer class,** the proportion of customers who joined 1 campaign should be about 0.248 _**in each class**_ ! Among the 34 Silver customers, the proportion of customers who joined a single campaign - should be 0.248, with a total of about 34 0,248 customers or more precisely (without rounding) - - 𝑪𝟏 𝑹𝟏/𝒏 = 34 41/165 = 8.448 where 𝑹𝟏=number of customers who joined 1 campaign, 𝑪𝟏 =number of Silver class customers, and 𝒏 =total number of customers in the sample.

## Chi-square test of independence

## Analysis of customer class and number of joined marketing campaigns

|**_Nr of_** **_campaigns_**|**Customer class**|**Customer class**|**Customer class**|**Total**|
|---|---|---|---|---|
|Silver|Gold|Platinum|
|1|15|20|6|**41**|
|2|7|30|10|**47**|
|3|6|15|20|**41**|
|4|6|10|20|**36**|
|**Total**|**34**|**75**|**56**|**165**|

Generalising, for each **cell** in the table, i.e. for each **values combination of the variables considered,** the **expected joint frequency under the assumption of independence** is: = - 𝑬 𝑹 𝑪 𝒌 /𝒏 𝒌𝒋 𝒋

To test the independence between two variables - **given** their observed marginal frequencies - we can apply the chi-square test by assessing how far the observed joint frequencies - which we denote by 𝑶 - are from those expected under the assumption of independence, 𝑬 𝒌𝒋 𝒌𝒋

## Chi-square test of independence

To test **H:** two variables are vs **H:** two variables **are 0 independent 1 not independent** We can use the test statistics:

𝑲 and 𝑱 indicate the number of categories of the two variables, 𝑶 is the observed joint 𝒌𝒋 absolute frequency (for the combination of row value and column value) and - 𝑬 = 𝑹𝒌 𝑪 /𝒏 is the expected absolute frequency under the assumption of independence. 𝒌𝒋 𝒋 2 The distribution of ො𝛘(𝟐) | **H0** (when 𝐸𝑘𝑗 ≥ 5 for each 𝑘, 𝑗*) is a chi-square 𝛘 𝑲−𝟏 𝑱−𝟏 (the df’s depend on the fact that ො𝛘(𝟐) is built **conditioning on** the marginal frequencies, and thus only ∙ 𝐾−1 𝐽−1 joint frequencies are ‘free to vary’). - are: The rejection region at the significance level and the p-value of a sample realisation  ොχ(2) 2 2 **Rejection region:** ොχ(2) > χ(𝐾−1)(𝐽−1),α percentile of order 1 −α of a 𝛘 𝑲−𝟏 𝑱−𝟏 2 **The p-value is** 𝑃(𝛘 𝑲−𝟏 𝑱−𝟏 > ොχ(2) )

**104** * In textbook the condition is that no more than the 20% of expected frequencies are  < 5

## Chi-square test of independence

**Analysis of customer class and number of joined marketing campaigns**

|**_Nr of_** **_campaigns_**|**Customer class**|**Customer class**|**Customer class**|**Total**|
|---|---|---|---|---|
|Silver|Gold|Platinum|
|1|15|20|6|**41**|
|2|7|30|10|**47**|
|3|6|15|20|**41**|
|4|6|10|20|**35**|
|**Total**|**34**|**75**|**56**|**165**|

**Rejection region to test H0: two variables are independent vs H1: two variables are not independent at the 0.001 significance level? The rejection region is:**

ොχ(2) > χ2(4−1)(3−1),α = χ26,0.001

**> qchisq(p=1-0.001,df=6)**

**(1) 22.45774**

→ **Rejection region:** ොχ(2) > 𝟐𝟐. 𝟒𝟓𝟕𝟕𝟒

## Chi-square test of independence

**Analysis of customer class and number of marketing campaigns joined;
- Rejection region of the null hypothesis of independence:** ොχ(2) > 𝟐𝟐. 𝟒𝟓𝟕𝟕𝟒.

ොχ(2) = **27.922 Conclusions?**

## Rstudio: chisq.test

The **chisq.test()** function available in R allows you to apply the independence test using the syntax

**chisq.test(x,y** )

## where

- **x** and are two vectors that contain the data for the two variables for **y with the same length x** and

- which independence is to be tested (note that **y** cannot simply be the names of two variables in a dataframe).

Note that in this case it is not necessary to specify the parameter **p** , as the theoretical reference distribution under the null hypothesis is the one expected under the independence hypothesis and is calculated automatically by the function.

**Important: when both the variables take 2 levels only, the function applies a correction factor, and therefore the results obtained using RStudio do not coincide with those obtained using the formula presented above**

## Hands on: Customer class and nr of campaigns joined

The dataframe **Class_Campaign** contains data on the customer’s class and the number of joined campaigns.

To test the hypotheses

**H:** two variables are vs. **0 independent**

**H:** two variables **are 1 not independent**

We use the function **chisq.test** to calculate the p-value:

**> chisq.test(x=Class_Campaign$Num,y=Class_Campaign$Class)**

**Pearson's Chi-squared test**

**data: Class_Campaign$Num and Class_Campaign$Class X-squared = 27.921, df = 6, p-value = 9.725e-05**

_The hypothesis of independence is rejected, whatever level of significance is chosen; we therefore conclude that the two variables are associated_

## Related Notes
- [[Lecture 17-21 Slides_Hypotheses Testing]]
- [[Lecture 15-16 Interval Estimation with FULL NOTES]]
- [[Lecture 15-16 Interval Estimation]]