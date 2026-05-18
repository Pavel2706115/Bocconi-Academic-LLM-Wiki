**==> picture [43 x 165] intentionally omitted <==**

**DESCRIPTIVE STATISTICS: APPLICATIONS AND EXAMPLES** 

**Materials prepared by R. Piccarreta for students of course 30001 / Bocconi University. Distribution - including via the web - without permission is prohibited.** 

## **Case 1: Income in UK by ethnic groups.** 

**UK income data, excluding housing costs (three-year estimates) Focus: assessing the distribution of different ethnicities in 5 income groups (quintiles)** 

**==> picture [350 x 349] intentionally omitted <==**

Plots show the income distribution of individuals in the 5 income quintiles (classes that contain roughly the same percentage of individuals, calculated for the entire population) conditional on ethnicity* (for 2 three-year periods). 

## **Comments?** 

For **White** , a fairly even distribution is observed, reflecting the distribution in the population. However, for the other groups, there is a greater concentration in the lower classes: **modal class and median?** 

**(*) https://www.ons.gov.uk/methodology/classificationsandstandards/measuringequality/ethnicgroupnationalidentityandreligion** 

**2** 

## **Case 1: Income in UK by ethnic groups.** 

**UK income data, excluding housing costs (three-year estimates) Focus: assessing the distribution of different ethnicities in 5 income groups (quintiles)** 

**==> picture [355 x 355] intentionally omitted <==**

A more detailed analysis of the different communities in the four groups shows that the differences are quite relevant. The distribution for **White Non-British** is more concentrated in the lower interval classes (especially in the **Mixed** class). Asian communities are quite heterogeneous. Some communities (Pakistan, Bangladesh) show a strong concentration in the lowest classes, especially in 2008-10 (please note the modal class and the median), with a slight improvement in the following three years. The Indian community shows a relatively even distribution, although with a hint of polarization. This is even more pronounced in the Chinese community, whose distribution is characterized by relatively low frequencies in the middle classes 

**(*) https://www.ons.gov.uk/methodology/classificationsandstandards/measuringequality/ethnicgroupnationalidentityandreligion** 

**3** 

## **Case 2: Vaccination and deaths due to Covid** 

# _**Comparing conditional distributions only makes sense if they are homogeneous with respect to other factors.**_ 

**==> picture [272 x 331] intentionally omitted <==**

Dead NoDead **Tot** Vax 3512 281313 284825 NoVax 24364 2676016 2700380 **Tot** 27876 2957329 2985205 **row Conditional distributions by** Dead NoDead **Tot** Vax **0.0123** 0.9877 1 NoVax **0.0090** 0.9910 1 

## **row Conditional distributions by** 

Example: Consider the number of **covid-19** deaths among vaccinated and unvaccinated (age >= 18) in a given month (in the year 2021, at the beginning of the vaccination campaign) 

The death rate among the vaccinated is higher than among the unvaccinated! 

https://covidactuaries.org/2021/11/22/simpsons-paradox-and-vaccines/ 

**4** 

## **Case 2: Vaccination and deaths due to Covid** 

## **Frequency of death by vaccination status** 

**Number of deaths per 10000 people by vaccination status and age group** 

**==> picture [820 x 156] intentionally omitted <==**

**----- Start of picture text -----**<br>
||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|
|Dead|NoDead|Tot|Vax:|Vax:|(Dead|Vax)*|NoVax:|NoVax:|(Dead|NoVax)*|
|Age|Dead|Tot|10000|Dead|Tot|10000|
|Vax|0.0123|0.9877|1|18-49|19|57154|3.32|541|1366914|3.96|
|-|
|50|59|29|31910|9.09|1225|513202|23.87|
|NoVax|
|0.0090|0.9910|1|
|-|
|60|69|76|18981|40.04|2765|424476|65.14|
|-|
|70|79|381|57210|66.60|5901|303782|194.25|
|-|
|80|89|1760|100091|175.84|8679|73510|1180.66|
|90+|1247|19479|640.18|5253|18496|2840.07|
|Tot|3512|284825|123.30|24364|2700380|90.22|

**----- End of picture text -----**<br>


**For each age group, the percentage of deaths is lower among the vaccinated than among the unvaccinated. However, when age is not considered, the relationship between the two percentages is reversed.** 

This is because: 1) the risk of dying from a covid increases with age 2) the percentage of unvaccinated people is much higher in the lower age groups (also due to decisions to prioritize the elderly in vaccination campaigns) and decreases significantly with age! Considering only aggregate data confuses the "effects" of vaccination and age. 

**5** 

## **Case 2: Vaccination and deaths due to Covid** 

## **Frequency of death by vaccination status** 

**Number of deaths per 10000 people by vaccination status and age group** 

**==> picture [820 x 156] intentionally omitted <==**

**----- Start of picture text -----**<br>
||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|
|Dead|NoDead|Tot|Vax:|Vax:|(Dead|Vax)*|NoVax:|NoVax:|(Dead|NoVax)*|
|Age|Dead|Tot|10000|Dead|Tot|10000|
|Vax|0.0123|0.9877|1|18-49|19|57154|3.32|541|1366914|3.96|
|-|
|50|59|29|31910|9.09|1225|513202|23.87|
|NoVax|
|0.0090|0.9910|1|
|-|
|60|69|76|18981|40.04|2765|424476|65.14|
|-|
|70|79|381|57210|66.60|5901|303782|194.25|
|-|
|80|89|1760|100091|175.84|8679|73510|1180.66|
|90+|1247|19479|640.18|5253|18496|2840.07|
|Tot|3512|284825|123.30|24364|2700380|90.22|

**----- End of picture text -----**<br>


**Simpson's paradox:** When groups are **aggregated** (in this case, when age group is not taken into account), relationships between frequencies conditional on specific groups (in this case, relationships between death rates between vaccinated and unvaccinated by age group) may or even **reverse** . **disappear** 

Comparing conditional distributions only makes sense if they are homogeneous with respect to possible confounding factors, which the researcher must necessarily identify and keep under control. 

**6** 

## **Case 3: Employee evaluation** 

The following variables (dataframe **`Ability_Performance`** in file **`Lesson 10_Data.Rdata`** ) are collected on consultants of an agency: **Manager** : rating of the consultant given by the manager in charge (relative index) and **Performance** : rating based on the time it took to complete the last assigned task (the shorter the time, the better the performance) and the quality of the work done. **What conclusions can we draw about the relationship between the two variables?** **`distr.plot.xy(x=Manager,y=Performance,plot.type = "scatter", fitline = TRUE,data=Ability_Performance) cor(Ability_Performance$Manager,Ability_Performance$Performance)`** 

**==> picture [406 x 205] intentionally omitted <==**

Corr. = -0.7405955 **Should we conclude that managers are incapable of rating their team members?** 

**7** 

## **Case 3: Employee evaluation** 

## **Considerations?** 

- } A manager will typically assign the most difficult tasks to the employees he/she thinks are best at the job, who will need more time to complete the task than other employees assigned to simpler tasks. 

- } Thus, the difficulty of the assigned task could be related to both the employee's ability and . 

- performance, and therefore could act as a **confounding variable** 

- } It is necessary to assess the relationship between ability and performance taking into account (or controlling for) the difficulty of the task. 

**8** 

## **Case 4: Burglary and Employment in the U.S.** 

The **`Burglary.US`** dataframe contains data on the number of arrests for burglary ( **`Burglary_Arrest`** ), and the number of Employed and Unemployed people, ( **`Employed`** and **`Unemployed`** variables) for some US counties. Calculate and comment on the correlation between **`Burglary_Arrest`** and **`Employed`** 

```
> cor(Burglary.US$Employed,Burglary.US$Burglary_Arrests)
[1] 0.8770944
```

_The correlation is very high and positive. Before making comments, let us analyze the scatterplot_ 

```
distr.plot.xy(x=Employed_Pop,
              y=Burglary_Pop,
              plot.type = "scatter",
              fitline = TRUE,
              data=Burglary.US)
```

_The relationship is direct, but the high correlation is due to the presence of two outliers_ 

**==> picture [381 x 192] intentionally omitted <==**

**9** 

## **Case 4: Burglary and Employment in the U.S.** 

## We re-evaluate the correlation by removing outliers 

- **`Burglary.Reg<-Burglary.US[Burglary.US$Employed<2000000,]`** 

- **`distr.plot.xy(x=Employed,y=Burglary_Arrests,plot.type = "scatter",`** 

```
+               fitline = TRUE, data=Burglary.Reg)
```

- **`cor(Burglary.Reg$Employed,Burglary.Reg$Burglary_Arrests) [1] 0.6736751`** 

**==> picture [460 x 233] intentionally omitted <==**

**Can we conclude that the number of arrests for burglary increases with employment?** _The observed results suggest that counties with more employed people have more thefts: a causal relationship cannot be inferred. In fact, both variables depend_ _**on the size of the population** , which may explain this counterintuitive result._ 

**10** 

## **Case 4: Burglary and Employment in the U.S.** 

We evaluate the relationship between the two variables by removing the possible effect of population size by considering the number of arrests per capita and the percentage of the population that is employed. 

- **`Burglary.US$Pop<-Burglary.US$Unemployed+Burglary.US$Employed`** 

- **`Burglary.US$Burglary_Pop<-Burglary.US$Burglary_Arrests/Burglary.US$Pop > Burglary.US$Employed_Pop<-Burglary.US$Employed/Burglary.US$Pop`** 

- **`distr.plot.xy(x=Employed_Pop,y=Burglary_Pop,plot.type = "scatter",`** 

- **`+             fitline = TRUE,data=Burglary.US)`** 

- **`cor(Burglary.US$Employed_Pop,Burglary.US$Burglary_Pop)`** 

- **`[1] -0.3831735`** 

**==> picture [386 x 196] intentionally omitted <==**

_Looking at the normalized variables, taking population into account, the relationship is_ _**weaker and negative** , a more reasonable result (in line with expectations)!_ 

_Counties with a higher proportion of employed people have, on average, fewer thefts per capita, although the relationship is not particularly strong, as thefts certainly depend on other factors as well!_ 

**11** 

## **Case 5: Police and violent crime in the U.S.** 

The **`Police_Crime`** dataframe contains information on U.S. per capita expenditures on police personnel, **`Police`** , reported violent crimes ( **`Assault` ,** **`Rape` ,** **`Murder` ,** and **`ViolentCrime`** , related to population), region, and level of urbanization (%). 

What is the relationship between investment in law enforcement and crime? 

- **`cor(Police_Crime$Police,Police_Crime$Assault) > NA`** 

- **`cor(Police_Crime$Police,Police_Crime$Assault,use="complete") [1] 0.4336887`** 

- **`cor(Police_Crime$Police,Police_Crime$Rape,use="complete") [1] 0.4920527`** 

- **`cor(Police_Crime$Police,Police_Crime$Murder,use="complete") [1] 0.1091262`** 

- **`cor(Police_Crime$Police,Police_Crime$ViolentCrime,use="complete") [1] 0.4415267`** 

**12** 

## **Case 5: Police and violent crime in the U.S.** 

## **What relationship between investment in law enforcement and crime?** 

```
distr.plot.xy(x=Police,y=Assault,plot.type = "scatter", fitline = TRUE,
              data=Police_Crime) # same syntax for other variables
```

**==> picture [306 x 155] intentionally omitted <==**

**==> picture [306 x 154] intentionally omitted <==**

**==> picture [306 x 155] intentionally omitted <==**

**==> picture [306 x 155] intentionally omitted <==**

**Does an increase in the number of police officers increase the number of crimes?** 

**13** 

## **Case 5: Police and violent crime in the U.S.** 

## **Considerations?** 

- } First, the existence of a linear relationship does not imply a **causal relationship** , but rather suggests that states that invest more in police personnel tend to be states with higher crime rates. 

- } The "cause-and-effect" relationship may be **reversed** : states with high crime rates will tend to increase the presence of police personnel. 

- } It could also be that as spending on police personnel increases, the number of police officers and/or their efficiency increases, and the number of reported crimes also increases. 

- } States with higher police spending may be **wealthier states** , states with **higher income concentration** , or states with **more populous metropolitan areas** . In these states, costs or investments may be higher, and so may be the number of crimes. All these variables could therefore act as **confounding variables** , and their possible effects on police spending and crime should be taken into account before drawing conclusions. 

**14** 

## **Case 5: Police and violent crime in the U.S.** 

## **Possible relationship with level of urbanization** 

```
distr.plot.xy(x=UrbanPop,y=Police,plot.type = "scatter", fitline = TRUE,
              data=Police_Crime) # same syntax for other variables
```

**==> picture [305 x 155] intentionally omitted <==**

**==> picture [305 x 155] intentionally omitted <==**

**==> picture [305 x 155] intentionally omitted <==**

**==> picture [305 x 155] intentionally omitted <==**

**15** 

## **Case 6: Followers and Engagement** 

In social marketing, it is important to choose influencers you trust to spread the word about your products. Do you expect a direct correlation between the number of followers and engagement (likes, comments, shares)? 

The **`Followers`** dataframe presents the results of a study that measured an **`Engagement`** index (ranging between 0 and 10) for advertising posts related to similar products (cosmetics) published by influencers with different numbers of **`Followers`** (in thousands). Does the data support expectations?* 

Cor = 0.595 

_The positive and quite relevant correlation is consistent with the idea that relying on influencers with a large number of followers is the best marketing strategy. However, the graph shows that the relationship between the two variables is not linear! Some authors point out that it is difficult to actively interact with a large number of followers (e.g., respond to comments), and other studies show that a very large number of followers is associated with reduced trust in the influencer. So engagement increases at a decreasing rate as the number of followers increases!_ 

**==> picture [403 x 244] intentionally omitted <==**

* Syntax in the R script 

**16** 

## **Case 7: Gender and Salary** 

The **`Managers_Salary`** dataframe contains data on 100 managers from a large company in the U.S.: **`Salary`** (salary), **`Gender`** (gender), **`Education`** (education level), and **`Experience`** (years of **an** work experience). The company claims that it always had _**equal pay for equal work**_ **policy.** Compare salary distributions by gender, using graphical tools and summary measures*. 

```
> Summary measures for Salary | Gender
Requested statistics
 Gender  n n.a   min   p10    q1    mean median       q3    p90    max      sd  cv
 Female 38   0 30200 47187 57315 76188.9  78690  93742.5 101071 129790 22770.8 0.3
   Male 62   0 20860 67990 80650 97832.1  92965 115367.5 134287 175760 29375.4 0.3
```

**==> picture [318 x 193] intentionally omitted <==**

## **Can we conclude that there is discrimination?** 

_The results obtained show a difference in wage levels, with all statistics for "Male" being higher than those for "Female." However, wage differences could be related to other characteristics, such as education and/or work experience_ 

* Syntax in the R script 

**17** 

## **Case 7: Gender and Salary** 

## Compare the distributions of the level of education ( **`Education`** ) by gender. What considerations? 

```
# Let’s build a factor to order the education levels.
Managers_Salary$Education.F<-factor(Managers_Salary$Education,
                                    levels=c("College","Bachelor","Graduate",
"Post-Graduate"))
distr.table.xy(x=Gender,y=Education.F,freq="prop",freq.type = "y|x",
               data=Managers_Salary)
distr.plot.xy(x=Gender,y=Education.F,freq="prop",freq.type = "y|x",
              plot.type="bars",bars.type="stacked",data=Managers_Salary)
```

```
y|x: Proportions
        Education.F
Gender   College Bachelor Graduate Post-Graduate TOTAL
  Female    0.11     0.42     0.32          0.16  1.00
  Male      0.11     0.48     0.37          0.03  1.00
```

**==> picture [105 x 14] intentionally omitted <==**

**----- Start of picture text -----**<br>
Comments?<br>**----- End of picture text -----**<br>


**==> picture [292 x 177] intentionally omitted <==**

**18** 

## **Case 7: Gender and Salary** 

Compare the distributions of work experience( **`Experience`** ) by gender. What considerations?* 

```
Summary measures for Experience | Gender
Requested statistics
 Gender  n n.a min q1  mean median q3 max   sd   cv
 Female 38   0   1 10 12.08   11.5 15  23 4.62 0.38
   Male 62   0   5 14 16.98   16.0 20  36 5.51 0.32
```

**==> picture [358 x 217] intentionally omitted <==**

## **Comments?** 

_In terms of education, women tend to have higher levels of education (higher percentage of women in management positions who have a postgraduate degree), whereas men tend to have more work experience, which may be related to the salary._ 

* Syntax in the R script 

**19** 

## **Case 7: Gender and Salary** 

Can the observed differences between male and female managers in terms of education and work experience explain the observed salary differences? 

**==> picture [282 x 170] intentionally omitted <==**

**==> picture [286 x 173] intentionally omitted <==**

## **Comments?** 

_Salary is mainly related to work experience, and male managers have more experience on average._ 

**==> picture [286 x 174] intentionally omitted <==**

_Salary is also related to education level. However, work experience is more important (i.e. even highly educated but inexperienced managers have lower average salaries). Thus, the gender pay gap observed in_ _**this company** is due to other factors._ 

_**However, studies show that in general, when comparing the salaries of men and women with identical backgrounds, there is a gender gap in salaries!**_ 

* Syntax in the R script 

**20** 

## **Some final remarks** 

- } Two variables may be correlated (or associated) or uncorrelated (or not associated) due to the effect of other variables (confounding factors). To properly assess the relationship between two variables, it is necessary to take into account (or under control) the variables (if any) that **may influence** the relationship (at this aim we will introduce **multiple regression** in the last part of the course). 

- } In general, a high correlation between two variables does not imply that one variable has a causal effect on the other. Correlation measures the strength of the linear relationship between two variables. Causality exists when one event is the direct result of another, regardless of whether there is a linear relationship. 

- } https://www.tylervigen.com/spurious-correlations contains several examples of spurious relationships between variables; even if it is based on the relationship between time series -- data collected over time-- it gives a very clear idea of the risks involved in inferring relationships, and in particular causal relationships, on the basis of a linear relationship, [which may - also - be due to the existence of factors influencing both the considered variables]. 

- } In addition, as noted above, an average-to-high correlation does not always reflect a linear relationship [and may be affected by the presence of outliers]. 

**21** 

