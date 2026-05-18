**TABLES, GRAPHS AND SUMMARY MEASURES IN THE ANALYSIS OF TWO VARIABLES** 

**Material prepared by R. Piccarreta for students on course 30001 / Bocconi University. Distribution - even via the web - without authorisation is prohibited.** 

## **The study of two variables [READING]** 

In many applications, one is interested to study two variables and their relationship: 

- Is there a relationship between consumers’ attention/interest in healthy eating and their age? 

- Are there differences in the response times to complaint tweets from companies incorporating social media into their marketing strategy? 

- Is there a relationship between performance in the Bachelor’s degree and performance in the Master’s degree? Is it possible to use the possible relationship to select candidates? 

**2** 

# **Joint analysis of two variables Qualitative variables (or discrete taking few distinct values)** 

## **Qualitative variables: cross tabulation** 

## **Cross-tab (absolute frequencies)** 

## Distinct values taken by 𝒀 

**----- Start of picture text -----**<br>
∗ ∗ ∗<br>𝑿 \ 𝒀 𝒚𝟏 𝒚𝟐 ... 𝒚𝑱<br>∗<br>𝒙 ...<br>𝟏 f 11 f 12 f 1 J<br>∗<br>𝒙 ...<br>𝟐 f 21 f 22 f 2 J<br>... ... ... ... ...<br>∗<br>𝒙 ...<br>𝑲 fK 1 fK 2 fKJ<br>taken by<br>Distinct values<br>**----- End of picture text -----**<br>

Each cell reports the frequency (in this case, the absolute frequency) characterising each pair of values 

For the sake of simplicity, we will always denote by 𝒀 the variable on the columns and by 𝑿 the variable on the rows of the table 

**6** 

## **Qualitative variables: bar charts** 

## Example: Age and interest in healthy eating (sample of 1224 individuals) 

|**_Interest_**<br>**_Age_**<br>Low<br>Medium High<br>18-30<br>183<br>272<br>49|**Tot**<br>**504**|**Side-by-side bar diagrams**||
|---|---|---|---|
|31-45<br>97<br>168<br>68|**333**|||
|46-60<br>65<br>214<br>108|**387**|||
|**Tot**<br>**345**<br>**654**<br>**225**|**1224**|||
|e two diagrams show the**same bars,**||||
|**ouped byAge**or by**Interest**in||||
|althy eating||||
|ey allow to easily identify the most||||
|levant combinations of categories||||
|d to appreciate their relevance in||||
|lative terms (the**appearance**of the||||
|aphs**does not change**when||||
|idi lti fi||||

The two diagrams show the **same bars, grouped by Age** or by **Interest** in healthy eating They allow to easily identify the most relevant combinations of categories and to appreciate their relevance in relative terms (the **appearance** of the graphs **does not change** when considering relative frequencies) 

**10** 

## **Qualitative variables: bar charts** 

## Example: Age and interest in healthy eating (sample of 1224 individuals) 

|**_Interest_**<br>**_Age_**|Low|Medium|High|**Tot**|
|---|---|---|---|---|
|18-30|183|272|49|**504**|
|31-45|97|168|68|**333**|
|46-60|65|214|108|**387**|
|**Tot**|**345**|**654**|**225**|**1224**|

The two diagrams show the **same bars, stacked** by **Age** or by **Interest** in healthy eating Information is the same provided by side-by-side bars, with more emphasis on the marginal frequencies of the variable on the x-axis (the appearance of the graphs **does not change** when considering relative frequencies) 

## **Stacked bar diagrams** 

**11** 

## **Qualitative variables: conditional distributions** 

Example: Age and interest in healthy eating (sample of 1224 individuals) 

||**_Interest_**<br>**_Age_**|Low|Medium High|Medium High||**Tot**||**Column conditional distributions**|**Column conditional distributions**|**Column conditional distributions**|**Column conditional distributions**|**Column conditional distributions**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||18-30|183||272<br>49||**504**|||||||
||31-45<br>46-60<br>**Tot**|97<br>65<br>**345**||168<br>68<br>214<br>108<br>**654**<br>**225**||**333**<br>**387**<br>**1224**||**_Interest_**<br>**_Age_**<br>**18-30**<br>**31-45**|**Low**<br>**?**<br>**?**<br>**0.530**<br>**?**<br>**0.281**|**Medium** <br>**?**<br>?<br>**0.416**<br>**0.257**|**High**<br>**0.218**<br>**0.302**|Not<br>are<br>pre<br>res|
||||||||||||||
|tocalculate the conditional free .||||||Of|**46-60**<br>**Tot**<br>AGE||**0.188**<br>**1.00**|**0.327**<br>**1.00**|**0.480**<br>**1.00**|<br>me<br>pre|
|given IMELE , consider||||columns|individually||||||||

Note that among those who are most interested, seniors prevail, whilst among respondents with low/ medium interest, youngsters prevail 

**Column conditional frequency** : frequency of each category of the row variable 𝑿, in the **subset of** cases characterised by one of the categories of 𝒀. E.g. The frequency of **Age** = _46-60_ **conditioned on** the category **Interest =** _High_ is: �� Freq {𝐀𝐠𝐞 = _46-60_ | 𝐈𝐧𝐭𝐞𝐫𝐞𝐬𝐭 = _High_ } = ���[= 0.480] 

**14** 

## **Qualitative variables: conditional distributions** 

are In order to represent conditional distributions, **side-by-side or stacked bar charts** usually used, displaying conditional rather than joint frequencies. 

**Age distribution | Interest** 

## **Distribution of Interest | Age** 

**Stacked bar diagrams** Note that the height of the bars in the stacked bars diagram is 1, since each bar represents a frequency distribution (sum of frequencies conditional on each category = 1) 

**15** 

## **Rstudio: distr.table.xy()** 

The function **distr.table.xy()** allows to tabulate joint or conditional distributions. The syntax is similar to that of **distr.table.x()** . In the simple case of two variables taking few distinct values (qualitative or discrete numeric) and/or factors, the syntax is as follows 

**distr.table.xy(x,y, freq=c("counts"), freq.type=c("joint"), total=T, data)** where: 

- **x** and **y** are defined as in **distr.table.x()** : **x** is reported on the **rows** and **y** on the **columns** 

- **freq: vector** indicating the frequencies to be reported (a table is produced for each type). Available options are **counts** , **percentages** , **proportions** (possible abbreviations, e.g. **prop** ). 

- **freq.type** : **vector** indicating the requested types of frequencies (a table is produced for each type). The options are **joint** , **x|y** (or **column** ), and **y|x** (or **row** ). 

- **total** : **logical** value specifying whether totals are to be reported in the table or not. 

- **Note:** it is also possible to obtain tables for 

   - **numeric variables to be classified into intervals, using the breaks.x and/or breaks.y arguments to specify interval endpoints** 

   - **variables measured in classes by specifying interval.x=T and/or interval.y=T** 

**16** 

## **Rstudio: distr.plot.xy() - bars** 

With a similar syntax, the function **distr.plot.xy()** allows to graphically display joint or conditional distributions. To obtain **bar charts,** the syntax is as follows 

**distr.plot.xy(x,y, freq="counts", freq.type="joint", plot.type="bars", bar.type ="stacked",data)** 

where (other options similar to **distr.table.x()** ): 

- **x** and are defined as in : Note that in this case **x** is **y distr.table.xy() always on the** 

- horizontal axis and on the vertical axis **y is always** 

- **freq, freq.type** : **individual value** indicating which frequencies are to be plotted. 

- **plot.type** : **type of graph** (in this case, **"bars"** ; other options will be explained later) 

- bar. **type** : indicates whether a **stacked (bar.type ="stacked"** , default) or a side-by-side (bar **.type ="beside"** ) bar plot should be built 

- **Note:** plots can also be obtained for 

   - **numeric variables to be classified into intervals, using the breaks.x and/or breaks.y arguments to specify interval endpoints** 

   - **variables measured in classes by specifying interval.x=T and/or interval.y=T** 

**17** 

## **Hands on: tables&plots for qualitative/discrete variables** 

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason)** 

|**Satisf.F**|**_fj_**|**_pj_**|**_Fj_**|
|---|---|---|---|
|**Not at all**|**68 **|**0.031 **|**0.031**|
|**Slightly**|**111 **|**0.051 **|**0.082**|
|**Moderate**|**334 **|**0.153 **|**0.235**|
|**Very**|**675 **|**0.308 **|**0.543**|
|**Completely**|**1001 **|**0.457**|**1**|
|**Total**|**2189**|**1.00**||
|||||
|**Reason**|**_fk_**|**_pk_**||
|**Landline**|**597 **|**0.273**||
|**Mobile**|**999 **|**0.456**||
|**Activ/Transf**|**352 **|**0.161**||
|**Admin**|**241 **|**0.110**||
|**Total**|**2189 **|**1.000**||

**Univariate distributions: What considerations?** Most of the users contacted the call centre for issues related to the **mobile** line (the mode, with a frequency much higher than the other categories). As for the  satisfaction, frequencies are concentrated on the highest levels. Indeed, the mode is **Completely** and the median is **Very** : most users are completely satisfied and at least 50% are very satisfied. 

**19** 

## **Hands on: tables&plots for qualitative/discrete variables** 

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason) Cross-tab and side-by-side barplot** 

**distr.table.xy(x=Reason,y=Satisf.F, freq=c("counts", "prop"), freq.type="joint", f.digits=3,data=CallCenter) distr.plot.xy(x=Reason,y=Satisf.F, freq="prop", freq.type="joint", plot.type="bars",** 

**colour=c("red", "orange", "yellow", "green", "darkgreen"), data=CallCenter)** 

**21** 

## **Hands on: tables&plots for qualitative/discrete variables** 

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason)** 

||**Monitoring and evaluation of the performance of a call center: level of satisfaction**<br>**(Satisf.F) and reason for contact (Reason)**<br>**Hands on: tables&plots for qualitative/discrete variables**<br>**Counts**<br>**Satisf.F**<br>**Reason**<br>**Not at allSlightly Moderately Very Completely TOTAL**<br>**Activ/Transf**<br>**29**<br>**58**<br>**146**<br>**75**<br>**44**<br>**352**<br>**Admin**<br>**5**<br>**15**<br>**44**<br>**90**<br>**87**<br>**241**<br>**Landline**<br>**8**<br>**15**<br>**94**<br>**160**<br>**320**<br>**597**<br>**Mobile**<br>**26**<br>**23**<br>**50**<br>**350**<br>**550**<br>**999**<br>**TOTAL**<br>**68**<br>**111**<br>**334**<br>**675**<br>**1001**<br>**2189**<br>**Prop**<br>**Satisf.F**<br>**Reason**<br>**Not at allSlightly Moderately Very Completely TOTAL**<br>**Activ/Transf**<br>**0.013**<br>**0.026**<br>**0.067**<br>**0.034**<br>**0.02**<br>**0.161**<br>**Admin**<br>**0.002**<br>**0.007**<br>**0.02**<br>**0.041**<br>**0.04**<br>**0.11**<br>**Landline**<br>**0.004**<br>**0.007**<br>**0.043**<br>**0.073**<br>**0.146**<br>**0.273**<br>**Mobile**<br>**0.012**<br>**0.011**<br>**0.023**<br>**0.16**<br>**0.251**<br>**0.456**<br>**TOTAL**<br>**0.031**<br>**0.051**<br>**0.153**<br>**0.308**<br>**0.457**<br>**1**<br>free<br><br>><br><br>e<br><br>&marginal<br>distributi<br>of Reason|**Hands on: tables&plots for qualitative/discrete variables**|**Hands on: tables&plots for qualitative/discrete variables**|**Hands on: tables&plots for qualitative/discrete variables**|**Hands on: tables&plots for qualitative/discrete variables**|**Hands on: tables&plots for qualitative/discrete variables**|**Hands on: tables&plots for qualitative/discrete variables**|**Hands on: tables&plots for qualitative/discrete variables**|**Hands on: tables&plots for qualitative/discrete variables**|
|---|---|---|---|---|---|---|---|---|---|
|-<br><br>⑤<br>s<br>↳<br>↳|><br><br>e<br>|**Counts**|**Satisf.F**|||||||
|||**Reason**|**Not at all**|**Slightly**|**Moderately **|**Very **|**Completely **|**TOTAL**||
|||**Activ/Transf**|**29**|**58**|**146**|**75**|**44**|**352**||
|||**Admin**|**5**|**15**|**44**|**90**|**87**|**241**||
|||**Landline**|**8**|**15**|**94**|**160**|**320**|**597**||
|||**Mobile**|**26**|**23**|**50**|**350**|**550**|**999**||
|||**TOTAL**|**68**|**111**|**334**|**675**|**1001**|**2189**||
|||||||||||
|||**Prop**|**Satisf.F**|||||||
|||**Reason**|**Not at all**|**Slightly**|**Moderately **|**Very **|**Completely **|**TOTAL**||
|||**Activ/Transf**|**0.013**|**0.026**|**0.067**|**0.034**|**0.02**||**0.161**|
|||**Admin**|**0.002**|**0.007**|**0.02**|**0.041**|**0.04**||**0.11**|
|||**Landline**|**0.004**|**0.007**|**0.043**|**0.073**|**0.146**||**0.273**|
|||**Mobile**|**0.012**|**0.011**|**0.023**|**0.16**|**0.251**||**0.456**|
|||**TOTAL**|||||**0.457**|**1**||
||||**0.031**|**0.051**|**0.153**|**0.308**|**0.457**|||
|||||||||||

**22** 

## **Hands on: tables&plots for qualitative/discrete variables** 

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason)** 

|**Counts**|**Satisf.F**||||||
|---|---|---|---|---|---|---|
|**Reason**|**Not at all**|**Slightly**|**Moderately **|**Very **|**Completely **|**TOTAL**|
|**Activ/Transf**|29|58|146|75|44|**352**|
|**Admin**|5|15|44|90|87|**241**|
|**Landline**|8|15|94|160|320|**597**|
|**Mobile**|26|23|50|350|550|**999**|
|**TOTAL**|**68**|**111**|**334**|**675**|**1001**|**2189**|

_The joint distribution allows to identify the most relevant combinations of categories._ 

_However, to study in depth the level of satisfaction of users with different issues, one must consider_ _**conditional distributions** , providing information about the relevance of the satisfaction levels ._ _**within each segment**_ 

**23** 

## **Hands on: tables&plots for qualitative/discrete variables** 

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason) Conditional distribution:** 

**# conditional distributions of Satisf (y) | Reason (x, horizontal axis) distr.table.xy(x=Reason,y=Satisf.F, freq="prop", freq.type="y|x", data=CallCenter) distr.plot.xy(x=Reason,y=Satisf.F, freq="prop", freq.type="y|x", plot.type="bars",** 

**colour=c("red", "orange", "yellow", "green", "darkgreen"), data=CallCenter)** 

**24** 

## **Hands on: tables&plots for qualitative/discrete variables** 

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason)** 

|**Y|X**|**Satisf.F**||||||
|---|---|---|---|---|---|---|
|**Reason**|**Not at all**|**Slightly **|**Moderately **|**Very **|**Completely **|**TOTAL**|
|**Activ/Transf**|**0.08**|**0.16**|**0.41**|**0.21**|**0.12**|**1**|
|**Admin**|**0.02**|**0.06**|**0.18**|**0.37**|**0.36**|**1**|
|**Landline**|**0.01**|**0.03**|**0.16**|**0.27**|**0.54**|**1**|
|**Mobile**|**0.03**|**0.02**|**0.05**|**0.35**|**0.55**|**1**|

## **Comments?** 

_The support provided for landline and mobile linerelated problems works well, with mode and median satisfaction level equal to 5! For Administration there is a decrease (mode=median=4)._ 

_On the other hand, the service for Activ/Transf is critical, with mode (definitely dominant) and median both equal to 3, and the highest percentage of dissatisfied or very dissatisfied clients._ 

**26** 

## **Hands on: tables&plots for qualitative/discrete variables** 

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason)** 

|**Y|X**|**Satisf.F**||||||
|---|---|---|---|---|---|---|
|**Reason**|**Not at all**|**Slightly **|**Moderately **|**Very **|**Completely **|**TOTAL**|
|**Activ/Transf**|**0.08**|**0.16**|**0.41**|**0.21**|**0.12**|**1**|
|**Admin**|**0.02**|**0.06**|**0.18**|**0.37**|**0.36**|**1**|
|**Landline**|**0.01**|**0.03**|**0.16**|**0.27**|**0.54**|**1**|
|**Mobile**|**0.03**|**0.02**|**0.05**|**0.35**|**0.55**|**1**|

## **Comments?** 

_**The mode and median of Satisfaction at the** marginal_ _**level** are due to the aggregation of segments of clients having different levels of satisfaction. The apparent good performance at the overall level is due to the_ _**high number of customers contacting the call centre for fixed-line and mobile reasons, who are typically very satisfied!!!**_ 

**27** 

## **Hands on: tables&plots for qualitative/discrete variables** 

**Monitoring and evaluation of the performance of a call center: level of satisfaction (Satisf.F) and reason for contact (Reason)** 

|**Satisf.F**||||||
|---|---|---|---|---|---|
|**Not at all**|**Slightly **|**Moderately **|**Very **|**Completely **|**TOTAL**|
|**0.08**|**0.16**|**0.41**|**0.21**|**0.12**|**1**|
|**0.02**|**0.06**|**0.18**|**0.37**|**0.36**|**1**|
|**0.01**|**0.03**|**0.16**|**0.27**|**0.54**|**1**|
|**0.03**|**0.02**|**0.05**|**0.35**|**0.55**|**1**|

|**Prop**|**Satisf.F**||||||
|---|---|---|---|---|---|---|
|**Reason**|**Not at all**|**Slightly**|**Moderately **|**Very **|**Completely**|**TOTAL**|
|**Activ/Transf**|**0.013**|**0.026**|**0.067**|**0.034**|**0.02**|**0.161**|
|**Admin**|**0.002**|**0.007**|**0.02**|**0.041**|**0.04**|**0.11**|
|**Landline**|**0.004**|**0.007**|**0.043**|**0.073**|**0.146**|**0.273**|
|**Mobile**|**0.012**|**0.011**|**0.023**|**0.16**|**0.251**|**0.456**|
|**TOTAL**|**0.031**|**0.051**|**0.153**|**0.308**|**0.457**|**1**|

Given the **marginal** distributions, which conditional distributions do you expect in the case of no association (independence)? **They should all coincide with the marginal distribution; this would imply that the level of satisfaction has exactly the same distribution** _**regardless of the reason for contact** ._ 

**28** 

# **Joint analysis of two variables Variables of which one is continuous numeric** 

## **Tables and graphs for quantitative variables [READING]** 

For quantitative (numerical) variables, one must consider that: 

- The number of values assumed by **discrete variables** can be small (e.g. number of visits to a shop in a certain period), as well as quite large (e.g. years of age of a customer, number of transactions with credit card in a year) 

- **Continuous variables** typically take a different value for each observation, and thus the number of observed values is equal to or close to the number of cases 

As mentioned, the tables and graphs introduced to jointly analyse qualitative variables can also be used in the case of two discrete variables both taking a small number of distinct values. 

We introduce tools for the joint analysis of two variables of which **at least one is continuous numerical** (or discrete with many distinct values) 

**31** 

**Variables of which one is continuous numeric Continuous numeric variable and qualitative/discrete variable** 

## **Variables: continuous and qualitative** 

**Response times to users tweets by 5 companies incorporating social media into their marketing strategy.** 

**Company:** we consider 5 companies, identified by their activity ( **Airlines** , Express **Courier** and Money Remittance service, **Products** , **Mobile** Services, **Tour** Operator). 

**Time:** Response time (in seconds) to tweets with questions or requests for assistance/support/information 

For each company, response times to 100 randomly selected tweets were measured. 

**33** 

## **Variables: continuous and qualitative - frequency table** 

**Response times to tweets measured on 5 companies.** 

|**Variables: continuous and qualitative - frequency table**<br>**Response times to tweets measured on 5 companies.**<br>**Cross tabulation**(portion): joint absolut<br>frequencies of the response times an<br>companies<br>**Time**<br>**Company**<br>**Tot**<br>**Airplane Courier Products Telecom Tour**<br>**713**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**728**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**780**<br>0<br>**2**<br>0<br>0<br>0<br>**2**<br>**795**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**840**<br>0<br>0<br>0<br>0<br>1<br>**1**<br>**855**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**870**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**878**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**893**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**900**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**908**<br>0<br>**2**<br>0<br>**1**<br>**2**<br>**5**<br>**...**<br>...<br>...<br>...<br>...<br>...<br>**...**<br>**3000**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**3043**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**Tot**<br>**100**<br>**100**<br>**100**<br>**100**<br>**100**<br>**500**<br>**Comments?**<br>The**continuous**variable**Time**takes (as<br>expected) a very high number of values;<br>the joint frequencies are very low.<br>The cross-tab is not an effective tool for<br>the analysis of the two variables.<br>**Which tools for a more efficient**<br>**analysis?**<br>tkJOINTFREQUENCYTABES<br>An|**Variables: continuous and qualitative - frequency table**<br>**Response times to tweets measured on 5 companies.**<br>**Cross tabulation**(portion): joint absolut<br>frequencies of the response times an<br>companies<br>**Time**<br>**Company**<br>**Tot**<br>**Airplane Courier Products Telecom Tour**<br>**713**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**728**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**780**<br>0<br>**2**<br>0<br>0<br>0<br>**2**<br>**795**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**840**<br>0<br>0<br>0<br>0<br>1<br>**1**<br>**855**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**870**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**878**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**893**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**900**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**908**<br>0<br>**2**<br>0<br>**1**<br>**2**<br>**5**<br>**...**<br>...<br>...<br>...<br>...<br>...<br>**...**<br>**3000**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**3043**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**Tot**<br>**100**<br>**100**<br>**100**<br>**100**<br>**100**<br>**500**<br>**Comments?**<br>The**continuous**variable**Time**takes (as<br>expected) a very high number of values;<br>the joint frequencies are very low.<br>The cross-tab is not an effective tool for<br>the analysis of the two variables.<br>**Which tools for a more efficient**<br>**analysis?**<br>tkJOINTFREQUENCYTABES<br>An|**Variables: continuous and qualitative - frequency table**<br>**Response times to tweets measured on 5 companies.**<br>**Cross tabulation**(portion): joint absolut<br>frequencies of the response times an<br>companies<br>**Time**<br>**Company**<br>**Tot**<br>**Airplane Courier Products Telecom Tour**<br>**713**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**728**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**780**<br>0<br>**2**<br>0<br>0<br>0<br>**2**<br>**795**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**840**<br>0<br>0<br>0<br>0<br>1<br>**1**<br>**855**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**870**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**878**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**893**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**900**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**908**<br>0<br>**2**<br>0<br>**1**<br>**2**<br>**5**<br>**...**<br>...<br>...<br>...<br>...<br>...<br>**...**<br>**3000**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**3043**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**Tot**<br>**100**<br>**100**<br>**100**<br>**100**<br>**100**<br>**500**<br>**Comments?**<br>The**continuous**variable**Time**takes (as<br>expected) a very high number of values;<br>the joint frequencies are very low.<br>The cross-tab is not an effective tool for<br>the analysis of the two variables.<br>**Which tools for a more efficient**<br>**analysis?**<br>tkJOINTFREQUENCYTABES<br>An|**Variables: continuous and qualitative - frequency table**<br>**Response times to tweets measured on 5 companies.**<br>**Cross tabulation**(portion): joint absolut<br>frequencies of the response times an<br>companies<br>**Time**<br>**Company**<br>**Tot**<br>**Airplane Courier Products Telecom Tour**<br>**713**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**728**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**780**<br>0<br>**2**<br>0<br>0<br>0<br>**2**<br>**795**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**840**<br>0<br>0<br>0<br>0<br>1<br>**1**<br>**855**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**870**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**878**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**893**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**900**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**908**<br>0<br>**2**<br>0<br>**1**<br>**2**<br>**5**<br>**...**<br>...<br>...<br>...<br>...<br>...<br>**...**<br>**3000**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**3043**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**Tot**<br>**100**<br>**100**<br>**100**<br>**100**<br>**100**<br>**500**<br>**Comments?**<br>The**continuous**variable**Time**takes (as<br>expected) a very high number of values;<br>the joint frequencies are very low.<br>The cross-tab is not an effective tool for<br>the analysis of the two variables.<br>**Which tools for a more efficient**<br>**analysis?**<br>tkJOINTFREQUENCYTABES<br>An|**Variables: continuous and qualitative - frequency table**<br>**Response times to tweets measured on 5 companies.**<br>**Cross tabulation**(portion): joint absolut<br>frequencies of the response times an<br>companies<br>**Time**<br>**Company**<br>**Tot**<br>**Airplane Courier Products Telecom Tour**<br>**713**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**728**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**780**<br>0<br>**2**<br>0<br>0<br>0<br>**2**<br>**795**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**840**<br>0<br>0<br>0<br>0<br>1<br>**1**<br>**855**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**870**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**878**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**893**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**900**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**908**<br>0<br>**2**<br>0<br>**1**<br>**2**<br>**5**<br>**...**<br>...<br>...<br>...<br>...<br>...<br>**...**<br>**3000**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**3043**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**Tot**<br>**100**<br>**100**<br>**100**<br>**100**<br>**100**<br>**500**<br>**Comments?**<br>The**continuous**variable**Time**takes (as<br>expected) a very high number of values;<br>the joint frequencies are very low.<br>The cross-tab is not an effective tool for<br>the analysis of the two variables.<br>**Which tools for a more efficient**<br>**analysis?**<br>tkJOINTFREQUENCYTABES<br>An|**Variables: continuous and qualitative - frequency table**<br>**Response times to tweets measured on 5 companies.**<br>**Cross tabulation**(portion): joint absolut<br>frequencies of the response times an<br>companies<br>**Time**<br>**Company**<br>**Tot**<br>**Airplane Courier Products Telecom Tour**<br>**713**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**728**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**780**<br>0<br>**2**<br>0<br>0<br>0<br>**2**<br>**795**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**840**<br>0<br>0<br>0<br>0<br>1<br>**1**<br>**855**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**870**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**878**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**893**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**900**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**908**<br>0<br>**2**<br>0<br>**1**<br>**2**<br>**5**<br>**...**<br>...<br>...<br>...<br>...<br>...<br>**...**<br>**3000**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**3043**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**Tot**<br>**100**<br>**100**<br>**100**<br>**100**<br>**100**<br>**500**<br>**Comments?**<br>The**continuous**variable**Time**takes (as<br>expected) a very high number of values;<br>the joint frequencies are very low.<br>The cross-tab is not an effective tool for<br>the analysis of the two variables.<br>**Which tools for a more efficient**<br>**analysis?**<br>tkJOINTFREQUENCYTABES<br>An|**Variables: continuous and qualitative - frequency table**<br>**Response times to tweets measured on 5 companies.**<br>**Cross tabulation**(portion): joint absolut<br>frequencies of the response times an<br>companies<br>**Time**<br>**Company**<br>**Tot**<br>**Airplane Courier Products Telecom Tour**<br>**713**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**728**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**780**<br>0<br>**2**<br>0<br>0<br>0<br>**2**<br>**795**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**840**<br>0<br>0<br>0<br>0<br>1<br>**1**<br>**855**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**870**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**878**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**893**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**900**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**908**<br>0<br>**2**<br>0<br>**1**<br>**2**<br>**5**<br>**...**<br>...<br>...<br>...<br>...<br>...<br>**...**<br>**3000**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**3043**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**Tot**<br>**100**<br>**100**<br>**100**<br>**100**<br>**100**<br>**500**<br>**Comments?**<br>The**continuous**variable**Time**takes (as<br>expected) a very high number of values;<br>the joint frequencies are very low.<br>The cross-tab is not an effective tool for<br>the analysis of the two variables.<br>**Which tools for a more efficient**<br>**analysis?**<br>tkJOINTFREQUENCYTABES<br>An|**Variables: continuous and qualitative - frequency table**<br>**Response times to tweets measured on 5 companies.**<br>**Cross tabulation**(portion): joint absolut<br>frequencies of the response times an<br>companies<br>**Time**<br>**Company**<br>**Tot**<br>**Airplane Courier Products Telecom Tour**<br>**713**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**728**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**780**<br>0<br>**2**<br>0<br>0<br>0<br>**2**<br>**795**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**840**<br>0<br>0<br>0<br>0<br>1<br>**1**<br>**855**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**870**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**878**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**893**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**900**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**908**<br>0<br>**2**<br>0<br>**1**<br>**2**<br>**5**<br>**...**<br>...<br>...<br>...<br>...<br>...<br>**...**<br>**3000**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**3043**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**Tot**<br>**100**<br>**100**<br>**100**<br>**100**<br>**100**<br>**500**<br>**Comments?**<br>The**continuous**variable**Time**takes (as<br>expected) a very high number of values;<br>the joint frequencies are very low.<br>The cross-tab is not an effective tool for<br>the analysis of the two variables.<br>**Which tools for a more efficient**<br>**analysis?**<br>tkJOINTFREQUENCYTABES<br>An|**Variables: continuous and qualitative - frequency table**<br>**Response times to tweets measured on 5 companies.**<br>**Cross tabulation**(portion): joint absolut<br>frequencies of the response times an<br>companies<br>**Time**<br>**Company**<br>**Tot**<br>**Airplane Courier Products Telecom Tour**<br>**713**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**728**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**780**<br>0<br>**2**<br>0<br>0<br>0<br>**2**<br>**795**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**840**<br>0<br>0<br>0<br>0<br>1<br>**1**<br>**855**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**870**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**878**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**893**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**900**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**908**<br>0<br>**2**<br>0<br>**1**<br>**2**<br>**5**<br>**...**<br>...<br>...<br>...<br>...<br>...<br>**...**<br>**3000**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**3043**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**Tot**<br>**100**<br>**100**<br>**100**<br>**100**<br>**100**<br>**500**<br>**Comments?**<br>The**continuous**variable**Time**takes (as<br>expected) a very high number of values;<br>the joint frequencies are very low.<br>The cross-tab is not an effective tool for<br>the analysis of the two variables.<br>**Which tools for a more efficient**<br>**analysis?**<br>tkJOINTFREQUENCYTABES<br>An|**Variables: continuous and qualitative - frequency table**<br>**Response times to tweets measured on 5 companies.**<br>**Cross tabulation**(portion): joint absolut<br>frequencies of the response times an<br>companies<br>**Time**<br>**Company**<br>**Tot**<br>**Airplane Courier Products Telecom Tour**<br>**713**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**728**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**780**<br>0<br>**2**<br>0<br>0<br>0<br>**2**<br>**795**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**840**<br>0<br>0<br>0<br>0<br>1<br>**1**<br>**855**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**870**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**878**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**893**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**900**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**908**<br>0<br>**2**<br>0<br>**1**<br>**2**<br>**5**<br>**...**<br>...<br>...<br>...<br>...<br>...<br>**...**<br>**3000**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**3043**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**Tot**<br>**100**<br>**100**<br>**100**<br>**100**<br>**100**<br>**500**<br>**Comments?**<br>The**continuous**variable**Time**takes (as<br>expected) a very high number of values;<br>the joint frequencies are very low.<br>The cross-tab is not an effective tool for<br>the analysis of the two variables.<br>**Which tools for a more efficient**<br>**analysis?**<br>tkJOINTFREQUENCYTABES<br>An||
|---|---|---|---|---|---|---|---|---|---|---|
||**Response times to tweets measured on 5 companies.**<br>**Cross tabulation**(portion): joint absolut<br>frequencies of the response times an<br>companies<br>**Time**<br>**Company**<br>**Tot**<br>**Airplane Courier Products Telecom Tour**<br>**713**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**728**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**780**<br>0<br>**2**<br>0<br>0<br>0<br>**2**<br>**795**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**840**<br>0<br>0<br>0<br>0<br>1<br>**1**<br>**855**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**870**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**878**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**893**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**900**<br>0<br>**1**<br>0<br>0<br>0<br>**1**<br>**908**<br>0<br>**2**<br>0<br>**1**<br>**2**<br>**5**<br>**...**<br>...<br>...<br>...<br>...<br>...<br>**...**<br>**3000**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**3043**<br>**1**<br>0<br>0<br>0<br>0<br>**1**<br>**Tot**<br>**100**<br>**100**<br>**100**<br>**100**<br>**100**<br>**500**<br>**Comments?**<br>The**continuous**variable**Time**takes (as<br>expected) a very high number of values;<br>the joint frequencies are very low.<br>The cross-tab is not an effective tool for<br>the analysis of the two variables.<br>**Which tools for a more efficient**<br>**analysis?**||||||||||
|||**Time**|**Company**|||||**Tot**|**Cross tabulation**(portion): joint absolut<br>frequencies of the response times an<br>companies<br>**Comments?**<br>The**continuous**variable**Time**takes (as<br>expected) a very high number of values;<br>the joint frequencies are very low.<br>The cross-tab is not an effective tool for<br>the analysis of the two variables.<br>**Which tools for a more efficient**<br>**analysis?**|e<br>d|
||||**Airplane **|**Courier **|**Products **|**Telecom **|**Tour**||||
|||**713**|0|**1**|0|0|0|**1**|||
|||**728**|0|**1**|0|0|0|**1**|||
|||**780**|0|**2**|0|0|0|**2**|||
|||**795**|0|**1**|0|0|0|**1**|||
||||||||||||
|||**840**|0|0|0|0|1|**1**|||
|||**855**|0|**1**|0|0|0|**1**|||
|||**870**|0|**1**|0|0|0|**1**|||
|||**878**|0|**1**|0|0|0|**1**|||
|||**893**|0|**1**|0|0|0|**1**|||
|||**900**|0|**1**|0|0|0|**1**|||
|||**908**|0|**2**|0|**1**|**2**|**5**|||
||||||||||||
|||**...**|...|...|...|...|...|**...**|||
|||**3000**|**1**|0|0|0|0|**1**|||
|||**3043**|**1**|0|0|0|0|**1**|||
|||**Tot**|**100**|**100**|**100**|**100**|**100**|**500**|||
||||||||||||

**34** 

## **Variables: continuous and qualitative – classifying into intervals** 

**Response times to tweets measured on 5 companies.** 

|**Time**<br>**Time**||**Company**<br>**Company**|**Company**<br>**Company**|**Company**<br>**Company**|**Company**<br>**Company**|**Company**<br>**Company**|**Company**<br>**Company**|**Company**<br>**Company**|**Company**<br>**Company**|**Company**<br>**Company**||**ot**<br>**To**|**t**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**Ai**|**rplane **<br>**Airpla**|**Co**<br>**ne**|**urier **<br>**Cou **|**Pr**<br>**ie **|**oducts **<br> **Produ**|**Te**<br>**cts**|**lecom **<br>**Teleco**|**T**<br>**m **|**our**<br> **Tou**|**T**<br>**r**|||
|**713**<br>[600,780)||0<br>0||**1**<br>**2**||0<br>0||0<br>0||0<br>0||**1**<br>|**2**|
|**728**<br>[780,960)||0<br>0||**1**<br>**15**||0<br>0||0<br>**11**||0<br>**3**||**1**<br>**2**|**9**|
|**780**<br>[960,1140|)|0<br>0||**2**<br>**51**||0<br>**16**||0<br>**35**||0<br>**14**||**2**<br>**11**|**6**|
|**795**<br>[1140,132|0)|0<br>0||**1**<br>**27**||0<br>**23**||0<br>**26**||0<br>**34**||**1**<br>**11**|**0**|
|**840**<br>[1320,150|0)|0<br>0||0<br>**4**||0<br>**18**||0<br>**21**||1<br>**34**||**1**<br>**7**|**7**|
|**855**<br>[1500,168|0)|0<br>**1**||**1**<br>**1**||0<br>**14**||0<br>**7**||0<br>**12**||**1**<br>**3**|**5**|
|**870**<br>[1680,186|0)|0<br>**2**||**1**<br>0||0<br>**10**||0<br>0||0<br>**3**||**1**<br>**1**|**5**|
|**878**<br>[1860,204|0)|0<br>**6**||**1**<br>0||0<br>**6**||0<br>0||0<br>0||**1**<br>**1**|**2**|
|**893**<br>[2040,222|0)|0<br>**21**||**1**<br>0||0<br>**7**||0<br>0||0<br>0||**1**<br>**2**|**8**|
|**900**<br><br>[2220,240|0)|0<br>**21**||**1**<br>0||0<br>**4**||0<br>0||0<br>0||**1**<br>**2**|**5**|
|**908**<br><br>[2400,258|0)|0<br>**27**||**2**<br>0||0<br>**1**||**1**<br>0||**2**<br>0||**5**<br>**2**|**8**|
|~~**...**~~<br><br>[2580,276|0)|~~...~~<br>**13**||~~...~~<br>0||~~...~~<br>0||~~...~~<br>0||~~...~~<br>0||~~**...**~~<br>**1**|**3**|
|~~**3000**~~<br><br>[2760,294|0)|~~**1**~~<br>**6**||~~0~~<br>0||~~0~~<br>**1**||~~0~~<br>0||~~0~~<br>0||~~**1**~~<br>|**7**|
|~~**3043**~~<br><br>[2940312|0]|~~**1**~~<br>**3**||~~0~~<br>0||~~0~~<br>0||~~0~~<br>0||~~0~~<br>0||~~**1**~~<br>|**3**|
|,||||||||||||||
|~~**Tot**~~<br>**Tot**||~~**100**~~<br>**100**||~~**100**~~<br>**100**||~~**100**~~<br>**100**||~~**100**~~<br>**100**|~~**1**~~<br>|~~**00**~~<br>**10**|~~**5**~~<br>**0**|~~**00**~~<br>**50**||
|||||||||||||||

Adopting the same approach followed to analyse a continuous variable, it might seem sensible to classify the **Time** variable into intervals, and to build the cross-tab between time in classes and company. 

Equal-width interval classes (180 = 3 minutes) 

## **Comments?** 

**35** 

## **Variables: continuous and qualitative - boxplots side by side** 

# **Response times to tweets measured on 5 companies: comparison of boxplots.** 

## **Comments?** 

_We note that_ _**Airplane** is the company that “generally” has the slowest response time, followed by_ _**Product** , even if the two distributions of response times for these companies are more dispersed compared to the others._ 

_In particular, note that_ _**Airplane** presents a rather symmetric distribution, which partly overlaps with_ _**Product** 's distribution. The latter distribution is skewed to the right; in particular, the median response time - not much higher than that of Courier, Telecom and Tour - is higher than the third quartile of the distributions for Courier and Telecom, and the 25% of the slowest response times are higher than the maximum response times of these 3 companies._ 

**38** 

## **Variables: continuous and qualitative - side by side boxplots** 

# **Response times to tweets measured on 5 companies: comparison of boxplots.** 

## **Comments?** 

_**Courier** is definitely the fastest responding company in a fairly systematic manner, followed as mentioned by Telecom and Tour._ 

_In conclusion, the variable_ **Time** _is associated with the variable_ **Company,** _**as its distribution varies as**_ **Company** _**changes.**_ 

To compare the characteristics of the distributions in a more synthetic way, one can use the summary measures of **Time** conditional on **Company** . 

**39** 

## **Variables: continuous and qualitative - summary measures** 

**Response times to tweets measured on 5 companies: conditional summary measures.** 

|#|**Variables: continuous and qualitative - summary measures**<br>**Response times to tweets measured on 5 companies: conditional summary measures.**<br>**`Summary measures for Time | Company`**<br>**`Summary measures`**<br>**`Company   n n.a`**<br>**`min`**<br>**`q1 median`**<br>**`mean`**<br>**`q3  max`**<br>**`sd`**<br>**`var`**<br>**`Airplane 100   0 1629 2175.75 2370.5 2371.95 2542.25 3043 269.69`**<br>**`72732.43`**<br>**`Courier 100   0  713  998.00 1076.5 1077.32 1163.00 1508 145.52`**<br>**`21176.54`**<br>**`Products 100   0 1038 1215.75 1398.0 1519.72 1764.25 2898 397.37 157905.78`**<br>**`Telecom 100   0  908 1020.00 1148.0 1185.12 1323.75 1673 186.81  34898.53`**<br>**`Tour 100   0  840 1187.25 1313.0 1317.04 1442.00 1785 188.38  35485.72`**<br>**`Requested statistics`**<br>**`Company   n n.a`**<br>**`p10    p90     p95`**<br>**`Airplane 100   0 2090.3 2695.4 2829.45`**<br>**`Courier 100   0  907.2 1231.5 1299.85`**<br>**`Products 100   0 1097.1 2143.9 2299.70`**<br>**`Telecom 100   0  953.0 1448.7 1509.50`**<br>**`Tour 100   0 1077.8 1583.0 1605.40`**<br> APPROACH : Conditional summary measures<br>h<br>conditional summary measures for<br>the variable time<br>in correspondence<br>to<br>the Airplane<br>company|
|---|---|

**40** 

## **Rstudio: distr.plot.xy() & summary.x()** 

The function **distr.plot.xy()** can be used to easily to obtain **side-by-side boxplots:** 

**distr.plot.xy(x,y, plot.type="boxplot",data)** 

Note that as in the case of the boxplot for a single variable, the plot can only be built for **numeric variables** (classification into intervals is not possible). It is clearly not necessary to indicate the frequencies to be plotted as the boxplot is based on the raw data. 

The **distr.summary.x()** function allows to obtain conditional summary measures by specifying, in addition to the arguments already used for the analysis of a single variable, the conditioning variable(s) (no more than 2) using the **by1** and/or **by2** arguments: 

**distr.summary.x(x, by1, by2, stats, digits=2,f.digits=4, data)** 

**41** 

## **Hands on: analysis of tweets** 

**Response times (Time) to tweets measured on 5 companies (Company): syntax used to obtain the results shown in the slides** 

**# original cross-table(INADEQUATE) distr.table.xy(x=Time,y=Company,freq="counts",freq.type="joint", date=Tweets)** 

**# cross-table with Time classified in intervals distr.table.xy(x=Time,y=Company,freq="counts",freq.type="joint", breaks.x=seq(600,3120,by=180),data=Tweets)** 

- **# the syntax to obtain a collection of histograms is not reported # Side-by-side boxplots** 

- **distr.plot.xy(x=Company,y=Time,plot.type="boxplot", data=Tweets) # conditional summary measures (summary reports a collection of stats) distr.summary.x(x=Time,by1=Company,stats=c("summary", "p5","p10","p90","p95"),data=Tweets)** 

**42** 

# **Variables of which one is continuous numeric** 

**Two numeric variables** 

## **Variables: numeric** 

## **House price data in a US city** 

**Joint distribution analysis of price and landValue? And of and or price livingArea rooms?** 

Variables are continuous. It is possible to construct a cross table after classification into intervals, but this would imply an over- **simplification** and compression of data. To analyse the **pairs of values actually observed in** more detail, a **scatterplot is** typically used. 

**45** 

## **Analysis of the relationship between numerical variables** 

In the joint study of two **numerical variables,** we introduced the scatterplot as a graphical tool to describe the relationship between the variables. 

- } **Example.** Price, living area, number of rooms, lot size for houses in a US city 

There is a relationship between the three pairs of variables: as the width of the living area, the number of rooms and the size of the property increase, the price of houses increases, but the intensity of the relationship is different!!! **How to measure and compare the strength of these relationships?** 

**48** 

## **Concordant and discordant value pairs** 

## **House price data in a US city: prices and livingArea** 

**----- Start of picture text -----**<br>
A                                                                       B<br>𝒚<br>C                                                                        D<br>𝒙<br>**----- End of picture text -----**<br>

Based on the **means of the two variables,** we can identify four quadrants in the plot. Quadrants **B** and **C: pairs of concordant values** : cases with values both greater or both less than the mean. 

Quadrants **A** and **D: pairs of discordant values:** cases with values greater than (resp. less than) the mean on one variable and lower than (resp. greater than) the mean on the other variable. 

Two variables are **positively (or directly)** associated if concordant pairs prevail and **negatively (or inversely)** associated if discordant pairs prevail. 

**49** 

## **Cross-products (cross-products)** 

To assess the strength of the relation between two variables, we have to consider both the **direction** of the deviations from the means and their **size** . At this aim, we consider for each case (𝑥�, 𝑦�) its cross-product, i.e. the product of the deviations from the means 

(𝑥� −̄𝑥)(𝑦� −̄𝑦) 

- } The cross-product informs both on the concordance/discordance (sign) of the values observed on the two variables and on the extent of the deviations from the means. 

   - } Cases with a **positive** cross-product are **concordant** : they have both values greater or lower than the means (Panels B and C) 

   - } Cases with **negative** cross-product are **discordant** : the deviations from the means have opposite signs; for one variable the value is above the mean, for the other it is below the mean (Panels A and D). 

- } To  assess whether concordant or discordant pairs prevail, i.e. if between two variables a direct or inverse (or no) relation exists, the average of the cross-products is considered, the so-called **covariance** 

**50** 

## **Covariance: definition for population and for sample** 

The definition of the covariance is slightly different for a population and for a sample } For data measured on the entire **population** the covariance is defined as: 

} The **sample covariance** instead is defined as: 

As seen for the variance, this is not exactly the **average of** the product of the deviations, 𝒏−𝟏 𝒏 _**.**_ The reason for this difference will because the sum is divided by **( )** and not by be explained when discussing about inference, and specifically about estimation 

**51** 

## **The covariance: indirect calculation (shortcut) formula** 

Focusing on the **sample** covariance, we introduce the so-called indirect calculation formula, that can be useful to calculate the covariance in some cases: 

_The covariance can be calculated based on the mean of the products between values and on the product of the means!_ 

We will use this formula only in particular cases, and specifically when the covariance is calculated based on aggregated data 

**52** 

## **The covariance: indirect calculation formula [OPTIONAL]** 

## Focusing on the **sample covariance,** note that: 

## In the case of a **population,** the same reasoning leads to: 

**----- Start of picture text -----**<br>
N<br>N  xi yi<br>1<br>i  1<br> XY   ( xi  X )( yi  Y )   X Y<br>N i  1 N<br>**----- End of picture text -----**<br>

**53** 

## **Covariance** 

**----- Start of picture text -----**<br>
Positive covariance Negative covariance<br>Concordant pairs prevail Discordant pairs prevail<br>Y Y<br>X X<br>**----- End of picture text -----**<br>

**Covariance close to zero No prevalence of concordant or discordant pairs is observed** 

**----- Start of picture text -----**<br>
Y<br>X<br>**----- End of picture text -----**<br>

**54** 

## **Covariance: calculation based on raw data** 

## **Example: calculation of the covariance between price and livingArea based on the first** 𝒏 = 10 houses 

## _The means are_ 

|||**living**<br>**Area**<br>**𝒙𝒊**<br>**906**<br>**1953**||**price**<br>**𝒚𝒊**<br>**132500**<br>**181115**|**price**<br>**𝒚𝒊**<br>**132500**<br>**181115**|(𝒙𝒊−�𝒙) <br>**-714.1**<br>**332.9**|(𝒚𝒊−�𝒚) <br>**542.5**<br>**49157.5**|(𝒙𝒊−�𝒙)(𝒚𝒊−�𝒚)<br>**-387399**<br>**16364532**|_The means are_<br>�𝒙**=(16201/10)=1620.1**<br>�𝒚**=(1319575/10)=131957.5**<br>_The sum of the products of the deviations_||
|---|---|---|---|---|---|---|---|---|---|---|
|||**1944**||**109000**||**323.9 **|**-22957.5**|**-7435934**|_from the means (rounding all intermediate_||
|||**1944**||**155000**||**323.9**|**23042.5**|**7463466**|_results to 2 decimal places) is_**84167938**.||
|||**840**||**86060**||**-780.1 **|**-45897.5**|**35804640**|So :||
|||**1152**||**120000**||**-468.1 **|**-11957.5**|**5597306**|**84167938**||
|||**2752**<br>**1662**||**153000**<br>**170000**||**1131.9**<br>**41.9**|**21042.5**<br>**38042.5**|**23818006**<br>**1593981**|𝑠��=<br>**9**<br>=**9351993**||
|||**1632**||**90000**||**11.9 **|**-41957.5**|**-499294**|**Comments?**||
||**Somma**|**1416**<br>**16201 **||**122900**<br> **1319575**||**-204.1**|**-9057.5**<br>**0**|**1848636**<br>**84167938**|_The covariance is positive: the relationship_<br>||

_The covariance is positive: the relationship between the two variables is_ _**direct** ._ 

**55** 

## **Rstudio: distr.plot.xy() & cov()** 

The scatterplot of two variables can be obtained using the function **distr.plot.xy()** : 

**distr.plot.xy(x,y, plot.type="scatter",data)** 

Note that it is not necessary to specify the frequencies to report in the plot because the scatterplot is built based on raw data. 

The function **cov()** in R returns the covariance between two **numeric variables** using the syntax **:** 

**cov(x, y)** 

Note that _**cannot be**_ **the names of the columns in x, y  are the names of two vectors and they a dataframe** 

**In the case when some data are missing, they can be excluded from computations by specifying that the calculation of the covariance should be based only on cases with complete information on the two variables:** 

**cov(x, y, use="complete")** 

**56** 

## **Hands on: relationship between numerical variables** 

## **Scatterplot: house price and three numerical variables** 

**# scatterplots distr.plot.xy(x=livingArea,y=price,plot.type = "scatter",data=House_Price) distr.plot.xy(x=rooms,y=price,plot.type = "scatter",data=House_Price) distr.plot.xy(x=lotSize,y=price,plot.type = "scatter",data=House_Price)** 

## **The R function cov(x,y) can be used to calculate the covariance** 

- **cov(House_Price$livingArea,House_Price$price) [1] 25617618** 

- **cov(House_Price$rooms,House_Price$price)** 

**[1] 74923.6** 

- **cov(House_Price$lotSize,House_Price$price)** 

- **[1] NA** 

- **cov(House_Price$lotSize,House_Price$price,use="complete")** 

- **[1] 182595271** 

**57** 

## **Analysis of covariances** 

**House price data in a US city:** Price, living area, number of rooms, property size 

**cov = 25617618                                         cov = 74923.6                                      cov = 182595271** 

**Can we conclude that price has the strongest direct relationship with lotSize?** 

_The covariance (as the variance) depends on the_ _**deviations from the means,** and both the means and the deviations depend on the units of measurement of the variables_ _**!**_ 

_Thus, covariance allows to deduce the_ _**direction of the relationship between two variables,** but not to assess the strength of such relationship, since it is an_ _**absolute and not a relative measure!**_ 

**58** 

## **Correlation coefficient** 

_r_ = 0.16 _r_ = 0.49 _r_ = 0.78 _xy xy xy_ As _r_ moves away from 0 _xy_ – (towards 1 or towards 1) the points tend to be more and more  concentrated around a straight line (with positive or negative slope _r_ = 0.16 _r_ = -0.55 _r_ = -0.86 _xy xy xy r_ depending on the sign of ) _xy_ 

**60** 

## **Hands on: relationship between numerical variables** 

## **To calculate the covariance, the R function cor(x,y)(very similar to cor(x,y)) can be used** 

- **cor(House_Price$livingArea,House_Price$price) [1] 0.685806** 

- **cor(House_Price$rooms,House_Price$price) [1] 0.4855333** 

**> # to deal with missing values use="complete" > cor(House_Price$lotSize,House_Price$price,use="complete") [1] 0.2062668** 

**61** 

## **Correlation: some considerations** 

**----- Start of picture text -----**<br>
|||||
|---|---|---|---|
|A|B|
|r|= 0.816|r|= 0.816|
|xy|xy|
|C|D|
|r|= 0.816|r|= 0.816|
|xy|xy|

**----- End of picture text -----**<br>

_**It is important to consider that the correlation in some cases may not be reliable.**_ 

In the 4 cases shown in the plots (Anscombe , 1973), the variables have the same means, variances, covariance and correlation. 

However, the relationship between the variables is very different: 

**Plot A:** the correlation properly reflects the relationship between the variables. **Plot B:** perfect **non-linear** relationship, **Plot C/D:** the value of _**r**_ is influenced _**xy**_ by **extreme values (** outliers) whose 

_r r r_ presence causes a decrease in (Plot C: without the outlier it would be =1) or an increase in _xy xy xy r_ (Plot D: without the  outliers it would be =0) _xy_ 

**62** 

