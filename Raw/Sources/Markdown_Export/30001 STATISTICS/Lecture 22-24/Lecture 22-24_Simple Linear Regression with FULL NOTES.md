## **SIMPLE LINEAR REGRESSION** 

**Material prepared by R. Piccarreta for students on course 30001 / Bocconi University. Distribution - even via the web - without authorisation is prohibited.** 

## **Motivation [READING]** 

In many cases it is necessary to make decisions, assess scenarios, define business strategies or political actions under conditions of uncertainty. 

Such decisions are often based on the (hypothesised) relationship between a variable of interest and one or more variables supposedly linked to it. 

 After assessing the relationship between sales and expenditure on advertising on TV, radio and social media, the marketing manager of a company can use this relationship to predict sales given certain levels of advertising expenditure in the different media. 

- The relationship between electricity demand and daytime temperatures can be used to predict next month's electricity use from daytime temperature forecasts 

**2** 

## **Regression analysis** 

Regression analysis is a statistical procedure aimed at determining, on the basis of an – appropriate set of (sample) data, an equation that describes or, better, **estimates** - the relationship between variables, and specifically the relationship between 

 a **dependent variable (or response variable** ) - conventionally denoted _**Y** -_ that one is interested in explaining/predicting as a function of 

 one or more **independent (or explanatory) variables** - denoted by , 𝑿1[,] 𝑿2[,] … , 𝑿𝑃 

We start considering the **simple regression model,** i.e. the case when 

 the dependent variable _**Y**_ **must be explained/predicted on** the basis of a **single** explanatory variable, 𝑿. 

 _**Y**_ and 𝑿 are both numerical 

**3** 

## **Simple linear regression model for the population [READING]** 

**Example.** A financial advisory firm has set up an online advisory service and, on an experimental basis, has started an online chat service for its clients, where they exchange ideas or information on investments. Given the success of the initiative, the company is considering selling advertising space (banners) to other companies. 

Certainly, crucial aspects concern the number of active users, the possible evolution of the number of users over time, etc. 

However, it is of interest to start analysing the characteristics of the users, and to study the relationship between the time spent on chat and some socio-demographic characteristics, in order to provide companies interested in purchasing advertising spaces with information on the characteristics of the users who use the chat the most, in order to assess whether or not the platform's users are on target. 

**4** 

## **The simple linear regression model for the population** 

Given the target group of a specific set of companies, we are interested in studying the relationship between age and time spent chatting by focusing on users under 60 years of age. It is considered reasonable to **assume** that: 

- **Time spent on chat** depends (also) on age 

– The relationship between **time spent on chat** and **age** is direct. 

- The relationship between **time spent on chat** and **age,** at least with reference to the focal age group, is linear. 

These assumptions imply that **there is a linear model** linking **time spent on chat** to **age** 

**5** 

## **The simple linear regression model for the population** 

Linear model describing the relationship between the dependent variable and the values of the explanatory variable in the population ( **deterministic** component) 

**Time (** _**Y**_ **) (minutes)** 

**Base:** 𝛃0 

**----- Start of picture text -----**<br>
𝑥<br>𝛃0 [+ ] 𝛃1<br>**----- End of picture text -----**<br>

**Age in years (** 𝑿 **)** 

**6** 

## **The simple linear regression model for the population** 

A **probabilistic component is** added to the linear model, to describe the different values taken by the dependent variable corresponding to the same value of the explanatory variable 

**Time (** _**Y**_ **) (minutes) Baseline:**  **0** 

**----- Start of picture text -----**<br>
Consider users aged<br>𝑥<br>𝛃0 [+ ] 𝛃1<br>described by  Y ).<br>mean<br>with different ages.<br>an  erratic<br>model.<br>**----- End of picture text -----**<br>

Consider users aged **40** : the time on chat of these users will be different (random, described by _Y_ ). 

The linear model can only describe the **mean** _Y_ for users (or expected value) of with different ages. 

Since, given a certain age, the time spent on chat by different users **varies in a** nondeterministic and unpredictable manner, an **erratic** component is added to the model. 

**Age in years (** 𝑿 **)** 

**40** 

**7** 

## **The simple linear regression model for the population** 

The simple linear regression model of a random variable _**Y**_ given a specific value of the explanatory variable is defined as: 

= _**Y**_ 𝒙 + 𝛆 𝛃𝟎 **[+ ]** 𝛃𝟏 

_**Y**_ **= dependent variable (** _**random**_ **)** 

𝒙 **= value taken by the independent variable (** _**deterministic, known**_ **)** 

𝛃𝟎 **[ , ]** 𝛃𝟏 **[ = intercept and slope of the linear model]** 𝛆 **= error (** _**random**_ **)** 

**8** 

## **The simple linear regression model for the population** 

## Simple linear regression model: 

= _**Y**_ 𝒙 + 𝛆 𝛃𝟎 **[+ ]** 𝛃𝟏 

**----- Start of picture text -----**<br>
Linear positive  Linear negative  No linear<br>relationship  relationship  relationship<br>Y Y Y<br> 0<br> 1 >0  1 <0  1   0<br> 0<br> 0<br>𝑿 𝑿 𝑿<br>**----- End of picture text -----**<br>

**9** 

## **The simple linear regression model for the population** 

Although it is assumed that a linear relationship exists between two variables at the population level, the **parameters** 𝛃𝟎[and] 𝛃𝟏 **[ in the regression model ]**[are ] **[unknown]**[. ] **Sample data are therefore used to** 

 **Estimate** the parameters of the linear model 

 Analytically **describe** the linear relationship between the dependent variable and the explanatory variable  **Predict** the dependent variable based on the observed values of the explanatory variable using the estimated model 

**10** 

## **The simple linear regression model: sample data [READING]** 

- **Simple linear regression model for the population:** 

= _**Y**_ 𝛃𝟎 **[+ ]** 𝛃𝟏𝒙 + 𝛆 with 𝛃𝟎[,] 𝛃𝟏 **not known** 

- **Simple linear regression model for the units in a random sample** 

= = _**Y**_ 𝒊 𝛃𝟎 **[+ ]** 𝛃𝟏𝒙𝒊 + 𝛆𝒊 𝒊 𝟏, … , 𝒏 

where: 

𝒙[sample observation] 𝒊 **[ = ]**[value of the independent variable measured on the ] _[i]_[-th] _**Y**_ **=** _**x i**_ random value of the dependent variable corresponding to _**i**_ 𝛆 **[= ]**[deviation of ] _**[Y]**_ 𝒊 _**i**_[ from the linear model (] **[random quantity]**[)] 

**11** 

## **Linear model estimation: procedure [READING]** 

To estimate the linear model, we should: 

- ෡ ෡ 

- Propose **appropriate estimators** 𝛃𝟎 and 𝛃𝟏 for the unknown parameters, 𝛃0[ and] 𝛃1 

- Use the sample data, (𝒙𝟏, 𝒚𝟏[), ..., (] 𝒙𝒏, 𝒚𝒏[) to obtain the ] **[estimates,]** 𝒃𝟎 and 𝒃𝟏 , i.e. the ෡ ෡ 

- realisations of and 𝛃𝟎 𝛃𝟏[ based on the observed sample.] 

The procedure we follow to introduce the estimators used is slightly different: 

- We consider the **sample data** and introduce the **least squares** approach to derive the parameters 𝒃𝟎 and 𝒃𝟏[of the ] **[regression line ]**[that ] **[best interpolates the sample data ]**[and ] introduce criteria to assess the quality of this line for the observed data 

- We define the **least squares estimators** by generalising the estimates obtained on an observed sample to a random sample 

- We study the **properties** of the **least-squares estimators** under appropriate assumptions 

**12** 

## **The regression line** 

**Study of the relationship between time on chat and age (in years):** on a sample of 96 users, information on certain socio-demographic characteristics is collected by telephone interview and the time (in minutes) spent on the site in a certain period is recorded from the site log data **Scatterplot:** 

**At the sample level (descriptive), there is a relationship between the two variables, certainly a direct one. The linear approximation seems acceptable** 

**13** 

## **The regression line: the least squares approach** 

**Which line describes at best the linear relationship between two variables?** The **least squares approach** identifies the line that **cuts the data at best** Consider a sample of data and a **generic straight line** with intercept 𝑏0∗ and slope 𝑏1∗ For a sample observation 𝑥 characterised by 𝑖, 𝑦𝑖 𝒚𝒊 consider ∗ ∗ ො𝑦[∗] = 𝑏0∗ + 𝑏1∗𝑥  the prediction ො𝑦𝑖∗ 𝑒 𝑖 = (𝑦𝑖 −ො𝑦𝑖 )  the deviation between the observed value and the value ∗ ∗ − on the line, 𝑒𝑖 = 𝑦𝑖 ො𝑦𝑖 Among all the possible straight ∗ = 𝑏∗ + 𝑏∗𝑥 ො𝑦𝑖 0 1 𝑖 lines, we choose the one **minimising the sum of the squared errors** 𝒙 𝒊 

**14** 

## **The regression line: the least squares approach** 

For each sample observation 

𝑥 observed value of 𝑿 𝑖 

value of _**Y**_ observed at 𝑿= 𝑥 𝑖 

𝑦𝑖 𝑖 ∗ ∗ ∗ ො𝑦𝑖 = 𝑏0[+ ][𝑏] 1𝑥𝑖 prediction of _**Y**_ corresponding to 𝑿= 𝑥𝑖 using a straight line with intercept 𝑏0∗ and slope 𝑏1∗ 

Consider the sum of the squared differences between the observed values 𝑦1, 𝑦2, … , 𝑦𝑛 and the ∗ ∗ ∗ predictions ො𝑦1, ො𝑦2, … , ො𝑦𝑛, i.e. the Sum of Squared Errors: 𝑛 𝑛 ∗ 2 ∗ ∗ 2 𝑺𝑺𝑬[∗] −𝑏 −𝑏 𝑥 (𝑦𝑖 −ො𝑦𝑖 ) (𝑦𝑖 0 1 𝑖 ) = ෍ = ෍ 𝑖=1 𝑖=1 

We find the line that cuts the data at best by determining the coefficients minimising the sum of the squared differences between the observed and the predicted values 

**15** 

## **The regression line: the least squares approach** 

The coefficients that minimise the sum of the squared differences between the values observed on the dependent variable and the predictions obtained using a straight line can be determined by setting the partial derivatives equal to zero and solving the equations, obtaining: 

**16** 

## **The regression line** 

**Study of the relationship between time on chat and age.** Assume that the sample statistics calculated from the collected data are:ഥ𝑥= 39.4792, ത𝑦= 809.1354, 𝑠𝑥[2] = 88.06, 𝑠 = 30237.95, 𝑟 = 0.79 . What are the coefficients of the regression line? 𝑦[2] 𝑥𝑦 We can determine them 'by hand', using a calculator or using R as a calculator*: 

2 2 𝑠 = 𝑟 𝑠 𝑠 = 0.79 88.06 ∙30237.95 = 1289.118 𝑥𝑦 𝑥𝑦 𝑥 𝑦 𝑏 = 𝑠 𝑠 14.6391 1 𝑥𝑦/ 𝑥[2] = 1289.118/88.06 = = 𝑏0 ത𝑦−𝑏1 ∙ҧ𝑥= 809.1354 −14.6391 ∙39.4792 = 231.1954 

**The equation of the line (rounding intermediate and final results) is:** 

= 𝟐𝟑𝟏. 𝟐𝟎+ 𝟏𝟒. 𝟔𝟒∙𝒙 ෝ𝒚𝒊 𝒊 

- For the commands to obtain results using R see the script 

**18** 

## **Interpretation of the regression line** 

No data **Estimated intercept,** 𝒃𝟎 ෝ𝒚𝒊 = 𝟐𝟑𝟏. 𝟐𝟎+ 𝟏𝟒. 𝟔𝟒∙𝒙𝒊 **Estimated slope,** 𝒃𝟏 **. Please note:** 𝒃𝟎 **cannot be interpreted as 'time spent For each additional year of age, based on chat by subjects aged 0'. There is no information on the regression line, time spent on on subjects aged less than 20 (no predictions should chat is 'expected' to increase on average be obtained corresponding to values outside the by** 𝒃𝟏 **= 14.64 minutes (approximately, range of** 𝑿 **). rounded coefficient)** 

**19** 

## **Evaluation of the simple regression model [READING]** 

The least squares approach leads to the identification of the best line (with reference to the sum of the squared errors), _**regardless of whether there is a relationship between the two variables or not**_ . 

- It is therefore important to assess the adequacy of the model, i.e. the ability of the data collected on the explanatory variable to explain/recover the values observed on the dependent variable by means of a linear model based on the considered explanatory variable. 

 To assess the goodness of fit of the regression line, we can refer at the sum of the squared **errors** , 𝑺𝑺𝑬 , i.e. the sum of the squared differences between the observed values and those predicted using the regression line: 

**Note: the mean of the residuals from the estimated least-squares model is 0 (the regression line cuts the data at best by balancing positive and negative deviations from the line)** 

**20** 

## **The sum of squared errors, SSE** 

**In this case the sum of the squared deviations of all the observed data (on the dependent variable, time) from the line is*:** 

𝑺𝑺𝑬= 𝟏𝟎𝟕𝟗𝟖𝟏𝟐 

Since no assumptions were made about the amount of dispersion in data, it is difficult to evaluate 𝑺𝑺𝑬 (as it was difficult to evaluate the value taken by the variance!), because it is an absolute measure whose value _**also**_ depends on the unit of measurement of the dependent and explanatory variables. To assess the fit of the model, we therefore introduce a **relative** measure 

* We will see later how the SSE can be calculated based on the available data 

**21** 

## **Goodness of fit of the regression line** 

The 𝑺𝑺𝑬 is an **absolute measure** , whose value also depends on the units of measurement of the dependent variable and the explanatory variable. 

To derive a **relative** measure (with a clear and well-defined range of variation), we introduce:  The **Total Sum of Squares (** 𝑺𝑺𝑻 ), the sum of the squared deviations of the observed values 𝑦1, 𝑦2, … , 𝑦𝑛 from their mean, ത𝑦 

𝑛 (𝑦𝑖 −ത𝑦)[2] **???** 𝑺𝑺𝑻= ෍ = (𝑛−1)𝑠𝑦[2] 𝑖=1  The sum of the **squares of the regression (** 𝑺𝑺𝑹 ), the sum of the squared deviations of the predictions ො𝑦1, ො𝑦2, … , ො𝑦𝑛 from the mean of the dependent variable 

𝑛 𝑺𝑺𝑹 (ො𝑦𝑖 −ത𝑦)[2] = ෍ 𝑖=1 

**22** 

## **The sum of the total sum of squares, SST** 

_**x**_ **=55; =1378** _**y**_ ഥ𝒚= 𝟖𝟎𝟗. 𝟏𝟒 

What if we were to predict the time spent on chat based only on the values taken by the dependent variable? 

We would use the average of the observed values (809.1354) The 𝑺𝑺𝑻 therefore gives an indication of the quality of the **mean** as a predictor of the dependent variable i.e. the fit of a straight line without a slope!!! 

**23** 

## **Decomposition of the total sum of squares** 

**----- Start of picture text -----**<br>
By referring to a single case, there<br>=  𝒃 +  𝒃 𝒙<br>ෝ𝒚 𝟎 𝟏<br>is a relationship between the<br>deviations.<br>ത𝑦<br>ෝ ഥ<br>−<br>𝒚𝒊 𝒚<br>𝒚𝒊 −ഥ𝒚<br>𝒚𝒊 −ෝ𝒚𝒊<br>𝑦𝑖<br>What happens when we consider<br>the sums of these deviations<br>**----- End of picture text -----**<br>

By referring to a single case, there is a relationship between the deviations. 

What happens when we consider the sums of these deviations squared? 

**----- Start of picture text -----**<br>
𝑥𝑖<br>**----- End of picture text -----**<br>

**24** 

## **Decomposition of the total sum of squares** 

The following relationship can be proven between the sums of squares for 𝑛 observations: 

**Total sum of squares (Dispersion of** 𝑦𝑖 **)** 

**Regression sum of squares (Dispersion explained by the line)** 

**Error sum of squares (Dispersion not explained by the line)** 

𝑺𝑺𝑻 **=** 𝑺𝑺𝑹 **+** 𝑺𝑺𝑬 

**----- Start of picture text -----**<br>
𝑛<br>(𝑦𝑖 −ത𝑦) [2]<br>𝑺𝑺𝑻= ෍<br>𝑖=1<br>=<br>𝑛<br>𝑺𝑺𝑹 (ො𝑦𝑖 −ത𝑦) [2]<br>= ෍<br>𝑖=1<br>+<br>𝑛<br>𝑺𝑺𝑬<br>(𝑦𝑖 −ො𝑦𝑖) [2]<br>= ෍<br>𝑖=1<br>**----- End of picture text -----**<br>

**25** 

## **The coefficient of determination** 

By comparing 𝑺𝑺𝑬 (or 𝑺𝑺𝑹) with its maximum value (𝑺𝑺𝑻), one can define a relative measure of the **goodness of fit of** the regression line, the so-called **coefficient of determination** : 

𝑺𝑺𝑹 𝑺𝑺𝑬 = 𝑹[𝟐] 𝑺𝑺𝑻[= 1 −] 𝑺𝑺𝑻 

𝟐 𝑹 measures the proportion of the variation in the dependent variable explained by the regression line, and since 𝑺𝑺𝑻 = 𝑺𝑺𝑬 + 𝑺𝑺𝑹 , it takes on values between 0 and 1. 

 𝑹[𝟐] = 𝟏 : The line perfectly explains the dependent variable (perfect linear relationship): 𝑺𝑺𝑬 =0 : there are no prediction errors and the data are perfectly linearly aligned 

 𝑹[𝟐] = 𝟎 : The line does not improve at all the prediction of the dependent variable compared to the mean. 

𝑺𝑺𝑹 =0: the regression line coincides with a line with zero slope and intercept equal to t ~~he~~ mean of the dependent variable 

𝟐 𝑹 seems strongly related to the **strength of** the **linear relationship** between the two variables. This is no coincidence: in fact, it can be shown that **in the case of simple linear regression** 𝑹[𝟐] 𝟐 coincides with the **squared linear correlation coefficient** 𝒓 𝒙𝒚 

**26** 

## **The coefficient of determination** 

## Note that: 

**----- Start of picture text -----**<br>
Since:<br>**----- End of picture text -----**<br>

𝑺𝑺𝑹 𝑺𝑺𝑬 𝟐 = 𝑹[𝟐] 𝑺𝑺𝑻[= 1 −] 𝑺𝑺𝑻[= 𝒓][𝒙𝒚] 𝑺𝑺𝑻= (𝑛−1)𝑠𝑦[2] 

it is 

Given the line, 𝑺𝑺𝑹 increases as the variance of the explanatory variable increases! 

**27** 

## **The coefficient of determination** 

**Study of the relationship between time on chat and age Assess the goodness of fir of the estimated regression model:** 

ෝ = 𝟐𝟑𝟏. 𝟐𝟎+ 𝟏𝟒. 𝟔𝟒∙𝒙 𝒚𝒊 𝒊 

𝟐 𝟐 𝑟 = 0.79 →𝑹[𝟐] = 𝒓 = 𝟎. 𝟕𝟗 = 𝟎. 𝟔𝟐𝟒𝟏 𝑥𝑦 𝒙𝒚 

_The 62% of the variation in time spent on chat is explained by age (thus, the time spent on chat changes depending on the user’s age)_ 

_The remaining 38% is not explained by the model._ 

_Age explains the 62% of the variability of the time on chat._ 

* For the commands to obtain results using R see the script 

**28** 

## **Simple linear model: from sample to population [READING]** 

**Study of the relationship between time on chat and age** At the sample level, we determined the regression line 

𝒚ෝ𝒊 = 𝟐𝟑𝟏. 𝟐𝟎+ 𝟏𝟒. 𝟔𝟒∙𝒙𝒊,  characterised by 𝑹[𝟐] = 𝟎. 𝟔𝟐𝟒𝟏 

The line and its explanatory ability were determined on the basis of a specific **sample** . How can these results be extended to the **population** ? 

To evaluate the model with reference to the population, we must consider that the coefficients of the line are obtained by referring to a specific sample. In order to make inference about the linear model in the population, it is necessary to explicitly take into account the **sample variability,** thus defining **statistics** that can be used as **estimators or as test statistics** and allow for inference 

**29** 

## **Regression model: least-squares estimators [READING]** 

In order to estimate the coefficients of the linear model in the **population** , we propose the **least-squares estimators** obtained by substituting the specific sample observations, 𝑦1, 𝑦2, … , 𝑦𝑛 **, with the random sample observations** _Y_ 1, _Y_ 2, … , _Y_ 𝑛, which describe the - random - measurements observed on a **generic random sample of values of the dependent variable** corresponding to the values observed on the explanatory variable, 𝑥1, 𝑥2, … , 𝑥𝑛 **:** 

that is the random error, ε 

**30** 

# **Simple regression Weak and strong assumptions and inference on the linear model parameters** 

## **Weak assumptions** 

The error term is a r. v. with **expected value equal to zero** : 𝐸 ε𝑖 = 0  for each 𝑖 

_Y_ 𝑥 for each 𝑖 𝑖 𝐸( 𝑖)) = β0 + β10 + β1 + β11 𝑖 

_Y_ 𝑥+ ε _Y_ 𝑥 for each 𝑖 𝑖 = β0 + β1 𝐸( 𝑖)) = β0 + β10 + β1 + β11 𝑖 Thus, the information on 𝑿 makes it possible to explain the **expected values** of _Y_ 𝑖 (but **not** the specific realisations _Y_ 𝑖) and there are no other factors that systematically influence 𝐸( _Y_ 𝑖) _Y x_ 𝑬( 3) β0 + β1 3 **The expected value of** _**Y**_ **varies** 𝑿 **. linearly with** _Y_ 𝑥 𝑬( 2) β0 +β1 2 **It is assumed that there are no other factors that systematically influence** _**Y**_ **i.e. that the** 𝑬 _Y_ β0 +β1 𝑥1 ( 1) **differences in the expected values of** _**Y**_ **are only due to** 𝑿 **(or that** 𝑿 **is sufficient to explain them)** _**x x x**_ **1 2 3 32** 

## **Weak assumptions** 

The error term is a r.v. with constant variance, σε[2] whatever _xi_ ( **homoskedasticity** ): 𝑉𝑎𝑟 ε𝑖 = σε[2] for every 𝑖 

= _Y_ σ for each 𝑖 𝑖 𝑉𝑎𝑟( 𝑖)) ε[[2]] 

= _Y_ 𝑥+ ε _Y_ σ for each 𝑖 𝑖 = β0 + β1 𝑉𝑎𝑟( 𝑖)) ε[[2]] ~~_**Y x** :_ Thus, the variance (and standard deviation) of~~ _**i**_ ~~does not depend on~~ _**i** x_ **The standard deviation (the** β0 + β1 3 **amount of dispersion around the** 𝑥 **line) remains constant as** 𝑿 β0 +β1 2 **changes. Thus, although they have different expected values, the** _**Yi**_ 𝑥 β0 +β1 1 **have the same variance (they can be considered a homogeneous sample with reference to the squared deviation from the mean)** _**x x x**_ **1 2 3 33** 

## **Weak assumptions** 

The errors ε1, … , ε𝑛 are **uncorrelated** 

_Y_ 𝑥+ ε = β0 + β1 

𝐶𝑜𝑟 _Y_ 𝑖, _Y_ ℎ = 𝐶𝑜𝑟(β0 + β1𝑥𝑖 + 𝜀𝑖, β0 + β1𝑥ℎ + 𝜀ℎ) = = 𝐶𝑜𝑟(ε𝑖, εℎ) = 0  for each 𝑖, ℎ 

Thus, random variables - i.e. the sample realisations - _Y_ 1, … , _Y_ 𝑛 are uncorrelated 

**34** 

## **Properties of least-squares estimators [OPTIONAL]** 

It can easily be proved that: 

It can be proved that under the weak assumptions the least squares estimators are uncorrelated, are unbiased for the corresponding parameters, and it is possible to derive their variance and their standard error 

Moreover, when the sample size is large enough, the distributions of the least-squares estimators, which are in fact linear combinations of the _**Yi**_ , can be approximated by a normal. 

**35** 

## **Properties of least-squares estimators [IMPORTANT!]** 

**It can be proved that under the weak assumptions the least squares estimators:** 

 Are **unbiased** for the population parameters 𝐸(β[෠] 1) = 𝛃𝟏 𝐸(β[෠] 0) = 𝛃𝟎 

**----- Start of picture text -----**<br>
 Their variances  measure the expected squared deviation around the parameters of interest  :<br>𝟏 ഥ𝒙 [𝟐]<br>𝑉𝑎𝑟(β [෠] 0) = 𝛔𝛆 [𝟐] 𝟐<br>𝒏 [+]<br>(𝒏−𝟏)𝒔𝒙<br>𝛔<br>𝛆 [𝟐]<br>𝑉𝑎𝑟(β [෠] 1) = 𝟐<br>(𝒏−𝟏)𝒔𝒙<br>**----- End of picture text -----**<br>

**As the sample size increases** the variances (and therefore the standard errors) **of the estimators tend to zero, and therefore the estimates of the coefficients are more and more concentrated around the corresponding population’s parameters.** 

**37** 

## **Standard error of the model** 

. The **estimate** of the parameter 𝜎ε[2] at a specific sample realisation 𝑦1, … , 𝑦𝑛 is: 𝑛 − 𝑏 +𝑏 𝑥 𝑺𝑺𝑬 [𝑦𝑖 ( 0 1 𝑖)][2] 𝑠 = ε[2] = ෍ (𝑛−2) (𝑛−2)[= 𝑴𝑺𝑬] 𝑖=1 also called the **mean of the squares of the errors** (𝑴𝑺𝑬), given by the **sum of the squares of the errors (** 𝑺𝑺𝑬) divided by (𝑛−2) Thus, the deviations of the 𝑦𝑖 observed around the estimated line are considered estimates of the model errors, and the 𝑺𝑺𝑬 is used to estimate the dispersion. 

The estimate of  is  

𝑺𝑺𝑬 **standard error of the model or** 𝒔 = 𝛆 **standard error of residuals** (𝑛−2) 

**38** 

## **Evaluation of point estimators** 

. 

**Study of the relationship between chat time and age. Consider the estimated model:** 

= 𝟐𝟑𝟏. 𝟐𝟎+ 𝟏𝟒. 𝟔𝟒∙𝒙 ෝ𝒚𝒊 𝒊 

**Is it possible to assess the reliability of the estimated slope, 14.64? How would you proceed?** 

It is not possible to assess the reliability of the estimate but only of the **estimator.** The observed estimate is just one of the possible realisations of the estimator. Remember that 𝑛= 96, 𝑠𝑥[2] = 88.06, 𝑠𝑦[2] = 30237.95, and 𝑅[2] = 0.6241. Therefore: 2 = 𝑆𝑆𝐸= (1 −𝑅[2] ) ∙𝑆𝑆𝑇= (1 −𝑅[2] ) ∙(𝑛−1)𝑠𝑦 1 −0.6241 ∙95 ∙30237.95 = 1079812.31 𝑠 ε[2] = 𝑆𝑆𝐸/(𝑛−2) = 1079812.314/94 = 11487.37 and: The (estimate of the) expected deviation of 2 sε 11487.37 a generic estimate of the slope from the 𝒔𝒆 = ෡𝛃𝟏 2[=] 95 ∙88.06[= 1.1718] parameter 𝛃𝟏 𝛃𝟏𝟏 is **1.1718** (𝑛−1)𝑠𝑥 

The (estimate of the) expected deviation of a generic estimate of the slope from the is **1.1718** parameter 𝛃𝟏 𝛃𝟏𝟏 

* For the commands to obtain results using R see the script 

**39** 

## **Inference on the model’s parameters in the population** 

To apply more advanced inferential techniques, e.g. constructing confidence intervals or t **determine the distribution of**[መ] **and**[መ] **.** esting hypotheses, it is necessary to 𝛽 ~~0~~ 𝛽 ~~1~~ For this purpose - at least when the sample size is not very large - it is necessary to make a further assumption on the **distribution of model errors** , in addition to the weak ones already assumed. 

**Weak assumptions: :** 𝐸 ε𝑖 = 0 and 𝑉𝑎𝑟 ε𝑖 = σε[2] for each 𝑖; 𝐶𝑜𝑟(ε𝑖, εℎ) = 0 for each 𝑖, ℎ ~ **+ The error**  **has normal distribution:** ε **Strong assumptions: Weak assumptions** 𝑖 𝒩(0, σε[2] ) 

_Y_ = β0 + β1𝑥+ ε _Yi_ ~𝒩(β0 + β1𝑥𝑖, σε[2] ) 

**Under the normality hypothesis, non-correlation implies independence. Thus** _**under the strong assumptions**_ **the** _**Yi**_ **are independent and normally distributed.** 

**40** 

## **Strong Assumptions** 

## **Weak assumptions** 

## **Strong assumptions** 

**----- Start of picture text -----**<br>
Y Y<br>Yi  = β0 + β1𝑥𝑖 + ε𝑖 Yi ~𝒩(β0 + β1𝑥𝑖, σε [2] )<br>𝑉𝑎𝑟 ε𝑖 = σ2ε E ( Yi ) = β0 + β1𝑥𝑖 E ( Yi ) = β0 + β1𝑥𝑖<br>𝑥<br>β0 + β1<br>𝑥<br>β0 + β1<br>𝑥 𝑥 𝑥 𝑥<br>𝑖 𝑖<br>**----- End of picture text -----**<br>

**41** 

## **Strong Assumptions [READING]** 

## **Strong assumptions** 

_**Y** Yi_ ~𝒩(β0 + β1𝑥𝑖, σε[2] ) _E Y_ 𝑥 ( _i_ ) = β0 + β1 𝑖 𝑥 β0 + β1 𝑥 𝑥 𝑖 

_**Yi**_ is dispersed around its expected value, β0 + β1𝑥𝑖 (the deterministic component of the linear model) with an σ expected absolute deviation equal to ε whatever the value of 𝑥 𝑖 As the values of the explanatory variable change, the distribution of _**Yi**_ **always has the same shape and only its** expected **value changes!!!!** 

**42** 

## **Strong Assumptions [READING]** 

**Strong assumptions** _**Y**_ 

**----- Start of picture text -----**<br>
x x x x<br>1 2 3<br>**----- End of picture text -----**<br>

**43** 

## **Strong Assumptions [OPTIONAL]** 

. 

In order to understand what are the implications of strong assumptions, consider that: 

**----- Start of picture text -----**<br>
𝑛 𝑛<br>𝑛 −ഥ<br>෡ 𝑥 −ҧ𝑥 Y Y 𝑥 −ҧ𝑥<br>σ𝑖=1( 𝑖 )( 𝑖 ) 𝑖<br>=<br>w Y<br>𝛃𝟏 𝑛 2 2 [Y] [𝑖] [= ෍] 𝑖 𝑖<br>= ෍<br>σ𝑖=1(𝑥𝑖 −ҧ𝑥) (𝑛−1)𝑠𝑥<br>𝑖=1 𝑖=1<br>**----- End of picture text -----**<br>

## **Known coefficient** 

The estimator of the slope is a linear combination of the _**Yi**_ **, which under the strong assumptions are independent and normally distributed** ; therefore, **the estimator also has a normal distribution** , even when the sample size is limited 

. The same applies to the linear model’s intercept estimator, 𝛃[෡] 𝟎 

Furthermore, under the strong assumptions the least squares estimators are independent. 

**44** 

## **Properties of least-squares estimators [RECAP]** 

. 

and[መ] _**Y**_ . The least squares estimators 𝛽[መ] 0 𝛽1 are both linear combinations of the _**i**_ 

Under **weak assumptions** : 

**----- Start of picture text -----**<br>
𝑬(𝛃 [෡] 𝟎) = 𝛃𝟎 𝑬(𝛃 [෡] 𝟏) = 𝛃𝟏<br>1 ҧ𝑥 [2] σ<br>ε [2]<br>𝑽𝒂𝒓(𝛃 [෡] 𝟎) = σε [2] 2 𝑽𝒂𝒓(𝛃 [෡] 𝟏) = 2<br>𝑛 [+]<br>(𝑛−1)𝑠𝑥 (𝑛−1)𝑠𝑥<br>Under  strong assumptions :<br>෡ 1 ҧ𝑥 [2] ෡ σε [2]<br>𝛃𝟎 ~𝒩 β0, σε [2] 𝛃𝟏 ~𝒩 β1,<br>𝑛 [+]<br>(𝑛−1)𝑠𝑥 [2] (𝑛−1)𝑠𝑥 [2]<br>**----- End of picture text -----**<br>

**45** 

## **Inference on** 𝛃𝟏 

. 

We specifically refer to inference on 𝛃𝟏, the parameter we are most interested in, since it measures the expected variation in the dependent variable corresponding to a variation in the explanatory variable (the same procedures can be used for inference on 𝛃𝟎). Note that: 

σ ε[2] ෡𝛃𝟏 ~𝒩 𝛃𝟏, 2 (𝑛−1)𝑠𝑥 

**Replacing** 𝛔𝛆 **, unknown, with its estimator, we obtain a statistic that (under the strong assumptions) has a Student's** _**t**_ **distribution with** (𝒏−𝟐) **degrees of freedom** 

෡ **This result cannot** ෡𝛃𝟏 −𝛃𝟏 𝛃𝟏 − 𝛃𝟏 = ~𝒩 0,1 **be used because** ෡ 𝑺𝑬 𝛃𝟏 σ **is not known!** 𝟏 ε[2] 𝛔 𝛆 2 (𝑛−1)𝑠𝑥 

**----- Start of picture text -----**<br>
෡ ෡<br>𝛃𝟏 −𝛃𝟏 𝛃𝟏 − 𝛃𝟏<br>=<br>෢ ~𝒕𝑛−2<br>෡<br>𝑺𝑬<br>ෝ 𝟏 𝛃𝟏<br>𝛔<br>𝛆 2<br>(𝑛−1)𝑠𝑥<br>**----- End of picture text -----**<br>

**46** 

## **Confidence interval for** 𝛃𝟏 

. 

## Since 

**----- Start of picture text -----**<br>
෡ ෡<br>𝛃𝟏 −𝛃𝟏 𝛃𝟏 −𝛃𝟏<br>=<br>෢ ~𝒕𝑛−2<br>෡<br>𝑺𝑬<br>𝟏 𝛃𝟏<br>ෝσ<br>ε 2<br>(𝑛−1)𝑠𝑥<br>**----- End of picture text -----**<br>

The confidence interval estimate at the level for based on the estimate of the (1 −α) 𝛃𝟏 slope determined on the basis of a specific sample (i.e. the sample realisation of 𝛃[෡] 𝟏), 𝒃𝟏, is: 

where 𝑡𝒏−𝟐,𝛂/𝟐 is the percentile of order (1 −α/2) of a **Student’s** _**t**_ distribution with (𝒏− 𝟐) degrees of freedom. 

**47** 

## **Testing Hypotheses on** 𝛃𝟏 

. 

## It is possible to use the illustrated results to test the null hypothesis 

Against alternative hypotheses such as: 

The test statistic to be used is 

**----- Start of picture text -----**<br>
෡ 𝟎 ෡ 𝟎<br>𝛃𝟏 − 𝛃𝟏 𝛃𝟏 − 𝛃𝟏<br>=<br>෢<br>𝑺𝑬<br>𝟏 ෡𝛃𝟏<br>ෝσ<br>ε 2<br>(𝑛−1)𝑠𝑥<br>**----- End of picture text -----**<br>

which under the null hypothesis has a **Student’s** _**t**_ distribution with (𝒏−𝟐) **degrees of freedom** 

**48** 

## **Testing Hypotheses on** 𝛃𝟏 

. 

 Given a level of significance, , the rejection region of the null hypothesis is built by comparing the value of the test statistic observed in a sample: 

with the appropriate percentile of **Student’s** _**t**_ distribution with (𝒏−𝟐) degrees of freedom : 

**49** 

## **Testing Hypotheses on** 𝛃𝟏 

. 

**Usually,** we are interested in testing the null hypothesis that the parameter  1 is equal to zero, i.e. that the line has zero slope in the population and that the linear model defined on the basis of the considered explanatory variable is ineffective, towards the alternative that the coefficient is non-zero. 

**----- Start of picture text -----**<br>
H :  < 𝟎 H :  = 𝟎 H :  > 𝟎<br>1 𝛃𝟏 0 𝛃𝟏 1 𝛃𝟏<br> 0<br> 0<br>The slope   1 The slope   1  0 The slope   1<br>is negative is zero is positive<br>**----- End of picture text -----**<br>

**----- Start of picture text -----**<br>
H :  ≠𝟎<br>1 𝛃𝟏<br>**----- End of picture text -----**<br>

**50** 

## **Testing Hypotheses on** 𝛃𝟏 

. 

## **Study of the relationship between time on chat and age.** 

**Check whether there is sufficient empirical evidence to conclude that the slope of the**  **= 0.05. regression model is different from 0 (in the population), using a test of level** We must test the hypotheses: **H0** : 𝛃𝟏 = 𝟎 vs **H1** : 𝛃𝟏 ≠𝟎 **Rejection region?** The realisation of the test statistic is: 

Since we are testing a simple hypothesis against a bilateral the rejection region is: 

**Region of rejection :** 𝑡𝑜𝑏𝑠 > 𝑡𝒏−𝟐; 𝛂/𝟐 

**51** 

## **Testing Hypotheses on** 𝛃𝟏 

. 

**Study of the relationship between time on chat and age Rejection region to test H0:** 𝛃𝟏 = 𝟎 **vs H1:** 𝛃𝟏 ≠𝟎 **at level**  **= 0.05.** Since 𝑛= 96, the critical value of the rejection region (percentile of the 𝒕 distribution) is 𝑡 = 𝟏. 𝟗𝟖𝟓𝟓: 𝟗𝟒;𝟎.𝟎𝟐𝟓 

**> qt(0.975,df=94)** 

**[1] 1.985523** 

and the rejection region is 

𝒃 𝟏 = 𝑅= 𝑡 > 𝟏. 𝟗𝟖𝟔 𝑜𝑏𝑠 𝒔𝒆෡ 𝛃𝟏 ෡ Remember that 𝑏1 = 14.64 and 𝑠𝑒 = 1.1718 (rounded results). Therefore: β1 𝟏𝟒. 𝟔𝟒 = 𝑡 𝑜𝑏𝑠 𝟏. 𝟏𝟕𝟏𝟖[= 𝟏𝟐. 𝟒𝟗] _Since_ 𝑡𝑜𝑏𝑠 = 𝟏𝟐. 𝟒𝟗>  𝟏. 𝟗𝟖𝟔 , **H0** _is rejected in favour of the alternative: there is sufficient evidence to conclude that the slope of the linear model in the population is different from zero_ 

* For the commands to obtain results using R see the script 

**52** 

## **Testing Hypotheses on** 𝛃𝟏 

. 

**Study of the relationship between time on chat and age. What is the p-value of the observed sample realisation?** 

The p-value of the sample realisation is the probability of observing a value of the test statistic less favourable to the null hypothesis **H0** than the observed one: 

**P−value** = 2𝑃𝑟 𝒕 > 𝑛−2 

**----- Start of picture text -----**<br>
𝒃<br>𝟏<br>= 2𝑃𝑟 𝒕 > 𝟏𝟐. 𝟒𝟗<br>𝑛−2<br>𝒔𝒆෡<br>𝛃𝟏<br>**----- End of picture text -----**<br>

**> 2*(1-pt(12.49,df=94)) [1] 0** 

## **Interpretation? Conclusions?** 

_The observed sample realisation is extremely 'far' from_ _**H0** in probabilistic terms: the probability of observing a sample regression line with such a high slope when the population is actually characterised by a regression line with zero slope is practically zero. We underline that the rejection - of the null hypothesis does not depend on the chosen significance level, being the p value lower_ α _than any standard value of_ 

* For the commands to obtain results using R see the script 

**53** 

## **Confidence intervals for** 𝛃𝟏 

. 

**Study of the relationship between time on chat and age. What is the confidence interval at the 0.95 level for**   **1** 

The estimated confidence interval is 

= ෡ 𝒄𝒊 𝒃 ∓𝒕 ∙𝒔𝒆 𝟏. 𝟗𝟖𝟓𝟓 𝟏−𝛂 𝛃𝟏 𝟏 𝒏−𝟐;𝟎.𝟎𝟐𝟓 𝛃𝟏 = [𝟏𝟒. 𝟔𝟒∓ ∙𝟏. 𝟏𝟕𝟏𝟖] = [𝟏𝟐. 𝟑𝟏, 𝟏𝟔. 𝟗𝟕] 

## **Interpretation?** 

Since the 95% of the estimated intervals (based on all the possible samples of size 96 that can be drawn from the population) contain the parameter or, in other words, the probability that a generic interval contains the parameter is 0.95, one can **expect** with 95% confidence a variation in the **average** time spent on the chat between 12.31 and 16.97 minutes corresponding to 1-year variation in the age of a user 

* For the commands to obtain results using R see the script 

**54** 

## **Cautions in drawing conclusions based on inference on** 𝛃𝟏 

Rejecting the hypothesis that  **1 = 0** and concluding that the slope of the line is not zero and that the estimated slope is statistically significant 

 **does not allow** to infer that there is a cause-and-effect relationship between 𝑿 and _**Y**_ . This conclusion is only possible when there is some theoretical justification to support it. 

 **does not allow to** conclude that the relationship between 𝑿 and _**Y**_ **is linear** . One can only say that **for values** of 𝑿 **in the range of the observed sample values of** 𝑿 **(i.e. values not too dissimilar/distant from those on which the estimate was based on)** a significant linear variation of the dependent variable can be expected corresponding to a 1-unit variation of the explanatory variable. 

- **does not allow** to conclude that the linear model explains to a satisfactory extent the dependent variable. This conclusion can be drawn only based on the determination coefficient, but still even if such coefficient is high it is not possible to state that the relation is linear. One can only say that the linear model based on 𝑿 explains a significant portion of the variance of _**Y**_ **for values** of 𝑿 **in the range of the sample values of** 𝑿 **(i.e. values not too dissimilar/distant from those on which the estimate was based on)** 

**55** 

## **Simple regression** 

## **Prediction** 

## **Prediction** 

The estimated regression model can be used to make predictions about the dependent variable at a given value of the explanatory variable. As we have already pointed out, before **using the model** it would be appropriate to check whether the assumptions (weak and strong) at the basis of the linear model are indeed reasonable. However, we postpone this argument even though it is fundamental. 𝑿 𝑥 . Let us consider a new observation characterised by a value of equal to According to the 𝑔 linear model: 

_Y_ 𝑥 + ε 𝑔 = β0 + β1 𝑔 𝑔 

_Y_ 𝑥 𝐸( 𝑔) = μ𝑔 = β0 + β1 𝑔 

It is important to distinguish between:  The prediction of the **expected value** of _Y_ corresponding to  𝑥𝑔, μ𝑔 = 𝐸( _Y_ 𝑔)  The prediction of the **exact value** of _Y_ corresponding to 𝑥 , _Y ._ Compared to μ , _Y_ also 𝑔 𝑔 𝑔 𝑔 'incorporates' the unobservable error ε , which causes the deviation of _Y_ from the 𝑔 𝑔 regression line (i.e. from μ ). 𝑔 

**57** 

## **Point Prediction** 

## The two types of prediction 

**----- Start of picture text -----**<br>
Y<br>𝒙<br>𝛃𝟎 + 𝛃𝟏<br>Y 𝒙 + 𝛆<br>𝒈 = 𝛃𝟎 + 𝛃𝟏 𝒈 𝒈<br>𝛍𝒈 = 𝛃𝟎 + 𝛃𝟏𝒙𝒈<br>𝒙<br>𝒈<br>**----- End of picture text -----**<br>

**58** 

## **Point Prediction** 

- **The estimator of** 𝑬( _**Y**_ 𝒈) = 𝛍𝒈 **.** To a specific value of 𝑥𝑔, corresponds a **sub-population** of values of _**Y**_ whose average is estimated with: 

- **The estimator of** _**Y**_ = 𝛍 + 𝛆 . Since the erratic component is random and cannot be 𝒈 𝒈 𝒈 _**Y**_ 𝑥 

- estimated, the specific value of corresponding to is estimated using the same **point** 𝑔 

- **estimator** used to predict 𝛍 : 𝒈 

The (identical) point estimates are obtained by substituting the coefficient estimators with the estimates based on the available sample: 

= = 𝑏 𝑥 Ƹ𝜇𝑔 ො𝑦𝑔 0 + 𝑏1 𝑔 

**59** 

## **Point Prediction** 

. 

**Study of the relationship between time on chat and age. Estimated regression line (rounded values)** 

   - = 𝟐𝟑𝟏. 𝟐𝟎+ 𝟏𝟒. 𝟔𝟒∙𝒙 

   - ෝ𝒚𝒊 𝒊 

- **What is the average time spent in chat by a generic 30-year-old user?** 

Ƹ𝜇 = 231.20 + 14.64 ∙30 = 670.4 𝑔 

- **What is the time spent on chat by a 30-year-old user?** The point estimate is the same: 

   - ො𝑦𝑔 = 231.20 + 14.64 ∙30 = 670.4 

**However, the prediction of the time spent on chat by a** _**user aged 30**_ **(i.e. not the average time for all users the users aged 30, but the time spent by a generic specific user) should include the error term, which, however, cannot be predicted** 

**60** 

## **Confidence and prediction intervals** 

Rather than a point estimator, it is recommendable to build confidence intervals for predictions, that **account for the uncertainty on prediction** . Even if the point estimators for 𝐸( _Y_ 𝑔) = μ𝑔 and _Y_ 𝑔 are the same, the intervals built for the two parameters are different  **Confidence interval** for μ , the expected value of _Y_ corresponding to 𝑥 : 𝑔 𝑔 

_The prediction interval is wider than the confidence interval, since besides accounting for the uncertainty due to the estimation of the expected value, it also accounts for uncertainty due to the deviation of individual values from the expected value_ 

**61** 

## **The effect of** 𝑥 **on the width of the intervals** 𝑔 

**Confidence interval** for 𝛍𝒈 = 𝑬( _**Y**_ 𝒈) ො𝑦𝑔 ± 𝑡 𝑛−2 ,αΤ2[𝑠] ε 𝑛1[+] (𝑥𝑔−ǉ𝑥)[2] (𝑛−1)𝑠𝑥[2] − **Forecast interval** for _**Y**_ 𝒈 ො𝑦𝑔 ± 𝑡 𝑛−2 ,αΤ2[𝑠] ε 1 + 𝑛1[+] (𝑥𝑔 𝑥)[2] (𝑛−1)𝑠𝑥[2] 

The width of the intervals increases with the distance of 𝑥 from ҧ𝑥, the mean of the values of 𝑔 the explanatory variable calculated on the sample data used to estimate the linear model 

Intervals have minimum width when 𝑥 = ҧ𝑥; the 𝑔 width increases as 𝑥 deviates from ҧ𝑥. 𝑔 This is because when 𝑥 is far from ҧ𝑥 predictions rely 𝑔 on values of 𝑿 that are far from those used to estimate the model (risk associated with extrapolation) 

~~_x_~~ 

**64** 

## **Confidence and prediction intervals** 

. 

## **Study of the relationship between  time on chat and age.** 

**95% confidence interval for the average time spent on chat by 30-year-old users?** 

* For the commands to obtain results using R see the script 

**65** 

## **Confidence and prediction intervals** 

. 

## **Study of the relationship between  time on chat and age.** 

**95% confidence interval for the time spent in chat by a 30-year-old user?** 

## Therefore: 

The confidence interval for _Y_ is **much** wider than that one determined for μ 𝑔 𝑔 

**66** 

## **Extrapolation [READING]** 

. 

**Study of the relationship between time on chat and age. Would use the estimated model to the time on chat a user 90? you predict spent by aged Why?** 

_The model was estimated based on a sample of users with a maximum age of 60. Extrapolating and obtaining predictions for users aged much more than 60 is very risky as we have no data to support the assumption that the trend observed for age values in the range of X remains the same even for age values far outside the range._ 

**67** 

## **Extrapolation [READING]** 

. 

## **Study of the relationship between time on chat and age.** 

_Note how the width of the confidence and_ 𝑥 _prediction interval increases as moves away_ 𝑔 _from the mean ,_ ǉ𝑥 _. This reflects the risk associated with predictions far from the 'centre' of the data used to estimate the model Note in particular that the impact of the distance of_ 𝑥 _from_ ǉ𝑥 _is much less relevant for_ 𝑔 _the prediction interval. Indeed, the third addendum in_ 1 + 1 (𝑥𝑔−𝑥)[2] _[is typically much]_ 𝑛[+] 𝑛−1 𝑠 𝑥[2] _lower than 1, and therefore it becomes relevant only when_ 𝑥 _is very far from_ ǉ𝑥 𝑔 

**68** 

## **Rstudio: lm() function for estimating the linear model** 

The function **lm(formula,data)** in R allows estimating a linear model based on raw data. In the function: 

**formula** is a description of the model to be estimated, which in the case of a **simple linear regression** model has the form 

**formula = y ~ x** 

Where **y** is the dependent variable and **x** is the explanatory variable. 

In the formula, **x** and **y** may be two vectors or the names of two variables contained in the dataframe specified in **data** . 

**69** 

## **Linear model estimation** 

The dataframe **Basket** * contains information on the customers of a supermarket who live in a specific area of a large city. In particular, besides other information, an indicator of household economic well-being (called **income** for simplicity) is obtained based on the declared address, the price per square metre of dwellings and rental prices, and the declared number of cohabitants. For each customer, the 'quality' of their expenditure is assessed on the basis of the products purchased ( **basket** ), taking into account the prices and alternatives available. One wants to assess whether the **income** indicator is related to the expenditure quality indicator, **basket.** 

To estimate the linear model: **lm(formula = basket ~ income, data = Basket) lm(formula = Basket$basket ~ Basket$income)** 

**> lm(formula = basket ~ income, data = Basket)** 

**Call:** 

**lm(formula = basket ~ income, data = Basket)** 

**Coefficients:** 

**(Intercept) income 3.16383 0.01097** 

_Note that by giving the command as an expression, the function only returns the coefficients estimates_ 

* All the dataframes used in the slides are in file **Lesson 22-24_Data.Rdata** 

**70** 

## **Linear model estimation** 

It is convenient to assign the output obtained by applying the **lm()** function to an R object. The saved object is a **list** 

**> sreg.model <- lm(basket ~ income, data = Basket)** 

**> str(sreg.model) List of 12** 

- **$ coefficients : Named num [1:2] 3.164 0.011** 

**..- attr(*, "names")= chr [1:2] "(Intercept)" "income" $ residuals : Named num [1:99] 4.81 1.3 3.79 -1.42 -2.68 ... ..- attr(*, "names")= chr [1:99] "1" "2" "3" "4" ...** 

**$ effects : Named num [1:99] -669.31 -166.19 3.44 -1.87 -3.04 ... ..- attr(*, "names")= chr [1:99] "(Intercept)" "income" "" ... $ rank : int 2** 

**$ fitted.values: Named num [1:99] 37.8 70.1 46.1 65.3 48.2 ... ..- attr(*, "names")= chr [1:99] "1" "2" "3" "4" ...** 

**...** 

- **$ model :'data.frame': 99 obs. of 2 variables: ..$ basket: num [1:99] 42.6 71.4 49.9 63.9 45.5 ... ..$ income: num [1:99] 3156 6101 3914 5662 4103 ... ..- attr(*, "terms")=Classes 'terms', 'formula' language basket ~ income** 

A list is an object whose elements may be objects of **any** type. The elements and subelements of a list can be accessed using the $ symbol (e.g. 

**sreg.model$coefficients** as well as **sreg.model$model$basket** ) 

**71** 

## **Linear model estimation** 

## To display more detailed results, the **summary()** function can be applied to the output of the **lm()** function 

**> sreg.model <- lm(basket ~ income, data = Basket) > summary(sreg.model) Call:** ෡ ෡ **lm(formula = basket ~ income, data = Basket)** 𝒔𝒆𝛃𝟎, 𝒔𝒆𝛃𝟏 **Residuals: Min      1Q Median     3Q     Max -22.0429 -7.2305 0.0133 6.3991 23.6122** 𝒃 𝒔𝒆 𝟏/ ෡𝛃𝟏 **Coefficients: ?? Estimate Std. Error t value Pr(>|t|) (Intercept) 3.1638282  3.9037148    0.81     0.42 income      0.0109748  0.0006467   16.97   <2e-16 *** --Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' 1** 𝒔 𝛆 **Residual standard error: 9.793 on 97 degrees of freedom Multiple R-squared: 0.748, Adjusted R-squared: 0.7454** 𝑹[𝟐] **F-statistic: 288 on 1 and 97 DF, p-value: < 2.2e-16** 

**72** 

## **Confidence intervals for coefficients with R/RStudio** 

To determine the confidence intervals of the coefficients of the linear model, it is possible to apply the function 

## **confint(object,level=0.95)** 

where **object** is the output of the **lm()** function, and **level** is the confidence level of the interval 

## **99% confidence intervals for the coefficients of the linear model?** 

**> sreg.model$coefficient (Intercept) income 3.16382818 0.01097483** 

**>** 

**> confint(sreg.model,level=0.99)** 

**0.5 %      99.5 % (Intercept) -7.093056538 13.42071290 income       0.009275569  0.01267409** 

**73** 

## **Confidence intervals for coefficients with R/RStudio** 

**> sreg.model$coefficient** 

**(Intercept)     income 3.16382818 0.01097483** 

**>** 

- **confint(sreg.model,level=0.99)** 

**0.5 %      99.5 % (Intercept) -7.093056538 13.42071290 income       0.009275569  0.01267409** 

_**The coefficient of**_ **income** _**is close to zero: can we conclude that**_ **income** _**is not particularly relevant in the explanation of**_ **basket?** 

The statement is completely **wrong** ! 

- . 

- **1) The** p-value of the slope ( 0) leads to **reject the null hypothesis that the coefficient is zero 2** ) _**R**_ **[2]** indicates that a high proportion (about 75%) of the **basket** variation is explained by differences in customer **income.** 

- **3)** The estimated coefficient, 0.009276, represents the **average** (estimated) **basket change** corresponding to a unit change in **income** . 

Indeed* for **basket** it is ത𝑦=67.27 and 𝑠𝑦=19.41, while for **income** ҧ𝑥=5841.07 e 𝑠𝑥=1529.66!!! At a 'standard' variation of **income** we expect a variation of 0.009276*1529.66  14.188, which - compared to the standard deviation of **basket** - is not small at all!!! **The unit of measurement of** 𝒃𝟏 depends on the units of measurement of 𝑿 and 𝒀 ! 

* Commands in the script 

**74** 

## **Prediction with R/RStudio** 

To determine the confidence intervals for the mean of the prediction and the forecast interval, you can use the function 

**predict(object, newdata, interval, level=0.95)** 

where 

**object** is the output of the **lm()** function 

**newdata** is a **dataframe** containing the values of the explanatory variable at which the prediction is to be determined. **The name of the variable in the dataframe must match the name of the variable in the dataframe used to estimate the model. interval** is the type of interval required; you can specify **'none'** to get only the point forecast, ' **confidence'** to get the confidence interval for the expected value, and **'prediction'** to get the prediction interval **level** is the confidence level of the interval (default=0.95) 

**75** 

## **Forecasting with RStudio** 

**Relationship between income and quality of expenditure (basket). Obtain the 95% intervals for the prediction of the average basket value for two customers with income levels of 7500 and 9000 respectively** 

|**>**|**# dataframe creation**||
|---|---|---|
|**>**|**newdata<-data.frame(income=c(7500,9000))**||
|**>**|**newdata**||
||**income**||
|**1**|**7500**||
|**2**|**9000**||
|**>**|**predict(sreg.model,newdata=newdata,**||
||**interval='confidence',level=0.95)**||
||**fit      lwr       upr**|**Interpretation?**|
|**1**|**85.47505 82.58536  88.36475**||
|**2**|**101.93730 97.43652 106.43808**||
|**>**|**predict(sreg.model,newdata=newdata,**||
||**interval="prediction",level=0.95)**||
||**fit      lwr      upr**||
|**1**|**85.47505 65.82438 105.1257**||
|**2**|**101.93730 81.98597 121.8886**||

**76** 

## **Simple regression Analysis of residuals** 

## **Analysis of residuals: motivation** 

**Even before using the linear model to make predictions, one should assess whether the assumptions necessary to make inferences about the model are actually fulfilled. we** There are various procedures and even specific tests developed for this purpose. However, follow **an exploratory approach, and describe how to use regression residuals to assess:** 

   - Whether the assumption of linearity is supported by the data (not particularly useful in the case of simple linear regression because the relation can be visualized using a scatterplot; we see it here to better understand its use in the case of multiple linear regression). 

   - If there are  systematic structural differences between the average levels of error at specific values of the explanatory variable 

   - If the variance of the errors is indeed constant (assumption of homoskedasticity) 

   - If errors have normal distribution* 

   - If there are specific cases that overly influence the results (outliers) 

   - The possible **correlation** between errors; this can be a problem in specific applications (surveys over time, surveys on the same units under different conditions...). 

- If the sample is large, the distribution of the least-squares estimators can be approximated by a normal, as both are linear combinations of the realizations of the dependent variable 

**78** 

## **Residuals** 

## Regression residuals: 

𝑒 −𝑏 𝑥 𝑖 = (𝑦𝑖 −ො𝑦𝑖) = (𝑦𝑖 0 − 𝑏1 𝑖) 

The residuals analysis can be conducted based on the original residuals or on the residuals:  **standardised** using the standard error of residuals 

−ො 𝑒 𝑖 (𝑦𝑖 𝑦𝑖) = 

where ℎ𝑖 , the so-called leverage, measures the deviation of 𝑥𝑖 from the mean ҧ𝑥 based on the relative contribution of 𝑥 to the variance 𝑠 𝑖 𝑥[2] 

**79** 

## **Rstudio: analysis of residuals** 

From the **output of the lm()** function, it is possible to obtain some **plots of the residuals** using: 

## **plot(object, which)** 

where **object** is the output of the function **lm()** and **which** indicates the type of graph to be obtained. We limit attention to some of these plots (see later for others): **which=1** scatterplot: relationship between residuals and predictions of the dependent variable 

**which=2** q-q plot of residuals. Plot of the quantiles of the standardised residuals against the quantiles of the normal distribution. 

**which=3** scale-location plot. Plot of the square root of the standardized residuals (in absolute value) against the predictions of the dependent variable 

Note that the output of the function **lm()** also contains the regression residuals ( **object$residuals** ). The standardised residuals can be obtained using the function **rstandard(object)** 

**80** 

## **Residuals: structural characteristics** 

## **Relationship between income and quality of expenditure (basket).** 

**> plot(sreg.model,which=1)** 

**The residuals should** _**have**_ **no** _**structure**_ **.** The mean of the residuals is **zero** by construction; it must be assessed whether the mean level of the residuals changes at certain expected values. Furthermore, the variance of the residuals should be constant. We do not observe any particular structure of residuals, although some cases, highlighted in the plot, have relatively large residuals and corresponding to higher and lower predictions the (local) average of residuals is slightly higher than in the centre 

**81** 

## **Residuals: structural characteristics** 

## **Relationship between income and quality of expenditure (basket).** 

**> plot(sreg.model,which=3)** 

**The residuals should** _**have**_ **no** _**structure**_ **.** The magnitude of (absolute) residuals and their dispersion should not vary with predictions. Also in this case no particular structure can be noted. The average magnitude of (absolute) residuals is quite constant, even if slightly lower and higher corresponding respectively to lower and higher predictions. A slight reduction of the dispersion corresponding to higher predictions can be also appreciated. 

**82** 

## **Residuals: distribution - comparison with normal distribution** 

## **Relationship between income and quality of expenditure (basket).** 

**> plot(sreg.model,which=2)** 

**Although not strictly necessary for inferential purposes as the sample size is sufficiently large, we check whether the residuals have an approximately normal distribution, particularly to assess skewness and possible tails.** 

The distribution is approximately normal, although some deviation is observed on the tails. The left tail is slightly 'heavier' (quantiles are higher than those of the normal distribution) and the right tail is slightly 'lighter' 

**83** 

## **Residuals: distribution** 

## **Relationship between income and quality of expenditure (basket).** 

**> distr.plot.x(sreg.model$residuals,plot.type="histogram") > distr.plot.x(rstandard(sreg.model),plot.type="histogram")** 

A simpler graphical analysis of the distribution of residuals, possibly standardised, is based on histograms. One can easily appreciate that in this case the distribution is quite symmetric  even if the shape of the tails is not particularly ‘normal’. 

**84** 

## **Analysis of residuals: some examples** 

The dataframe **Advertising** contains information on the amount in thousands of dollars invested in advertising on different media ( **youtube** , **facebook** , **newspapers** ) and sales ( **sales** , appropriately measured and indexed). Evaluate the assumptions underlying the linear model of **sales** on **facebook** 

**> sreg.ads<-lm(sales ~ facebook , data=Advertising) > plot(sreg.ads,which=1) > plot(sreg.ads,which=3)** 

**> distr.plot.x(sreg.ads$residuals, plot.type="histogram", breaks=12)** 

**87** 

## **Analysis of residuals: some examples** 

## **sales and advertising investment on facebook** 

## **Observations?** 

_We note an increase in the 'local' average of residuals and a greater dispersion of residuals around the average for higher values of the prediction. The increase in magnitude is really evident in the scale-location plot._ 

_**This indicates possible violation of the hypothesis of homoskedasticity (heteroskedasticity)**_ 

**88** 

## **Assumption of homoskedasticity** 

Plotting the residuals against the predicted values can signal situations where the assumption of homoskedasticity is violated. 

**----- Start of picture text -----**<br>
Residual<br>Residual<br>ˆ ˆ<br>y y<br>**----- End of picture text -----**<br>

**The dispersion of the residuals varies as** ො𝑦 **varies (and therefore as** 𝑥 **varies in the case of a simple linear model). In the case of heteroskedasticity, the scale-location plot will exhibit a patterned average of the square roots of absolute residuals and a variation in their dispersion.** 

**89** 

## **Assumption of homoskedasticity** 

**Violation of the assumption of homoskedasticity (heteroskedasticity): the variance varies when** 𝑿 **varies** 

**----- Start of picture text -----**<br>
Residual<br>𝒀<br>ˆ<br>y<br>x x x<br>1 2 3 𝑿<br>**----- End of picture text -----**<br>

**90** 

## **Assumption of homoskedasticity** 

**sales and advertising investment on facebook** 

**In the case of the simple linear model, linearity and homoschedasticity can be verified immediately from the data.** 

We present the analysis of residuals in this simplified context because when **several explanatory variables are** considered (multiple regression), the linear model cannot be represented graphically as simply and therefore the analysis of residuals can prove very useful. 

**91** 

## **Analysis of residuals: some examples** 

The dataframe **Restaurants** contains information on the revenues of the restaurants of a **revenue** fast-food chain ( ) and on the characteristics of the neighbourhood in which they are located, in particular the average **income revenue** on income*. Evaluate the assumptions underlying the linear model of 

The residuals are characterised by an obvious **revenue** is non-linear structure: in particular, underestimated at lower values of **income** and heavily and systematically underestimated for higher values of **income** ; this indicates that the observed values of **revenue** for high or low values of **income** deviate from the straight line! Same conclusions can be drawn based on the scale-location plot* and the distribution of residuals is clearly not normal* 

* Code in the script 

**92** 

## **Analysis of residuals: non-linearity** 

Receipts ( **revenue** ) average **income** of the district in which they are located Again, in order to deduce non-linearity, it was sufficient to consider the scatterplot of the two variables from the beginning, which is always recommendable 

The plot clearly shows the non-linear structure of the relationship: from a certain **revenue** decreases as point onwards **income** increases because in 'richer' neighbourhoods the propensity to visit fast food restaurants is lower; the same is observed for 'less wealthy' neighbourhoods **Note:** residuals analysis allows non-linear relationships to be identified even for models with several explanatory variables that cannot be represented graphically using a scatterplot 

**93** 

## **Simple linear regression: summary** 

- Develop a model that has a reasonable theoretical basis, and collect data on the variables involved 

- **Descriptive analysis** 

   - Analyse the scatter plot to assess whether the linearity assumption makes sense 

   - Determine the regression line 

   - Assess the presence of anomalous observations influencing the model to a too great 

      - extent 

   - Assess the quality of the model 

. At this level, the analysis is purely **descriptive** 

To make **inference** about the model at the population level, certain assumptions must be made 

**94** 

## **Simple linear regression: summary** 

- Assess whether assumptions are violated by analysing  residuals. There are clearly more sophisticated procedures to assess assumptions, as well as specific approaches developed to suitably modify the model in the event of a violation. 

- If the assumptions are not violated, the estimated model can be used for inference 

   - Check the significance of the coefficients 

   - If one is interested in prediction **, it is important to consider that a significant coefficient does not imply that the model fits the data well (the R-squared should be used at this** . 

   - **aim)** 

      - Avoid extrapolation 

      - Prefer confidence intervals to point estimates for forecasting 

      - Choose the proper type of interval (confidence and prediction) based on the goal of analysis/prediction. 

**95** 

