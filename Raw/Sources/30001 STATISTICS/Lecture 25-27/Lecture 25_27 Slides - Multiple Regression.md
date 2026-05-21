---
course: Statistics
course_code: "30001"
tags:
  - "source"
  - course_30001
Links:
Title: "Which plane best describes the linear relationship between the dependent variable and the explanatory variables (here 2)? Least squares** method **: plane that best interpolates the data"
Reference: "Course Material"
Created: 2026-05-18
Processed: false
---


## MULTIPLE REGRESSION

## The multiple linear regression model

We extend the simple linear model by considering the case where the dependent variable is assumed to be associated with several explanatory variables:

_Y_ 𝑥 𝑥 + ε = β0 + β1 1 + ⋯+ β𝐾 𝐾

_Y_ **= dependent variable (** _**random variable**_ **)**

𝑥1, 𝑥2, … , 𝑥𝐾 **= independent variables (** _**deterministic, known**_ **)** β0 **= intercept of the linear model**(β) 1(, β) 2(, … , β) 𝐾 **(= model parameters)** ε **= error (** _**random variable**_ **)**

## The multiple linear regression model

We expect the model to fit the data better, as we are considering more information to explain the dependent variable.

In addition, the multiple regression model allows to study the relationship between the dependent variable and more explanatory variables, and to take into account/ **control for** factors that possibly influence the dependent variable (Simpson's paradox)

- Employees: observed inverse relationship between amount of bonus compensation and number of successful transactions in the last year

_**Because the difficulty of the assigned operations is not taken into account**_

- Consumers: observed weak relationship between declared purchase intention and amount spent _**Because the age or income of customers is not taken into account**_

- Mega-store customers: observed strong relationship between number of complaints and level of satisfaction

_**Because the number of customers is not taken into account**_

- Relationship between hours of support classes and negative performance _**Because the support was offered to students in difficulty**_

## The multiple linear regression model for the population

Linear model describing the relationship between the dependent variable and the values of the explanatory variables in the population ( **deterministic** component)

## The multiple linear regression model for the population

A **probabilistic component** is added to the linear model describing the different realisations of the dependent variable observed at the same values of the explanatory variables

## Estimation of the linear model: procedure

Also for this case:

- We consider **the sample data** and derive the model parameters using the **least squares** approach and introduce criteria to assess the model's fit

- We define **least-squares estimators** by generalising the estimates obtained on an observed sample to a random sample

- Under the weak and strong assumptions, we define the procedures for inference on the model parameters in the population

**The least squares approach**

# Which plane best describes the linear relationship between the dependent variable and the explanatory variables (here 2)? Least squares** method **: plane that best interpolates the data

**Y** 𝒚𝒊 𝒀 Consider a data sample and a **generic** 𝑒 𝑖 = (𝑦𝑖 −$\hat{y}_i$ ) **model** with parameters 𝑏0 , 𝑏1 and 𝑏 . 2 For a sample observation we consider - the forecast $\hat{y}_i$ $\hat{y}_i$ = 𝑏0 + 𝑏1 𝑥𝑖1 + 𝑏2 𝑥𝑖2 - the deviation between the observed value and the value on 𝑿 𝟐 the line, 𝑒𝑖 = 𝑦𝑖 −$\hat{y}_i$ **Among all the possible planes, we** 𝒙 𝒊𝟐 **choose the one that minimizes the sum of the squared errors** 𝒙 𝒊𝟏 𝑿 𝟏

## The least squares approach

For each sample observation, say the 𝑖 -th

> (𝑥) 𝑖1(, 𝑥) 𝑖2(, … , 𝑥) 𝑖𝐾

values taken by the explanatory variables

𝑦𝑖

value of _**Y**_ corresponding to 𝑥𝑖1, 𝑥𝑖1, … , 𝑥𝑖𝐾

$\hat{y}_i$ = 𝑏0 + 𝑏1 𝑥𝑖1 + 𝑏2 𝑥𝑖2 + … + 𝑏𝐾 𝑥𝑖𝐾 forecast of _**Y**_ corresponding to 𝑥𝑖1, 𝑥𝑖1, … , 𝑥𝑖𝐾

Let us consider the sum of the squared differences between the observed values and the ∗ ∗ ∗ predictions ො𝑦1, ො𝑦2, … , ො𝑦𝑛 , i.e. the Sum of Squared Errors: 𝑛 𝑛 𝑺𝑺𝑬 −𝑏 −𝑏 𝑥 𝑥 … −𝑏 𝑥 (𝑦𝑖 −$\hat{y}_i$ )(2) (𝑦𝑖 0 1 𝑖1 −𝑏2 𝑖2 − 𝐾 𝑖𝐾)(2) = ෍ = ෍ 𝑖=1 𝑖=1

We determine the coefficients that minimise 𝑺𝑺𝑬 , i.e. the hyper-plane that best interpolates the data and minimises the sum of the squared differences between observed and predicted values. To determine these coefficients, it is necessary to resort to matrix calculation; therefore the model’s coefficients will always be determined using a statistical software

## Least squares: determination of coefficients

**(OPTIONAL)**

To derive the coefficients of the linear model using the least squares method, it is necessary to resort to matrix calculation. The system of equations:

∗ ∗ ∗ ∗ = 𝑏 + 𝑏 𝑥 + 𝑏 𝑥 𝑏 𝑥 𝑦1 0 1 11 2 12 + … + 𝐾 1𝐾 ∗ ∗ ∗ ∗ = 𝑏 + 𝑏 𝑥 + 𝑏 𝑥 𝑏 𝑥 𝑦2 0 1 21 2 22 + … + 𝐾 2𝐾 …. ∗ ∗ ∗ ∗ 𝑦𝑛 = 𝑏0 + 𝑏1𝑥𝑛1 + 𝑏2𝑥𝑛2 + … + 𝑏𝐾𝑥𝑛𝐾

Can be written in matrix form as:

## Least squares: determination of coefficients

**(OPTIONAL)**

To derive the coefficients of the linear model using the least squares method, it is necessary to resort to matrix calculation.

= 𝐗𝐛(∗) 𝐞(∗) = −𝐗𝐛(∗) −𝐗𝐛(∗𝐓) −𝐗𝐛(∗) 𝐲 𝐲 𝐲 𝐲 **The model The error The sum of the squares vector of the errors,** 𝑺𝑺𝑬(∗)

The vector of coefficients solution of the optimisation problem

min 𝐲−𝐗𝐛(∗𝐓) 𝐲−𝐗𝐛(∗) 𝐛(∗)

is:

−𝟏 T 𝐛= 𝐗(T) 𝐗 𝐗 𝐲

and must be calculated using a software

## Least squares: coefficients

The **`Prices*`** dataframe contains information on the weekly sales ( **`Sales`** , in appropriate units) of a product, the price ( **`Price`** ) at which it was offered (at a certain shop, as a percentage) and the price at which the main competing product was offered ( **`Price.Comp`** , percentage). ^30nbss

```
> distr.plot.xy(x=Price,y=Sales,
+               plot.type="scatter",
+               fitline=T, data=Sales)
```

- **`reg.price<-lm(Sales ~ Price, data = Sales) > reg.price Coefficients: (Intercept)  Price 206.222 -1.528`**

**Surely there is an inverse relationship between Sales and Price (product price). Can we conclude that a promotional offer to sell at a reduced price will lead to an increase in sales?** _**This analysis at the marginal level does not take into account the fact that sales probably**_ **also** _**depend on the price set for the competing product**_

- This and all other dataframes in **`Lesson 25-27_Data.Rdata`**

## Least squares: coefficients

**Sales and price of a product** . We consider the plot of residuals vs the predicted values, and the plot of the standardized residuals (obtained using the command **`rstandard(reg.price)`**

```
> plot(reg.price,which=1)
> distr.plot.xy(Sales$Price.Comp,
+               rstandard(reg.price),
+               plot.type='scatter')
```

**The residual plot shows no particular structure, except for a slight increase in the average (locally) for higher prices. However, let us consider the plot of the residuals vs. the variable** **`Price.Comp`**

_We note that the standardised residuals increase as the price set for the competing product increases: the higher the price, the higher the residual, i.e. the deviation of the observed Sales value from the forecast obtained from Price. This indicates that when the price of the competitor product is very high, sales are_ _**higher than predicted by the model**_

## Least squares: coefficients

## . **Sales and price of a product**

- **`distr.plot.xy(x=Price.Comp,y=Sales,`**

```
+               plot.type="scatter",
+               fitline=T, data=Sales)
```

```
> regr.comp<-lm(Sales ~ Price.Comp,
```

```
+               data = Sales)
> regr.comp
Coefficients:
```

```
(Intercept) Price.Comp
40.715      1.181
```

_Sales_ _**also** depend on the price of the competitor's product; not taking this into account can lead to considerable errors when the prediction of sales volume is based only on the price charged for one's own product, even though the linear regression of_ _**Sales** on_ _**Price** correctly describes the relationship between the two variables (_ _**omitted variables**: neglecting a variable related to the dependent variable in the model definition)._

## Least squares: coefficients

## **Sales and Prices:** Relationship between Sales, Price and Price.Comp.

```
> regr.sales<-lm(Sales ~ Price+Price.Comp,
+                data = Sales)
> regr.sales
Coefficients:
```

```
(Intercept)  Price Price.Comp
119.314 -1.284      1.039
```

_Multiple linear regression explains Sales as a linear function (i.e. a linear combination with weights given by the least squares coefficients) of both variables_

_**(points in grey are those lying below the regression plane).**_

## Multiple regression: Interpretation of coefficients

**Sales and prices of a product**

- ො𝑦= 119.314 −1.284𝑥1 + 1.039𝑥2

**(** 𝑦 **= Sales** , _**x**_ **1 = Price ;** _**x**_ **2 = Price.Comp)**

𝒃𝟎 **= 119.314** is the estimated **intercept.**

**It represents the expected level of sales when both the product of the company in question and the main competitor are sold at zero price.**

In this case, it is a purely technical coefficient because obviously this price combination has never been observed in the data (nor will it ever be observed, by the way)

𝒃 **= -1.284** is the estimated coefficient for **Price** 𝟏 𝒃𝟐 **= 1.039** is the estimated coefficient for **Price.Comp**

**How should the coefficients be interpreted? Can we say that for an increase of 1 Price unit we can expect an average decrease of 1.284 points in sales volume?**

## Interpretation of coefficients

## Sales and prices of a product

𝑥 In simple regression, a change of 1 unit of 1 corresponds to an average change in 𝑦 proportional to the slope of the line. **In the multiple regression model:**

𝒃 𝟎

−1.284𝑥 1.039𝑥 ො𝑦= 119.314 1 + 2 the average variation of 𝑦 corresponding to a unit variation of 𝑥1 **also** depends on 𝑥2 _**, if**_ 𝑥 2 _**can vary!**_ 𝒃𝟏 thus represents the average change in 𝑦 𝑥 corresponding to a 1 unit change in 1 𝑥 . assuming 2 **is constant**

## Evaluation of the multiple regression model

To assess the explanatory power of the multiple regression model, we refer to the **sum of squared errors** (data vs. predictions based on least squares coefficients) 𝑛 𝑛 𝑺𝑺𝑬 −𝑏 𝑥 𝑥 … −𝑏 𝑥 (𝑦𝑖 −$\hat{y}_i$)(2) (𝑦𝑖 0 −𝑏1 𝑖1 −𝑏2 𝑖2 − 𝐾 𝑖𝐾)(2) = ෍ = ෍ 𝑖=1 𝑖=1

## and the decomposition of the **sum of squares total**

## Sum of squares of the regression

## The coefficient of determination

As in the case of simple regression:

𝑺𝑺𝑹 𝑺𝑺𝑬 = 𝑹(𝟐) 𝑺𝑺𝑻(= 1 −) 𝑺𝑺𝑻 In the case of multiple regression, a modification of the R(2) is also considered, the so-called **adjusted R(2)** which also takes into account the sample size but above all the **number of** . **explanatory variables in the model** 𝑺𝑺𝑬/(𝒏−𝑲−𝟏) 𝑨𝒅𝒋𝒖𝒔𝒕𝒆𝒅𝑹(𝟐) = 1 − 𝑺𝑺𝑻/(𝒏−𝟏)

**Why?** If the number of explanatory variables included in the model is very high (compared to the number of cases), the R(2) may be excessively high and not provide a reliable measure of the model's fit (at the limit, if as many explanatory variables are used as there are cases, the R(2) would be equal to 1 regardless of the quality of the model) The **adjusted R(2)** is used to **compare the fit of models with a different number of explanatory variables**

## The coefficient of determination

**(READING)**

To illustrate why it is appropriate to use the **Adjusted R(2)** in multiple regression, we add to the model explaining **Sales** based on **Price** and **Price.Comp** an increasing number of **randomly** generated variables, which therefore have no relation with **Sales**

We monitor the R(2) of regressions that include, besides **Price** and **Price.Comp,** an increasing number of randomly generated variables. _The_ _**R**_ **(2)** _increases and approaches 1 as the number of random explanatory variables in the model increases, even if such variables have_ _**no relation to Sales**_

_This is not the case when the_ _**Adj-R**_ **(2)** _is taken into account: this goodness of fit statistic remains lower or aligned to that of the model including only_ _**Price** and_ _**Price.Comp** ._

# Multiple linear regression Weak assumptions, strong assumptions and inference on linear model parameters

## Regression model: least-squares estimators

**(READING)**

As in the case of simple regression, the results obtained from the actually observed sample are descriptive. The least-squares estimators of the model parameters in the population model:

are the counterpart of the sample least-squares coefficients obtained by substituting to the actually observed data random measurements of the response corresponding to the observed set of explanatory variables:

In order to study the properties of these estimators, and make inferences about the model parameters in the population, it is necessary to make assumptions about the characteristics of the error distribution, which are the same as those introduced for simple linear regression

## Regression model: least-squares estimators

In order to make inferences about the model parameters in the population, it is necessary to make assumptions about errors, which are the same as those introduced for simple linear 𝑛 regression. Assuming therefore that the linear model is valid for sample observations:

## Weak assumptions

The expected value of the residuals is zero: 𝐸 ε𝑖 = 0 f or each 𝑖

The variance of the residuals is the same whatever the values assumed by the explanatory variables: 𝑉𝑎𝑟 ε = σ f or each 𝑖 𝑖 ε(2)

The errors are uncorrelated i.e. 𝐶𝑜𝑟(ε𝑖, εℎ) = 0 f or each 𝑖, ℎ

**Strong assumptions**: include all the weak assumptions, and add the following: ~ The distribution of the residuals is normal ε𝑖 𝒩(0, σε(2) ) **.** Under this assumption, the residuals (and the - random - sample observations of the dependent variable) are not only uncorrelated but also independent.

## Regression model: least-squares estimators

The analytical expression of the least squares estimators and their variances is complicated (matrix-based) and in particular the variances cannot be calculated manually.

However, such estimators have the following properties:

- They are linear combinations of the (random) sample observations on the dependent variable

- Under the weak assumptions the **estimators**:

- Are **unbiased** for the corresponding model parameters in the population

- Have variance that tends to zero as the sample size increases and depends on the sample observations and also on the variance of the errors, 𝛔𝛆(𝟐) . They are also the lowest variance estimators in the class of the unbiased linear estimators (linear combinations of the sample observations on the dependent variable)

- Under the strong assumptions the estimators have a normal distribution

It is therefore possible to make inference on the parameters of the linear model in the population

## Estimator of the error variance

.

The variances of the least-squares estimators depend on the **variance of the errors** , 𝛔𝛆(𝟐) **, which is unknown and must be estimated.**

The **unbiased estimator** of 𝛔𝛆(𝟐) in the case of a model with _**K**_ explanatory variables (in addition 𝒏– 𝑲– 𝟏 to the intercept) is based on the sum of the squared errors divided by **( )** (degrees of freedom), and the corresponding estimate is:

Which is an estimate of the variance of the errors taking into account the number of observations and on the **number of estimated parameters on which the model is based** (which are the 𝑲 coefficients for the explanatory variables and the intercept, hence 𝑲+ 𝟏 ) The square root of 𝑠ε(2) , 𝑠ε , is called - as in the case of the simple linear model - **standard error of the model or standard error of the residuals**

## Estimation and inference on the model’s coefficients

## **Sales and Prices:** Relationship between Sales, Price and Price.Comp.

**`> reg_sales<-lm(Sales ~ Price+Price.Comp, data = Sales) > summary(reg_sales) # risultati della regressione Coefficients: Estimate Std. Error t value Pr(>|t|) (Intercept) 119.31366   10.38034   11.49  < 2e-16 *** Price        -1.28361    0.13085   -9.81 3.45e-16 ***` 0** **`Price.Comp    1.03933    0.08958   11.60  < 2e-16 *** --Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1 Residual standard error: 20.26 on 97 degrees of freedom Multiple R-squared:  0.739, Adjusted R-squared:  0.7336 F-statistic: 137.3 on 2 and 97 DF,  p-value: < 2.2e-16`**

Estimation of coefficients and standard errors, calculation of _**tstatistics**_ for **H0** - - _**k**_ = **0** vs **H1** - - _**k**_ - **0** and their p-values.

## Based on the output: how were test statistics and their p-value determined?

```
> tstat_Price<-(-1.28361/0.13085) # rounded values

> pvalue_Price<-2*(1-pt(abs(tstat_Price),df=97))
> print(c(tstat_Price,pvalue_Price))
```

- **`(1) -9.809782e+00  4.440892e-16`**

## Goodness of fit and global significance of the model

## **Sales and Prices:** Relationship between Sales, Price and Price.Comp.

**`> reg_sales<-lm(Sales ~ Price+Price.Comp, data = Sales) > summary(reg_sales) # regression results Coefficients: Estimate Std. Error t value  Pr(>|t|) (Intercept) 119.31366   10.38034   11.49  < 2e-16 *** Price        -1.28361    0.13085   -9.81 3.45e-16 ***`** 𝒔 **`Price.Comp    1.03933    0.08958   11.60  < 2e-16 ***`** 𝜺 **`--Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' 1 Residual standard error: 20.26 on 97 degrees of freedom` R(2)** and adjusted **R(2)** **`Multiple R-squared: 0.739, Adjusted R-squared: 0.7336 F-statistic: 137.3 on 2 and 97 DF, p-value: < 2.2e-16` ??**

**The model’s goodness of fit is assessed using the R(2)** (the adjusted **R(2)** is used to compare models with different dimension). Nonetheless, the **R(2  )** is a descriptive measure, based on the sample. The **global significance of the model is verified using the socalled** 𝑭 **test** .

## Hypothesis testing on** _**all**_ **model coefficients

The 𝑭 test is used to verify the _**overall significance of a model,**_ i.e. whether there is a significant relationship between the dependent variable and the set of **all** explanatory variables _._

Specifically, one is interested in assessing whether the model _**includes at least one explanatory variable that is significant for the explanation of the dependent variable**_ This problem can be addressed by testing the following hypotheses:

**H:** = 0 **0** β1 = ⋯= β𝐾 **H is different from 0. 1: At least one parameter** β𝑘

**If the null hypothesis is rejected, it can be concluded that** _**at least**_ **one of the coefficients in the model is significantly different from zero and that the model therefore has some validity (subject to checking which coefficient is significant by means of the specific** _**t-tests**_ **for each explanatory variable). Although this test may seem redundant, since variable-specific** _**t-tests**_ **are available, we shall see that it is actually very useful in some particular cases**

## Hypothesis testing on** _**all**_ **model coefficients

To test the hypotheses, it is necessary to identify test statistic allowing to discriminate between the null and the alternative hypotheses. In this case, the test statistic is:

𝑺𝑺𝑹/𝑲

_**F**_ = 𝑺𝑺𝑬/(𝒏−𝑲−𝟏)

That is the ratio between the **sum of the squared regression errors** 𝑺𝑺𝑹 divided by the **number of explanatory variables in the model** , 𝑲 , and the **sum of the squared residuals** 𝑺𝑺𝑬 divided by the errors’ **degrees of freedom,** (𝒏−𝑲−𝟏) = Note that since 𝑹(𝟐) 𝑺𝑺𝑹/𝑺𝑺𝑻= 1 −(𝑺𝑺𝑬/𝑺𝑺𝑻) **the statistic can be written as:**

Thus, the higher the 𝑹(𝟐) the higher is the value taken by _**F**_ . Clearly, a high 𝑹(𝟐) indicates that the model includes **at least one explanatory variable** significantly related to the dependent variable, and therefore it explains a high proportion of its variance.

## Hypothesis testing on** _**all**_ **model coefficients

In order to verify the hypotheses, the distribution of the test statistic should be known under the null hypothesis. It can be shown that **under the null H0**: β1 = ⋯= β𝐾 = 0 , the statistic

## 𝑺𝑺𝑹/𝑲

_**F**_ = 𝑺𝑺𝑬/(𝒏−𝑲−𝟏)

has an _**F**_ distribution with _**K**_ degrees of freedom at the numerator and ( 𝒏 –  𝑲 –  𝟏 ) degrees of freedom at the denominator, _**F**_ 𝑲,(𝒏−𝑲−𝟏)

A r.v. with an _**F**_ distribution takes only **non-negative** values. The _**F distribution**_ **right skewed,** and depends on two parameters, called degrees of freedom (of the numerator and of the denominator), which influence its shape.

## Hypothesis testing on** _**all**_ **model coefficients

**Test for H0:** β1 = ⋯= β𝐾 = 0 **vs H1: At least one parameter** β𝑘 **is different from zero, at a** 𝛂 **given level of significance,**

𝑺𝑺𝑹/𝑲(under ) **(H)(0)** 𝑺𝑺𝑬/(𝒏−𝑲−𝟏)

Consider the distribution of _**F**_ =

The **critical tail is the right one: high values** of _**F**_ indicate that 𝑺𝑺𝑹 **is much larger than** 𝑺𝑺𝑬 **, and that the model includes at least one significant variable. The shape of the rejection region will be: Rejection region:** _**F**_ > _**F**_ *** with** _**F**_ ***  set in such a way that Pr(Reject H0|H0 is true) =** Pr( _**F**_ > _**F**_ ***** | **H0** ) **=** - 𝟎 = = Thus, _**F**_ ***** _**F**_ 𝟏−𝛂 _F_ α;𝐾,(𝑛−𝐾−1) **the percentile of order (** 𝟏−α **) of a** _**F**_ **distribution** 𝑲,(𝒏−𝑲−𝟏)

## Hypothesis testing on** _**all**_ **model coefficients

## **Sales and Prices:** Relationship between Sales, Price and Price.Comp.

**`> reg_sales<-lm(Sales ~ Price+Price.Comp, data = Sales) > summary(reg_sales) # regression results Coefficients: Estimate Std. Error t value  Pr(>|t|) (Intercept) 119.31366   10.38034   11.49  < 2e-16 *** Price        -1.28361    0.13085   -9.81 3.45e-16 *** Price.Comp    1.03933    0.08958   11.60  < 2e-16 *** --Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' 1` Observed value of the** _**F-statistic**_ **and** **`Residual standard error: 20.26 on 97 degrees of freedom` its p-value.** **`Multiple R-squared: 0.739, Adjusted R-squared: 0.7336 F-statistic: 137.3 on 2 and 97 DF, p-value: < 2.2e-16` Conclusions?**

## Analysis of residuals

## Sales and Prices:** Relationship between Sales, Price and Price.Comp. **Assess whether there are evident violations of the assumptions by analysing the model’s residuals

```
> plot(reg_sales,which=1)
```

```
> plot(reg_sales,which=3)
```

```
> distr.plot.x(reg_sales$residuals,plot.type="histogram")
```

## Comments?

## Predictions

## The model can be used to obtain

- The point prediction of the dependent variable corresponding to values of the explanatory variables

- The **confidence** interval for the expected value of the dependent variable corresponding to specific values of the explanatory variables.

- The **prediction** interval for the value of the dependent variable corresponding to specific values of the explanatory variables.

It is clearly sensible to use the model for forecasting only when it includes significant variables and fits the data decently. In any case, the confidence and prediction intervals account for the dispersion of data around the model. They will be wider when the standard error of the model is high.

Confidence intervals for the expected value and prediction intervals corresponding to specific values of the explanatory variables can be determined in Rstudio as in the case of simple regression.

## Predictions

**Sales and Prices:** Relationship between Sales, Price and Price.Comp. **Would you use the model to forecast the average sales for shops where Price=50 and Price.Comp=25,50,75 and the sales for specific shops adopting such prices?** _The goodness of fit of the model is good, and there are no evident violations of assumptions. Therefore, we can use the model to make predictions._

```
> newdata<-data.frame(Price=50,Price.Comp=c(25,50,75))
> predict(reg_sales,newdata=newdata,
+         interval='confidence',level=0.95)
fit       lwr       upr
1  81.11674  71.82766  90.40581
2 107.10009 101.44271 112.75746
3 133.08344 128.93195 137.23492
```

**What comments on the lengths of the confidence intervals?** _**When Price.Comp=25, the width is about 18 (90-72) and decreases to about 12 (113-101) and then to 8 (137-129) when Price.Comp increases from 25 to 50 and 75 (the prediction interval differences are less pronounced in absolute terms because the width of the intervals is much larger).**_

```
> predict(reg_sales,newdata=newdata,
+         interval="prediction",level=0.95)
fit      lwr      upr
1  81.11674 39.85291 122.3806
2 107.10009 66.49931 147.7009
3 133.08344 92.66498 173.5019
```

## Multiple linear regression: customers’ retention

The dataframe **`Retention`** contains information on a simple random sample of customers **one** who made purchases only in of the shops of a chain of shops in a certain period. It is of interest to study the relationship between the customer’s propensity to buy again in the shop ( **`Retention`:** indicator based on the willingness to buy again in the shop in the future, measured by questionnaire) and the quality of the staff ( **`SalesPersons`:** evaluation of the quality of the sales staff, measured via «mystery shopping», which remained unchanged in the considered period for all the shops taken into account) and the degree of customer loyalty ( **`Loyalty`:** indicator based on a questionnaire, obtained by evaluating the degree of attachment, the propensity to «advertise» the brand on social channels, etc.). The shops are all organised in the same way and are therefore assumed to differ only in the quality of the sales staff ^buyyp4
*(See also: [[Lecture 25_27 Slides - Multiple Regression with NOTES up to L26#^s24v20]])*

## Multiple linear regression: customers’ retention

## Estimate and compare the simple regression models of** **`Retention` on** **`Loyalty` and on** **`SalesPersons`

```
distr.plot.xy(x=Loyalty,y=Retention,plot.type="scatter",
fitline=TRUE,bw=TRUE,data=Retention)
distr.plot.xy(x=SalesPersons,y=Retention,plot.type="scatter",
fitline=TRUE,bw=TRUE,data=Retention)
summary(lm(Retention ~ Loyalty, data = Retention))
summary(lm(Retention ~ SalesPersons, data = Retention))
```

**Comments on the regressions?** _The relationship between_ **`Retention`** _and_ **`Loyalty`** _is rather strong and significant*, while that between_ **`Retention`** _and_ **`SalesPersons`** _is rather weak and the coefficient has a . quite high pvalue*_ **Can we conclude that** **`SalesPersons` is irrelevant?**

ො𝑦= 19.17 + 4.84𝑥1; 𝑅(2) = 0.81 ො𝑦= 45.29 + 8.06𝑥2 ; 𝑅(2) = 0.01

* Refer to the script for details on the regressions’ results

## Multiple linear regression: customers’ retention

# Analyse graphically the relation between the residuals of the regression of** **`Retention` on** **`Loyalty` and** **`SalesPersons` . What considerations?

```
> regr.loyalty<-lm(Retention ~ Loyalty, data = Retention)
> distr.plot.xy(x=SalesPersons,y=rstandard((regr.loyalty)),
plot.type="scatter",fitline=TRUE,bw=TRUE,data=Retention)
```

## Comments?

_The plot of the standardized residuals against_ **`SalesPersons`** _exhibits a pattern (same holds for residuals)!! This violates the assumption that the expected value of the residuals is equal to 0 for any observation. The residuals increase with_ **`SalesPersons`** _, indicating that the model explains worse – on average –_ **`Retention`** _for clients visiting shops with high quality staff_ _**The structural information in residuals should be included in the deterministic component of the model**_

## Multiple linear regression: customers’ retention

## Build the multiple regression model of** **`Retention` on** **`Loyalty` and** **`SalesPersons` .

**`> regr.retention<-lm(Retention ~ Loyalty+SalesPersons, data = Retention) > summary(regr.retention) Coefficients: Estimate Std. Error t value Pr(>|t|) (Intercept)   12.4315     1.4210   8.748   <2e-16 *** Loyalty        4.8683     0.1178  41.310   <2e-16 ***`** _Selected Output_ **`SalesPersons  11.6481     1.9781   5.889    9e-09 *** --Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1 Residual standard error: 7.446 on 357 degrees of freedom Multiple R-squared:  0.8284, Adjusted R-squared:  0.8274 F-statistic: 861.6 on 2 and 357 DF,  p-value: < 2.2e-16`**

**How do you explain the different value and significance for the** **`SalesPersons` ’s coefficient in multiple regression and in the simple one based only on** **`SalesPersons` ?** _When limiting attention to the relationship between_ **`Retention`** _and_ **`SalesPersons`** _, the different level of_ **`Loyalty`** _of clients is not taken into account: less loyal customers don’t have a high propensity to return, even if the staff’s quality; opposite  holds for very loyal customers._

## Simple vs Multiple regression (IMPORTANT INTUITION!)

**Consider the two models:** ෣ 𝑅𝑒𝑡𝑒𝑛𝑡𝑖𝑜𝑛= 45.29 + 8.06 ∙𝑆𝑎𝑙𝑒𝑠𝑃𝑒𝑟𝑠𝑜𝑛𝑠 ; 𝑅(2) = 0.01 ෣ 𝑅𝑒𝑡𝑒𝑛𝑡𝑖𝑜𝑛= 12.43 + 4.87 ∙𝐿𝑜𝑦𝑎𝑙𝑡𝑦+ 11.65 ∙𝑆𝑎𝑙𝑒𝑠𝑃𝑒𝑟𝑠𝑜𝑛𝑠 ; 𝑅(2) = 0.83 They are both **correct** , but

- The first model estimates the **average variation of** **`Retention` as** **`SalesPersons` changes** - The second model estimates the **average variation of** **`Retention` as** **`SalesPersons` changes, for clients with a certain level of** **`Loyalty`**

Thus, the first model compares the average level of **`Retention`** for clients visiting shops with levels of **`SalesPersons`** respectively low and high; since these two groups of clients include both loyal and non loyal clients, the effect of **`SalesPersons`** does not emerge! When the second model is used, the comparison is more accurate and reasonable, because the model compares the average level of **`Retention` for clients with a certain level of loyalty** who buy in shops with a low or high (evaluated) staff’s quality, **thus taking the level of loyalty under control.** This allows a fair comparison, taking into account **also** the effect of loyalty on **`Retention`**

## Multiple linear regression: customers’ retention

## Estimate the 95% confidence intervals for the model’s coefficients

```
> confint(regr.retention)
2.5 %    97.5 %
(Intercept)  9.636895 15.226158
Loyalty      4.636540  5.100068
SalesPersons 7.757942 15.538303
```

## Interpretation?

_With a confidence 95% we can conclude that for customers with the same level of_ **`Loyalty`** _, a 1 unit increase in the quality of sales staff corresponds to an increase in the average level of_ **`Retention`** _between 4.64 and 5.1. Similar interpretation for the coefficient of_ **`SalesPersons`**

**Would you conclude that** **`SalesPersons` is more relevant than** **`Loyalty` in the explanation of** **`Retention` ?**

_No; for a 1-unit increase in_ **`SalesPersons`** _an average increase in_ **`Retention`** _is expected higher than that corresponding to a 1-unit change in_ **`Loyalty`** _. However, the coefficient of_ **`Loyalty`** _is definitely more significant than that of_ **`SalesPersons`** _. Moreover, the «standard» deviation of_ **`Loyalty`** _is 3.34, much greater than 0.2, the standard deviation of_ **`SalesPersons`** _(which takes values between 0 and 1!!). (see the script for details)_

## Multiple linear regression: customers’ profitability

The dataframe **`Bank.Invest`** contains information on the (estimated) wealth of a sample of customers ( **`Wealth`** , in appropriate units), the profitability of customers for the bank ( **`Profit`** , measured by an indicator linked to returns, type of contract, amount deposited, securities deposit, etc.). For each customer, the marketing strategy applied is also available ( **`Strategy`** )

## Estimate the model relating** **`Profit` to** **`Wealth`

```
> regr.bank<-lm(Profit ~ Wealth, data = Bank.Invest)
> summary(regr.bank)
```

## `Coefficients:`

```
Estimate Std. Error t value Pr(>|t|)
(Intercept) 42.84728   10.13984   4.226 3.8e-05 ***
Wealth       0.06311    0.00286  22.065 < 2e-16 ***

```

## Selected Output

```
Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' 1
Residual standard error: 54.83 on 178 degrees of freedom
Multiple R-squared: 0.7323, Adjusted R-squared: 0.7308
F-statistic: 486.9 on 1 and 178 DF, p-value: < 2.2e-16
```

## Comments?

## Multiple linear regression: customers’ profitability

## Discuss about possible violations of model’s assumptions

```
plot(regr.bank,which=1)
plot(regr.bank,which=3)
distr.plot.x(regr.bank$residuals,plot.type="histogram")
```

## Comments?

## Multiple linear regression: customers’ profitability

## Relationship between** **`Profit` and** **`Wealth.` Analyse the relationship between the model’s residuals and the variable** **`Strategy`

- **`distr.plot.xy(x=Strategy,y=regr.bank$residuals,plot.type="boxplot", +               data=Bank.Invest)`**

## Considerations?

_The structural characteristics of residuals (same holds for standardized residuals) – at least their central tendency (median, but also mean) vary with the strategy adopted to retain/increase customer profitability When strategy_ _**B** is adopted residuals have a median around 0; turning to strategy_ _**A** residuals exhibit different features: median around -50, box including only negative values and maximum slightly above 0: the variable Profit variable is structurally_ _**over-estimated** for this group of customers. The opposite is observed for strategy C!_

## Multiple linear regression: customers’ profitability

**Relationship between** **`Profit` and** **`Wealth.` Analyse the relation between the model’s residuals and the variable** **`Strategy`** To visualise the relation between residuals and a possibly omitted qualitative variable it is also possible to use the function **`distr.plot.xy`** , to obtain the scatterplot of residuals against fitted values, specifying that cases should be coloured based on the values taken **`var.c`** by the variable specified using the argument

```
> distr.plot.xy(x=regr.bank$fitted.values,
+               y=regr.bank$residuals,
+               plot.type="scatter",
+               var.c=Bank.Invest$Strategy)
```

## Considerations?

_The plot confirms conclusions drawn based on the side-by-side boxplots! The average of residuals changes with the strategy._ **How to include qualitative variables in a regression model?**

## Multiple linear regression and qualitative variables

**Relationship between** **`Profit` and** **`Wealth.`** In the case of this simple linear model, we can evaluate the 'effect' of **`Strategy`** on the dependent variable graphically.

```
> distr.plot.xy(x=Wealth,y=Profit, plot.type="scatter", var.c=Strategy,
```

```
+               data=Bank.Invest)
```

## Considerations?

_We note that the_ _**intercept of the model varies as**_ **`Strategy`** _**varies**_

## Multiple linear regression: dummy variables

Let us consider the following specification for the model that explains the dependent variable _**Y**_ (here, **`Profit`** ) as a function of a set of numerical explanatory variables (here, only one explanatory variable, 𝑿1 = **`Wealth`** ) in the case when a qualitative variable (here, **`Strategy`** , which takes only 3 distinct values) has an effect on the model intercept: **Level A:** _**Y**_ **= Intercept A** +β1𝒙1 + ε 𝒙 **=** 𝒙 𝛃𝟎 + β1 1 + ε 𝛃𝟎𝑨 + β1 1 + ε **Level B:** _**Y**_ **= Intercept B** +β1𝒙1 + ε **=** 𝒙 𝛃𝟎 + 𝛃𝑩 + β1𝒙1 + ε 𝛃𝟎𝑩 + β1 1 + ε **Level C:** _**Y**_ **= +** _**x**_ **+** e **Intercept C** - **1 1 =** 𝛃𝟎𝑪 + β1𝒙1 + ε 𝛃𝟎 + 𝛃𝑪 + β1𝒙1 + ε

Models with different intercepts corresponding to different levels of the qualitative variable . can be combined into a single model using the so-called **indicator or dummy variables**

## Multiple linear regression: dummy variables

**Dummy** variables are binary variables that **indicate** whether a condition is fulfilled (in which case they take value 1) or not (in which case they take value 0)

1 if the condition **is met** I= 0 if the condition **is not met**

For example, with reference to the data we are considering:

**1 if strategy A was adopted with the customer I = A 0 if strategy A was not adopted with the customer 1 if strategy B was adopted with the customer I = B 0 if strategy B was not adopted with the customer 1 if strategy C was adopted with the customer I = C not a 0 if strategy C was dopted with the customer**

## Multiple linear regression: dummy variables

**The dummy** variables, which in the present case indicate which strategy was adopted with the customer, would be:

Note that, for each case, given the values taken by 𝐈𝐵 e 𝐈𝐶 the value taken by 𝐈𝐴 is known

## Multiple linear regression: dummy variables

The model based on intercepts varying with the strategy adopted is:

_**Y**_ **=** 𝐈 𝐈 𝒙 β0 +β𝐵 𝐵 +β𝐶 𝐶 +β1 1 +ε

**Level A** (𝐈𝐵= 0, 𝐈𝐶 = 0) **:** _**Y**_ **=** β0 + β1𝒙1 +ε **Level B** (𝐈𝐵= 1, 𝐈𝐶 = 0) **:** _**Y**_ **=** β0 + β𝐵 + β1𝒙1 +ε **Level C** (𝐈𝐵= 0, 𝐈𝐶 = 1) **:** _**Y**_ **=** β0 + β𝐶 + β1𝒙1 +ε

Thus, two **additional intercepts** are added to the model, indicating the **change in the intercept for** customers for whom strategy B or C was adopted. The intercept refers to the model intercept at the level **chosen as base/reference,** in this case level **A.** Clearly, the model can be parameterised differently by choosing another level as the base. In essence, to include a qualitative variable with 𝑳 levels in the model, ( 𝑳−𝟏 ) indicator variables are added.

## Multiple linear regression: customers’ profitability

The function **`lm()`** automatically defines dummy variables for a qualitative variable or factor, setting as reference category the first (alphabetical order or order of factor’s level)

**`> regr.bank<-lm(Profit~ Wealth + Strategy, data = Bank.Invest) > summary(regr.bank) Coefficients: Estimate Std. Error t value Pr(>|t|) (Intercept) -11.974381   6.345635  -1.887   0.0608 . Wealth        0.063049   0.001556  40.532   <2e-16 *** StrategyB    52.811764   5.444007   9.701   <2e-16 ***`** _Selected Output_ **`StrategyC   112.280339   5.444015  20.625   <2e-16 *** --Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1 Residual standard error: 29.82 on 176 degrees of freedom Multiple R-squared:  0.9217, Adjusted R-squared:  0.9204 F-statistic: 690.7 on 3 and 176 DF,  p-value: < 2.2e-16`**

**Would you prefer this model to that based on** **`Wealth` only??** _The variables related to the adopted strategy are all significant, and indeed the adjusted R(2) increases from 0.73 to 0.92. Therefore this model is preferable to the previous one!_

## Multiple linear regression: customers’ profitability

## Consider the estimated model’s coefficients:

```
Coefficients:
Estimate Std. Error t value Pr(>|t|)
(Intercept) -11.974381   6.345635  -1.887   0.0608 .
Wealth        0.063049   0.001556  40.532   <2e-16 ***
StrategyB    52.811764   5.444007   9.701   <2e-16 ***
StrategyC   112.280339   5.444015  20.625   <2e-16 ***
```

**How do you interpret the coefficients related to the adopted strategy?** _The coefficients of the dummy variables for the levels of the variable_ **`Strategy`** _indicate the estimated mean difference in profit when a strategy alternative to A (which is the reference category) is adopted, keeping_ **`Wealth`** _fixed._

_For example, considering_ _**customers with the same Wealth** , adopting strategy B entails an expected and significant increase in profit of 52 units compared to adopting strategy A; a similar interpretation holds for strategy C_

## Multiple linear regression: customers’ profitability

## Consider the estimated model’s coefficients:

```
Coefficients:
Estimate Std. Error t value Pr(>|t|)
(Intercept) -11.974381   6.345635  -1.887   0.0608 .
Wealth        0.063049   0.001556  40.532   <2e-16 ***
StrategyB    52.811764   5.444007   9.701   <2e-16 ***
StrategyC   112.280339   5.444015  20.625   <2e-16 ***
```

**Can we conclude that (for fixed values of Wealth) adopting strategy C entails a mean profit significantly higher compared to adopting strategy B?** _Even if the difference between the two estimated coefficients is high (112.28-52.81=59.47), the coefficients of the dummy variables (and their significance) in this model refer to the expected difference in the mean profit entailed by strategies B and C compared to A. Therefore, to properly_ _**test** whether the difference between B and C is significant we need to re-estimate the model setting one of the two categories as the reference. By doing so we find that the expected difference in profit when strategy C rather than B is adopted (for given values of Wealth) is highly significant (p-value<2e-16)  (procedure in the script)_

## Multiple linear regression: music downloads

The dataframe **`Downloads`** contains information on the sales performance (sales from downloaded tracks, **`Sales`** ) recorded for the tracks of a sample of artists in a certain country: besides the amount spent in advertising ( **`Ads` .** **`Exp`** , in Euro), the dataframe includes the average number of weekly radio plays ( **`Radio`** ), the popularity of the artist ( **`Popularity`** , index from 1 to 100), the genre of music ( **`Genre`** ) and finally a variable indicating whether the artist is also known internationally (concerts abroad, plays on foreign radio stations, followers of different nationalities, variable **`International`** )

## Multiple linear regression: music downloads

## Estimate the model relating sales performance to advertising expenditure, popularity and (national) radio airplay.

**`> regr.music<-lm(Sales ~ Ads.Exp+Radio+Popularity, data = Downloads) > summary(regr.music) Coefficients: Estimate Std. Error t value Pr(>|t|)`** _Selected Output_ **`(Intercept) -31.467024  17.863068  -1.762   0.0797 . Ads.Exp       0.085323   0.006897  12.370  < 2e-16 *** Radio         3.361137   0.276994  12.134  < 2e-16 *** Popularity    1.104823   0.235972   4.682  5.3e-06 *** --Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1 Residual standard error: 46.95 on 196 degrees of freedom Multiple R-squared:  0.6666, Adjusted R-squared:  0.6615 F-statistic: 130.6 on 3 and 196 DF,  p-value: < 2.2e-16`**

## Model’s significance? Goodness of fit?

**Interpretation of coefficients? Can we conclude that** **`Radio` is the most relevant variable for** **`Sales` ?**

## Multiple linear regression: music downloads

**Determine the 99% confidence intervals for the model’s parameters**

```
> confint(regr.music, level=0.99)
```

```
0.5 %     99.5 %
(Intercept) -77.93146121 14.9974126
Ads.Exp       0.06738164  0.1032639
Radio         2.64063581  4.0816383
Popularity    0.49102435  1.7186209
```

**Based on the estimated model (and on the output of the regression) illustrate how the confidence interval for** **`Radio` was built and provide its interpretation Can we say something about the expected difference in the average sales performance of songs by artists having popularity indices that differ by 10 points? If not, explain why, discuss about whether (and which) specific assumptions are needed to answer and, eventually answer under such assmptions.**

## Multiple linear regression: music downloads

# Verify whether the assumptions at the basis of the model appear violated in any sense via the analysis of its residuals

```
plot(regr.music,which=1)
plot(regr.music,which=3)
distr.plot.x(regr.music$residuals,plot.type="histogram")
```

## Comments?

## Multiple linear regression: music downloads

## Analyze the possible relation between model’s residuals and the variables** **`International` and** **`Genre` .

- **`distr.plot.xy(x=International,y=regr.music$residuals,plot.type="boxplot", +               data=Downloads) > distr.plot.xy(x=Genre,y=regr.music$residuals,plot.type="boxplot", +               data=Downloads)`**

**What considerations? Would you suggest adding such variables to the model?**

## Multiple linear regression: music downloads

## Estimate the model including, besides the variables considered before, also** **`International` and** **`Genre`

```
> regr.music<-lm(Sales ~ Ads.Exp+Radio+Popularity+International+Genre,
+                data = Downloads)
> summary(regr.music)
Coefficients:
```

**Would you prefer this model to the simpler one?**

```
Estimate Std. Error t value Pr(>|t|)
(Intercept)      -36.221914  16.993992  -2.131 0.034317 *
Ads.Exp            0.072678   0.006535  11.121  < 2e-16 ***
Radio              2.702598   0.267029  10.121  < 2e-16 ***
Popularity         1.059742   0.211760   5.004 1.26e-06 ***
InternationalYes  41.114589   8.360607   4.918 1.87e-06 ***
Genrepop          47.852953  10.435878   4.585 8.13e-06 ***
Genreelectronic   27.751379   8.132335   3.412 0.000784 ***

Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
Residual standard error: 41.97 on 193 degrees of freedom
Multiple R-squared:  0.7376, Adjusted R-squared:  0.7295
F-statistic: 90.44 on 6 and 193 DF,  p-value: < 2.2e-16
```

**Interpretation of the coefficient of** **`Interpretation` ? How does** **`Sales` vary depending on** **`Genre` ? Is it possible to assess whether the difference between pop and electronic genre is significativa?**

## Multiple linear regression: music downloads

## Obtain a 95% interval for the predicted sales corresponding to advertising expenses of 500, 1000 or 1500 for the song of an internationally known pop artist with a popularity level of 60, for whom an average number of radio plays of 55 is expected.

- **`newdata<-data.frame(Ads.Exp=c(500,1000,1500),Radio=55,Popularity=60, +                     International="Yes",Genre="pop") > predict(regr.music,newdata=newdata,`**

- **`+         interval="prediction",level=0.95) fit      lwr      upr 1 301.3121 215.7997 386.8244 2 337.6510 252.2812 423.0209 3 373.9900 288.2769 459.7031`**

## Multiple linear regression: house prices

A real estate agency (U.S.A.) is interested in estimating the selling price of a house **(** **`Price` )** as a function of a few selected characteristics, such as size ( **`HSize`** ), number of bedrooms ( **`Bedrooms`** ) and plot size ( **`LSize`** ). Data for a sample of 87 houses are included in the dataframe **`House`** .

## Estimate the model

```
> reg_house<-lm(Price ~ Bedrooms+HSize+LSize,
+               data = House)
> summary(reg_house)
Coefficients:
```

```
Estimate Std. Error t value Pr(>|t|)
(Intercept) 42669.838  15166.580   2.813  0.00612 **
Bedrooms    -1573.490   7731.835  -0.204  0.83924
HSize          58.898     57.080   1.032  0.30514
LSize           2.685     18.557   0.145  0.88531

```

```
Residual standard error: 24920 on 83 degrees of freedom
Multiple R-squared:  0.5599, Adjusted R-squared:  0.544
F-statistic: 35.19 on 3 and 83 DF,  p-value: 8.961e-15
```

## Comments?

_The model is_ _**globally significant** (_ _**F-test** ) and has a good_ _**fit** (R(2) )._

_However, none of the explanatory variables is significant! Moreover, the coefficient of_ **`Bedrooms`** _is negative, which contradicts reasonable expectations!_

## Multiple linear regression: house prices

**Estimate the simple linear regression model of** **`Price` on each explanatory variable** Simple linear regressions and their R(2 ) (syntax in the script)

## Comments?

_The three explanatory variables are all significantly related to_ **`Price`** _when taken individually, but become non-significant (and for_ **`Bedrooms`** _, the sign is reversed) when included in a multiple regression model_

## Multiple linear regression: house prices

## Consider the correlations between all the pairs of variables (all numeric) in the dataframe

```
> cor(House)
Price  Bedrooms     HSize     LSize
Price    1.0000000 0.6306415 0.7480247 0.7444450
Bedrooms 0.6306415 1.0000000 0.8531433 0.8499681
HSize    0.7480247 0.8531433 1.0000000 0.9937202
LSize    0.7444450 0.8499681 0.9937202 1.0000000
```

The explanatory variables are strongly The dependent variable is correlated with each other! correlated with all explanatory variables considered

## Multiple linear regression: house prices

## A closer look at the multiple regression model

## `Coefficients:`

```
Estimate Std. Error t value Pr(>|t|)
(Intercept) 42669.838  15166.580   2.813  0.00612 **
Bedrooms    -1573.490   7731.835  -0.204  0.83924
HSize          58.898     57.080   1.032  0.30514
LSize           2.685     18.557   0.145  0.88531

```

```
Residual standard error: 24920 on 83 degrees of freedom
Multiple R-squared: 0.5599, Adjusted R-squared: 0.544
F-statistic: 35.19 on 3 and 83 DF,  p-value: 8.961e-15
```

Regression coefficients describe the average **change** in the dependent variable corresponding to a change in **one of** the explanatory variables _**while controlling for all the others, or in other words, when the other variables are included in the model.**_

Since the explanatory variables are **strongly correlated** , none of them adds any **significant information** to a **model including the others** . Thus, each variable turns out to be **redundant** , because the other two have basically the **same information content** (in this case, they are all related to size). **As a consequence, none of the variables is able to significantly contribute to a model that already includes the other two.**

This situation occurs in the case of **multicollinearity, that is when the explanatory variables are so correlated that one masks the effect of the other on the dependent variable**

## Multicollinearity: the problem

It may be the case that some (not necessarily all) of the explanatory variables are **highly** correlated . with each other ( **multicollinearity)**

**In this case, a change in one of these explanatory variables also leads to a change in the others (e.g. in the previous case, if the number of bedrooms increases, the size of the house generally** . **increases)**

This leads to **high standard errors of the coefficients, as it** is not possible to vary a single variable 'while keeping all the others fixed': the higher the correlation between the explanatory variables, the more difficult it is to separate the effect of the individual variables on the prediction of the values of the dependent variable.

Accordingly:

- The estimates of the coefficients may be very distant from the true values of the parameters (due to the high dispersion of the distribution of the estimators). In extreme situations, it may even happen that the estimates have an opposite sign to the expected one.

- Due to the high standard errors of the estimators, the _**t-statistics**_ used for hypothesis testing (defined as the ratio of coefficient to standard error) are very small, leading to the (erroneous) acceptance of the hypothesis that the parameters are zero in the population.

Fortunately, multicollinearity has no effect on the R(2) , the _**F-statistic**_ **and the** _**F-test**_ **.**

## Multiple linear regression: house prices

## Multicollinearity, R(2) , and** _**F**_ **-test

## `Coefficients:`

```
Estimate Std. Error t value Pr(>|t|)
(Intercept) 42669.838  15166.580   2.813  0.00612 **
Bedrooms    -1573.490   7731.835  -0.204  0.83924
HSize          58.898     57.080   1.032  0.30514
LSize           2.685     18.557   0.145  0.88531

```

```
Residual standard error: 24920 on 83 degrees of freedom
Multiple R-squared: 0.5599, Adjusted R-squared: 0.544
F-statistic: 35.19 on 3 and 83 DF,  p-value: 8.961e-15
```

_The contradiction between the_ _**F-test** and the R_ _**(2)** and the_ _**t-tests** , and the sign opposed to the expected one for_ **`Bedrooms`** _is due to the presence of multicollinearity, which leads to very high standard errors, and thus low_ _**tstatistics** , leading to the acceptance of the null hypothesis of the coefficients_

Multicollinearity may be due either to the existence of direct correlations between the explanatory variables (as in this case, where we observe high correlations between all pairs of explanatory variables) or to more complex linear relationships, which are not necessarily reflected in high correlations. Thus, in addition to specific tests to verify any relationships between each of the explanatory variables and the others, the non-significance of some variables that should at least theoretically be relevant, the possible discordance between F-test and R(2) and _**t**_ tests, and possibly coefficients with a sign opposite to the expected one are some of the signals of the possible presence of multicollinearity

## Multiple linear regression: house prices

A possible solution (sometimes too simplistic) when multicollinearity is linked to strong bivariate correlations between some explanatory variables, is to select only one of the explanatory variables linked by a strong linear correlation.

```
> reg_house<-lm(Price ~ HSize, data = House)
> summary(reg_house)
Coefficients:
```

```
Estimate Std. Error t value Pr(>|t|)
(Intercept) 40970.982  11392.034   3.596 0.000541 ***
HSize          64.919      6.247  10.391  < 2e-16 ***

```

```
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
```

```
Residual standard error: 24640 on 85 degrees of freedom
Multiple R-squared:  0.5595, Adjusted R-squared:  0.5544
F-statistic:   108 on 1 and 85 DF,  p-value: < 2.2e-16
```

_**Here we use the variable singularly most correlated with the dependent variable . Note that the coefficient of determination is almost the same obtained using all three explanatory variables and the adjusted R2 increases!!!**_

**Multicollinearity problems are typically diagnosed using more sophisticated measures, allowing identifying more complex relations, not necessarily evidenced by correlation coefficients. Moreover, the problem is solely solved resorting to procedures for the automatic selection of the model or more refined approaches not covered in this course**

## Hotel location and performance

**Location of a business (hotel)**

A hotel chain (U.S.A.) is considering expansion.

Management is interested in **assessing** the **performance of existing hotels** and predicting . **the profitability of new hotels depending on their possible location** The following predictors of profitability were identified:

- Level of competition

- Market awareness

- Demand generators

- Socio-demographic characteristics of the resident community

- Quality of the position

## Hotel location and performance

## The model

## Hotel location and performance

## **The data.** Information is collected on 100 hotels in the chain

## The model:

**Margin =** 𝛃𝟎 **+** 𝛃𝟏 **Number +** 𝛃𝟐 **Nearest +** 𝛃𝟑 **Office +** 𝛃𝟒 **Enrollment +** 𝛃𝟓 **Income + +** 𝛃𝟔 **Distance +** 𝛆

## Hotel location and performance

## Estimation of the multiple regression model

- **`reg_hotel<-lm(Margin ~ Number+Nearest+Office+Enrollment+Income+Distance, +               data = Hotel) > summary(reg_hotel)`**

## `Coefficients:`

- **`Estimate Std. Error t value   Pr(>|t|) (Intercept) 38.138575.  6.992948   5.454   4.04e-07 *** Number      -0.007618   0.001255  -6.069   2.77e-08 *** Nearest      1.646237   0.632837   2.601     0.0108 * Office       0.019766   0.003410   5.796   9.24e-08 *** Enrollment   0.211783   0.133428   1.587     0.1159 Income       0.413122   0.139552   2.960     0.0039 ** Distance    -0.225258   0.178709  -1.260     0.2107 ---`**

**Goodness of fit?** _The model and explains the 52.51% of the variance of the operating margin_

```
Residual standard error: 5.512 on 93 degrees of freedom
Multiple R-squared: 0.5251, Adjusted R-squared: 0.4944
F-statistic: 17.14 on 6 and 93 DF, p-value: 3.034e-13
```

## Hotel location and performance: analysis of residuals

Before using the model, we analyse the residuals to check whether the plot of residuals has no structure, whether the variance of the errors is approximately constant and whether the distribution of errors is at least approximately normal

No obvious violations of assumptions, even if the distribution of the errors is slightly skewed (note: this is confirmed by more specific tests which we do not cover in the course)

## Normality and Homoschedasticity Tests

**(OPTIONAL)**

Even if we will not study them, consider the results of some tests (typically covered in more advanced courses) of normality and of homosjedasticity. Note indeed that the graphical analysis of residuals allows drawing conclusions only when the assumptions violations are very evident, and in some cases might lead to conclusions depending on the analyst (eye)

_Even if we do not know how the tests statistics are built, we can conclude that the null hypoheses of normality and of omoskedasticity of residuals_ _**cannot be rejected** because the p- values are higher than any_ 𝛼 _standard value of_

**Test for homoskedasticity (H0: Residuals are Homoskedastic)** Breusch-Pagan statistic: BP = 4.11, p-value = 0.66

## Test for normality

**(H0: Residuals’ distribution is normal)** Shapiro-Wilk statistic: W = 0.98, p-value = 0.21 Kolmogorov-Smirnov statistic: D = 0.07, p-value = 0.68

## Hotel location and performance

## Inference on the model for population: Global significance of the model

```
> reg_hotel<-lm(Margin ~ Number+Nearest+Office+Enrollment+Income+Distance,
+               data = Hotel)
```

```
> summary(reg_hotel)
```

## Comments?

```
Coefficients:
```

```
Estimate Std. Error t value Pr(>|t|)
(Intercept) 38.138575   6.992948   5.454 4.04e-07 ***
Number      -0.007618   0.001255  -6.069 2.77e-08 ***
Nearest      1.646237   0.632837   2.601   0.0108 *
Office       0.019766   0.003410   5.796 9.24e-08 ***
Enrollment   0.211783   0.133428   1.587   0.1159
Income       0.413122   0.139552   2.960   0.0039 **
Distance    -0.225258   0.178709  -1.260   0.2107

```

_Based on the F-test, we reject the null hypothesis that all the coefficients in the model are null, and conclude that at least one of them is significantly different from 0. Hence, at least one explanatory variable is significantly related to the dependent variable. The  model is_ _**globally valid.**_

```
Residual standard error: 5.512 on 93 degrees of freedom
Multiple R-squared:  0.5251, Adjusted R-squared:  0.4944
F-statistic: 17.14 on 6 and 93 DF,  p-value: 3.034e-13
```

## Hotel location and performance

## Inference on the model for population: Model’s coefficients

```
> reg_hotel<-lm(Margin ~ Number+Nearest+Office+Enrollment+Income+Distance,
+               data = Hotel)
```

```
> summary(reg_hotel)
```

## Most relevant explanatory variables?

```
Coefficients:
```

_The relative importance of each variable cannot be assessed by the magnitude of the estimated coefficient - which has a unit of measurement - but rather by its p- value._

```
Estimate Std. Error t value Pr(>|t|)
(Intercept) 38.138575   6.992948   5.454 4.04e-07 ***
Number      -0.007618   0.001255  -6.069 2.77e-08 ***
Nearest      1.646237   0.632837   2.601   0.0108 *
Office       0.019766   0.003410   5.796 9.24e-08 ***
Enrollment   0.211783   0.133428   1.587   0.1159
Income       0.413122   0.139552   2.960   0.0039 **
Distance    -0.225258   0.178709  -1.260   0.2107

```

_For example,_ **`Number`** _**has the** smallest coefficient but the highest value of the t-statistic_ _**. To assess the significance of the explanatory variables we refer to their p-value**_

```
Residual standard error: 5.512 on 93 degrees of freedom
Multiple R-squared:  0.5251, Adjusted R-squared:  0.4944
F-statistic: 17.14 on 6 and 93 DF,  p-value: 3.034e-13
```

## Hotel location and performance

## Inference on the model for population: Model’s coefficients

```
> reg_hotel<-lm(Margin ~ Number+Nearest+Office+Enrollment+Income+Distance,
+               data = Hotel)
```

**Most relevant explanatory variables?**

```
> summary(reg_hotel)
```

_**Number** and_ _**Office** are the two most significant variables._ **Interpretation of coefficients?** _**All other conditions being equal: Number:** For each additional room within 3 miles, Margin (the operating margin %) decreases on average by .0076._

```
Coefficients:
```

```
Estimate Std. Error t value Pr(>|t|)
(Intercept) 38.138575   6.992948   5.454 4.04e-07 ***
Number      -0.007618   0.001255  -6.069 2.77e-08 ***
Nearest      1.646237   0.632837   2.601   0.0108 *
Office       0.019766   0.003410   5.796 9.24e-08 ***
Enrollment   0.211783   0.133428   1.587   0.1159
Income       0.413122   0.139552   2.960   0.0039 **
Distance    -0.225258   0.178709  -1.260   0.2107

```

_**Office**: for every additional 1000 sqft of office space_ _**Margin** increases on average by .02._

```
Residual standard error: 5.512 on 93 degrees of freedom
Multiple R-squared:  0.5251, Adjusted R-squared:  0.4944
F-statistic: 17.14 on 6 and 93 DF,  p-value: 3.034e-13
```

## Hotel location and performance

## Inference on the model for population: Model’s coefficients

```
> reg_hotel<-lm(Margin ~ Number+Nearest+Office+Enrollment+Income+Distance,
+               data = Hotel)
```

**Most relevant explanatory variables?**

```
> summary(reg_hotel)
```

_**All other** conditions being_ _**equal: Income**: For every $1000 increase in median household income,_ _**Margin** increases on average by .41; the variable is only significant if_ α _>0.004!_

```
Coefficients:
```

```
Estimate Std. Error t value Pr(>|t|)
(Intercept) 38.138575   6.992948   5.454 4.04e-07 ***
Number      -0.007618   0.001255  -6.069 2.77e-08 ***
Nearest      1.646237   0.632837   2.601   0.0108 *
Office       0.019766   0.003410   5.796 9.24e-08 ***
Enrollment   0.211783   0.133428   1.587   0.1159
Income       0.413122   0.139552   2.960   0.0039 **
Distance    -0.225258   0.178709  -1.260   0.2107

Residual standard error: 5.512 on 93 degrees of freedom
Multiple R-squared:  0.5251, Adjusted R-squared:  0.4944
F-statistic: 17.14 on 6 and 93 DF,  p-value: 3.034e-13
```

_**Nearest**: For each additional mile away from the nearest competitor,_ _**Margin** increases on average by 1.65. The p-value just above 0.01, leads to accepting the hypothesis that the coefficient is null at this level_

## Hotel location and performance

## Inference on the model for population: Model’s coefficients

```
> reg_hotel<-lm(Margin ~ Number+Nearest+Office+Enrollment+Income+Distance,
+               data = Hotel)
```

## Considerations on Enrollment and Distance?

```
> summary(reg_hotel)
```

_There is insufficient evidence to reject the hypothesis that_ _**Distance** and_ _**Enrollment** do not_ _**contribute** significantly to the explanation of_ _**Margin** , once_ _**the other explanatory variables are included in the model.**_

```
Coefficients:
```

```
Estimate Std. Error t value Pr(>|t|)
(Intercept) 38.138575   6.992948   5.454 4.04e-07 ***
Number      -0.007618   0.001255  -6.069 2.77e-08 ***
Nearest      1.646237   0.632837   2.601   0.0108 *
Office       0.019766   0.003410   5.796 9.24e-08 ***
Enrollment   0.211783   0.133428   1.587   0.1159
Income       0.413122   0.139552   2.960   0.0039 **
Distance    -0.225258   0.178709  -1.260   0.2107

```

```
Residual standard error: 5.512 on 93 degrees of freedom
Multiple R-squared:  0.5251, Adjusted R-squared:  0.4944
F-statistic: 17.14 on 6 and 93 DF,  p-value: 3.034e-13
```

## Hotel location and performance

## Inference on the model for population: Model’s coefficients

```
> reg_hotel<-lm(Margin ~ Number+Nearest+Office+Enrollment+Income+Distance,
+               data = Hotel)
```

**Can we conclude that Enrollment and Distance are not related to Margin based on the observed results?**

```
> summary(reg_hotel)
```

```
Coefficients:
```

```
Estimate Std. Error t value Pr(>|t|)
(Intercept) 38.138575   6.992948   5.454 4.04e-07 ***
Number      -0.007618   0.001255  -6.069 2.77e-08 ***
Nearest      1.646237   0.632837   2.601   0.0108 *
Office       0.019766   0.003410   5.796 9.24e-08 ***
Enrollment   0.211783   0.133428   1.587   0.1159
Income       0.413122   0.139552   2.960   0.0039 **
Distance    -0.225258   0.178709  -1.260   0.2107
```

_No! The two variables_ _**could** be related to Margin - their relationship to Margin must be verified. From the results, it is only possible to say that neither variable significantly improves a model that includes all other variables_

```

```

```
Residual standard error: 5.512 on 93 degrees of freedom
Multiple R-squared:  0.5251, Adjusted R-squared:  0.4944
F-statistic: 17.14 on 6 and 93 DF,  p-value: 3.034e-13
```

**Even if Enrollment and Distance do not contribute significantly to the model, it is not good practice to simply remove them, as there may be relationships with the other explanatory variables. Thus, we consider the model as it is in order to keep all explanatory vars under control**

## Hotel location and performance

We want to evaluate a potential location for the new hotel, with the following characteristics:

- 3815 rooms available within 3 miles ( **`Number`** =3815),

- Nearest competitor at 0.9 miles ( **`Nearest`** =0.9),

- 476,000 sq-ft of office space ( **`Office`** =476),

- 24,500 university students ( **`Enrollment`** =24.5),

- Median income of households living in the area $35,000 ( **`Income`** =35),

- Distance to the centre: 11.2 miles ( **`Distance`** =11.2)

**What is the point forecast of the average profitability (as measured by the profit margin %) for hotels located in an area with these characteristics? And of a specific hotel?**

- ො𝑦𝑔 **= 38.14 – 0.0076·3815 +1.65·0.9  + 0.020·476 + 0.21·24.5 + 0.41·35 – 0.23·11.2**

- **=  37.07**

## Hotel location and performance

## Predict the performance of the average operating margin of hotel located in sites with the considered characteristics and of the operating margin of a specific hotel

```
> to_predict <- data.frame(Number= 3815,Nearest=0.9,Office=476,Income=35,
+                          Distance=11.2,Enrollment=24.5)
```

```
>
```

```
> predict(reg_hotel, to_predict,interval = "confidence", level = 0.95)
fit      lwr      upr
```

- **`1 37.09149 32.96972 41.21326`**

```
> predict(reg_hotel, to_predict,interval = "prediction", level = 0.95)
fit      lwr      upr
1 37.09149 25.39525 48.78772
```

**A hotel is considered very profitable if its operating margin is more than 50%. Comments?**

With a 95% confidence we can conclude that on average hotels located in areas with the considered characteristics have operating margins between 32 e 41, thus lower than 50. Even considering the prediction interval, accounting for the deviations from the average of the operating margins of specific hotels, and therefore of the possible extra-performance of specific hotels,  the upper limit of the interval is lower – even if slightly – than 50.

## Hotel location and performance

## Predict the performance of the average operating margin of hotel located in sites with the considered characteristics and of the operating margin of a specific hotel

```
> to_predict <- data.frame(Number= 3815,Nearest=0.9,Office=476,Income=35,
+                          Distance=11.2,Enrollment=24.5)
>
```

```
> predict(reg_hotel, to_predict,interval = "confidence", level = 0.95)
fit      lwr      upr
1 37.09149 32.96972 41.21326
```

```
> predict(reg_hotel, to_predict,interval = "prediction", level = 0.95)
fit      lwr      upr
1 37.09149 25.39525 48.78772
```

**A hotel is considered unprofitable if its operating margin is less than 30%. Comments?** With a 95% confidence we can conclude that on average hotels located in areas with the considered characteristics have operating margins between 32 e 41, thus higher than 30 (therefore, on average, the hotels in these areas are profitable – although not very profitable). Nonetheless, 30% is **included** in the prediction interval; therefore we cannot exclude that specific hotels in these areas have performance lower than average and are unprofitable!

## Hotel location and performance

The regression model can also be used to compare the observed value for the dependent variable for a certain unit and the prediction obtained on the basis of the characteristics measured by the explanatory variables ( **in-sample** prediction).

**Performance evaluation of an existing hotel** Let us consider a specific hotel in the sample, **already existing and operational (observation 87)** with the following characteristics

- 1988 rooms within 3 miles,

- Nearest competitor at 3.6 miles,

- 461,000 sq-ft of office space,

- 19,000 university students,

- Median household income $41,000,

- Distance from the centre 4.9 miles

**The operating margin of this hotel is 49%. What are your considerations on its performance?**

## Hotel location and performance

## Performance of an existing hotel

```
> conf.pred<-predict(reg_hotel, Hotel,interval = "confidence",level = 0.95)
> pred.pred<-predict(reg_hotel, Hotel,interval = "prediction",level = 0.95)
> conf.pred(87,)
```

```
fit      lwr      upr
57.81456 54.08090 61.54823
```

```
> pred.pred(87,)
fit      lwr      upr
57.81456 46.24939 69.37973
```

**The hotel (observation No. 87) has an operating margin of 49%. What considerations? .** The hotel has an operating margin lower than expected given its location In particular, we can be 95% confident that the **average** operating margin of all hotels **operating under the same conditions** (having the same characteristics in terms of explanatory variables) is greater than 49 (between 54.08 and 61.55)

However, **49** is **included in the prediction interval,** which takes into account the dispersion of the specific operating margin values around the average: one can be 95% confident that the operating margin of a specific hotel is within a range that includes 49; therefore, the hotel’s operating margin is within the range of 'expected' values for specific hotels in areas with the same characteristics.

## Hotel location and performance

**Performance evaluation of some existing hotels (observations 2, 54, 42, and 95;** predictions and 95% intervals; syntax in the script):

|**Margin **|**Number **|**Nearest **|**Office**|**Enroll.**|**Income**|**Dist. **|**Prediction **|**Confidence Int.**|**Confidence Int.**|**Prediction Int.**|**Prediction Int.**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**33.8**|**2810**|**2.8**|**496**|**17.5**|**35**|**14.4**|**46.06**|**43.12**|**49.01**|**34.73**|**57.40**|
|**48.8**|**2825**|**1.1**|**744**|**13.0**|**40**|**9.0**|**50.98**|**47.99**|**53.96**|**39.63**|**62.32**|
|**51.5**|**3069**|**3.3**|**512**|**20.5**|**37**|**7.7**|**48.20**|**46.19**|**50.21**|**37.08**|**59.33**|
|**60.5**|**2932**|**1.8**|**469**|**19.5**|**39**|**6.1**|**46.90**|**45.07**|**48.73**|**35.80**|**58.00**|

**1(st) obs: 33.8** is below the lower bound of both the intervals! Given the characteristics of the area, the hotel should/could have a better performance. Try and understand the reasons for underperformance. **2(nd) obs: 48.8** is included both in the confidence and in the prediction interval

**3(rd) obs: 51.5** is higher than the upper bound of the confidence interval. We can be 95% confident that the operating margin is above the average operating margin of hotels located in areas with its characteristics. Even so, 51.5 is included in the prediction interval and the hotel’s performance is therefore not exceptional or beyond expectations for a specific hotel.

**4(th) obs:** Hotel with high performance, even higher than the upper limit of the prediction interval. Understand the reasons for the performance evaluating whether the area has special characteristics - to be included in the model - or whether the good performance is related to management

## Related Notes
- [[Lecture 25_27 Slides - Multiple Regression with NOTES up to L26]]
- [[Lesson 22-24_Simple Linear Regression]]
- [[Lecture 22-24_Simple Linear Regression with FULL NOTES]]