**==> picture [42 x 165] intentionally omitted <==**

# **RANDOM VARIABLES AND THEIR COMBINATIONS** 

**Materials prepared by R. Piccarreta for students of course 30001 / Bocconi University. Distribution - including via the web - without permission is prohibited.** 

## **Motivation: the statistical inference problem [READING]** 

The statistical inference problem arises when one is interested in evaluating measures that describe (or summarize) the characteristics of an **entire population** , called _**parameters**_ , but collecting data on all units of the population is _**prohibitively**_ expensive (cost or time), _**difficult**_ or **even** _**impossible.**_ This is the case, for example, when the population is very large (all companies operating in Europe) or not fully defined or accessible (all the people who purchased a certain brand’s products or who were exposed to an advertising message). In such cases, it may be necessary or convenient to collect data only on a **random sample** of units drawn from the population and to infer about population _**parameters**_ based on the sample summary measures calculated on observed data, called _**statistics**_ . 

**2** 

## **Motivation: the statistical inference problem [READING]** 

When inferring a **population parameter** from a **statistic** calculated from a **sample** of size 𝒏, it is crucial to assess the **reliability** of this generalization and the **risk associated with it** . Therefore one must appropriately **quantify the uncertainty** inherent to the fact that inference is **one** based upon only of the samples that could have been drawn from the population. 

Thus, one must evaluate the relationship between the **parameter** of interest and the distribution of the considered **statistic** calculated based on **all the possible samples** of size 𝒏 that can be drawn from the population, in order to quantify, for example, the dispersion of the **statistic** around the **parameter** and the consequent uncertainty of the inferential process. 

In order to make such an assessment, we will first consider the case when it is possible to make assumptions about the population (or better _about the distribution of a variable of interest in the population_ ) and examine: 

▪ The distribution of statistics based on simple random samples drawn from the population ▪ The relationship between the characteristics of this distribution and the parameter of interest Specifically, we consider **random variables* (r.v.)** to describe the outcome of drawing a sample from a population 

- **(*) The formal definition of a random variable was introduced in the Mathematics 2 course.** 

**4** 

**==> picture [42 x 165] intentionally omitted <==**

**==> picture [29 x 100] intentionally omitted <==**

# **Random variables (r.v.) Discrete and continuous random variables** 

## 

## **Discrete r.v.: introduction [see notes]** 

A company is interested to the number of exposures to an advertising message on a social network (during a pre-specified time period) for subjects in a specific segment (for example, subjects with a certain age class). Below are results observed during a marketing campaign on 1500 subjects. 

|.|.|**Consider**𝑿**= nr of exposures for a****_generic_ subject. What can be said about**<br>𝑿**?**<br>_The number of exposures to the message for a  “generic” subject –randomly_<br>_chosen among those targeted during the campaign–  is not known a priori: _<br>_it is impossible to know which subject will be drawn! Thus,_𝑿_is random:_**_it is_**<br>**_not possible to know which value it will take corresponding to a generic_**<br>**_subject but only to assess the probability of observing each possible value._**|
|---|---|---|
|**Exposures**|**Counts**|**Consider**𝑿**= nr of exposures for a****_generic_ subject. What can be said about**<br>𝑿**?**<br>_The number of exposures to the message for a  “generic” subject –randomly_<br>_chosen among those targeted during the campaign–  is not known a priori: _<br>_it is impossible to know which subject will be drawn! Thus,_𝑿_is random:_**_it is_**<br>**_not possible to know which value it will take corresponding to a generic_**<br>**_subject but only to assess the probability of observing each possible value._**|
|**0**|**525**||
|**1**|**450**||
|**2**|**300**||
|**3**|**150**||
|**4**|**75**||
|**Total**|**1500**||
||||



**Consider** 𝑿 **= nr of exposures for a** _**generic**_ **subject. What can be said about** 𝑿 **?** 

**What is the probability that a generic subject did not visualize the advertising message?** _Probability of drawing one of the subjects who did not visualize the message Since the subjects who did not visualize the message are 525 out of a total of 1500 :_ 𝑃𝑟 **(** 𝑿 **= 0) = 525/1500 = 0.35** 

**6** 

## **Discrete r.v.: probability function [see notes]** 

Number of exposures to an advertising message on a social network (during a pre-specified time period) for subjects in a specific segment; campaign targeting 1500 individuals. 

|||**r.v.**𝑿**= nr of exposures for a randomly chosen subject.**<br>𝑿is a**discrete r.v. (counting process)**that can take 5 values only. The<br>**probabily**function of a random number assigns a probability to each value<br>𝑥:<br>035<br>= 0|**r.v.**𝑿**= nr of exposures for a randomly chosen subject.**<br>𝑿is a**discrete r.v. (counting process)**that can take 5 values only. The<br>**probabily**function of a random number assigns a probability to each value<br>𝑥:<br>035<br>= 0|**r.v.**𝑿**= nr of exposures for a randomly chosen subject.**<br>𝑿is a**discrete r.v. (counting process)**that can take 5 values only. The<br>**probabily**function of a random number assigns a probability to each value<br>𝑥:<br>035<br>= 0|
|---|---|---|---|---|
|**Exposures**|**Counts**||||
|**0**|**525**||||
|**1**|**450**||||
|**2**|**300**||||
||||035<br>= 0||
|**3**|**150**||||
||||𝑃𝑿<br>𝑥=<br>.<br>𝑥<br>0.30<br>𝑥= 1<br>0.20<br>𝑥= 2<br>0.10<br>𝑥= 3<br>0.05<br>𝑥= 4<br>0<br>𝑎𝑙𝑡𝑟𝑜𝑣𝑒||
|**4**|**75**||||
|**Total**|**1500**||||



The probability function describes the **population** , that is, the characteristics of a generic population element with respect to 𝑿. In this case, the probability of observing each value is equal to the frequency of the value in the population. 

**7** 

## **Discrete r.v.: probability function, expected value [see notes]** 

The company is about to launch a new marketing campaign aimed at all the subjects in the **assumes** target segment, and that the probability of exposures to the advertising message is . **the same observed in the previous “pilot” campaign** 

**What is the probability function of** the **r.v.** 𝑿 _**=**_ **“** _**number of exposures to the ad for a generic subject”?**_ 

|**_bject”?_**|||
|---|---|---|
|0.35|𝑥= 0|_The probability function describes the outcome of a single_|
|0.30|𝑥= 1|_"random sampling" from the population, based on the_|
|𝑃𝑿<br>𝑥=<br>0.20<br>0.10|𝑥= 2<br>𝑥= 3|**_assumptions_** _made about the number of exposures to the ad_<br>_based on past experience._|
|0.05|𝑥= 4||
|0|𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒||



## **What is the expected number of exposures for a generic subject?** 

_To determine the_ _**expected value** of  the r.v._ 𝑿 _it is necessary to consider the values that can be observed for a generic subject, weighted by their probability of occurrence!_ 

     𝐸 𝑿= 0.35 0 + 0.30 1 + 0.2 2 + 0.1 3 + 0.05 4 = 1.2 

**8** 

## **Discrete r.v.: probability function and variance [see notes]** 

The company is about to launch a new marketing campaign aimed at all the subjects in the **assumes** target segment, and that the probability of exposures to the advertising message is . **the same observed in the previous “pilot” campaign** 

## **r.v.** 𝑿 _**=**_ **“** _**number of exposures to the ads for a generic subject”**_ 

0.35 𝑥= 0 0.30 𝑥= 1 0.20 𝑥= 2 𝐸 𝑿= 1.2 𝑃 𝑥= 𝑿 0.10 𝑥= 3 0.05 𝑥= 4 0 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒 **Expected quadratic deviation from** 𝐸 𝑿 **of the number of exposures for generic subject** _? Again, it is necessary to consider the values of quadratic deviations that can be observed on a generic client and weight them by their associated probability!_ 𝑉𝑎𝑟 𝑿= 0 −1.2[2] ∙0.35 + 1 −1.2[2] ∙0.3 + 2 −1.2[2] ∙0.2 + 3 −1.2[2] ∙0.1 + 4 −1.2[2] ∙0.05 = 1.36 

**9** 

## **Discrete r.v.: probability and cumulative distribution function** 

A **discrete** random variable 𝑿 can take only a **countable number of distinct values Probability function** of 𝑿: assigns to each value 𝑥 the probability that 𝑿 is equal to 𝑥: 

𝑃 𝑿 𝑥= Prob(𝑿= 𝑥) 

_Probability to observe on a unit randomly selected from a_ 𝑥 _on_ 𝑿 _population the value_ 

This function has the following properties: 

- 0 ≤𝑃 𝑥≤ 1    for each 𝑥 𝑿 

σ𝑥 𝑃𝑿 𝑥= 1 

**The cumulative distribution function** of 𝑿 associates to each 𝑥 the probability that 𝑿 is 𝑥: less than or equal to 

𝐹 ≤ 𝑿 𝑥= Prob(𝑿 𝑥) 

_Probability to observe on a unit randomly selected from a_ 𝑿 𝑥 _. population a value on at most equal to_ 

**10** 

## **Discrete r.v.: expected value and variance [see notes]** 

For random variables, we are also interested in calculating some summary measures, such as the **expected value** and the **variance.** 

**Expected value** 𝐸 𝑥𝑃 𝑿(𝑥) 𝑿= μ = ෍ 𝑥 **Variance: expected quadratic deviation of the values of** 𝑿 **from the expected value** 𝑉𝑎𝑟 𝑿= σ[2] = 𝐸[2] 𝑿−μ = 𝐸(𝑿[2] ) −μ[2] 

**Note:** If the probability function exactly reflects the composition of the population, **the expected value and the variance will coincide with the population mean and variance!** 

**11** 

## **Discrete r.v.: the Bernoulli distribution [see notes]** 

A company assumes that the number of exposures to an advertising message on a social network for a generic subject is characterized by the following probability function. 

It is generally assumed that an ad is more effective when subjects **Exposures Probability 0 0.35** are exposed to it at least 3 times (useful frequency). **1 0.30 What is the probability function of the r.v.** 𝑿 **indicating (1/0) 2 0.20 whether a subject will be exposed to the ad for a “useful” 3 0.10 number of times? 4 0.05** = Prob 𝑿 0 = 0.35 + 0.30 + 0.2 = 0.85 **Total 1.00** = Prob 𝑿 1 = 0.10 + 0.05 = 0.15 0.85 𝑥= 0 𝑥= 0, 1 𝑃 0.15 𝑥= 1 𝑃 𝑿 𝑿 0 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒 𝑥= ቊ[0.15][𝑥][(1 −0.15)][1−𝑥] 0 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒 𝑥= ቐ **Bernoulli ’s r.v.:** for a subject randomly selected from the population, 𝑿 describes whether _success_ 𝑿= 1 𝑿= 0 (an event coded as) a (case when ) or a _failure_ (when ) occurs. 

**12** 

## **Discrete r.v.: the Bernoulli distribution** 

A company assumes that the number of exposures to an advertising message on a social network for a generic subject is characterized by the following probability function. **The r.v.** 𝑿 **indicating (1/0) whether a subject will be exposed to the ad for a “useful” number of times has a Bernoulli distribution characterised by a probability of success equal to = 0.15** 𝒑 

0.85 𝑥= 0 𝑥= 0, 1 𝑃 0.15 𝑥= 1 𝑃 𝑿 𝑿 0 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒 𝑥= ቊ[0.15][𝑥][(1 −0.15)][1−𝑥] 0 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒 𝑥= ቐ 

**Expected value and variance?**   𝐸 𝑿= 0.85 0 + 0.15 1 = 0.15 = 𝒑 𝑉𝑎𝑟 𝑿= 0 −0.15[2] ∙0.85 + 1 −0.15[2] ∙0.15 = = 0.15[2] ∙0.85 + 0.85[2] ∙0.15 = 0.15 ∙0.85 ∙ 0.15 + 0.85 = 0.15 ∙0.85 = 0.1275 = 𝒑 𝟏−𝒑 

**13** 

## **Discrete r.v.: the Bernoulli distribution [see notes]** 

**A Bernoulli's r.v. is characterized by the parameter** 𝒑 **(indicating the probability of observing a success, i.e., the proportion of successes in the population) has a probability distribution:** (1 −𝑝) 𝑥= 0 𝑥= 0, 1 𝑃 𝑥= 1 𝑿 𝑝 0 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒 = ቊ[𝑝][𝑥][(1 −𝑝)][1−𝑥] 0 𝑜𝑡ℎ𝑒𝑟𝑤𝑖𝑠𝑒 𝑥= ቐ **Expected value and variance of** 𝑿~𝐁𝐞𝐫𝐧𝐨𝐮𝐥𝐥𝐢 𝒑: 𝐸 𝑿= 1 −𝑝∙0 + 𝑝∙1 = 𝑝 𝑉𝑎𝑟 𝑿= 0 −𝑝[2] (1 −𝑝) + 1 −𝑝[2] 𝑝= 𝑝−𝑝[2] = 𝑝 1 −𝑝 

**14** 

## **Continuous r.v.: notable distributions** 

Defining a density function that adequately describes the population (based on past experience or on the researcher’s assumptions) can be complicated. Theoretical models have been developed to describe some typical situations 

Uniform r.v.                         Normal r.v.                     Chi-squared r.v. 

**==> picture [176 x 177] intentionally omitted <==**

**==> picture [175 x 176] intentionally omitted <==**

**==> picture [174 x 176] intentionally omitted <==**

These distributions depend on **parameters** that act on their **shape so as** to **fit the assumed** characteristics of the population’s distribution 

**18** 

## **Continuous r.v.: the normal distribution** 

## The two and **σ[2]** determine the characteristics of the distribution **parameters μ** 

## **μ** 

## **Features:** 

- Bell-shaped and symmetrical 

- Centered on the mean **μ** (=median) 

- The amount of spread depends on the standard deviation, **σ** 

- As **μ** and **σ** vary, we get a large collection of density functions 

**σ=8** Changes in **μ** (keeping constant **σ** ) shift the **μ =16** distribution without **μ=5 μ=24** changing its shape **σ μ=16 σ=5** Changes in (keeping constant **μ** ) affect the dispersion and **σ=8** concentration of values around the mean **σ=24** 

**20** 

## **Rstudio: pnorm() and qnorm() - normal distribution** 

**The cumulative distribution function of a normal r.v.** cannot be calculated **manually** by integrating the density function. 

The functions **pnorm()** and **qnorm()** available in R allow to determine the **cumulative distribution function** and the **percentiles** of a normal distribution, respectively. To simplify the syntax as much as possible, we will use the functions in this way: 

**pnorm(q, mean=0, sd=1)** 

**qnorm(p, mean=0, sd=1)** 

## Where: 

- **mean** and **sd** (with default values 0 and 1) allow to specify the parameters of the distribution 

- **q** is the numeric value at which you want to calculate the cumulative distribution function of a normal distribution with the specified parameters. Thus, the function **pnorm()** calculates 𝐹 **`q`** = Prob(𝑿≤ **`q`** ) (i.e., the area under the normal density curve up to **q** ) 

- **p** indicates the order of the **percentile** to be calculated, i.e., the value at which the cumulative distribution function of a normal distribution with the specified parameters is equal to **p** . Thus, the function **qnorm()** calculates 𝒙 **`1−p`** (*) i.e., the value such that 𝐹 𝒙 **`1−p`** = Prob 𝑿≤ 𝒙 **`1−p`** = **p** . 

* The notation 𝒙 **`1−p`** to indicate the percentile of order **`p`** is as used in the textbook 

**21** 

## **Hands-on exercises: the normal distribution** 

**Suppose** the income of freelancers working in a particular industry and region over the past year has a normal distribution with a mean of 71K and a variance of 324K[2] 

## **A professional declares an income of 20K. What considerations?** 

**> sqrt(324) # sd** 

**[1] 18** 

- **# probability that income is less than 20K:** 

- **pnorm(20,mean=71,sd=18)** 

**[1] 0.002303266** 

_The reported income is exceptionally low: only the 0.23% of the population is expected to have an income less than 20K_ 

## **What is the probability that the income is between 20K and 80K?** 

**> pnorm(80,mean=71,sd=18)- pnorm(20,mean=71,sd=18)** 

**[1] 0.6891592** 

## **What is the probability that the income is greater than 90K?** 

**> 1-pnorm(90,mean=71,sd=18)** 

**[1] 0.1455857** 

**22** 

## **Hands-on exercises: the normal distribution** 

# **What is the interval including the 90% of the most common incomes?** 

**> c(qnorm(0.05,mean=71,sd=18), qnorm(0.95,mean=71,sd=18)) [1] 41.39263 100.6074** 

**Declaring an income exceeded only by the 10% of the population qualifies for a certain type of tax relief. What is the minimum income threshold for such relief?** 

**> qnorm(0.9,mean=71,sd=18)** 

**[1] 94.06793** 

**The revenue office decides to systematically assess professionals who declared an income below the lowest 5% of income values. What income threshold triggers the tax assessment?** 

**> qnorm(0.05,mean=71,sd=18) [1] 41.39263** 

**There is a** _**risk**_ **of having a tax assessment if declaring an income below the threshold exceeded by the 70% of the population. What income threshold puts a professional at risk?** 

**> qnorm(0.3,mean=71,sd=18)** 

**[1] 61.56079** 

**23** 

**==> picture [42 x 165] intentionally omitted <==**

**==> picture [29 x 100] intentionally omitted <==**

# **Random variables Linear transformation and standardization** 

## 

## 

## 

**Expected value and variance of linear transformations of a r.v.** 

Consider a **linear transformation** of a **r.v.** 𝑿,  𝒀= 𝑎+ 𝑏𝑿. Expected value and variance of 𝒀 are related to expected value and variance of 𝑿 (μ and σ[2] ): 

𝐸 𝒀= 𝐸 𝑎+ 𝑏𝑿= 𝑎+ 𝑏𝐸 𝑿= 𝑎+ 𝑏μ 

𝑉𝑎𝑟 𝒀= 𝑉𝑎𝑟 𝑎+ 𝑏𝑿= 𝑏[2] 𝑉𝑎𝑟 𝑿= 𝑏[2] σ[2] →𝑆𝑑 ∙ σ 𝒀= |𝑏| ∙𝑆𝑑 𝑿= |𝑏| 

In fact, referring for the sake of simplicity to a discrete r.v. (“proof” required), it is: = 𝐸 (𝑎+ 𝑏𝑥)𝑃𝑿 𝑃𝑿 𝑥𝑃𝑿 𝑥= 𝑎+ 𝑏𝐸 𝑿 𝑎+ 𝑏μ 𝒀= ෍ (𝑥) = 𝑎෍ 𝑥+ 𝑏෍ 𝑥 𝑥 𝑥 2 𝑉𝑎𝑟 𝑎+ 𝑏𝑥− 𝑎+ 𝑏μ 𝑃𝑿 𝑏𝑥−𝑏μ[2] 𝑃𝑿(𝑥) 𝒀= ෍ (𝑥) = ෍ 𝑥 𝑥 = 𝑏[2][2] 𝑃 𝑏[2] 𝑉𝑎𝑟 𝑿 = 𝑏[2] σ[2] 𝑥−μ 𝑿(𝑥) = ෍ 𝑥 (same reasoning for a continuous r.v.) 

**25** 

## **Expected value and variance of linear transformations of a r.v.** 

A company is considering whether to launch a new product with a unit selling price of $25. After considering several scenarios, the company expects to sell 300K units of the product, with an expected deviation of 90K units. The variable product cost per unit is assumed to be $15, while the fixed costs are expected to be $900K. 

**What is the expected profit? What deviation do you expect from the expected profit?** 

𝑿 **=** _**units sold**_ 

𝐸 𝑿= 300𝐾 𝑆𝑑 𝑿= 90𝐾 

𝒀 **=** _**Profit**_ **=** 𝑿∙ 𝟐𝟓−𝟏𝟓−𝟗𝟎𝟎𝑲= 𝟏𝟎𝑿−𝟗𝟎𝟎 𝐸 𝒀= 𝐸 𝟏𝟎𝑿−𝟗𝟎𝟎= 𝟏𝟎𝐸 𝑿−900 = 3000 −900 = 2100𝐾 𝑆𝑑 𝒀= 𝑆𝑑 𝟏𝟎𝑿−𝟗𝟎𝟎= 𝟏𝟎𝑆𝑑 𝑿= 900𝐾 

**26** 

## **Normal r.v.: linear transformation** 

For a given r.v. 𝑿 with expected value and variance equal to μ and σ[2] , we saw that the linear transformation 𝒀= 𝑎+ 𝑏𝑿 has expected value and variance: 

𝐸 𝒀= 𝐸 𝑎+ 𝑏𝑿= 𝑎+ 𝑏𝐸 𝑿= 𝑎+ 𝑏μ 𝑉𝑎𝑟 𝒀= 𝑉𝑎𝑟 𝑎+ 𝑏𝑿= 𝑏[2] 𝑉𝑎𝑟 𝑿= 𝑏[2] σ[2] →𝑆𝑑 𝒀= |𝑏| ∙𝑆𝑑 𝑿= |𝑏| ∙σ 

Nonetheless, it is not always possible to easily determine the probability or density distribution of 𝒀 based on the distribution of 𝑿. Even so, in the **particular case** of a **normally** distributed r.v. 𝑿 , with expected value μ and variance σ[2 ] , any linear transformation of 𝑿 has a **normal distribution:** 

𝑿~𝓝(μ, σ[2] ) → 𝒀= 𝑎+ 𝑏𝑿~𝓝 𝑎+ 𝑏μ, 𝑏[2] σ[2] 

**27** 

## **Standardization of a r.v.** 

We consider a particular linear transformation of an r.v., called **standardization** . Given **any random variable** 𝑿, the **standardized variable** is: 

𝑿−μ 𝒁= σ 

The r.v. 𝒁 is defined based on the expected value and variance of 𝑿 (indicated by μ and σ[2 ] ), and its expected value and variance are the following: 

𝑿 𝐸 𝑿 μ ( ) μ − 𝐸 𝒁= 𝐸 σ[−] σ[=] σ σ[= 𝟎] 𝑿 1 μ 𝑉𝑎𝑟 𝒁= 𝑉𝑎𝑟[𝑉𝑎𝑟(𝑿)][= 𝟏] σ[−] σ[=] σ[2] 

**29** 

## **Normal r.v.: standardization** 

We saw that for a  normally distributed r.v. 𝑿 , with expected value μ and variance σ[2 ] **:** 𝑿~𝓝(μ, σ[2] ) → 𝒀= 𝑎+ 𝑏𝑿~𝓝 𝑎+ 𝑏μ, 𝑏[2] σ[2] 

Therefore, the **standardized normal r.v.** has a normal distribution, with an expected value of 0 and a variance of 1, which is called the **standard normal** distribution. 

𝑿−μ 𝑿~𝓝(μ, σ[2] ) → 𝒁= σ[~𝓝] 0,1 

**Note that for a standardized normal distribution :** Prob 𝒁≤𝟎= **0.5** = Prob **=** 𝒁≥𝟎 **Prob 𝒁≤𝟎= ??0.5 Prob 𝒁≥𝟎** If **If** Prob **Prob** 𝒁≤ **𝒁≤** 𝒛 **𝒛** = **= p** →Prob **→Prob** 𝒁≤−𝒛= **𝒁≤−𝒛= 1   ???1 –– p p p** →Prob 𝒁≥−𝒛= **???** →Prob 𝒁≥−𝒛= **p** 

**-** 𝒛 **0** 𝒛 

**30** 

## **Normal r.v.: standardization** 

Although normal distribution probabilities and percentiles can be easily computed with R, it is important to note that 

𝑿−μ 𝑥−μ 𝑥−μ 𝑿~𝓝(μ, σ[2] ) → Prob 𝑿< 𝑥= Prob < = Prob 𝒁< σ σ σ 𝒙 **`1−`** −μ **`p`** → Prob 𝑿< 𝒙 = → Prob 𝒁< = Prob 𝒁< 𝒛 = **`p p 1−p 1−p`** σ 

𝒙 **`1−`** −μ **`p`** → = 𝒛 → 𝒙 = μ + 𝒛 σ **`1−p 1−p 1−p`** σ → 𝒙 = μ − 𝒛 σ **`1−p p`** 

**31** 

## **Hands on: the standard normal distribution** 

Consider again the income of freelancers working in a particular industry and region over the past year, normally distributed with a mean of 71K and a variance of 324K[2] 

## **Probabily of income lower than 20K calculated using the original and the standard normal** 

**> pnorm(20,mean=71,sd=18)** 

- **[1] 0.002303266** 

- **pnorm((20-71)/18,mean=0,sd=1) # standardisation** 

- **[1] 0.002303266** 

## **90-th percentile calculated using the original and the standard normal** 

**> qnorm(0.9,mean=71,sd=18)** 

- **[1] 94.06793** 

- **71 + qnorm(0.9,mean=0,sd=1)*18** 

- **[1] 94.06793** 

## **10-th percentile calculated using the original and the standard normal** 

**> qnorm(0.1,mean=71,sd=18)** 

- **[1] 47.93207** 

- **71 + qnorm(0.1,mean=0,sd=1)*18** 

- **[1] 47.93207** 

- **71 - qnorm(0.9,mean=0,sd=1)*18** 

**[1] 47.93207** 

**32** 

**==> picture [42 x 165] intentionally omitted <==**

**==> picture [29 x 100] intentionally omitted <==**

**Random variables Linear combinations of random variables** 

## **Joint distribution of** _**two**_ **r.v. [READING]** 

To study **linear combinations** of two **r.v.** we must briefly introduce the concept of **joint distribution.** 

The **joint probability (or density) function** of **two r.v.** 𝑿 and 𝒀 assigns a probability to each pair of values (or each pair of intervals in the continuous case): 𝑃 𝑿𝒀 𝑥, 𝑦= Prob(𝑿= 𝑥, 𝒀= 𝑦) 𝑏 𝑑 Prob 𝑎≤𝑿≤𝑏, 𝑐≤𝒀≤𝑑 = ׬ ׬ 𝑓𝑿𝒀 𝑥𝑦𝑑𝑥𝑑𝑦 𝑎 𝑐 From these functions, the covariance between the two r.v., 𝐶𝑜𝑣 𝑿, 𝒀 , and their correlation, 𝐶𝑜𝑟𝑟 𝑿, 𝒀 , can be determined. 

2 2 Specifically, given the expected values and variances of 𝑿(μ𝑋 and σ𝑋) and 𝒀 (μ𝑌 and σ𝑌): 𝐶𝑜𝑣 𝑿, 𝒀= σ𝑋𝑌 = 𝐸 𝑿−μ𝑋 (𝒀−μ𝑌) 

σ 𝑋𝑌 

= 𝐶𝑜𝑟𝑟 𝑿, 𝒀= ρ𝑋𝑌 σ σ 𝑋 𝑌 

**34** 

## **Bivariate normal distribution [READING]** 

A particularly important joint density distribution is the **bivariate normal** distribution: 

**==> picture [812 x 93] intentionally omitted <==**

where 𝑧 σ and 𝑧 σ 𝑋 = (𝑥− μ𝑋)/ 𝑋 𝑌 = (𝑦− μ𝑌)/ 𝑌 

**==> picture [250 x 196] intentionally omitted <==**

**We will never go into the technical details of this** 

**distribution** ; for our purposes, it is only important to note that if 𝑿 and 𝒀 have a joint normal distribution, then we also have that: 

**==> picture [411 x 55] intentionally omitted <==**

**35** 

## **Independent r.v.** 

A fundamental concept  for the analysis of linear combinations of two r.v. is **independence** 

Two r.v. 𝑿 and 𝒀 are said to be independent if the **probability of observing certain values for one r.v. does not depend in any way on the values taken by the other r.v.** , so that: 𝑃 𝑿= 𝑥Prob 𝑥𝑃 𝑿𝒀 𝑥, 𝑦= Prob 𝑿= 𝑥, 𝒀= 𝑦= Prob 𝒀= 𝑦= 𝑃𝑿 𝒀 𝑦 

𝑓𝑿𝒀 𝑥, 𝑦= 𝑓𝑿 𝑥𝑓𝒀 𝑦 

This means that the probability of jointly observing values of 𝑿 and 𝒀 can be determined from the (marginal) distributions of the two r.v. 

For our purposes, this result is relevant because when two r.v. are **independent** they are also **linearly independent** , that is: 

𝐶𝑜𝑣 𝑿, 𝒀= 𝐶𝑜𝑟𝑟 𝑿, 𝒀= 𝟎 

**36** 

## 

## 

## **Linear combinations of r.v.** 

Consider a **linear combination** of two r.v. 𝑿 and 𝒀 _**:**_ 

𝑎𝑿+ 𝑏𝒀 2 2 with 𝐸 𝑿= μ𝑋, 𝑉𝑎𝑟 𝑿= σ𝑋, 𝐸 𝒀= μ𝑌, 𝑉𝑎𝑟 𝒀= σ𝑌 and 𝐶𝑜𝑣(𝑿, 𝒀)= σ𝑋𝑌. The **expected value** and the **variance** of the linear combination are: 𝐸 𝑎𝑿+ 𝑏𝒀= 𝑎μ𝑋 + 𝑏μ𝑌 2 2 2 𝑉𝑎𝑟 𝑎𝑿+ 𝑏𝒀= 𝑎[2] σ + 𝑏 σ + 2𝑎𝑏σ 𝑋 𝑌 𝑋𝑌 _**IfIf**_ 𝑿 𝑿 and and 𝒀𝒀 _**are independentare independent,?**_ 𝛔𝑿𝒀 = 𝟎 _**and**_ 𝑽𝒂𝒓 𝒂𝑿+ 𝒃𝒀= 𝒂[𝟐] 𝛔𝟐𝑿 + 𝒃𝟐𝛔𝟐𝒀 

The **distribution of** (𝑎𝑿+ 𝑏𝒀) depends on the joint distribution of the two r.v. In the **special case** where 𝑿 and 𝒀 have a **joint normal** distribution it is: 2 2 2 (𝑎𝑿+ 𝑏𝒀) ~𝓝(𝑎μ𝑋 + 𝑏μ𝑌, 𝑎[2] σ𝑋 + 𝑏 σ𝑌 + 2𝑎𝑏σ𝑋𝑌) And therefore, in the case of **independence:** 2 2 2 (𝑎𝑿+ 𝑏𝒀) ~𝓝(𝑎μ𝑋 + 𝑏μ𝑌, 𝑎[2] σ𝑋 + 𝑏 σ𝑌) 

**37** 

## **Linear combinations of r.v. [OPTIONAL]** 

A production process consists of 3 phases, A, B and C. The durations (in minutes) of phases A 2 and B are two r.v., 𝑻𝐴 (μ𝐴=10 and σ𝐴=1) and 𝑻𝐵 (μ𝐵=16 and σ𝐵 =2), which are correlated, with ρ𝐴𝐵=0.2. The duration of phase C is fixed and it’s 4 minutes. **Expected value and standard deviation of the overall duration of the production process?** The overall duration is 𝑻= 𝑻𝐴 + 𝑻𝐵 + 4 (the last phase has a fixed duration, not random) **Expected value:** 𝐸 𝑻𝐴 + 𝑻𝐵 + 4 = μ𝐴 + μ𝐵 + 4 = 10 + 16 + 4 = 𝟑𝟎 **Variance:** 𝑉𝑎𝑟 𝑻 + 𝑻 + 4 = 𝑉𝑎𝑟 𝑻 + 𝑻 = σ2 + σ2 + 2σ 𝐴 𝐵 𝐴 𝐵 𝐴 𝐵 𝐴𝐵 𝐶𝑜𝑣 𝑻𝐴, 𝑻𝐵 = σ𝐴𝐵 = ρ𝐴𝐵σ𝐴σ𝐵 = 0.2 ∙1 ∙2 = 0.4 →𝑉𝑎𝑟 𝑻 + 𝑻 + 4 = 1 + 4 + 2 ∙0.4 = 𝟓. 𝟖 𝐴 𝐵 

**If** 𝑻𝐴 **and** 𝑻𝐵 **are assumed to be jointly normally distributed, what is the probability that the total duration of the process is between 25 and 35 minutes?** 

**> pnorm(35,mean=30,sd=sqrt(5.8))- pnorm(25,mean=30,sd=sqrt(5.8)) [1] 0.9621187** 

**39** 

**==> picture [42 x 165] intentionally omitted <==**

**==> picture [29 x 100] intentionally omitted <==**

# **Random variables Sum and mean of i.i.d. random variables Central Limit Theorem** 

## **Sum and mean of i.i.d. r.v.** 

An important case is when, given a r.v. 𝑿 with expected value 𝛍 and variance 𝛔[2] , we consider 𝒏 r.v. 𝑿𝟏, 𝑿2, … , 𝑿𝑛 with the following properties: 

 They are **independent** (and consequently all the pairs 𝑿𝑖 **,** 𝑿𝑘 have **covariance** equal to 0) 

 Thay all have the **same distribution as** 𝑿 That is, 𝑿𝟏, 𝑿2, … , 𝑿𝑛 are **independent** and **identically distributed** ( **i.i.d.** ) as 𝑿. 

𝒏 units from the **same** This is the case, for example, when we consider **randomly selected population** (with replacement, i.e. assuming to repeatedly draw from the entire population) and each of them describes the ( **random** ) result of the selection. 

Consider two particular **linear combinations** of the 𝒏 r.v. 𝑿𝟏, 𝑿2, … , 𝑿𝑛, their **sum** and their **mean:** 

**Sum:** 𝑺= 𝑿 +𝑿 1 2 + ⋯+ 𝑿𝑛 

**Mean:**[ഥ] 𝑿= ( 𝑿1 + 𝑿2 + ⋯+ 𝑿𝑛)/𝒏= 𝑺/𝒏 

**42** 

## **Sum and mean of i.i.d. r.v.: expected value and variance** 

If the r.v. 𝑿𝟏, 𝑿2, … , 𝑿𝑛 are 𝒏 **r.v. i.i.d.** as a r.v. 𝑿, with expected value 𝛍 and variance 𝛔[2] (for 𝑿 **sum** and their **mean** are example, the outcomes of independent observations on ), their . r.v. whose expected values and variances can be determined from 𝛍𝑎𝑛𝑑𝛔[2 ] 

**Sum:** 𝑺= 𝑿1 + ⋯+ 𝑿𝑛 _**All the**_ 𝑿𝑖 _**have the same expected value**_ 𝛍 _**and the same variance**_ 𝛔[2] _**;**_ **→ 𝐸 𝑺=** ?𝐸 𝑿1 + ⋯+ 𝐸 𝑿𝑛 = 𝒏𝛍 _**the covariances are zeros as they are independent.**_ 

- **→ 𝑉𝑎𝑟 𝑺=** ?𝑉𝑎𝑟 𝑿 + ⋯+ 𝑉𝑎𝑟 𝑿 = 𝒏𝛔[2] 1 𝑛 

**Mean:**[ഥ] 𝑿= ( 𝑿1 + ⋯+ 𝑿𝑛)/𝒏= 𝑺/𝒏 

**ഥ → 𝐸 𝑿=** ?𝐸 𝑿1/𝑛+ ⋯+ 𝐸 𝑿𝑛/𝑛= 𝒏∙𝛍/ 𝒏= 𝛍 

**→ 𝑉𝑎𝑟 ഥ𝑿=** ?𝑉𝑎𝑟 𝑿1/𝑛+ ⋯+ 𝑉𝑎𝑟 𝑿𝑛/𝑛= 𝒏∙𝛔[2] / 𝒏[2] = 𝛔[2] / 𝒏 

**43** 

## **Sum and mean of i.i.d. r.v.: distribution** 

Even if it is possible to determine the **expected value** and **variance of the sum and of the mean of** 𝒏 **i.i.d. r.v.** 𝑿𝟏, 𝑿2, … , 𝑿𝑛 **, it is not always possible to determine their probability (or density) functions. However:** 

- **The sum and mean of** 𝒏 **normally distributed i.i.d. r.v.** 𝑿𝟏, 𝑿2, … , 𝑿𝑛, have **normal distribution** , with mean and variance obtained as described above: 

𝑿1, 𝑿2, … , 𝑿𝑛 **i.i.d.** 𝑿 ~𝓝(μ, σ[𝟐] ) 

   - 𝑺= (𝑿1 +𝑿2 + ⋯+ 𝑿𝑛)~𝓝(𝒏μ, 𝒏σ[𝟐] ) 𝑿= (𝑿[ഥ] 1 +𝑿2 + ⋯+ 𝑿𝑛)/𝒏 ~𝓝(μ, σ[𝟐] /𝒏) 

- **Central Limit Theorem:** For **sufficiently** large 𝒏, the distributions of the **sum** and of the **mean** of 𝒏 **r.v.** 𝑿𝟏, 𝑿2, … , 𝑿𝑛 **i.i.d.** as a r.v. 𝑿  can be _**approximated**_ by the **normal distribution** (with expected value and variance as above), **whatever the distribution of** 𝑿 **.** 

**44** 

## **Sum and mean of i.i.d. r.v.** 

A company assumes that the amount spent on its products by a customer in a generic shop where a promotion is running has an average of 22€ and a standard deviation of 9 € . Assume that exactly 80 customers take advantage of the promotion. **Obtain the probability that the average amount spent by the 80 clients is higher than 25** € **, specifying whether and what assumptions are needed to obtain it.** 

It is possible to determine the required probability without specific assumptions, because the hypothesized number of clients is high enough to apply the central limit theorem and **=** approximate the distribution of the mean as follows, 𝑿~𝓝(μ, σ[ഥ][𝟐] /𝟖𝟎) 𝓝(22, 9[𝟐] /𝟖𝟎). **> 1-pnorm(25,mean=22,sd=9/sqrt(80)) [1] 0.0014** 

**What is the total amount spent by the 80 clients that the company can expect to be exceeded with probability 0.9?** 

**> qnorm(0.1,mean=22*80,sd=9*sqrt(80))** 

**[1] 1656.837** 

**45** 

## **Sum and mean of i.i.d. r.v.** 

The daily electricity consumption of a generic household at a given time of year is assumed . to be normally distributed with a mean of 48 Kwh and a variance of 16Kwh[2] **What is the probability that the average daily consumption of 5 households is greater than 50Kwh?** ഥ **=** ~~𝑿~𝓝(μ, σ~~[𝟐] ~~/𝒏)~~ 𝓝(48,16/5) 

**> 1-pnorm(50,mean=48,sd=sqrt(16/5)) [1] 0.1317762** 

**How much electricity is needed to meet the daily electricity demand of 10 households with a probability of at least 0.95? =** We are looking for the 95-th percentile of 𝑺~𝓝(𝒏μ, 𝒏σ[𝟐] ) 𝓝(480,160). **> qnorm(0.95,mean=480,sd=sqrt(160)) [1] 500.8059** 

**Is it possible to determine the required quantities if normality is not assumed?** 

No: the number of cases is too small to apply the Central Limit Theorem 

**46** 

## **Sum and mean of i.i.d. r.v.: Bernoulli distribution** 

Consider 𝒏 **r.v.** 𝑿𝟏, 𝑿2, … , 𝑿𝑛 that are **i.i.d.** as 𝑿~𝐁𝐞𝐫𝐧𝐨𝐮𝐥𝐥𝐢 𝒑 whose parameter is the _**success**_ 𝐸 : probability of observing a in a population, with 𝑿= 𝑝, 𝑉𝑎𝑟 𝑿= 𝑝 1 −𝑝 𝑺= 𝑿 **= number of successes** 1 + 𝑿2 + ⋯+ 𝑿𝑛 ෡ 𝑷= (𝑿1 + 𝑿2 + ⋯+ 𝑿𝑛)/𝒏= **proportion of successes** 

For sufficiently large 𝑛 (typically higher than 30*) the distribution of 𝑺 and 𝑷[෡] can be approximated by a normal distribution, that is 

and[෡] 𝑺≈𝓝(𝒏𝒑, 𝒏𝒑 𝟏−𝒑) 𝑷≈𝓝(𝒑, 𝒑 𝟏−𝒑/𝒏) 

n=5mean=0.125 n=10mean=0.125 n=30mean=0.125 n=100mean=0.125 Distribution of 𝑷[෡] for var=0.021875 var=0.0109375 var=0.0036458 var=0.0010938 increasing values of 𝒏, given 𝑝=0.125 

* When 𝒑 is very small or very high, some authors suggest to verify whether 𝒏𝒑 𝟏−𝒑> 𝟓 

**52** 

## **Sum and mean of i.i.d. r.v.: Bernoulli distribution** 

A company installs surveillance cameras and estimates that the 15% of the installed cameras require post-installation work for changes. **Based on the orders received, 50 cameras will be installed next month. What is the probability that the percentage of cameras requiring postinstallation work will be higher than 25%?** The r.v. describing whether a random camera will require a second intervention is: 𝑿~𝐁𝐞𝐫𝐧𝐨𝐮𝐥𝐥𝐢(𝑝= 0.15); 𝐸 𝑿= 𝟎. 𝟏𝟓; 𝑽𝒂𝒓 𝑿= 𝟎. 𝟏𝟓∙𝟎. 𝟖𝟓= 𝟎. 𝟏𝟐𝟕𝟓 The r.v.’s describing whether each of the 50 installed cameras will require a second intervention, 𝑿1, 𝑿2, … , 𝑿50, are **iid as** 𝑿 The % of cameras (out of the 50 installed) that require further intervention is: ෡𝑷=(𝑿1 + 𝑿2 + … +𝑿50)/50 

Since the sample size is sufficiently large, the distribution of 𝑷[෡] (which is the sample mean of a sample from a Bernoulli population) can be approximated by a normal distribution. 

**> 1-pnorm(0.25,mean=0.15,sd=sqrt(0.15*(1-0.15)/50)) [1] 0.02383519** 

**53** 

