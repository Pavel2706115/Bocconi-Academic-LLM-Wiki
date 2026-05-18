**==> picture [42 x 165] intentionally omitted <==**

# **SUMMARY MEASURES: DISPERSION MEASURES** 

**Material prepared by R. Piccarreta for students on course 30001 / Bocconi University. Distribution - even via the web - without authorisation is prohibited.** 

## **Motivation** 

## Consider the two distributions below. 

**==> picture [287 x 151] intentionally omitted <==**

**==> picture [287 x 163] intentionally omitted <==**

## **Considerations?** 

- Both distributions are symmetrical and are characterised by the same measures of central tendency 

- The level of dispersion around the centre is different: the first distribution is more dispersed (longer tails) 

- We can effectively describe and summarise the differences between the distributions using a box plot or by comparing their percentiles 

- **measures** that 

- However, we may be interested to use effectively summarise the differences between the two distributions in terms of dispersion 

**2** 

## **Introduction** 

- A **measure of dispersion or variability** quantifies and summarises the amount of dispersion in the observed data 

- Quantifying the amount of dispersion is crucial especially when summarising the distributions of numerical variables. 

- Although measures of dispersion have also been introduced for qualitative variables, here we focus on the most relevant and common measures of variability, defined only for **numeric variables** 

## **Variability** 

**==> picture [632 x 100] intentionally omitted <==**

**----- Start of picture text -----**<br>
Range of  Difference  Variance Standard  Coefficient of<br>variation (range)  deviation variation<br>Interquartile<br>**----- End of picture text -----**<br>


**3** 

**==> picture [42 x 165] intentionally omitted <==**

**==> picture [29 x 100] intentionally omitted <==**

# **Variability/dispersion measures Range of variation and interquartile range** 

## **Range of variation (or range)** 

The simplest and most intuitive measure of dispersion is based on the evaluation of the **width of the interval** containing **all the observed data, the** so-called **range of variation** given by the difference between the highest and lowest observed value 

 **Example.** Amount spent on the website of a pharmacy (11 transactions in a certain day) 

**Ordered data Range 55.5 60.4 61.3 62.3 66.7 72.8 74.6 80.2 81.1 90.5 91.3 91.3 - 55.5 = 35.8** 

**5** 

## **Range of variation (or range)** 

**Example.** Amount spent on a pharmacy's website related to 9 transactions in one day 

## **Ordered data** 

## **55.5 60.4 62.3 66.7 72.8 74.6 81.1 90.5 91.3** 

## **Range 91.3 - 55.5 = 35.8** 

Suppose that exactly the same data were observed on other days, except for the maximum or minimum transaction amount 

## **Ordered data** 

**55.5 60.4 62.3 66.7 72.8 74.6 81.1 90.5 111.1 55.5 60.4 62.3 66.7 72.8 74.6 81.1 90.5 148 25.8 60.4 62.3 66.7 72.8 74.6 81.1 90.5 91.3 60.3 60.4 62.3 66.7 72.8 74.6 81.1 90.5 91.3** 

## **Range** 

**55.6 92.5 65.5** 

**30.0** 

_Being based exclusively on minimum and maximum values, the is a_ _**non-robust range** measure, very sensitive to the presence of_ _**extreme values** , very far from the rest of the data._ 

**6** 

## **The interquartile range (or difference)** 

The range is sensitive to extreme values i.e. **not robust** with respect to extreme values. A possibility to circumvent this problem is to eliminate the largest and the smallest values and to calculate the range on the remaining ones. 

The **interquartile range** is the length of the interval containing the 50% of central values, i.e. the range calculated by excluding 25% of the smallest data and 25% of the largest data It is defined as the ~~difference between the third and first quartile: IQR = Q3 - Q1~~ (width of the box in the box plot), and inform about the width of the interval including central values around the median. It is a **robust** measure **, not influenced by extreme values** 

 **Example.** Amount spent on the website of a pharmacy (9 transactions in one day) 

**Ordered data IQR 81.1 - 62.3 = 18.8** 

**55.5 60.4 62.3 66.7 72.8 74.6 81.1 90.5 91.3** 

**Q1 =62.3 Q3 =81.1** 

**7** 

**==> picture [42 x 165] intentionally omitted <==**

**==> picture [29 x 100] intentionally omitted <==**

# **Variability/dispersion measures Variance and standard deviation** 

## **The variance: deviations from the mean** 

The **variance** is a measure of the dispersion of data around their mean. Referring initially to a sample, consider: 

> **val** ue fore **o** r the sservato sull' - esimo caso _i_ -th observation _i_ 

> _[x] i_ ~~_x_~~ media dei d **a** nti sample me _x_ ~~_x_~~ ( _i_ − ) 

The **deviation** of _x_ from the mean: _i_ 

 quantifies the deviation of the _i-_ th observation from the centre (i.e. the sample mean)  _x_ quantifies the error that occurs if _i_ was replaced (or estimated) by the sample mean 

A measure of dispersion can therefore be based on the deviations from the mean. Such a measure would provide both a summary of the dispersion around the centre and a measure of the risk involved when using the mean as “representative” of the observed data. 

**9** 

## **The variance: summary of deviations** 

Note that 

 The **sum of the deviations of the data from the mean is zero** (the mean is the centre of gravity of the data). Thus, the deviations from the mean cannot be directly used to assess dispersion. 

- When assessing the dispersion around the mean, we are not really interested to the **direction of the deviations** (values higher or lower than the mean) but, rather, to their **magnitude** 

The dispersion around the mean can therefore be summarised by the **mean of** the **squared deviations from the mean,** the so-called **variance** 

**10** 

## **The variance: definition for population and sample** 

The definition of variance is slightly different for populations and samples.  The **population variance** (variance of a population) is defined as: 

**==> picture [812 x 83] intentionally omitted <==**

 The **sample variance** is instead defined as: 

𝑛 1 𝑠[2] = (𝑥𝑖 − ҧ𝑥)[2] where ҧ𝑥 is the sample mean 𝑛 −1[෍] 𝑖=1 

- 

- _**n**_ 

- This is not exactly the **mean of the squared deviations** , since the sum is divided by **(** _**n.**_ 

- **1)** and not by The reason for this difference will be explained when discussing about inference, and specifically about estimation 

**11** 

## **The variance: characteristics** 

: Without loss of generality we focus on the **sample variance** 

**==> picture [219 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑛<br>1<br>𝑠 [2] =<br>(𝑥𝑖 −ҧ𝑥) [2]<br>𝑛−1  [෍]<br>𝑖=1<br>**----- End of picture text -----**<br>


## note that 

- The variance is calculated based on **all the observed values** and not focusing on specific values or summaries as in the case of the range and interquartile range 

- Being based on the mean (that is sensitive to extreme values) and being itself the mean of the squared deviations of the data from mean, the variance is a **non-robust** measure of dispersion. Thus, it is influenced by possible extreme values 

- The variance can be interpreted as the “average” **squared error** incurred when replacing the raw data with their mean. Therefore, it can also be regarded as a measure of the **reliability of the mean as a summary of the data** 

**12** 

**==> picture [456 x 212] intentionally omitted <==**

## **The variance: indirect calculation formula [OPTIONAL]** 

## Focusing on the **sample** variance, we note that: 

**==> picture [753 x 247] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑛 𝑛 𝑛 𝑛<br>1 1 1<br>𝑠 [2] = 𝑛−1 [෍] (𝑥𝑖 −ҧ𝑥) [2] = 𝑛−1 [෍] (𝑥𝑖2 + ҧ𝑥2 −2𝑥𝑖ҧ𝑥) = 𝑛−1 ෍ 𝑥𝑖2 + 𝑛ҧ𝑥2 −2ҧ𝑥෍ 𝑥𝑖<br>𝑖=1 𝑖=1 𝑖=1 𝑖=1<br>𝑛 𝑛<br>1 1<br>= 𝑛−1 ෍ 𝑥𝑖2 + 𝑛ҧ𝑥2 −2𝑛ҧ𝑥2 = 𝑛−1 ෍ 𝑥𝑖2 −𝑛ҧ𝑥2<br>𝑖=1 𝑖=1<br>𝑛<br>2<br>𝑛 𝑥𝑖 The variance can be calculated from the mean<br>= of the squared data and the square of the<br>𝑛−1 ෍ 𝑛 [−ҧ𝑥][2]<br>𝑖=1 mean!<br>**----- End of picture text -----**<br>


**==> picture [507 x 107] intentionally omitted <==**

**----- Start of picture text -----**<br>
In the case of a  population,  the same reasoning leads to:<br>𝑁<br>𝑁<br>1 2<br>𝑥<br>σ [2] = − 𝑖<br>(𝑥𝑖 μ) [2]<br>𝑁 [෍]<br>= ෍ 𝑁 [−] [μ][2]<br>𝑖=1<br>𝑖=1<br>**----- End of picture text -----**<br>


**13** 

## **The variance: indirect calculation formula** 

Focusing on the **sample** variance, we introduce the so-called indirect calculation formula, that can be useful to calculate the variance in some cases: 

**==> picture [386 x 68] intentionally omitted <==**

_The variance can be calculated based on the mean of the squared data and on the squared mean!_ 

We will use this formula only in particular cases, and specifically when the variance is calculated based on grouped data (for example in the case of variables measured in classes). 

**14** 

## **The variance: calculation on raw data** 

_n_ = 9 customers: **35 25 54 60 44 61 27 55 62 Example.** Age in years measured on a sample of 

 _The average is:_ 35 + 25 + ... + 55 + 62 423 ~~_x_~~ = = = **47** 9 9 

 _The variance is:_ 

2 2 2 2 − − 35 47 + 25 47 + ... + 55 - 47 + 62 - 47 1740 2 ( ) ( ) ( ) ( ) _s_ = = = **217.5** 8 8 : _Indirect calculation formula_ 9 2 _x_  _i_ 2 2 2 _i_ = 19 = 35 + 25 9 + ... + 62 = **21621** 9 = **2402.333** _s_ 2 = 98[(] 2402.333 − 472 ) = **217.5** 

 : _Indirect calculation formula_ 

**15** 

## **Standard Deviation** 

The interpretation and the evaluation of the variance can be complicated by the fact that, being based on the **squared** deviations from the mean **,** its unit of measurement is the squared unit of measurement of data. 

- A measure of dispersion around the mean having the same unit of measurement as the data is obtained by considering the square root of the variance, the **standard deviation (sd):** 

## **Sample Standard Deviation:** 

## **Population Standard Deviation:** 

**==> picture [645 x 66] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 n 1 N<br>2 2 2 2<br>s = s = ( xi − x ) =  =  ( xi − )<br>− []<br>n 1 i = 1 N i = 1<br>**----- End of picture text -----**<br>


- ~~The standard deviation can be interpreted as a measure of the~~ ~~**average (standard) distance (absolute deviation)** of the data from the mean~~ (since the variance is the average squared deviation from the mean) 

**16** 

## **Rstudio: distr.summary.x() - dispersion** 

The function **distr.summary.x()** allows determining dispersion measures, specified via the **stats** argument **.** You can either use **stats="dispersion"** to obtain all dispersion measures, or list the specific statistics you are interested in ( **"range"** , **"IQrange"** , **"sd"** , **"var"** ) 

**distr.summary.x(x, stats="dispersion", data) distr.summary.x(x, stats=c("range"** , **"IQrange"** , **"sd"** , **"var"), data)** 

**> distr.summary.x(x=Profitability,stats="dispersion", data=Loyalty) Summary measures for Profitability Measures of dispersion** We will discuss about this in a moment **n n.a range IQrange  sd      var   cv 125   0 765.2   141.3 156 24335.64 0.67** 

_The dispersion measures suggest that the distribution has relatively long tails, as one can note from the difference between the range and the interquartile range. The standard deviation indicates that the deviation (in absolute value) of the data from the mean is 'on average' 156 points. As we will discuss in more details later, it is not trivial to assess whether the observed standard deviation is high or not, since such evaluation must necessarily take into account also the size of the mean around which the data are dispersed_ 

**17** 

## **Variance and standard deviation for grouped data** 

**Nr_visits (Loyalty dataframe): number of visits to the store in the considered period** 

|**Nr_visits**|**_fk_**|**_pk_**|**𝒙𝒌**<br>**∗****_pk_**|𝒙𝒌<br>∗𝟐**_pk_**|
|---|---|---|---|---|
|**1**<br>X&<br>:|**18**|**0.144**|**0.144**|**0.144**|
|**2**<br>X* -|**48**|**0.384**|**0.768**|**1.536**|
|**3**<br>**4**<br>**6**<br>**7**<br>x =<br>=<br>X =<br>YY=|**35**<br>**16**<br>**6**<br>**2**|**0.280**<br>**0.128**<br>**0.048**<br>**0.016**|**0.840**<br>**0.512**<br>**0.288**<br>**0.112**|**2.520**<br>**2.048**<br>**1.728**<br>**0.784**|
|**Totale**|**125**|**1**|**2.664**|**8.760**|



**Variance and standard deviation from the frequency table?** 

To calculate variance and standard deviation, one must calculate the mean and the 'average' of the squared deviations from it or, using the indirect calculation formula, the mean of the squared values 

In the case of grouped data, we saw that the **mean** can be calculated as **the sum of the** . observed distinct values weighted by their **relative frequency In this case, the mean is 2.664** 

Using the same procedure, the **mean of the squared observed values** can be calculated obtaining **8.760** 

This gives 𝒔[𝟐] = (125/124)[8.760 – 2.664[2] ] = **1.6765** and 𝒔 = **1.295** 

**18** 

## **Variance and standard deviation for grouped data** 

In the case of discrete variables, the variance can be calculated also for grouped data, that is when only the variable’s  frequency distribution is available, based on the observed distinct values and on their relative (or absolute) frequencies. 

## For a **sample** 

**==> picture [603 x 273] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑛 𝐾 𝐾<br>1 1 𝑛<br>∗ 2 ∗ 2<br>𝑠 [2] = = =<br>(𝑥𝑖 −ҧ𝑥) [2] (𝑥𝑘 −ҧ𝑥) 𝑓𝑘 (𝑥𝑘 −ҧ𝑥) 𝑝𝑘<br>𝑛−1 [෍] 𝑛−1 [෍] 𝑛−1 [෍]<br>𝑖=1 𝑘=1 𝑘=1<br>𝐾<br>𝑛<br>∗2 2<br>= 𝑥 −ҧ𝑥<br>𝑘 𝑝𝑘<br>𝑛−1 ෍<br>𝑘=1<br>**----- End of picture text -----**<br>


**19** 

## **Calculation for Variables measured in interval classes** 

## Example: variable **Income** (dataframe **Loyalty** ), collected in interval classes 

|**Income**|**_fk_**<br>**_k_**|**_pk_**<br>**_k_**|**_mk_**|**_mk_****_pk_**|**_m_2****_k_****_pk_**|
|---|---|---|---|---|---|
|**[5,15)**|**14 **|**0.112**|**10**|**1.12**|**11.20**|
|**[15,20)**|**26 **|**0.208**|**17.5**|**3.64**|**63.70**|
|**[20,25)**|**37 **|**0.296**|**22.5**|**6.66**|**149.85**|
|**[25,35)**|**24 **|**0.192**|**30**|**5.76**|**172.80**|
|**[35,60)**|**17 **|**0.136**|**47.5**|**6.46**|**306.85**|
|**[60,80]**|**7**|**0.056**|**70**|**3.92**|**274.40**|
|**Totale**|**125 **|**1.00**||**27.56**|**978.80**|



**Variance and standard deviation?** In this case, it is not possible to calculate the measures exactly; they can only be approximated **by discretizing the variable on the midpoints of the intervals** and proceeding as just seen for the grouped data 

Discretizing on the midpoints of the intervals 

- The average is **27.56** 

 The mean of the squared values is **978.80** 

This gives 𝒔[𝟐] = (125/124)[978.80 – 27.56[2] ] = **221.01** e 𝒔 = **14.87** 

**20** 

## **Applications / 1** 

# **Comparison of income per household in UK and US (excluding the richest 5%, US data processed for teaching purposes)** 

**==> picture [240 x 251] intentionally omitted <==**

**==> picture [242 x 250] intentionally omitted <==**

_Variance and standard deviation_ _**both have a unit of measurement** ; therefore they are_ _**absolute** measures of dispersion._ 

_It is meaningless to compare the extent of dispersion in the two distributions based on these measures!_ 

**UK:** ഥ𝒙 = 32467.03; 𝒔 = **16190.32 US:** ഥ𝒙 =94.88; 𝒔 = **66.29 Can we conclude that the distribution of income in the UK is more dispersed than in the US?** 

**21** 

**==> picture [42 x 165] intentionally omitted <==**

**==> picture [29 x 100] intentionally omitted <==**

# **Variability/dispersion measures The coefficient of variation** 

## **The coefficient of variation** 

The coefficient of variation is defined as: 

**==> picture [164 x 46] intentionally omitted <==**

It measures the amount of dispersion in the data in **relation to their mean** .  It is an a-dimensional index: it has no unit of measurement. Consequently, it can (and should) be used to ~~**compare the dispersion of variables with different units o**~~ **f measurement or with the same unit of measurement but means structurally very different** (for example, the price of cars and the price of scooters) 

 However, the coefficient of variation does **not have a well-defined range** ; therefore, it is not possible to draw conclusions on the level of dispersion of a single distribution based on the CV 

**23** 

## **Applications / 1** 

**Comparison of income per household in UK and US (excluding the richest 5%, US data processed for teaching purposes)** 

**==> picture [240 x 251] intentionally omitted <==**

**==> picture [242 x 250] intentionally omitted <==**

**Can we conclude that the distribution of income in the UK is more dispersed than in the US?** 

_**The CV for UK and US is** CV_UK: 16190.32/32467.03 =_ **0.499** _CV_US: 66.29/94.88 =_ **0.699** 

_In relation to the mean, the income is more dispersed in the US, despite lower standard deviation and variance:_ 

- _1) due the different_ _**currency** (£ and $) 2) because the US income is_ _**measured** in thousands of $_ 

**UK:** ഥ𝒙 = 32467.03; 𝒔 = **16190.32 (sterling, £) US:** ഥ𝒙 =94.88; 𝒔 = **66.29 (thousands, $)** 

_**The CV allows a correct comparison between data with different units of measurement.**_ 

**24** 

## **Applications / 1** 

# **Comparison of income per household in UK and US (excluding the richest 5%, US data processed for teaching purposes)** 

**==> picture [240 x 251] intentionally omitted <==**

**==> picture [242 x 250] intentionally omitted <==**

_The CV of the distribution of  income in US is [data in thousands of dollars]: CV= 66.29/94.88 = 0.699 [data in dollars]:_ 

_CV= 66290/94880 = 0.699 By changing the scale (dollars or thousands of dollars), the mean, the variance and the standard deviation_ _**change! The coefficient of variation instead does not change because it does not react to changes in the unit of measurement!!!**_ 

**US (income in thousands of dollars)** : ഥ𝒙 =94.88; 𝒔 = **66.29** ഥ **US (income in dollars)** : 𝒙 =94880; 𝒔 =66290 **The mean and the standard deviation change with the unit of measurement** 

**25** 

## **Applications / 2** 

Let us consider the average one-year return and volatility (standard deviation) of the shares of some companies, evaluated considering the same years 

||**Mean**|**Variance**|**sd**|
|---|---|---|---|
|**Amazon**|0.362|0.471|0.686|
|**Coca-Cola**|0.072|0.023|0.151|
|**Colgate**|0.075|0.019|0.137|



||**CV**|
|---|---|
|**Amazon**|1.896|
|**Coca-Cola**|2.109|
|**Colgate**|1.824|



## **Comments?** 

Amazon’s shares have a much higher volatility compared to  those of Coca-Cola and Colgate. 

_The standard deviations of the returns of the three stocks are different, but so are their averages! The average returns of Coca-Cola and Colgate are lower, and this implies lower deviations from their averages._ 

_In contrast, the CVs show that_ _**the variability of returns, expressed as a % of the average return, is greater for Coca-Cola! The conclusion is opposite to that reached by comparing the standard deviations.**_ 

_**The CV also allows a correct comparison between data with the same unit of measurement (here %) but very different averages (related to different phenomena)**_ 

**26** 

