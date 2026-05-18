**==> picture [42 x 165] intentionally omitted <==**

## **POINT ESTIMATION** 

**Material prepared by R. Piccarreta for students of course 30001 / Bocconi University. All right reserved. Distribution - even via the web – without permission is prohibited.** 

## **Covered so far... [READING]** 

- Descriptive statistics: description of the characteristics of a set of observations with reference to a specific variable. Observations might consist of a **sample** or of the **entire** . 

- **population** 

   - Measures of (central or non-central) tendency and dispersion, calculation of the frequency with which values of a variable are observed; calculation of measures summarizing the extent of the relationship between two variables (correlation and covariance) 

- Random variables: description of the outcome of a **random** sampling of a unit from a population with **known** characteristics **.** 

   - It is not possible to know with certainty what the observed result will be for a randomly drawn unit: a random variable describes the probabilities with which specific values are observed, as well as the characteristics of the population (e.g. expected value and variance) 

   - draws from the **same** 

   - In the case of repeated **independent** population, it is not possible to know with certainty what the values of the calculated statistics (e.g. the mean) will be. However, we have seen that for some statistics it is possible to assess aspects of their probability distribution (expected value and variance, probability of observing specific values) and - in some cases (normal distribution or central limit theorem) - their distribution is known. 

**2** 

## **Inference [READING]** 

**Inferential** statistics concerns the procedures required to make **extrapolations** on **parameters** of a population 𝑿 from **statistics** (e.g. the sample mean) calculated for a simple random sample 𝑿1, 𝑿2, … , 𝑿𝑛 extracted from 𝑿 

- **Estimation** of a parameter 

   - **Point** estimation: a single value 

 **Interval** estimation: a range of values 

- **Hypothesis testing** for a parameter: assess which of two possible hypotheses is more supported by sample results 

**3** 

## **Point estimation: parameter, estimator, estimate** 

With reference to point estimation, it is fundamental to distinguish between: 

 **Parameter: θ.** Measurable characteristic of the **population with reference to a r.v.** 𝑿 Examples of parameters are the mean, **μ** , or the standard deviation, **σ** , of the population, or the proportion 𝒑 of cases with a certain characteristic in the population. 

 **Estimator:** 𝛉[෡] . **Statistic** used to **estimate θ** . 𝛉[෡] is a function of the outcome of (simple) random sample of 𝑛 i. i. d. draws 𝑿1, … , 𝑿𝑛 distributed as 𝑿 , i.e. 𝛉[෡] = 𝑓(𝑿1, … , 𝑿𝑛) . Since the realisations of 𝑿1, … , 𝑿𝑛 are **random,** 𝛉[෡] is a **r.v.** describing the realisations of 𝛉[෡] with respect 𝑿 . to all the samples that can be extracted from 

For example, the sample mean 𝑿[ഥ] = [(𝑿1 + ⋯+ 𝑿𝑛)/𝒏 ] is a possible estimator of the population mean, **μ** . Note that until a sample is actually drawn, 𝑿[ഥ] is a random variable, whose realisation is not known a priori. 

- **Estimate:** 𝜗[መ] 𝛉[෡] **. Sample realisation of an estimator** calculated from the specific sample 

actually drawn, 𝒙1, … , 𝒙𝑛 . 

For example, extracting a **specific** sample of size 10 from 𝑿 , ( **1, 0.5, 2.5, 4, 3.5, 6, 7, 8, 8.5, 9** ) the realisation of 𝑿[ഥ] is ҧ𝑥 = 5 . 

**4** 

## **Point estimation: parameter, estimator, estimate** 

Examples. We are interested in assessing a master’s degree with reference to the placement of graduates. A simple random sample of 200 graduates one year after graduation is  drawn. 

- **What is the monthly salary a generic graduate can expect?** 

 𝑿 **= monthly salary of a randomly selected graduate** 

 **Parameter of interest: population average,**  **, calculated on all graduates** 

 **Estimator: sample mean (random variable)** 

- **What is the (squared) expected deviation around the average salary?** 

 𝑿 **= monthly salary of a randomly selected graduate**  [2] **Parameter of interest: population variance,**  **Estimator: sample variance (random variable)** 

 **What percentage of graduates found a job within 6 months of graduation?**  𝑿 **= Bernoulli r.v. indicating whether a graduate found (1) or not (0) work within 6 months**  **Parameter of interest: proportion of graduates who found a job within 6 months, p**  **Estimator: sample success rate,** 𝑷[෡] **(random variable, average of** 𝑿1, 𝑿2, … , 𝑿200 **)** 

**5** 

## **Point estimatation: parameter, estimator, estimate [READING]** 

Unlike when we considered extractions from a population described by a r.v. with **known** parameters, in the inferential case the characteristics of the population are **not** known. The inference will necessarily have to be based on the specific estimate corresponding to a specific sample extracted from the population. 

However, to assess the reliability of the inferential procedure, we can ask ourselves: 

- What is the **expected value** of the **estimator we decide to use to estimate a certain parameter?** Does it coincide with the parameter of interest or not? 

 What is the dispersion of the **estimates** around the parameter of interest? Can we expect realisations of the estimator far away from the parameter of interest? And with what probability? With what probability will we extract a sample that yields estimates very far from the parameter? 

**We will assess the reliability of the inferential process by choosing the estimator with the best properties. However, given the estimate calculated from a specific sample, we will not be able to make any assessment, especially with respect to how close (if close at all!) this estimate is to the value of the parameter (which is unknown).** 

**6** 

## **Properties of estimators: unbiasedness** 

A point estimator θ[෠] 𝑛 based on a (simple random) sample of 𝑛 units is said to be **unbiased** for a parameter θ if its expected value coincides with the parameter itself, for any value of 𝑛 and θ : 

෠ 𝐸 θ𝑛 = θ for any value of 𝑛 and θ 

If an estimator θ[෠] 𝑛 is **biased** for a parameter θ , its **bias** is defined by 

**==> picture [192 x 26] intentionally omitted <==**

A **biased** estimator for a parameter θ , is said to be **asymptotically unbiased** if, as the sample size increases, the bias is reduced: 

lim ෠θ𝑛 = 0 or equivalently lim ෠θ𝑛 = θ 𝑛→∞[𝐷] 𝑛→∞[𝐸] 

**7** 

## **Standard error of an unbiased estimator** 

For a generic **unbiased** estimator θ[෠] for a parameter θ , i.e. such that 𝐸(θ)[෠] = θ : 

**==> picture [380 x 35] intentionally omitted <==**

The **variance of an unbiased estimator is the expected squared deviation** of **the estimator** from **the parameter of interest** (as the expected value of the estimator is the parameter itself). **The standard deviation of an unbiased estimator** is called **standard error of the estimator** . The variance (and the standard error) of an unbiased estimator provides information on the **reliability** of the estimator. 

Among all the unbiased estimators for a certain parameter, the one with the smallest **variance (or standard error)** will be preferable, as it guarantees the **greatest concentration of estimates around the parameter.** 

**8** 

## **Estimator for the population mean** 

Given a population described by a r.v. 𝑿, we are typically interested in is its **mean** (or expected = value) 𝐸(𝑿) 𝛍 . A ‘natural’ (or intuitive) estimator for 𝛍 based on an i.i.d. random sample 𝑿1, 𝑿2, … , 𝑿𝑛 , is the **sample mean** 𝑿[ഥ] . 

As we have already seen, **whatever the distribution of** 𝑿 is, the following hold **:** 

ഥ  the expected value of 𝑿[ഥ] is: 𝐸 𝑿= 𝐸 𝑿1 + ⋯+ 𝐸 𝑿𝑛 /𝒏= 𝒏∙𝛍 / 𝒏= 𝛍 therefore 𝑿[ഥ] is an **unbiased estimator for** 𝛍 

 The variance of 𝑿[ഥ] is: 𝑉𝑎𝑟 ഥ𝑿= 𝑉𝑎𝑟 𝑿1/𝑛+ ⋯+ 𝑉𝑎𝑟 𝑿𝑛/𝑛= 𝒏∙𝛔[2] / 𝒏[2] = 𝛔[2] / 𝒏 with 𝛔[2] = 𝑉𝑎𝑟(𝑿) and therefore its standard error is 𝑺𝑬𝑿ഥ = 𝛔[2] / 𝒏 . As 𝒏 increases, the dispersion of **estimates** around 𝛍 decreases! 

In addition 

- It can be shown that given 𝒏 , 𝑿[ഥ] is the unbiased estimator with **minimum variance (the most** _**efficient**_ **)** 

- If 𝑿 is normally distributed, the **distribution** of 𝑿[ഥ] is also **normal;** the same applies, whatever the distribution of 𝑿 , if 𝒏 is sufficiently high (central limit theorem). 

**9** 

## **Estimator for the population variance** 

Note that the variance of 𝑿[ഥ] 𝛔[2] depends on the variance of the population, which **is typically unknown.** To estimate 𝛔[2] one can use the **sample variance** 𝑺[𝟐] : 

𝑛 −[ഥ] 𝑿 𝑿 ( 𝑖 )[2] 𝑺[2] = ෍ 𝑛−1 𝑖=1 

It can be shown that: 

The sample variance 𝑺[2] is an **unbiased estimator** 𝐸(𝑺[2] ) = 𝛔[2] **for** 𝛔[2] **whatever the distribution of** 𝑿 

The so-called **unadjusted** sample variance: 

𝑛 −[ഥ] 𝑿 𝑿 ( 𝑖 )[2] ෨𝑺[𝟐] = ෍ 𝑛 𝑖=1 

𝒏−𝟏 𝑺[𝟐] is characterised by: 𝐸([෨] ) = 𝒏[𝛔][2] 

෨𝑺[𝟐] is a **biased estimator for** 𝛔[2] , but it is **asymptotically unbiased** 

**10** 

## **Hands on: estimating the population mean** 

To assess the efficiency of a call centre, a survey is conducted on a random sample of **300** calls received in a week (dataframe **`CallCenter.P`** *): the day and time of each call, the reason for the contact ( **`Topic`** ), the duration (in seconds) of the wait ( **`TimeWaiting`** ) and of the conversation ( **`TimeTalk`** ) are recorded. Customers are also contacted in order to record whether they are satisfied with the service ( **`Satisfaction`** ) and whether or not their problem has been resolved ( **`Solved`** ). The conversation duration is assumed to have a standard deviation of 150 sec. 

**Determine the estimate of the average conversation duration. What is the standard error of the estimator used and what is its interpretation?** 

- **`xbar <- mean(CallCenter.P$TimeTalk) # no missing values`** 

- **`xbar`** 

- **`[1] 254.3733`** 

_Estimate of the population mean duration_ 

- **`sigmaX <- 150 # standard deviation assumed known > n <- nrow(CallCenter.P) # no  missing values`** 

- **`SE_Xbar <- sigmaX/sqrt(n)`** 

- **`SE_Xbar`** 

_The standard error represents the_ _**expected deviation** of a_ _**generic** estimate from_ **`[1] 8.660254`** _the population mean duration_ 

- This dataframe and all the other used below are in file **`Lesson 13-14_Data.Rdata`** 

**11** 

## **Hands on: estimating the population mean** 

ഥ ഥ **“Since the standard error is** 𝑺𝑬𝑿 **= 8.66 and** 𝒙 **= 254.3733 we can conclude that the expected deviation between the population mean,** 𝛍 **, and 254.3733 is 8.66”. Comments** ? 

The statement is false: **8.66** is the deviation from of a and not of a **expected** 𝛍 **generic specific** estimate! We cannot exclude higher or lower deviations: **8.66** is only a **summary** of the deviations characterising the estimates calculated on **all** possible samples. 

To further clarify this fundamental aspect, remember that since 𝒏 =300, 𝑿[ഥ] has a distribution that can be **approximated** by a normal (central limit theorem): 

𝑿~𝓝(ഥ  **, σ[2]** /300) = 𝓝(  **, 8.66[2]** ) 

**==> picture [247 x 164] intentionally omitted <==**

The standard error measures the **dispersion** of the **estimates** . obtained based on all the possible samples around 𝛍 

_We cannot rule out that the estimate obtained based on the specific available sample (254.3733) is far from_ 𝛍 _. What we can say though is that the probability to draw a sample leading to an estimate close to_ 𝛍 _is higher than the probability to draw a sample leading to an estimate far from_ 𝛍 _. The lower the standard error of the estimator the higher the probability of estimates close to_ 𝛍 _._ 

**μ** 

**12** 

## **Hands on: estimating the population mean** 

**How to obtain an estimator with a lower standard error? What effects on estimation?** By increasing the sample size the standard error of 𝑿[ഥ] decreases. 

**What is the sample size required to reduce the standard error to a maximum of 5 seconds?** For the standard error of the sample mean to be at most 5, we must have: 

**==> picture [567 x 92] intentionally omitted <==**

**Assume that a sample of size 900 is drawn leading to an estimate equal to 7.24. “** _**Since 7.24 is based upon a larger sample (900) such estimate is more reliable than the estimate, 8.66, based on a sample of size 300**_ **”. Comments?** 

Surely the standard error of the estimatore based upon a larger sample is smaller. Therefore the concentration of the possible estimates around 𝛍 will be higher and the probability of estimates far from 𝛍 lower. Nonetheless, we cannot draw any conclusions about a **specific estimate** , because it might be that the larger sample contains some extreme or outlying cases and the smaller sample contains very “central” observations 

**13** 

## **Hands on: estimating the population mean** 

**How would your assessment of the standard error of** 𝑿[ഥ] **and of the sample size needed to have a standard error lower than 5 change if** 𝛔 **[2] was not known?** It is not possible to answer precisely as in the case when the variance is known. Even so, it is possible to **estimate** 𝛔[2] using the sample variance, 𝑺[𝟐] ; the **estimate** of the standard error based on the available sample is: 𝒔𝒆𝑿ഥ = 𝒔[𝟐] /𝒏 

- **`n <- nrow(CallCenter.P)`** 

- **`s2_X <- var(CallCenter.P$TimeTalk) # estimate of the variance`** 

- **`s2_X`** 

- **`[1] 28445.97`** 

- **`se_Xbar <- sqrt(s2_X/n) # estimate of the standard error > se_Xbar`** _Note that the estimated variance based on the sample (and the estimated_ **`[1] 9.737552`** _standard error) is larger than the one assumed before,_ 𝛔[2] = 150[2] =22500 

Based on such estimate we can approximate the sample size needed to reduce the standard error using 𝑛≥𝒔[𝟐] / **5**[𝟐] : 

- **`s2_X/25 [1] 1137.839`** 

- _Based on this result, a sample sized at least_ _**1138** should be drawn. As a precaution, it is best to consider the highest value obtained by using the highest variance for the calculations_ 

**14** 

## **RStudio: a note on missing values [OPTIONAL]** 

**For the sake of completeness, we consider the case when the dataset contains missing values, using the data in the** **`CallCenter.R.NoMiss` and** **`CallCenter.R.Miss` dataframes** 

- **`CallCenter.R.NoMiss$TimeWaiting`** 

- **`[1] 15 35 90 70 51 58 118 38 99 124 113 86`** 

- **`CallCenter.R.Miss$TimeWaiting # missing value [1] 15 35 90 70 51 58 118 38 99 124 113 86 NA > mean(CallCenter.R.NoMiss$TimeWaiting)`** 

- **`[1] 74.75`** 

- **`mean(CallCenter.R.Miss$TimeWaiting,na.rm=T)`** 

- **`[1] 74.75`** 

- **`var(CallCenter.R.NoMiss$TimeWaiting)`** 

- **`var(CallCenter.R.Miss$TimeWaiting,na.rm=T)`** 

- **`[1] 1279.477`** 

- **`# However:`** 

- **`nrow(CallCenter.R.NoMiss)`** 

- **`[1] 12`** 

_When there are missing values, the number of rows in the dataframe (or the length of a data vector)_ _**does not coincide with the number of instances! Note: We will derive the standard error of the estimators using the functions in UBStats for confidence intervals (introduced in the next lessons), which exclude missing values from the calculations!**_ 

- **`nrow(CallCenter.R.Miss) # the number of rows includes the missing value!`** 

- **`[1] 13`** 

- **`complete.cases(CallCenter.R.Miss$TimeWaiting) # not NA`** 

- **`[1] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE FALSE`** 

- **`n.Miss<-sum(complete.cases(CallCenter.R.Miss$TimeWaiting))`** 

- **`n.Miss`** 

- **`[1] 12`** 

* In the exam, datasets will not have NAs i.e. missing values 

**15** 

## **Estimator for the population proportion** 

Another parameter one is typically interested in is the **proportion** 𝒑 **of cases in a population that exhibit a characteristic (coded as 'success’)** , estimated on the basis of a simple random sample of 𝑛 units, by measuring the r.v. 𝑿1, … , 𝑿𝑛 indicating for each unit whether a success was observed (1) or not (0). 

To estimate 𝒑 we use the **sample proportion** 𝑷[෡] . 

- the r.v. 𝑿1, … , 𝑿𝑛 are i.i.d. according to a Bernoulli distribution with parameter 𝒑 , and 𝑷[෡] is therefore their **sample mean.** From the properties of the sample mean we have: 

- ෡ 

- 𝐸 𝑷= 𝐸 𝑿= 𝒑 

෡ 𝑷 is an **unbiased estimator for** 𝒑 , 

- 𝑉𝑎𝑟 ෡𝑷= 𝑉𝑎𝑟(𝑿)/𝒏 = 𝒑(𝟏−𝒑) /𝒏 

The variance of 𝑷[෡] ( **never known** ) is smaller the larger the sample 

- If 𝑛 𝑷 is sufficiently high, the distribution of[෡] can be approximated by a normal distribution ෡𝑷 

- ෡𝑷≈𝓝(𝒑, 𝒑(𝟏−𝒑)/𝒏 ). Note that the variance of is not known (but it can be estimated by substituting 𝒑with its estimate). 

**16** 

## **Hands on: estimating the population proportion** 

The dataframe **`CallCenter.P`** includes, among others, a variable ( **`Solved`** ) indicating whether the customer’s problem has been solved. 

**Estimate the proportion** 𝒑 **of problems solved, and the standard error of the estimator.** 

```
> table(CallCenter.P$Solved)
```

```
  N Y
```

```
 27 273
```

Success in this case is coded as **`Y`** ! The estimate of 𝒑 is (there are no missing values) 

ෝ𝒑 **=273/300=0.91** 

෡ 𝑉𝑎𝑟 with its 𝑷= 𝒑(𝟏−𝒑) /𝒏 is not known (it depends on 𝒑 ) but it can be estimated by substituting 𝒑 estimate. Thus, the estimate of the standard error is 

ෝ ෝ 𝒔𝒆𝑷෡ = 𝒑∙(𝟏− 𝒑)/𝒏= **0.91∙(1−0.91)/300** = **0.0165** 

## **What can you conclude about the parameter?** 

We **cannot** conclude that 𝒑 is close to 0.91, the expected deviation from 𝒑 of a generic estimate is very low, and –  given the approximately normal distribution of 𝑷[෡] (high sample size, central limit and estimates far from theorem) – estimates are very concentrated around 𝒑 𝒑 are unlikely, though not impossible. 

* Syntax for the calculations using R in the script 

**17** 

## **Estimator for the difference between means (and proportions)** 

In many applications we are interested in evaluating the differences between the averages of two populations 

- Cholesterol-lowering drug 

   - Comparison of average cholesterol levels at the start of the treatment and after a certain period of treatment 

   - Comparison of average cholesterol levels in patients treated with two different drugs 

- Gender gap: comparison of average salary levels for men and women in the same position 

- Marketing campaigns 

   - Average expenditure before and after a sales campaign 

   - Comparison of the percentage of customers clicking on two different banners 

- Comparison of the percentage of users opening the link to an ad posted on different social media (e.g. facebook, instagram) 

**18** 

## **Estimators for the difference between means** 

## Problem setting: 

**==> picture [682 x 222] intentionally omitted <==**

**----- Start of picture text -----**<br>
Population 1 - described by the r.v.  𝑿 Population 2 - described by the r.v.  𝒀<br>𝑿1, … , 𝑿𝒏𝑿 i.i.d. sample of size  𝒏𝑿  from  𝒀1, … , 𝒀𝒏𝒀  i.i.d. sample of size  𝒏𝒀  from<br>𝟐 𝟐<br>𝑿  with mean   and variance  𝛔 𝒀  with mean   and variance  𝛔<br>𝛍𝑿 𝑿 𝛍𝒀 𝒀<br>ഥ𝑿= (𝑿1+ … + 𝑿𝒏𝑿)/𝒏𝑿 ഥ𝒀= (𝒀1+ … + 𝒀𝒏𝒀)/𝒏𝒀<br>𝒏𝑿 𝒏𝒀<br>𝑺𝟐𝑿 = ෍ (𝒏𝑿𝑿𝑖−−𝟏𝑿 [ഥ] ) [𝟐] 𝑺𝟐𝒀 = ෍ (𝒏𝒀𝒀𝑖−−𝟏𝒀 [ഥ] ) [𝟐]<br>𝒊=𝟏 𝒊=𝟏<br>**----- End of picture text -----**<br>


**The parameter of interest is the difference between the means of the two populations** 𝛍𝑿 −𝛍𝒀 

**19** 

## **Estimators for the difference between means** 

To estimate the difference between the means of two populations described by two r.v. 𝑿 and 𝒀 on the basis of two samples 𝑿1, … , 𝑿𝒏𝑿 and 𝒀1, … , 𝒀𝒏𝒀, it is natural to use the estimator: ഥ𝑿−ഥ𝒀. **Whatever the distribution of** 𝑿 and 𝒀 we have: 

- 𝑿−[ഥ] 

- 𝐸([ഥ] 𝒀) = 𝐸(𝑿) −𝐸([ഥ] 𝒀) =[ഥ] 𝛍𝑿 −𝛍𝒀 

   - 𝑿−[ഥ] is therefore an **unbiased estimator for** 

   - ([ഥ] 𝒀) 𝛍𝑿 −𝛍𝒀 

- The variance, and thus the standard error, of the estimator **depends on the relationships between the two populations (and thus between the samples drawn from them) and on the assumptions on the joint distribution of di** 𝑿 **and** 𝒀 **!** 

 The **distribution** of 𝑿−[ഥ] 𝒀[ഥ] also depends on the relationship between 𝑿 and 𝒀 and on their joint distribution. In general, with **large** samples the distribution of the sample means can be approximated with a **normal** (even if the variances are not known). However, some clarifications are necessary - especially for **small** samples; we will discuss about this when knowing the distributions of the estimators will be of crucial importance. 

**20** 

## **Estimators for the difference between means** 

We deal with two specific cases: 

 **Independent** samples. We are interested in comparing the means of two populations on the basis of samples, **possibly of different sizes,** drawn **independently** (e.g. average wages for men and women, profitability of customers reached by different marketing campaigns, sales volumes in restructured and non-restructured stores,…). This is the case where the two samples are made up of different statistical units, so that it makes sense to assume that the results observed on one sample are in no way linked to the results observed on the other. 

 **Paired same** samples. In this case, the two samples represent two measurements from the **statistical units.** For example, the same variable is measured at different times, or under different conditions (e.g. the average amount spent by a customer before and after a promotional campaign, or at different times of the year). Thus, the two samples have the **same size** and are **paired** in the sense that two measurements are available for the same **unit.** 

**21** 

## **Estimator for the difference between means: independent samples** 

In the case of **independent** samples, the sample averages 𝑿[ഥ] and 𝒀[ഥ] are **independent** and thus **uncorrelated,** and the **variance** of the estimator (𝑿−[ഥ] 𝒀)[ഥ] is: 

**==> picture [699 x 71] intentionally omitted <==**

The case where both variances are known is very rare. 

 If the variances **are not known** and are assumed to be **different** , 𝑉𝑎𝑟(𝑿−[ഥ] 𝒀[ഥ] ) is estimated by 2 2 𝟐 𝟐 replacing 𝛔𝑋 and 𝛔𝑌 with the sample variances obtained from the two samples, 𝑺𝑋 and 𝑺𝑌 . 2 2 2  If the two **unknown** variances are **assumed equal,** so that 𝛔𝑋 = 𝛔𝑌 = 𝛔 , the common variance is estimated using the so-called **pooled sample variance:** 

**==> picture [788 x 108] intentionally omitted <==**

**22** 

## **Estimators for the difference between means: paired samples** 

In the case of **paired samples** of size 𝒏 , two measurements are available for each sample unit: 𝑿𝑖 and 𝒀𝑖 ; the differences 𝑫𝑖 = 𝑿𝑖 −𝒀𝑖 can therefore be considered as 𝒏 measurements from the r.v. 𝑫= 𝑿−𝒀 . 

𝑫[ഥ] **=** 𝑿−[ഥ] 𝒀[ഥ] **.** One can then refer to the sample mean of the differences, 

 Clearly 𝐸(𝑫) = 𝛍[ഥ] 𝑫= 𝐸(𝑿−[ഥ] 𝒀[ഥ] ) = 𝛍𝑿 −𝛍𝒀 , 

 As for the variance of 𝑫[ഥ] , by the properties of the sample mean we have that: 

𝑉𝑎𝑟 ഥ𝑫= 𝛔2 𝑉𝑎𝑟(𝑫)/𝒏= 𝐷 /𝒏 

Using the properties of linear combinations of r.v. we have that 

2 2 = 𝑉𝑎𝑟 𝑫= 𝑉𝑎𝑟 𝑿−𝒀= 𝑉𝑎𝑟 𝑿+ 𝑉𝑎𝑟 𝒀−2𝐶𝑜𝑣(𝑿, 𝒀) 𝛔𝑋 +𝛔𝑌 −2𝛔𝑋𝑌 

In this case, it is very rare to assume that the variance of 𝑫= 𝑿−𝒀 is known, as it would 2 be necessary to make assumptions directly on the variance of differences, 𝛔𝐷 , **or** on the variances of 𝑿 and 𝒀 **and** on their covariance (or correlation) 

**23** 

## **Estimators for the difference between means: paired samples** 

To **estimate** the variance of 𝑫[ഥ] **=** 𝑿−[ഥ] 𝒀[ഥ] it is possible to proceed in the same way as for the sample mean, and use the **sample variance** calculated on the differences: 

**==> picture [174 x 66] intentionally omitted <==**

which is clearly related to the variances and sample covariance of the two samples: 

**==> picture [844 x 133] intentionally omitted <==**

**24** 

## **Hands on: estimating the difference between means** 

The dataframe **`Insurance`** (in **`Lesson 13_Data.Rdata`** ) contains information on reimbursements ( **`refunds`** , in $) for healthcare expenses to (unrelated) subscribers with different socio-demographic characteristics ( **`age, sex, bmi -`** body mass index – **`children, smoker, region`** ). 

**Estimate the difference in the average amount of expenditure reimbursed to smokers and nonsmokers,** _**limiting attention to those who do not have children**_ **.** 

The two samples are **independent** as the subscribers have no links to each other 

- **`# extraction of the two samples`** 

- **`refund.smoke <- Insurance$refund[Insurance$smoker=="yes" & + Insurance$children==0]`** 

- **`refund.nosmoke <- Insurance$refund[Insurance$smoker=="no" & + Insurance$children==0]`** 

- **`mean_x <- mean(refund.smoke)`** 

- **`mean_y <- mean(refund.nosmoke)`** 

- **`mean_x_y <- mean_x-mean_y`** 

- **`mean_x_y`** 

```
[1] 23729.57
```

_The average amount reimbursed to smokers is higher. Obviously, there could be other factors that influence spending and that could be 'controlled for', but overall there is a difference between the two means_ 

**25** 

## **Hands on: estimating the difference between means** 

The dataframe **`Insurance`** contains information on reimbursements ( **`refunds`** , in $) for healthcare expenses to subscribers (unrelated) with different socio-demographic characteristics ( **`age, sex, bmi -`** body mass index – **`children, smoker, region`** ). 

**Estimate the standard error of the estimator of the difference in the average amount of expenditure reimbursed to smokers and non-smokers,** _**limiting attention to those who do not have children**_ **.** 

- **`nx<-length(refund.smoke) # no missing values! > ny<-length(refund.nosmoke)`** 

- **`var_x<-var(refund.smoke)`** 

- **`var_y<-var(refund.nosmoke)`** 

- 2 2 

- **`> # S2_pooled`** 𝑛 −1 𝒔 𝟐 𝑋 𝑋 + (𝑛𝑌 −1)𝒔𝑌 

- 𝒔 = 

- **`> var_pooled<-((nx-1)*var_x+(ny-1)*var_y)/(nx+ny-2)`** 𝑃𝑜𝑜𝑙 **`> var_pooled`** 𝑛𝑋 + 𝑛𝑌 −2 **`[1] 54284441`** 2 2 

- 𝒔 𝒔 

- 𝑠𝑒ഥ ഥ = 𝑃𝑜𝑜𝑙 + 𝑃𝑜𝑜𝑙 𝑿−𝒀 

- **`> se_x_y<-sqrt(var_pooled*((1/nx)+(1/ny)))`** 𝑛 𝑛 𝑋 𝑌 

- **`> se_x_y [1] 768.3133`** 

* Please refer to the R script for details on the intermediate results 

**26** 

## **Hands on: estimating the difference between means** 

A clinical study conducted on 44 patients with high (bad) cholesterol levels to evaluate the efficacy of a cholesterol-lowering drug reported the following results: 

Cholesterol level at start of treatment: ҧ𝑥𝑖𝑛𝑖 = 155; 𝑠𝑖𝑛𝑖 = 19.9 Cholesterol level at 8 weeks: ҧ𝑥8𝑤 = 122; 𝑠8𝑤 = 24.5, 𝑠𝑖𝑛𝑖,8𝑤 = 23.4 

**Estimate the average reduction in cholesterol level following treatment. Standard error?** The two samples are **paired** : they relate to two measurements on the same individual 

We obtain the estimate of the difference between means and the estimate of the std error from the available sample statistics. If we had the data for each patient, we could determine them from the differences between the data on cholesterol levels before and after treatment for each patient! _**Estimate of the difference between means**_ **:** 

ҧ𝑥 −ҧ𝑥 = 155 −122 = 𝟑𝟑 𝑖𝑛𝑖 8𝑤 

_**Estimate of the variance of the difference,**_ 𝑫= 𝑿𝑖𝑛𝑖 −𝑿8𝑤 2 2 2 𝒔 = 𝒔 + 𝒔 −2𝒔 = 19.9[2] + 24.5[2] −2 ∙23.4 = 𝟗𝟒𝟗. 𝟒𝟔 𝐷 𝑖𝑛𝑖 8𝑤 𝑖𝑛𝑖,8𝑤 _**Estimate of the standard error of the difference between sample means,**_ 𝑫=[ഥ] 𝑿[ഥ] 𝑖𝑛𝑖 − 𝑿[ഥ] 8𝑤 2 𝑠𝑒 = 𝒔 949.46 ഥ𝑿𝑖𝑛𝑖−ഥ𝑿8𝑤 𝐷/𝑛= /44 = 𝟒. 𝟔𝟒𝟓𝟐𝟖𝟏 The expected deviation of a generic estimate of the difference between means is about 4.65. 

* Syntax for calculations using R in the script 

**27** 

## **Hands on: estimate and estimator of difference between means** 

The dataframe **`Fatalities_US`** contains data on the number of accidents (per 100,000 inhabitants) registered in 48 US states ( **`Accidents`** ). General information on the states is available (unemployment rate, % of drivers aged between 15 and 24, **`YoungDrivers`** ), besides the number of accidents at night ( **`Night`** ) and due to alcohol ( **`Alcohol`** ). In order to fight alcohol-related accidents, an awareness-raising campaign was carried out, following which a new survey of the number of such accidents (per 100,000 inhabitants, **`AlcoholPostCampaign`** ) was collected for each state. **Assess the drop in the average number of alcohol-related accidents after the campaign.** The two samples are **paired** : they refer to observations of the same state before and after the campaign. 

- **`diff <- Fatalities_US$Alcohol-Fatalities_US$AlcoholPostCampaign > mean_d <- mean(diff)`** 

- **`se_diff <- sd(diff)/sqrt(length(diff)) # estimate of standard error`** 

- **`mean_d`** 

- **`[1] 1.281191`** 

- **`se_diff`** 

- **`[1] 0.3328564`** 

_Check on the R script that the same result is obtained from the aggregated statistics_ 

**28** 

## **Estimators for the difference between proportions** 

Problem setting: we are interested in comparing the proportions of a certain phenomenon in two different populations 

## **Population 1** 

## **Population 2** 

𝑿1, … , 𝑿𝒏𝑿 i.i.d sample of size 𝒏𝑿 from 𝑿 𝒀1, … , 𝒀𝒏𝑿 i.i.d sample of size 𝒏𝒀 from 𝒀 distributed according to a Bernoulli with distributed according to a Bernoulli with parameter 𝒑𝑿 (i.e. 𝑿 takes 1 or 0 depending on parameter 𝒑𝒀 (i.e. 𝑌 takes 1 or 0 depending on whether a success is observed or not, and 𝒑𝑿 = whether a success is observed or not, and 𝒑𝒀 = proportion of successes in the population), proportion of successes in the population), with 𝐸 𝑿= 𝒑𝑿 and 𝑉𝑎𝑟 𝑿= 𝒑𝑿(𝟏− 𝒑𝑿 ) with 𝐸 𝒀= 𝒑𝒀 and 𝑉𝑎𝑟 𝒀= 𝒑𝒀(𝟏− 𝒑𝒀 ) ෡𝑷𝑿 = (𝑿1+ … + 𝑿𝒏𝑿)/𝒏𝑿 **= sample** ෡𝑷𝒀 = (𝒀1+ … + 𝒀𝒏𝒀)/𝒏𝒀 = **sample proportion of successes proportion of successes** 

**The parameter of interest is the difference between the proportions in the two populations:** 𝒑𝑿 −𝒑𝒀 

**29** 

## **Estimators for the difference between proportions** 

**To estimate the difference between the proportions in two populations, it is quite natural to** To estimate the difference between the proportions of 'successes' in two populations, it is natural to use the estimator **propose the estimator where and are the sample averages of two samples whose units have** 𝑷[෡] −𝑷[෡] where 𝑷[෡] and 𝑷[෡] 𝑿 𝒀 𝑿 𝒀 are the sample means of two samples whose units have Bernoulli distributions with parameters **Bernoulli distributions with parameters and respectively.** 𝒑𝑿 and 𝒑𝒀 respectively. **For the properties of sample averages: For the properties of sample means:** 

- [෡] 

- **??** 𝑷 − 𝑷[෡] 𝑷 𝑷  𝐸(𝑷[෡] 𝑿 𝑷𝒀) = 𝐸(𝑷[෡] 𝑿) −𝐸(𝑷[෡] 𝒀) = 𝐸(𝑿) −𝐸(𝒀) = 𝒑𝑿 −𝒑𝒀 𝐸([෡] 𝑿 𝒀) = 𝐸([෡] 𝑿) −𝐸([෡] 𝒀) = 𝒑𝑿 −𝒑𝒀 is therefore an −[෡] **unbiased estimator for** 𝑷 𝑷 is therefore an **unbiased estimator for** 

- ([෡] 𝑿 𝒀) 𝒑𝑿 −𝒑𝒀 

- The variance of the estimator **depends on the relationships between** 𝑿 **and** 𝒀 **. In the case of independent samples:**[[෡]][[෡]] 

−[[෡]] 𝑉𝑎𝑟(𝑷[[෡]] 𝑿 𝑷𝒀 ) _is unknown (it depends on_ 𝒑𝑿 and 𝒑𝒀 _), but can be estimated by replacing_ and _with their_ 𝒑𝑿 𝒑𝒀 _estimates, i.e. the observed sample proportions._ 

**==> picture [542 x 135] intentionally omitted <==**

**30** 

## **Hands on: estimating the difference between proportions** 

In order to determine which of two banners, A or B, is more effective, users of a social network are shown one of the two banners chosen at random. We are interested in the Click-Through Rate (CTR) of the two banners, i.e. the ratio between the number of clicks on each banner and the number of banner views served by the ad server (impressions). Banner A is viewed by 2364 users and generates 456 clicks. Banner B is viewed by 2323 users and generates 611 clicks. **Estimation of the difference between the CTRs? Standard error of the estimator?** The CTR is the sample proportion of clicks on impressions; the standard error of the estimator can be **estimated** as the two experiments and thus the two samples are independent. _**Estimates of the two proportions and of their difference:**_ ෝ𝒑𝑨 = 456/2364 = 0.1929 ; ෝ𝒑𝑩 = 611/2323 = 0.263 ; ෝ𝒑𝑨 −ෝ𝒑𝑩 = 𝟎. 𝟏𝟗𝟐𝟗−𝟎. 𝟐𝟔𝟑= −𝟎. 𝟎𝟕𝟎𝟏 _**Estimates of the variances of the sample proportions,**_ 𝑷[෡] 𝑨 _**e**_ 𝑷[෡] 𝑩, ෢ 𝑉𝑎𝑟(𝑷[෡] 𝑨 ) = 0.1929 ∙(1 −0.1929)/2364 = 0.000066 ෢ 𝑉𝑎𝑟(𝑷[෡] 𝑩 ) = 0.263 ∙(1 −0.263)/2323 = 0.000083 _**Estimate of the standard error of the difference between the two sample proportions,**_ 𝑷[෡] 𝑨 _**e**_ 𝑷[෡] 𝑩, ෢ 𝑠𝑒𝑷෡𝑨−𝑷෡𝑩 = 𝑉𝑎𝑟(𝑷[෡] 𝑨 ) + 𝑉𝑎𝑟([෢] 𝑷[෡] 𝑩 ) = 𝟎. 𝟎𝟎𝟎𝟎𝟔𝟔+ 𝟎. 𝟎𝟎𝟎𝟎𝟖𝟑= 𝟎. 𝟎𝟏𝟐𝟐 

- Syntax for calculations using R and using dati in a dataframe ( **`Banner`** ) in the script 

**31** 

## **Recap** 

**==> picture [782 x 408] intentionally omitted <==**

**----- Start of picture text -----**<br>
Parameter Estimator Estimate Samples Standard error,  SE Standard error estimate,  se<br>xxx<br>𝛍 ഥ𝑿 ഥ𝒙 𝛔/ 𝒏 𝒔/ 𝒏<br>෡<br>𝒑 𝑷 ෝ𝒑 𝒑(𝟏−𝒑)/𝒏 ෝ𝒑(𝟏−ෝ𝒑)/𝒏<br>𝟐 𝟐<br>𝒔 𝒔<br>2 2 𝑷𝒐𝒐𝒍 𝑷𝒐𝒐𝒍<br>𝛔 = 𝛔 → +<br>𝑋 𝑌<br>𝒏 𝒏<br>𝑿 𝒀<br>𝟐 𝟐<br>𝛔 𝛔<br>Independent 𝑿 + 𝒀<br>𝒏 𝒏<br>𝑿 𝒀<br>𝟐 𝟐<br>ഥ ഥ 𝒔 𝒔<br>𝛍𝑿 −𝛍𝒀 𝑿− 𝒀 ഥ𝒙−ഥ𝒚 𝛔𝑋2 ≠𝛔2𝑌 → 𝑿 + 𝒀<br>𝒏𝑿 𝒏𝒀<br>𝟐 𝟐 𝟐<br>𝒔 𝒔 + 𝒔 −𝟐𝒔<br>Paired 𝛔𝟐 𝛔𝟐 + 𝛔𝟐 −𝟐𝛔 𝑫 𝑿 𝒀 𝑿𝒀<br>𝑫 𝑿 𝒀 𝑿𝒀<br>𝒏 [=] 𝒏<br>𝒏 [=] 𝒏<br>𝒑𝑿(𝟏−𝒑𝑿) 𝒑𝒀(𝟏−𝒑𝒀) ෝ𝒑𝑿(𝟏−ෝ𝒑𝑿) ෝ𝒑𝒀(𝟏−ෝ𝒑𝒀)<br>𝒑𝑿 −𝒑𝒀 ෡𝑷𝑿 −෡𝑷𝒀 ෝ𝒑𝑿 −ෝ𝒑𝒀 Independent + +<br>𝒏 𝒏 𝒏 𝒏<br>𝑿 𝒀 𝑿 𝒀<br>**----- End of picture text -----**<br>


**32** 

## **From point estimate to interval estimate [READING]** 

**Point estimation:** sample data is used to determine a **single value** to estimate an unknown population parameter. 

In general, a point estimator coincides with the parameter of interest with zero probability! It is virtually impossible for a sample to provide an estimate that coincides with the parameter and –  even if it did – this would not be known. With reference to a point estimator, it is always **necessary to provide information on its standard error in** . **order to correctly convey the dispersion of estimates around the parameter** We may be interested in proposing estimators that **'incorporate' information about the dispersion around the parameter** , as well as in somehow **controlling the probability that** . **the estimator 'covers' the parameter of interest** 

**Interval estimation:** sample data are used to determine an **interval estimator** (whose extremes are functions of the sample observations) that contains an unknown population parameter with **a certain probability** 

**33** 

