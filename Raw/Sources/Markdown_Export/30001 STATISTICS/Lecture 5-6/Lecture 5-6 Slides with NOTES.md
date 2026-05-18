# **SUMMARY MEASURES: LOCATION MEASURES** 

**Material prepared by for students on course 30001 / Bocconi University. All Rights Reserved. Distribution - including via the web - without permission is prohibited.** 

## **Summary Measures: Motivation [READING]** 

## **Why using summary measures?** 

- Instead of describing all the values taken by one variable using for example tables or graphical tools it is often convenient to summarize the most relevant features of one variable 

- The comparison of different sets of data (populations or samples), even based on suitable tables or graphs, might be difficult or not effective. Summary measures ( **appropriately selected** ) allow to make comparisons easier and more immediate, and to communicate the largest amount of information in the simplest possible way. 

The choice of the summary measures used to effectively describe the most salient features of data depends on the type of data and on the characteristics of their distribution 

**2** 

## **Location measures** 

**Central tendency measures** 

## **Introduction** 

A **central tendency measure** is a single value that summarises **all the observed data.** 

- More precisely, a measure of **central** tendency aims at describing the **“centre” of the** data 

- There are different measures, depending on how we **can** or how we **decide to** define the “ **centre** ” **of the data** 

**----- Start of picture text -----**<br>
Central tendency measures<br>Mode Median Mean (arithmetic)<br>**----- End of picture text -----**<br>

**4** 

## **Mode** 

The **Mode** is **the value (or category)** most frequently observed in a set of data. Thus, the “centre”  of data is taken as the value describing the most typical “behaviour” of cases with respect to a variable 

Being based only upon the frequencies and not on the specific observed values, the mode can be calculated for **all the types of data, both categorical and numerical.** However, as we will discuss later, it might be not particularly effective when a variable takes a very large number of distinct values, that is the typical case for continuous and, sometimes also for discrete, numerical variables. 

**5** 

## **Mode: Examples** 

 **Dep (in dataframe Loyalty): the department where the customer spent the most** 

##  **Satisfaction level measured on** _**n**_ **= 14 customers** 

 **Nr_visits (in dataframe Loyalty): count of store visits within the given period** 

||**Nr_visits**|**_fk_**|**_pk_**||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|freg.<br>table|**1**<br>**2**<br>**3**<br>**4**<br>**6**|**18**<br>**48**<br>**35**<br>**16**<br>**6**|**0.144**<br>**0.384**<br>**0.280**<br>**0.128**<br>**0.048**|More<br>is<br>note<br>that<br>48||||2<br>is|the|abs|,|free·|
||**7**|**2**|**0.016**||||||||||
||**Total**|**125**|**1**|of|the||mode||||||

**6** 

## **Mode: Examples** 

**The mode may not be unique, it can be weak and in some cases it does not exist**  **Recommend.F (in dataframe Loyalty): propensity to recommend the store** 

 **Time needed to close 20 service request tickets 12, 13, 17, 21,** _**24, 24**_ **, 26,** _**27, 27**_ **, 30, 32, 35, 37, 38, 41, 43, 44, 46, 53, 58** 

 _**n**_ **= 10 customers Age in years for a set of 35 25 54 60 44 62 27 55 61 24** 

**7** 

## **Mode: Relevant aspects** 

~~For continuous numerical variables, the mode typically either does~~ ~~**not exist at all**~~ (all values have the same frequency) or it is **weak** (its frequency is the highest but it is very low). This latter case is common also when dealing with discrete variables taking many distinct values. 

In such cases, the so-called **modal class** is used: data are classified into intervals, and the interval with the **hi hest fre uenc densit g q y y** is identified as the modal class. It is important to note that the modal class depends on the specific classification used to group the data. 

**8** 

## **Mode: Relevant aspects** 

 **Profitability** (dataframe **Loyalty** ): profitability of customers, classified into different interval classes. 

## **What is the Modal class in the two cases?** 

**9** 

## **Median** 

The **median** is the value with the **middle position in the ordered sequence of data** . Thus, the “centre” is taken as the value **ideally** dividing the data into two blocks **of the same size** . It therefore separates the higher half of values  from the lower half of values Being based only upon the position of the **order** data and not on the specifically observed values, the median can be calculated **both for ordinal and for numerical** data **.** However, it cannot be calculated for nominal variables, whose values cannot be ordered. 

**10** 

## **Median: Computation (raw numerical data)** 

**** _**n**_ **= 9 customers Age in years measured on 35 25 54 60 44 62 27 55 62 25 27 35 44 54 55 60 62 62** _The median is_ **54** , the value in the middle position in the sequence of ordered data. In this distribution, there are _**4 cases** with values_ _**below 54** and_ _**4 cases** have values above_ _**54** ._ 

**** _**n**_ **= 10 customers Age in years measured on 35 25 54 60 44 62 27 55 61 24 24 25 27 35 44  54 55 60 61 62** _The median is_ **49=(44+54)/2** , the average of the two values in the central positions (44 and 54): _indeed,_ **5** _**cases** (24,25,27,35,44) have values_ _**below 49** and_ **5 cases** _(54,55,60,61,62) have values above_ **49** . 

**11** 

## **Median: Discrete variables** 

**** _**n**_ **= 16 customers : Number of credit card transactions in a store for sample of 4 3 3 1 0 1 2 3 3 4 2 5 4 3 4 5                                       0 1 1 2 2 3 3 3 3 3 4 4 4 4 5 5** 

_The median is_ **3:** data are repeated, and in both middle positions there is the same value. The median value separates the data into two groups; the first includes cases with values less than or equal to 3, the second includes cases with values greater than or equal to 3 Let us consider the frequency distribution of the variable: 

|**Nr_purchases**|**_fi_**<br>**_k_**|**_pi_**<br>**_k_**|**_Fi_**<br>**_k_**|
|---|---|---|---|
|**0**|**1**|**0.0625**|**0.0625**|
|**1**|**2**|**0.125**|**0.1875**|
|**2**|**2**|**0.125**|**0.3125**|
|**3**|**5**|**0.3125**|**0.625**|
|**4**|**4**|**0.25**|**0.875**|
|**5**|**2**|**0.125**|**1**|
|**Totale**|**16**|**1.000**||

**Is it possible to calculate the median from the table?** 

The median (3), is the first (i.e. smallest) value with a cumulative frequency higher than or equal to 0.5 _**–** – [In the case rare when_ _**n** is not small when the cumulative frequency at a value is exactly  0.5, the median is the mean between that value and the next one ]_ 

**12** 

## **Median: Ordinal variables** 

_**n**_ **= 8 customers Satisfaction level measured on a sample of** 

 

_T_ ~~_he median can be computed since data can be sorted (ordinal variable), and the median_~~ _category is_ **Low** , _the first value with a cumulative frequency equals or higher than 0.5 [this explains the definition: it is not possible to calculate the mean between Low e Neutral!!]_ 

 **Recommend.F (in dataframe Loyalty): propensity to recommend the store** 

**Recommend.F Count Prop Very Unlikely 13 0.10 Unlikely 30 0.24 Neutral 31 0.25 Likely 34 0.27 Very Likely 17 0.14 TOTAL 125 1.00** 

**13** 

## **Median: Variables measured in interval classes** 

For discrete or ordinal variables, the median can be **precisely** computed  also in the case when **only the frequency distributions** are available, using cumulative frequencies. However, when a variable is measured in classes and only the frequency table of the classified **raw** variable is available the median cannot be calculated precisely, because the original **numeric data are not available** . In this situation, the median can only **be approximated,** under the over **assumption** that the frequency associated with each interval is **uniformly distributed** the interval. The same holds when a variable is measured in classes. 

**14** 

## **Median: Variables measured in interval classes** 

|||want<br>to<br>calculate<br>an approximated median|want<br>to<br>calculate<br>an approximated median|want<br>to<br>calculate<br>an approximated median|want<br>to<br>calculate<br>an approximated median|want<br>to<br>calculate<br>an approximated median|want<br>to<br>calculate<br>an approximated median|
|---|---|---|---|---|---|---|---|
|||Example: variable**Income** (in dataframe**Loyalty**), measured in classes||||||
|median<br>is inthe<br>first<br>class<br>~~&~~||**Income**<br>**_fk_**<br>**_pk_**<br>**_wk_**<br>**_ck_**<br>**_Fk_**<br>**[5,15)**<br>**14**<br>**0.112**<br>**10 0.011 0.112**<br>**[15,20)**<br>**26**<br>**0.208**<br>**5**<br>**0.042**<br>**0.32**<br>**[20,25)**<br>**37**<br>**0.296**<br>**5**<br>**0.059 0.616**<br>~~cu~~mulative<br>~~f~~requency||*|||&<br>I want the<br>red<br>area<br>to<br>be<br>equial<br>to<br>10.5 - 0 .32) = 0 . 18|
|exceeding<br>cum-free,<br>of 0.,||**[25,35)**<br>**24**<br>**0.192**<br>**10 0.019 0.808**<br>**[35,60)**<br>**17**<br>**0.136**<br>**25 0.005 0.944**<br>**[60,80)**<br>**7**<br>**0.056**<br>**20 0.003**<br>**1**<br>**Total**<br>**125**<br>**1.00**<br>_In this case, it is not possible to calculate the_<br>_exact value of the median because no_||o .3> N<br>il|||base<br>of<br>red rectangle it :<br>0.18<br>= 3<br>. 05<br>0 .059|
|||_information is available on the actual_|_numeric_|||||
|||_values._<br>**_We can approximate the median with the value_**||Median|||: 23 . 05|

_**We can approximate the median with the value at which the cumulated area under the histogram is 0.5.**_ 

**15** 

## **Median: Variables measured in interval classes** 

Example: variable **Income** (in dataframe **Loyalty** ), measured in classes 

|**Income**|**_fk_**|**_pk_**|**_wk_**|**_ck_**|**_Fk_**|
|---|---|---|---|---|---|
|**[5,15)**|**14**|**0.112**|**10 **|**0.011 **|**0.112**|
|**[15,20)**|**26**|**0.208**|**5**|**0.042**|**0.32**|
|**[20,25)**|**37**|**0.296**|**5**|**0.059 **|**0.616**|
|**[25,35)**|**24**|**0.192**|**10 **|**0.019 **|**0.808**|
|**[35,60)**|**17**|**0.136**|**25 **|**0.005 **|**0.944**|
|**[60,80)**|**7**|**0.056**|**20 **|**0.003**|**1**|
|**Total**|**125**|**1.00**||||

(0.5-0.32) = **0.18** 

**What is the interval including the median?** The median is between **20 and 25:** the frequency cumulated up to 20 is 0.32 and the frequency cumulated at 25 is 0.616. 

**Median (approximation)?** The area cumulated up to 20 is 0.32 The area between 20 and the median value must be **(0.5-0.32) = 0.18** 

**16** 

## **Median: Variables measured in interval classes** 

## Example: variable **Income** (in dataframe **Loyalty** ), measured in classes 

|**Income**|**_fk_**|**_pk_**|**_wk_**|**_ck_**|**_Fk_**|
|---|---|---|---|---|---|
|**[5,15)**|**14**|**0.112**|**10 **|**0.011 **|**0.112**|
|**[15,20)**|**26**|**0.208**|**5**|**0.042**|**0.32**|
|**[20,25)**|**37**|**0.296**|**5**|**0.059 **|**0.616**|
|**[25,35)**|**24**|**0.192**|**10 **|**0.019 **|**0.808**|
|**[35,60)**|**17**|**0.136**|**25 **|**0.005 **|**0.944**|
|**[60,80)**|**7**|**0.056**|**20 **|**0.003**|**1**|
|**Total**|**125**|**1.00**||||

(0.5-0.32) = **0.18** 

The width of the interval between **20 and the median value** is the area of the rectangle divided by its length, which is the frequency density of the third class, **0.059** Therefore, since **0.18/0.059=3.05 The (approximate) median is 20+3.05=23.05** 

**17** 

## **Mean (arithmetic)** 

The **mean (arithmetic)** is by far the most known and the most widely used central tendency measure. It is defined as the sum of all data on a variable divided by the total number of cases: 

**----- Start of picture text -----**<br>
𝒏<br>𝒙<br>𝒊<br>ഥ𝒙= ෍ 𝒏<br>𝒊=𝟏<br>**----- End of picture text -----**<br>

**It is important to highlight that the mean can only be calculated for numerical variables, whose values can be summed.** 

## **About notation:** 

- ഥ𝒙 denotes the **arithmetic mean computed for a** _**sample (statistic)**_ while the **arithmetic .** 

- **mean computed for an** _**entire population (parameter)**_ is denoted by  

**18** 

## **Mean: Properties [OPTIONAL]** 

 _**n**_ **= 9 customers: 35 25 54 60 44 61 27 55 62 Age in years recorded from a sample of** 

_The mean is:_ 

To understand the concept of “centre” underlying the arithmetic mean, consider the : **deviations of the (ordered) data from their mean, 47** 

**(25-47) (27-47) (35-47) (44-47) (54-47) (55-47) (60-47) (61-47) (62-47) - -22 -20 -12 3 7 8 13 14 15 -57 57** 

The sum of the negative deviations from the mean coincides with the sum of the positive deviations, resulting in a total deviation sum of zero (the sum of all deviations is **zero!).** 

**19** 

## **Mean: Properties [OPTIONAL]** 

## Actually, it is: 

**----- Start of picture text -----**<br>
𝒏 𝒏 𝒏<br>𝒙 ഥ𝒙<br>(𝒙𝒊 𝒊<br>෍ −ഥ𝒙) = ෍ −෍<br>𝒊=𝟏 𝒊=𝟏 𝒊=𝟏<br>𝒏 𝒏 𝒏<br>𝒙𝒊 −𝒏ഥ𝒙 𝒙𝒊 𝒙𝒊 = 𝟎<br>= ෍ = ෍ −෍<br>𝒊=𝟏 𝒊=𝟏 𝒊=𝟏<br>**----- End of picture text -----**<br>

The mean can be regarded as the **centre of gravity of the observed data** , since it balances out the sum of positive and negative deviations from itself. 

As we will discuss in more detail later, this property of the mean makes it particularly sensitive to extreme values (non-robustness of the mean). 

**20** 

## **Mean: Discrete variables (simple and weighted mean)** 

 **Number of credit card transactions in a store from a surveyed sample of n = 16 customers 4 3 3 1 0 1 2 3 3 4 2 5 4 3 4 5** _The mean is_ **2.9775** : the sum of the observed values is **47** and the mean is **47/16 = 2.9775** Let us consider the frequency distribution of the variable: 

||||||||
|---|---|---|---|---|---|---|
||||||||
||**Nr_purchases**<br>**0**<br>~~x~~ =|**_fk_**<br>**1**|**_pk_**<br>**0.0625**||𝑥𝑘<br>∗∙𝑝𝑘<br>**0**|**Is it possible to calculate the mean from the frequency tabl**|
||**1**<br>**2**<br>**3**<br>~~*~~<br>X2 =<br>X,-<br>~~X~~<br>=|**2**<br>**2**<br>**5**|**0.125**<br>**0.125**<br>**0.3125**||**0.125**<br>**0.25**<br>**0.9375**|_The sum of the_**_observed data_**_is the_**_sum of_**_the_**_products_**_betwe_<br>_the distinct_**_values_**_and their_**_absolute frequency._**_The_**_mean is_**|
||**4**<br>**<br>=|**4**|**0.25**||**1**|_obtained by_**_dividing_**_this sum by the_**_number of cases._**|
||**5**<br>**Total**<br>~~X~~<br>=|**2**<br>**16**|**0.125**<br>**1.000**||**0.625**<br>**2.9975**|**_Alternatively,_**_the_**_mean_**_can be calculated_**_as the sum of_**_the_|
|||||||**_products_**_between the_**_distinct values_**_and their_**_relative frequen_**<br>6|
|*|- X fr<br>c=1np<br>-||0.||1 + 1|.2 + 2 .2 + 3 .5 + +<br>. 4<br>+ 5 .2<br>:<br>2 .9775 : [XPA<br>16<br>k = 1|

**Is it possible to calculate the mean from the frequency table?** 

_The sum of the_ _**observed data** is the_ _**sum of** the_ _**products** between the distinct_ _**values** and their_ _**absolute frequency.** The_ _**mean is** obtained by_ _**dividing** this sum by the_ _**number of cases.** the_ _**mean** can be calculated the_ _**Alternatively, as the sum of products** between the_ _**distinct values** and their_ _**relative frequency.**_ 

**21** 

## **Mean: Discrete variables (simple and weighted mean)** 

For discrete variables, the mean can be **precisely** calculated based on grouped data (frequency table) based on the observed distinct values and their relative or absolute frequencies. 

𝒏 𝑲 𝑲 𝑲 ∗ 𝒙 𝒙 𝒊 𝒌𝒇𝒌 ∗ 𝒇𝒌 ∗[෍] = 𝒙[෍] 𝒙 Formula for a sample 𝒌 𝒌𝒑𝒌 ഥ𝒙= ෍ 𝒏[=] 𝒏 ෍ 𝒏[=] 𝒊=𝟏 𝒌=𝟏 𝒌=𝟏 𝒌=𝟏 However, when a variable is measured in classes and only the frequency table of the classified variable is available the mean cannot be calculated precisely, because the original **raw numeric data are not available** . In this situation, the mean can only **be approximated,** under the **assumption** that the frequency associated with each interval is **uniformly distributed** over the interval. 

**22** 

## **Mean: Variables measured in interval classes** 

Example: variable **Income** (in dataframe 

**Loyalty** ), collected in interval classes 

|**Income**|**_fk_**|**_pk_**<br>**_k_**|**_wk_**<br>**_k_**|**_ck_**<br>**_k_**|**_mk_**<br>**_k_**|**_mk·pk_**|
|---|---|---|---|---|---|---|
|**[5,15)**|**14 **|**0.112 **|**10 **|**0.011**|**10**|**1.12**|
|**[15,20)**|**26 **|**0.208**|**5**|**0.042**|**17.5**|**3.64**|
|**[20,25)**|**37 **|**0.296**|**5**|**0.059**|**22.5**|**6.66**|
|**[25,35)**|**24 **|**0.192 **|**10 **|**0.019**|**30**|**5.76**|
|**[35,60)**|**17 **|**0.136 **|**25 **|**0.005**|**47.5**|**6.46**|
|**[60,80)**|**7**|**0.056 **|**20 **|**0.003**|**70**|**3.92**|
|**Total**|**125 **|**1.00**||||**27.56**|

**How to approximate the mean? Discretize data using the classes’ midpoints.** 

Consider a discrete variable whose values are **the intervals’ midpoints,** and associate to each midpoint the frequency of its class. 

**The approximate mean can be obtained as described for discrete variables,** thus by summing up the products between the midpoints and their class’ relative frequency. 

**23** 

## **Mean and median: Robustness** 

_Since the_ _**median** is the value in the middle position in the ordered sequence of data it is not – affected by_ _**extreme values and outliers** ; the opposite holds for the mean, that being the – centre of gravity of data is very sensitive to extreme values._ 

 Amount spent on a pharmacy’s website related to 9 transactions on a specific day **Ordered data Median Mean 55.5 60.4 62.3 66.7 72.8 74.6 81.1 90.5 91.3 72.8 = 72.8** 

Assume that the same exact data were observed on other days, except for the maximum or the minimum transactions amount: 

**Ordered data** 

**55.5 60.4 62.3 66.7 72.8 74.6 81.1 90.5 111.1 55.5 60.4 62.3 66.7 72.8 74.6 81.1 90.5 148 25.8 60.4 62.3 66.7 72.8 74.6 81.1 90.5 91.3 7.8 60.4 62.3 66.7 72.8 74.6 81.1 90.5 91.3** 

**Median Mean 72.8 < 75.0 72.8 < 79.1 72.8 > 69.5 72.8 > 67.5** 

**24** 

## **Mean and median: Shape of distribution** 

Differences between the mean and median suggest the presence of extreme values, and can inform about the **shape of the distribution** 

|**Symmetry**|**Right Skewed**|**Left Skewed**|
|---|---|---|
|**Symmetry**|**Right Skewed**|**Left Skewed**|

**What is the relation between the mean and median?** 

If the distribution is **symmetric** , the two measures have similar values. When the distribution is **skewed** , the mean deviates from the median, being attracted by values on the distribution’s tail. Specifically, the mean increases (resp. decreases) when the distribution is skewed to the right (resp. left). 

The difference between the measures is higher the more severe are the outliers, that is the longer is the tail of the distribution. 

**25** 

## **Rstudio: Basic functions [OPTIONAL]** 

The **mean()** and **median()** functions can be used to calculate the mean and the median of a numeric data vector; they require the handling of any missing values (if any). Note that the function **median()** does not support the calculation of the median for factors. An alternative function is available, but only for factor explicitly defined as ordinal. 

**mean(Loyalty$Age) mean(Loyalty$Age, na.rm=T) median(Loyalty$Age, na.rm=T) median(Loyalty$Recommend.F)** 

- **mean(Loyalty$Age) [1] NA > mean(Loyalty$Age, na.rm=T) [1] 50.75 > median(Loyalty$Age, na.rm=T) [1] 51.5 > median(Loyalty$Recommend.F) Error in median.default(Loyalty$Recommend.F) : need numeric data** 

**26** 

## **Rstudio: distr.summary.x() - central tendency measures** 

The function **distr.summary.x()** allows computing the most relevant summary measures, including the mode (for which there is no specific function in R) and the median for factors, even when they are not explicitly ordered. It disregards missing values in calculations. The syntax closely resembles that of functions **distr.table.x()** and **distr.plot.x()** : 

**distr.summary.x(x, stats, digits=2,f.digits=4, data)** 

The argument **stats** specifies the required summary measures; when **stats="central"** the function returns all the central tendency measures (mode, median, mean). It is also possible to limit attention to specific measures; in particular, **stats="central"** corresponds to **stats=c("mode", "median", "mean").** 

The **digits** and **f.digits** arguments allow specifying the number of decimals used for rounding respectively the statistics and any frequencies displayed in the output. 

**27** 

## **Hands on: Central tendency measures** 

**> distr.summary.x(x=Payment,stats="central", data=Loyalty) Warning: Some of the required 'stats' cannot be calculated when 'x' is character Summary measures for Payment Central tendency measures n n.a        mode n.modes mode% 125   0 Credit Card       1 0.408** 

**> distr.summary.x(x=Recommend.F,stats="central", data=Loyalty) Warning: Some of the required 'stats' cannot be calculated when 'x' is factor The required 'stats' will be calculated using the actual order of 'x' levels -> Very Unlikely < Unlikely < Neutral < Likely < Very Likely Summary measures for Recommend.F Central tendency measures n n.a   mode n.modes mode%  median 125   0 Likely       1 0.272 Neutral > distr.summary.x(x=Age,stats="central", data=Loyalty) Summary measures for Age Central tendency measures n n.a mode n.modes  mode% median  mean 124   1   46       1 0.0484   51.5 50.75** 

**28** 

**Applications / 1 [READING]** 

## **Data on the number of children per household in Italy (EUROSTAT)** 

|**ata on the number of children per**|**ata on the number of children per**|**ata on the number of children per**|
|---|---|---|
|**2006**|||
|**Nr.children**|**Count**|**Percent**|
|**0**|**16,936,800**|**0.723**|
|**1**|**3,560,500**|**0.152**|
|**2**|**2,486,200**|**0.106**|
|**3+**|**455,300**|**0.019**|
|**Total households**|**23,438,800**|**1.000**|

## **Comments?** 

2006: The distribution is **concentrated on 0** (both the mode and the median are 0). The mean (from other data sources) is 0.44, reflecting the presence of households with one or more children, even if their relevance is relatively low in the distribution. 

**29** 

## **Applications / 1 [READING]** 

## **Data on the number of children per households in Italy (EUROSTAT)** 

|**Nr.children**<br>**Count**<br>**Percent**<br>**0**<br>**16936.8**<br>**0.723**<br>**1**<br>**3560.5**<br>**0.152**<br>**2**<br>**2486.2**<br>**0.106**<br>**3+**<br>**455.3**<br>**0.019**<br>**Total households 23438.8**<br>**1.000**<br>**2006**|**Nr.children**<br>**Count**<br>**Percent**<br>**0**<br>**16936.8**<br>**0.723**<br>**1**<br>**3560.5**<br>**0.152**<br>**2**<br>**2486.2**<br>**0.106**<br>**3+**<br>**455.3**<br>**0.019**<br>**Total households 23438.8**<br>**1.000**<br>**2006**|**Nr.children**<br>**Count**<br>**Percent**<br>**0**<br>**16936.8**<br>**0.723**<br>**1**<br>**3560.5**<br>**0.152**<br>**2**<br>**2486.2**<br>**0.106**<br>**3+**<br>**455.3**<br>**0.019**<br>**Total households 23438.8**<br>**1.000**<br>**2006**|**Nr.children**<br>**Count**<br>**Percent**<br>**0**<br>**16936.8**<br>**0.723**<br>**1**<br>**3560.5**<br>**0.152**<br>**2**<br>**2486.2**<br>**0.106**<br>**3+**<br>**455.3**<br>**0.019**<br>**Total households 23438.8**<br>**1.000**<br>**2006**|**2011**|**2011**|**2011**|**2016**|**2016**|**2016**|**2021**|**2021**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Nr.children**|**Count**|**Percent**||**Count**|**Percent**||**Count**|**Percent**||**Count**|**Percent**|
|**0**|**16936.8**|**0.723**||**18320.7**|**0.735**||**19294.3**|**0.748**||**19762.5**|**0.766**|
|**1**|**3560.5**|**0.152**||**36002**|**0144**||**35492**|**0138**||**3303.1**|**0.128**|
|||||**.**|**.**||**.**|**.**||||
|**2**|**2486.2**|**0.106**||||||||**2281.3**|**0.088**|
|||||**2531.2**|**0.102**||**2488.8**|**0.096**||||
|**3+**|**455.3**|**0.019**||**469.7**|**0.019**||**464.9**|**0.018**||**441**|**0.017**|
|**Total households **|**23438.8**|**1.000**||**24921.8**|**1.000**||**25797.2**|**1.000**||**25787.9**|**1.000**|

An interesting question concerns how the distribution changes over time. 

In 2021, the median and mode do not change, although the relative significance of the mode increases. The average value (the mean) decreases from 0.44 in 2006 to 0.372 in 2021. The mean is a more sensitive measure than the median, and in this context, it is more suitable for highlighting variations in the data and their evolution over time. 

Alternatively, one could monitor the relative importance of the mode, which, however, implies a focus on households without children and does not react to changes in the number of children in households with children. 

**30** 

**Applications / 1 [READING]** 

## **Data on number of children per household in Italy (EUROSTAT)** 

|**Nr.children**<br>**Count**<br>**Percent**<br>**0**<br>**16936.8**<br>**0.723**<br>**1**<br>**3560.5**<br>**0.152**<br>**2**<br>**2486.2**<br>**0.106**<br>**3+**<br>**455.3**<br>**0.019**<br>**Total households 23438.8**<br>**1.000**<br>**2006**|**Nr.children**<br>**Count**<br>**Percent**<br>**0**<br>**16936.8**<br>**0.723**<br>**1**<br>**3560.5**<br>**0.152**<br>**2**<br>**2486.2**<br>**0.106**<br>**3+**<br>**455.3**<br>**0.019**<br>**Total households 23438.8**<br>**1.000**<br>**2006**|**Nr.children**<br>**Count**<br>**Percent**<br>**0**<br>**16936.8**<br>**0.723**<br>**1**<br>**3560.5**<br>**0.152**<br>**2**<br>**2486.2**<br>**0.106**<br>**3+**<br>**455.3**<br>**0.019**<br>**Total households 23438.8**<br>**1.000**<br>**2006**|**Nr.children**<br>**Count**<br>**Percent**<br>**0**<br>**16936.8**<br>**0.723**<br>**1**<br>**3560.5**<br>**0.152**<br>**2**<br>**2486.2**<br>**0.106**<br>**3+**<br>**455.3**<br>**0.019**<br>**Total households 23438.8**<br>**1.000**<br>**2006**|**2011**|**2011**|**2011**|**2016**|**2016**|**2016**|**2021**|**2021**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Nr.children**|**Count**|**Percent**||**Count**|**Percent**||**Count**|**Percent**||**Count**|**Percent**|
|**0**|**16936.8**|**0.723**||**18320.7**|**0.735**||**19294.3**|**0.748**||**19762.5**|**0.766**|
|**1**|**3560.5**|**0.152**||**36002**|**0144**||**35492**|**0138**||**3303.1**|**0.128**|
|||||**.**|**.**||**.**|**.**||||
|**2**|**2486.2**|**0.106**||||||||**2281.3**|**0.088**|
|||||**2531.2**|**0.102**||**2488.8**|**0.096**||||
|**3+**|**455.3**|**0.019**||**469.7**|**0.019**||**464.9**|**0.018**||**441**|**0.017**|
|**Total households **|**23438.8**|**1.000**||**24921.8**|**1.000**||**25797.2**|**1.000**||**25787.9**|**1.000**|

**Analysis of changes over time? Comparison with other countries?** 

One possibility ( **anticipating tools used to jointly study two variables)** would be to compare countries over time using sets of bar charts to display the frequency tables, but still the comparison between countries by year could be difficult. 

Simplified approach: **monitor how summary measures** for different countries change over time. Monitoring modes or medians is useless: they are constantly 0, also for other countries. One alternative approach is **to compare the relative frequency of 0** (that increases from 0.723 . in 2006 to 0.766 in 2021 in Italy)  or **to compare means** 

**31** 

## **Applications / 1 [READING]** 

## **Number of children per household in different European countries (EUROSTAT) Monitoring countries: Average number of children per household across time for a selected group of countries.** 

We observe a decrease in the average number of children per household across all countries, except for France (with a flat trend, decreasing only in the last period). Ireland is the country with the highest average number of children per household, despite the decrease since 2015 Italy and the Mediterranean countries have the lowest average number of children per household. 

**32** 

## **Applications / 2 [READING]** 

**Income of US citizens (US data, www.census.gov)** Histograms of income distribution in 2012 and 2020 (max. 500K) 

## **Comments?** 

The distribution of income (current $) in 2012 is strongly skewed to the right. 

From 2012 to 2020 the asymmetry decreases, the distribution is more dispersed, and higher incomes are observed with higher frequency (also due to the increased income at current $ and to inflation) 

## **What comments about central tendency measures?** 

It is quite evident the modal class has shifted towards higher values. Both the mean and the median will be higher in 2012, with a relatively higher variation for the mean, which is more responsive to the higher frequency in the upper intervals. 

**How would you assess whether the increase in income was “homogeneous” across different communities/ethnicities (as defined by census.gov)?** 

**33** 

## **Applications / 2 [READING]** 

**Income of US citizens (US data, www.census.gov) How to assess whether the increase in income was “homogeneous” across different communities (as defined by census.gov)?** 

Comparing the histograms for different communities (as defined by census.gov), we observe a common trend, with a shift of the distribution towards higher income levels and a lower concentration in the lowincome classes. However, there are differences among  communities, particularly with respect to the relevance of high-income classes. **The comparison becomes more difficult when we want to analyse the changes over more years (ethnicity effect on income growth)!** 

**34** 

## **Applications / 2 [READING]** 

## **Income of US citizens (US data, www.census.gov) How to assess whether the increase in income was 'homogeneous' across different ethnic groups?** 

To simplify comparison, we consider the time-series plot of the average income values for each community. 

The mean is certainly influenced by extreme values in the distributions; therefore it is crucial to include in the plots also the median values, providing a more robust description of the “centre” of the distribution. 

We observe consistent differences among communities and a growing gap between the mean and median in the case of WHITE and ASIAN communities. The overall shift towards higher incomes in USA is due to improvement across all groups, but it is certainly driven and dominated by the significant income growth in these two distinct segments of the population. **In this case, besides the «centre» distribution, it would be crucial to account also for the 'tails' of the distribution in the chart!** 

**35** 

# **Location measures Non-central tendency measures** 

## **Introduction** 

For qualitative variables, as well as for discrete numeric variables taking few values, the – – central tendency measures describing the “centre” of the distribution provide a concise but effective description of the most salient features of the variables’ distributions. 

For continuous numerical variables (or discrete variables taking many values) having a symmetric and short-tailed distribution, the mean, possibly combined with the median, still provide a fairly accurate description of the distribution. 

**However, if a distribution is strongly skewed and/or has long tails,** limiting attention to c ~~entral tendency measures might lead to loss of informatio~~ n and to a partial or inaccurate description of the distribution’s characteristics. In this case, it is therefore important to provide s ~~ummaries describing the behaviour of the distribution~~ ~~**around or**~~ **far from its centre.** 

**37** 

## **Quartiles: definition** 

Quartiles divide the ordered sequence of data into 4 blocks with (possibly) the same number of cases 

**----- Start of picture text -----**<br>
25% 25% 25% 25%<br>**----- End of picture text -----**<br>

Q1 Q2 Q3  The first quartile, Q1 (or P25) separates the **smallest** 25% of the data from the remaining 75%. It divides the data into two blocks (sized 25% and 75% respectively), one of values lower and one of values greater than Q1 

 The second quartile, Q2 (or P50) coincides with the median 

- The third quartile, Q3 (or P75) separates the **highest** 25% of data from the remaining 75%. It divides the data into two blocks (sized 75% and 25% respectively), one of values lower and one of values greater than Q3 

**38** 

## **Quartiles: calculation** 

_**n**_ **Example: Amount spent on a site by** = 13 customers (sorted data): **18.1  31.0 45.4 57.95  60.4  62.3  66.7  72.8  74.6  82.85 95.1 111.5 148.0** 

## **Median?** 

- Q2 , is **66.7** , the value in the 7[th] position in the ordered sequence of data, and divides the data into two blocks of equal width (6) 

## **First quartile?** 

- Q1 is the value in the 4[th] position in the ordered sequence of data, **57.95** : it separates the **3** smallest values from the **9** highest values. Note that 31% (>25%) of data are lower than or equal to 57.95 and 77% (>75%) of data are higher than or equal to 57.95 

- **Third quartile?** 

- Q3 is the value in the 10[th] position in the ordered sequence of data, **82.85** : it separates the **3** highest values from the **9** smallest values. Note that the 77% of data are lower than or equal to 82.85 and the 31% of data are higher than or equal to 82.85 

**39** 

## **Quartiles: calculation** 

Clearly, in some cases it is not possible to find values that divide the distribution exactly as described in the previous example, and quartiles may lie between two values. As already seen for the median, in these cases it is necessary to approximate the position of the quartiles or their value. 

**There are several ways to approximate quartiles in these cases, which may vary depending on the software used.** 

 In general, in the case of discrete or ordinal variables (i.e. with few distinct values), as well as in the case of manual calculation, **we** will identify the three quartiles as the values at which the cumulative frequency equals or exceeds 0.25, 0.5 and 0.75 for the first time, respectively 

 In the case of numerical values, this approach returns quartiles possibly different from those obtained using R, which approximates the quartile values through appropriate interpolation. 

**40** 

## **Rstudio: distr.summary.x() - quartiles** 

The function **distr.summary.x()** makes it easy to determine quartiles, both for numeric and factor variables, neglecting - as already mentioned - missing values. The syntax for obtaining quartiles is identical to that illustrated for obtaining measures of central tendency: 

**distr.summary.x(x, stats="quartiles", digits=2,f.digits=4, data)** 

**41** 

## **Quartiles: Continuous numeric variables** 

## Average amount per visit ( **Amount_V** , in dataframe **Loyalty** ) 

**> distr.summary.x(x=Amount_V,stats=c("central","quartiles", data=Loyalty) Summary measures for Amount_V** 

**Central tendency measures** 

**n n.a  mode n.modes mode% median  mean 125   0 77.25       5 0.016   87.3 87.86 Quartiles** 

**n n.a   min   p25  p50   p75   max 125   0 38.85 71.25 87.3 100.4 154.6** 

Q1 and Q3 are **non-central** tendency measures, and can be used to describe the behaviour of data **around the centre.** _Measures of central tendency accurately describe the centre of the data; Quartiles provide information on the concentration of data “around” the centre._ 

**42** 

## **Quartiles: Variables measured in interval classes** 

Example: variable **Income** (in dataframe **Loyalty** ), measured in classes 

|[15|,20)|**Income**<br>**_fk_**<br>**_pk_**<br>**_wk_**<br>**_ck_**<br>**[5,15)**<br>**14**<br>**0.112**<br>**10 0.011 **<br>**[15,20)**<br>**26**<br>**0.208**<br>**5**<br>**0.042**|**_Fk_**<br> **0.112**<br>**0.32**||STEP #<br>find<br>the base <br>0 .138<br>rea<br>rectangle<br>A|of|
|---|---|---|---|---|---|---|
|||**First and third quartile?**<br>**[20,25)**<br>**37**<br>**0.296**<br>**5**<br>**0.059 **<br>**[25,35)**<br>**24**<br>**0.192**<br>**10 0.019 **<br>**[35,60)**<br>**17**<br>**0.136**<br>**25 0.005 **<br>**[60,80)**<br>**7**<br>**0.056**<br>**20 0.003**<br>**Total**<br>**125**<br>**1.00**|**0.616**<br> **0.808**<br> **0.944**<br>**1**|0.117F<br>Ill|base :<br>0 .75. 0 .112<br>= 3<br>0 .042|.28|

They can only be approximated by considering cumulated frequencies! 

 Q1 lies between 15 and 20, and is such that **(Q1 - 15) 0.042 = (0.25 -0.112) = 0.138** → Q1 = 15 + (0.138/0.042) = **15+3.28=18.8** 

 Q3 lies between 25 and 35, and is such that **(Q3 - 25) 0.019 =(0.75 - 0.616)=0.134** → Q3 = 25 + (0.134/0.019) = **25+7.05 = 32.05** 

**43** 

## **Quartiles: Variables measured in interval classes** 

Example: variable **Income** (in dataframe **Loyalty** ), measured in classes 

|PRO<br>is in<br>[20,25)|**Income**<br>**[5,15)**<br>**[15,20)**<br>**[20,25)**<br>**[25,35)**<br>**[35,60)**<br>**[60,80)**<br>**Total**|**_fk_**<br>**14**<br>**26**<br>**37**<br>**24**<br>**17**<br>**7**<br>**125**|**_pk_**<br>**0.112**<br>**0.208**<br>**0.296**<br>**0.192**<br>**0.136**<br>**0.056**<br>**1.00**|**_wk_**<br>**10 **<br>**5**<br>**5**<br>**10 **<br>**25 **<br>**20 **|**_ck_**<br> **0.011 **<br>**0.042**<br>**0.059 **<br> **0.019 **<br> **0.005 **<br> **0.003**|**_Fk_**<br> **0.112**<br>**0.32**<br> **0.616**<br> **0.808**<br> **0.944**<br>**1**|ini|base :|0 .k - 0 .32<br>0 .059|: 113T|
|---|---|---|---|---|---|---|---|---|---|---|

## **First and third quartile?** 

They can only be approximated by considering cumulated frequencies! 

 Q1 lies between 15 and 20, and is such that **(Q1 - 15) 0.042 = (0.25 -0.112) = 0.138** → Q1 = 15 + (0.138/0.042) = **15+3.28=18.8**  Q3 lies between 25 and 35, and is such that **(Q3 - 25) 0.019 =(0.75 - 0.616)=0.134** → Q3 = 25 + (0.134/0.019) = **25+7.05 = 32.05** 

**43** 

**Percentiles: motivation** 

## Customer **Profitability** (in dataframe **Loyalty** ) 

_Central tendency measures and quartiles describe the centre of the data and its neighbourhood. However, providing only this information is not sufficient because it does not account in any way for the strong skewness of the distribution._ 

_The profitability of  the 'top clients' is very far from the centre of data! If one wants to effectively summarise the most salient features of the distribution, it is necessary to enrich the set of summary measures, offering also information on the tail!!!_ 

**44** 

## **Percentiles: definition** 

**Percentiles** divide the data into 100 groups with (possibly) the same number of cases Specifically, we denote by P the _q-th_ percentile, which separates the _q_ % of the _q_ smallest data from the remaining (100- _q_ )% 

_The plot shows the percentiles of order 90%, 95%, and 99%, which describe and make evident that the distribution has a long right tail!_ 

_Only 1% of clients have a profitability higher than 775.5! Such high profitability identifies top clients!!! Note: percentiles are calculated on raw data and_ _**do not depend on** the classification chosen by the analyst_ 

NB: the notation used in the textbook is slightly different 

**45** 

## **Rstudio: distr.summary.x() - quantiles and percentiles** 

The function **distr.summary.x()** allows determining different types of **quantiles** : quartiles, quintiles, deciles and percentiles, by specifying the statistics of interest via the **stats** argument **.** It is possible to request all quantiles of a certain order, or to select specific percentiles or quartiles: **distr.summary.x(x, stats="quartiles", data) distr.summary.x(x, stats="quintiles", data) distr.summary.x(x, stats="deciles", data) distr.summary.x(x, stats="percentiles", data) distr.summary.x(x, stats=c("p1","p5","p10","p90","p95","p99"), data)** 

**> distr.summary.x(x=Profitability,stats=c("q1","q2","mean","q3", "p90","p95","p99"), data=Loyalty) Summary measures for Profitability Requested statistics n n.a    q1    q2   mean    q3    p90    p95    p99 125   0 139.1 178.8 233.64 280.4 434.84 563.86 775.51** 

**46** 

## **Applications / 3 [READING]** 

**UK income data (disposable household income, Office for National Statistics) Focus: analysis of income over time, in order to assess if the asymmetry is worsening** 

Studying the evolution of histograms over time for many years makes the comparison of distributions difficult. It is therefore reasonable to study the temporal evolution of appropriately chosen summary measures. 

Instead of limiting attention to measures of central tendency alone, we monitor the **deciles** that divide the population into 10 equal-sized brackets, so as to describe also the **tails of** the (typically asymmetrical) income distribution 

The plot shows an increasing trend (except for falls during critical years - great recession) 

However, the incomes of the poorest classes of the population have a much lower rate of increase, and over time the differences between the highest and lowest income classes become more acute 

**47** 

## **Position measures** 

## **The box-plot** 

## **The box plot** 

The so-called **box plot** (or box-and-whiskers plot) provides a univocal, effective and schematic representation of the distribution of a **numerical** variable, without resorting to a histogram (whose descriptive efficacy may also depend on the choice of interval classes). In its **simplest** version, the box plot is based on the so-called **five summary numbers:** the minimum observed value in the data, the three quartiles and the maximum observed value. As suggested by its name, the plot is based on a box and two whiskers. 

 The **box** extends from the first to the third quartile, and is divided by the median Thus, the box includes 50% of data, with central positions in the ordered sequence of data  The **whiskers** connect the box to the lowest and highest observed value respectively 

**25%                               25%               25%                         25% Min                                                                                           MaxQ1 Q2 Q3** 

**49** 

## **The box plot** 

## Average amount per visit ( **Amount_V** in dataframe **Loyalty** ) 

_The box plot summarises the salient features of the distribution: it describes its centre and the local and global dispersion around it. It also shows a certain symmetry of distribution. The median divides the box almost in half. The whiskers are of similar length, and are not particularly extended. Being based on summary measures (quartiles, minimum and maximum values),_ _**the box plot does not change as the specific interval classes used to build the histogram vary.**_ 

**min                     Q1 Q2     Q3                                     max** 

_**Clearly, in the case when a variable has been measured in classes, the quartiles will be derived on the basis of the histogram**_ 

**50** 

**The box plot** 

## Customer **Profitability** (in dataframe **Loyalty** ) 

_The box plot clearly informs about the presence of a long tail and the right-skewness of the distribution._ 

_Note the disproportion between the left and right whiskers and between the first and second half of the box. This indicates a concentration of the 50% of the smaller data in a very small range compared to the range including the 50% of the higher values._ 

_However,_ _**it is not possible to assess** how_ _**'dense'** the right tail is, i.e. how dispersed the data are on the whisker connecting_ Q3 _to the maximum._ 

**51** 

## **The box plot: information on extreme values** 

Some statistical software provide a more detailed version of the box plot, which also allows to identify and visualize extreme values. 

In the plot 

- The box is built as before 

- Whiskers are built differently: 

   - Values that are very “far” from the centre of data are identified as **extremes** ; typically Values deviating from the box more **than 1.5 times the length of the box** (Q3 -Q1 , also called the interquartile range) are flagged as **outliers** and are **identified** by a specific symbol in the plot. 

   - Whiskers connect the box at **minimum and maximum regular value,** that is values that do not deviate from the box more than 1.5 times **the length of the box** 

**52** 

## **The box plot: information on extreme values (outliers)** 

Example. 11 cases: Example. 11 cases: **18.10  31.00  57.95  60.40  62.30  66.70  72.80  74.60  82.85 111.50 148.0018.10  31.00  57.95  60.40  62.30  66.70  72.80  74.60  82.85 111.50 148.00 Five numbers summary? Five numbers summary: Min=18.1; Q1 = 57.95; Q2 = 66.7; Q3 = 82.85; Max=148 “Basic” Box plot?** 

**----- Start of picture text -----**<br>
18.1 57.95 66.7       82.85 148<br>**----- End of picture text -----**<br>

**Box plot «without outliers»** 

**53** 

## **The box plot: information on extreme values (outliers)** 

Example. 11 cases: **18.10 31.00 57.95 60.40 62.30 66.70 72.80 74.60 82.85 111.50 148.00 Five numbers summary: Min=18.1; Q1 = 57.95; Q2 = 66.7; Q3 = 82.85; Max=148 Box plot “with outliers”?** 

- The **box** remains **unchanged** 

- –   

- To find extreme values, consider (Q3 Q1)=(82.82-57.95)= **24.9** and (Q3 Q1) 1.5=24.9 1.5= **37.35** . Regular values lie between (Q1 -37.5)= **20.6** and (Q3 +37.5)= **120.2** . 

- The **min** and **max** regular values, **31** and **111.50** , are connected to the box by whiskers) 

- The extreme values, 18.10 and 148, are identified in the plot by appropriate symbols 

**----- Start of picture text -----**<br>
18.1 57.95 66.7       82.85 148<br>**----- End of picture text -----**<br>

**Box plot «without outliers» 148 Box plot «with outliers» 148** 

**----- Start of picture text -----**<br>
18.1 31 57.95 66.7       82.85 111.5<br>**----- End of picture text -----**<br>

**54** 

## **Rstudio: distr.plot.x() - boxplot** 

The **distr.plot.x()** function allows to represent the distribution of a **numeric** variable using a boxplot, by specifying the plot type in **plot.type** 

**distr.plot.x(x, plot.type="boxplot", data)** 

Note that the boxplot can only be obtained for **raw data** on a numeric variable **; it is therefore not possible to obtain the boxplot for variables measured in classes.** 

**55** 

## **Hands on: boxplot** 

## Customer **Profitability** (in dataframe **Loyalty** ) 

**distr.plot.x(x=Profitability,plot.type="boxplot", data=Loyalty)** 

_The box plot with identified outliers allows evaluating the density of the data on the right tail. Note that the strong skewness of the variable is due to a relatively small number of cases, and that most customers have a profitability lower than 500._ 

_Also the histogram allowed identifying some classes with very low densities, but it did not inform about_ _**the dispersion of** ._ _**extreme values lie within the high-profitability intervals As we shall see later, the boxplot is the most effective graphical tool for comparing distributions**_ 

**56** 

