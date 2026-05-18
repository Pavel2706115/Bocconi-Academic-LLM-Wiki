---
course: "Statistics"
course_code: "30001"
tags:
  - "source"
  - course_30001
Title: "Joint analysis of two variables Qualitative variables (or discrete taking few distinct values)"
Reference: "Course Material"
Created: 2026-05-18
Processed: true
  - "source"
---

**TABLES, GRAPHS AND SUMMARY MEASURES IN THE ANALYSIS OF TWO VARIABLES**

## The study of two variables

**(READING)**

In many applications, one is interested to study two variables and their relationship:

- Is there a relationship between consumers’ attention/interest in healthy eating and their age?

- Are there differences in the response times to complaint tweets from companies incorporating social media into their marketing strategy?

- Is there a relationship between performance in the Bachelor’s degree and performance in the Master’s degree? Is it possible to use the possible relationship to select candidates?

# Joint analysis of two variables Qualitative variables (or discrete taking few distinct values)

## Qualitative variables: cross tabulation

## Cross-tab (absolute frequencies)

## Distinct values taken by 𝒀

Each cell reports the frequency (in this case, the absolute frequency) characterising each pair of values

For the sake of simplicity, we will always denote by 𝒀 the variable on the columns and by 𝑿 the variable on the rows of the table

## Qualitative variables: bar charts

## Example: Age and interest in healthy eating (sample of 1224 individuals)

|**_Interest_504**|**Side-by-side bar diagrams**|
|---|---|---|---|
|31-45 97 168 68|**333**|
|46-60 65 214 108|**387**|
|**Tot225**|**1224**|
|e two diagrams show the**same bars,**|
|**ouped byAge**or by**Interest**in|
|althy eating|
|ey allow to easily identify the most|
|levant combinations of categories|
|d to appreciate their relevance in|
|lative terms (the**appearance**of the|
|aphs**does not change**when|
|idi lti fi|

The two diagrams show the **same bars, grouped by Age** or by **Interest** in healthy eating They allow to easily identify the most relevant combinations of categories and to appreciate their relevance in relative terms (the **appearance** of the graphs **does not change** when considering relative frequencies)

## Qualitative variables: bar charts

## Example: Age and interest in healthy eating (sample of 1224 individuals)

|**_Interest_** **_Age_**|Low|Medium|High|**Tot**|
|---|---|---|---|---|
|18-30|183|272|49|**504**|
|31-45|97|168|68|**333**|
|46-60|65|214|108|**387**|
|**Tot**|**345**|**654**|**225**|**1224**|

The two diagrams show the **same bars, stacked** by **Age** or by **Interest** in healthy eating Information is the same provided by side-by-side bars, with more emphasis on the marginal frequencies of the variable on the x-axis (the appearance of the graphs **does not change** when considering relative frequencies)

## Stacked bar diagrams

## Qualitative variables: conditional distributions

Example: Age and interest in healthy eating (sample of 1224 individuals)

Note that among those who are most interested, seniors prevail, whilst among respondents with low/ medium interest, youngsters prevail

**Column conditional frequency**: frequency of each category of the row variable 𝑿, in the **subset of** cases characterised by one of the categories of 𝒀. E.g. The frequency of **Age** = _46-60_ **conditioned on** the category **Interest =** _High_ is: �� Freq {𝐀𝐠𝐞 = _46-60_ | 𝐈𝐧𝐭𝐞𝐫𝐞𝐬𝐭 = _High_ } = ���(= 0.480)

## Qualitative variables: conditional distributions

are In order to represent conditional distributions, **side-by-side or stacked bar charts** usually used, displaying conditional rather than joint frequencies.

**Age distribution | Interest**

## Distribution of Interest | Age

**Stacked bar diagrams** Note that the height of the bars in the stacked bars diagram is 1, since each bar represents a frequency distribution (sum of frequencies conditional on each category = 1) ^wxkydi

## Rstudio: distr.table.xy()

The function **distr.table.xy()** allows to tabulate joint or conditional distributions. The syntax is similar to that of **distr.table.x()** . In the simple case of two variables taking few distinct values (qualitative or discrete numeric) and/or factors, the syntax is as follows

**distr.table.xy(x,y, freq=c("counts"), freq.type=c("joint"), total=T, data)** where:

- **x** and **y** are defined as in **distr.table.x()**: **x** is reported on the **rows** and **y** on the **columns**

- **freq: vector** indicating the frequencies to be reported (a table is produced for each type). Available options are **counts** , **percentages** , **proportions** (possible abbreviations, e.g. **prop** ).

- **freq.type**: **vector** indicating the requested types of frequencies (a table is produced for each type). The options are **joint** , **x|y** (or **column** ), and **y|x** (or **row** ).

- **total**: **logical** value specifying whether totals are to be reported in the table or not.

- **Note:** it is also possible to obtain tables for

- **numeric variables to be classified into intervals, using the breaks.x and/or breaks.y arguments to specify interval endpoints**

- **variables measured in classes by specifying interval.x=T and/or interval.y=T**

## Rstudio: distr.plot.xy() - bars

With a similar syntax, the function **distr.plot.xy()** allows to graphically display joint or conditional distributions. To obtain **bar charts,** the syntax is as follows

**distr.plot.xy(x,y, freq="counts", freq.type="joint", plot.type="bars", bar.type ="stacked",data)**

where (other options similar to **distr.table.x()** ):

- **x** and are defined as in: Note that in this case **x** is **y distr.table.xy() always on the**

- horizontal axis and on the vertical axis **y is always**

- **freq, freq.type**: **individual value** indicating which frequencies are to be plotted.

- **plot.type**: **type of graph** (in this case, **"bars"** ; other options will be explained later)

- bar. **type**: indicates whether a **stacked (bar.type ="stacked"** , default) or a side-by-side (bar **.type ="beside"** ) bar plot should be built

- **Note:** plots can also be obtained for

- **numeric variables to be classified into intervals, using the breaks.x and/or breaks.y arguments to specify interval endpoints**

- **variables measured in classes by specifying interval.x=T and/or interval.y=T**

## Hands on: tables&plots for qualitative/discrete variables

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason)**

**Univariate distributions: What considerations?** Most of the users contacted the call centre for issues related to the **mobile** line (the mode, with a frequency much higher than the other categories). As for the  satisfaction, frequencies are concentrated on the highest levels. Indeed, the mode is **Completely** and the median is **Very**: most users are completely satisfied and at least 50% are very satisfied.

## Hands on: tables&plots for qualitative/discrete variables

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason) Cross-tab and side-by-side barplot**

**distr.table.xy(x=Reason,y=Satisf.F, freq=c("counts", "prop"), freq.type="joint", f.digits=3,data=CallCenter) distr.plot.xy(x=Reason,y=Satisf.F, freq="prop", freq.type="joint", plot.type="bars",**

**colour=c("red", "orange", "yellow", "green", "darkgreen"), data=CallCenter)**

## Hands on: tables&plots for qualitative/discrete variables

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason)**

## Hands on: tables&plots for qualitative/discrete variables

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason)**

_The joint distribution allows to identify the most relevant combinations of categories._

_However, to study in depth the level of satisfaction of users with different issues, one must consider_ _**conditional distributions** , providing information about the relevance of the satisfaction levels ._ _**within each segment**_

## Hands on: tables&plots for qualitative/discrete variables

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason) Conditional distribution:**

**# conditional distributions of Satisf (y) | Reason (x, horizontal axis) distr.table.xy(x=Reason,y=Satisf.F, freq="prop", freq.type="y|x", data=CallCenter) distr.plot.xy(x=Reason,y=Satisf.F, freq="prop", freq.type="y|x", plot.type="bars",**

**colour=c("red", "orange", "yellow", "green", "darkgreen"), data=CallCenter)**

## Hands on: tables&plots for qualitative/discrete variables

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason)**

## Comments?

_The support provided for landline and mobile linerelated problems works well, with mode and median satisfaction level equal to 5! For Administration there is a decrease (mode=median=4)._

_On the other hand, the service for Activ/Transf is critical, with mode (definitely dominant) and median both equal to 3, and the highest percentage of dissatisfied or very dissatisfied clients._

## Hands on: tables&plots for qualitative/discrete variables

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason)**

## Comments?

_**The mode and median of Satisfaction at the** marginal_ _**level** are due to the aggregation of segments of clients having different levels of satisfaction. The apparent good performance at the overall level is due to the_ _**high number of customers contacting the call centre for fixed-line and mobile reasons, who are typically very satisfied!!!**_

## Hands on: tables&plots for qualitative/discrete variables

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason)**

Given the **marginal** distributions, which conditional distributions do you expect in the case of no association (independence)? **They should all coincide with the marginal distribution; this would imply that the level of satisfaction has exactly the same distribution** _**regardless of the reason for contact** ._

# Joint analysis of two variables Variables of which one is continuous numeric

## Tables and graphs for quantitative variables

**(READING)**

For quantitative (numerical) variables, one must consider that:

- The number of values assumed by **discrete variables** can be small (e.g. number of visits to a shop in a certain period), as well as quite large (e.g. years of age of a customer, number of transactions with credit card in a year)

- **Continuous variables** typically take a different value for each observation, and thus the number of observed values is equal to or close to the number of cases ^bwcdqn

As mentioned, the tables and graphs introduced to jointly analyse qualitative variables can also be used in the case of two discrete variables both taking a small number of distinct values.

We introduce tools for the joint analysis of two variables of which **at least one is continuous numerical** (or discrete with many distinct values)

**Variables of which one is continuous numeric Continuous numeric variable and qualitative/discrete variable**

## Variables: continuous and qualitative

**Response times to users tweets by 5 companies incorporating social media into their marketing strategy.**

**Company:** we consider 5 companies, identified by their activity ( **Airlines** , Express **Courier** and Money Remittance service, **Products** , **Mobile** Services, **Tour** Operator).

**Time:** Response time (in seconds) to tweets with questions or requests for assistance/support/information

For each company, response times to 100 randomly selected tweets were measured.

## Variables: continuous and qualitative - frequency table

**Response times to tweets measured on 5 companies.**

## Variables: continuous and qualitative – classifying into intervals

**Response times to tweets measured on 5 companies.**

Adopting the same approach followed to analyse a continuous variable, it might seem sensible to classify the **Time** variable into intervals, and to build the cross-tab between time in classes and company.

Equal-width interval classes (180 = 3 minutes)

## Comments?

## Variables: continuous and qualitative - boxplots side by side

# Response times to tweets measured on 5 companies: comparison of boxplots.

## Comments?

_We note that_ _**Airplane** is the company that “generally” has the slowest response time, followed by_ _**Product** , even if the two distributions of response times for these companies are more dispersed compared to the others._

_In particular, note that_ _**Airplane** presents a rather symmetric distribution, which partly overlaps with_ _**Product** 's distribution. The latter distribution is skewed to the right; in particular, the median response time - not much higher than that of Courier, Telecom and Tour - is higher than the third quartile of the distributions for Courier and Telecom, and the 25% of the slowest response times are higher than the maximum response times of these 3 companies._
*(See also: [[Lecture 8-9 Slides#^0ix6sm]])*

## Variables: continuous and qualitative - side by side boxplots

# Response times to tweets measured on 5 companies: comparison of boxplots.

## Comments?

_**Courier** is definitely the fastest responding company in a fairly systematic manner, followed as mentioned by Telecom and Tour._

_In conclusion, the variable_ **Time** _is associated with the variable_ **Company,** _**as its distribution varies as**_ **Company** _**changes.**_

To compare the characteristics of the distributions in a more synthetic way, one can use the summary measures of **Time** conditional on **Company** .

## Variables: continuous and qualitative - summary measures

**Response times to tweets measured on 5 companies: conditional summary measures.**

|#|**Variables: continuous and qualitative - summary measures`Tour 100   0 1077.8 1583.0 1605.40`**  APPROACH: Conditional summary measures h conditional summary measures for the variable time in correspondence to the Airplane company|
|---|---|

## Rstudio: distr.plot.xy() & summary.x()

The function **distr.plot.xy()** can be used to easily to obtain **side-by-side boxplots:**

**distr.plot.xy(x,y, plot.type="boxplot",data)**

Note that as in the case of the boxplot for a single variable, the plot can only be built for **numeric variables** (classification into intervals is not possible). It is clearly not necessary to indicate the frequencies to be plotted as the boxplot is based on the raw data.

The **distr.summary.x()** function allows to obtain conditional summary measures by specifying, in addition to the arguments already used for the analysis of a single variable, the conditioning variable(s) (no more than 2) using the **by1** and/or **by2** arguments:

**distr.summary.x(x, by1, by2, stats, digits=2,f.digits=4, data)**

## Hands on: analysis of tweets

**Response times (Time) to tweets measured on 5 companies (Company): syntax used to obtain the results shown in the slides**

**# original cross-table(INADEQUATE) distr.table.xy(x=Time,y=Company,freq="counts",freq.type="joint", date=Tweets)**

**# cross-table with Time classified in intervals distr.table.xy(x=Time,y=Company,freq="counts",freq.type="joint", breaks.x=seq(600,3120,by=180),data=Tweets)**

- **# the syntax to obtain a collection of histograms is not reported # Side-by-side boxplots**

- **distr.plot.xy(x=Company,y=Time,plot.type="boxplot", data=Tweets) # conditional summary measures (summary reports a collection of stats) distr.summary.x(x=Time,by1=Company,stats=c("summary", "p5","p10","p90","p95"),data=Tweets)**

# Variables of which one is continuous numeric

**Two numeric variables**

## Variables: numeric

## House price data in a US city

**Joint distribution analysis of price and landValue? And of and or price livingArea rooms?**

Variables are continuous. It is possible to construct a cross table after classification into intervals, but this would imply an over- **simplification** and compression of data. To analyse the **pairs of values actually observed in** more detail, a **scatterplot is** typically used. ^zddub1

## Analysis of the relationship between numerical variables

In the joint study of two **numerical variables,** we introduced the scatterplot as a graphical tool to describe the relationship between the variables.

- } **Example.** Price, living area, number of rooms, lot size for houses in a US city

There is a relationship between the three pairs of variables: as the width of the living area, the number of rooms and the size of the property increase, the price of houses increases, but the intensity of the relationship is different!!! **How to measure and compare the strength of these relationships?**

## Concordant and discordant value pairs

## House price data in a US city: prices and livingArea

Based on the **means of the two variables,** we can identify four quadrants in the plot. Quadrants **B** and **C: pairs of concordant values**: cases with values both greater or both less than the mean.

Quadrants **A** and **D: pairs of discordant values:** cases with values greater than (resp. less than) the mean on one variable and lower than (resp. greater than) the mean on the other variable.

Two variables are **positively (or directly)** associated if concordant pairs prevail and **negatively (or inversely)** associated if discordant pairs prevail.

## Cross-products (cross-products)

To assess the strength of the relation between two variables, we have to consider both the **direction** of the deviations from the means and their **size** . At this aim, we consider for each case (𝑥�, 𝑦�) its cross-product, i.e. the product of the deviations from the means

(𝑥� −̄𝑥)(𝑦� −̄𝑦)

- } The cross-product informs both on the concordance/discordance (sign) of the values observed on the two variables and on the extent of the deviations from the means.

- } Cases with a **positive** cross-product are **concordant**: they have both values greater or lower than the means (Panels B and C)

- } Cases with **negative** cross-product are **discordant**: the deviations from the means have opposite signs; for one variable the value is above the mean, for the other it is below the mean (Panels A and D).

- } To  assess whether concordant or discordant pairs prevail, i.e. if between two variables a direct or inverse (or no) relation exists, the average of the cross-products is considered, the so-called **covariance**

## Covariance: definition for population and for sample

The definition of the covariance is slightly different for a population and for a sample } For data measured on the entire **population** the covariance is defined as:

} The **sample covariance** instead is defined as:

As seen for the variance, this is not exactly the **average of** the product of the deviations, 𝒏−𝟏 𝒏 _**.**_ The reason for this difference will because the sum is divided by **( )** and not by be explained when discussing about inference, and specifically about estimation

## The covariance: indirect calculation (shortcut) formula

Focusing on the **sample** covariance, we introduce the so-called indirect calculation formula, that can be useful to calculate the covariance in some cases:

_The covariance can be calculated based on the mean of the products between values and on the product of the means!_

We will use this formula only in particular cases, and specifically when the covariance is calculated based on aggregated data

## The covariance: indirect calculation formula

**(OPTIONAL)**

## Focusing on the **sample covariance,** note that:

## In the case of a **population,** the same reasoning leads to:

## Covariance

**Covariance close to zero No prevalence of concordant or discordant pairs is observed**

## Covariance: calculation based on raw data

## **Example: calculation of the covariance between price and livingArea based on the first** 𝒏 = 10 houses

## The means are

|**living16364532**|_The means are_ �𝒙**=(16201/10)=1620.1** �𝒚**=(1319575/10)=131957.5** _The sum of the products of the deviations_|
|---|---|---|---|---|---|---|---|---|---|---|
|**1944**|**109000**|**323.9 **|**-22957.5**|**-7435934**|_from the means (rounding all intermediate_|
|**1944**|**155000**|**323.9**|**23042.5**|**7463466**|_results to 2 decimal places) is_**84167938**.|
|**840**|**86060**|**-780.1 **|**-45897.5**|**35804640**|So:|
|**1152**|**120000**|**-468.1 **|**-11957.5**|**5597306**|**84167938**|
|**27529** =**9351993**|
|**1632**|**90000**|**11.9 **|**-41957.5**|**-499294**|**Comments?**|
|**Somma**|**141684167938**|_The covariance is positive: the relationship_ |

_The covariance is positive: the relationship between the two variables is_ _**direct** ._

## Rstudio: distr.plot.xy() & cov()

The scatterplot of two variables can be obtained using the function **distr.plot.xy()**:

**distr.plot.xy(x,y, plot.type="scatter",data)**

Note that it is not necessary to specify the frequencies to report in the plot because the scatterplot is built based on raw data.

The function **cov()** in R returns the covariance between two **numeric variables** using the syntax **:**

**cov(x, y)**

Note that _**cannot be**_ **the names of the columns in x, y  are the names of two vectors and they a dataframe**

**In the case when some data are missing, they can be excluded from computations by specifying that the calculation of the covariance should be based only on cases with complete information on the two variables:**

**cov(x, y, use="complete")**

## Hands on: relationship between numerical variables

## Scatterplot: house price and three numerical variables

**# scatterplots distr.plot.xy(x=livingArea,y=price,plot.type = "scatter",data=House_Price) distr.plot.xy(x=rooms,y=price,plot.type = "scatter",data=House_Price) distr.plot.xy(x=lotSize,y=price,plot.type = "scatter",data=House_Price)**

## The R function cov(x,y) can be used to calculate the covariance

- **cov(House_Price$livingArea,House_Price$price) (1) 25617618**

- **cov(House_Price$rooms,House_Price$price)**

**(1) 74923.6**

- **cov(House_Price$lotSize,House_Price$price)**

- **(1) NA**

- **cov(House_Price$lotSize,House_Price$price,use="complete")**

- **(1) 182595271**

## Analysis of covariances

**House price data in a US city:** Price, living area, number of rooms, property size

**cov = 25617618                                         cov = 74923.6                                      cov = 182595271**

**Can we conclude that price has the strongest direct relationship with lotSize?**

_The covariance (as the variance) depends on the_ _**deviations from the means,** and both the means and the deviations depend on the units of measurement of the variables_ _**!**_

_Thus, covariance allows to deduce the_ _**direction of the relationship between two variables,** but not to assess the strength of such relationship, since it is an_ _**absolute and not a relative measure!**_

## Correlation coefficient

_r_ = 0.16 _r_ = 0.49 _r_ = 0.78 _xy xy xy_ As _r_ moves away from 0 _xy_ – (towards 1 or towards 1) the points tend to be more and more  concentrated around a straight line (with positive or negative slope _r_ = 0.16 _r_ = -0.55 _r_ = -0.86 _xy xy xy r_ depending on the sign of ) _xy_

## Hands on: relationship between numerical variables

## To calculate the covariance, the R function cor(x,y)(very similar to cor(x,y)) can be used

- **cor(House_Price$livingArea,House_Price$price) (1) 0.685806**

- **cor(House_Price$rooms,House_Price$price) (1) 0.4855333**

**> # to deal with missing values use="complete" > cor(House_Price$lotSize,House_Price$price,use="complete") (1) 0.2062668**

## Correlation: some considerations

_**It is important to consider that the correlation in some cases may not be reliable.**_

In the 4 cases shown in the plots (Anscombe , 1973), the variables have the same means, variances, covariance and correlation.

However, the relationship between the variables is very different:

**Plot A:** the correlation properly reflects the relationship between the variables. **Plot B:** perfect **non-linear** relationship, **Plot C/D:** the value of _**r**_ is influenced _**xy**_ by **extreme values (** outliers) whose

_r r r_ presence causes a decrease in (Plot C: without the outlier it would be =1) or an increase in _xy xy xy r_ (Plot D: without the  outliers it would be =0) _xy_

## Related Notes
- [[Lecture 8-9 Slides]]
- [[Lecture 3-4 Slides with NOTES]]
- [[Lecture 5-6 Slides with NOTES]]