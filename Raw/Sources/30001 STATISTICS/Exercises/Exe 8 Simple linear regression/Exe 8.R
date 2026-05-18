# EXERCISE 8.1
## a)
### To estimate the regression model of Debt on Television we will use the lm() function.

m <- lm(Debt ~ Television, data = TeleDebt)
coef(m)
summary(m)

### The estimated intercept beta0 is 48039.68 and indicates the average value
### predicted by the model for the amount of debt of households where television
### was never on. This information is not useful because a quick descriptive analysis
### of the variable Television shows that its minimum value is 6, and therefore no
### household in which television was off for the entire week was observed;
### therefore, no meaningful interpretation can be provided for the intercept.
### The estimated coefficient beta1 is 2581.8: based on the model for each
### additional hour the TV is on, the average increase in debt is expected to be
### 2581.8. The variable is significant. In fact, the decision between the two
### hypotheses H0: beta1 = 0 and H1: beta != 0 is based on the observed value of
### the test statistic, t=beta1/se(beta1) = 13.77, characterized by a p-value close
### to zero. This leads to the rejection of the null hypothesis for any level of
### significance, and thus the conclusion that the regression coefficient is to be
### different from 0. Thus, corresponding to an increase in the number of hours the
### TV is on one can expect a significant increase of the average debt.

#### Side-note: we obtain the value of se(beta1) by using the summary(m) function, not
#### by hand.

## b) 
### We again have the coefficient of determination R squared.
### R-squared in the summary() function information.
### It is computed as the ratio between the sum of squares of the regression and the
### sum of total squares and it measures the proportion of the variance of the
### dependent variable explained by the model. In the case, the coefficient of
### determination is 0.3069, and it indicates that the explanatory capacity
### of the model is quite low.

## c)
### We can build the 99% interval simply using the function predict() but first
### we should define the specific subpopulation which we focus on.

### 1) Fit model
m <- lm(Debt ~ Television, data = TeleDebt)

### 2) One-row new data with the SAME variable name used in the model
xg <- data.frame(Television = 33)

### 3) 99% prediction interval with the function predict()
interval <- predict(m, newdata = xg, interval = "prediction", level = 0.99)

### 4) Show results
interval
interval[1, "lwr"]  # left side
interval[1, "upr"]  # right side

### The interval's left side is equal to 33057.97 and its right side is equal to 
### 233419.6. The result allows us to conclude that for a household in which the
### TV is on for 33 hours a week we can be 99% confident that its debt is between
### about 33058 and 233420.
### The width of the interval depends on:
### - the confidence level (the larger the confidence level, the larger the interval)
### - the variability of the explanatory variable (the larger it is the smaller
###   the width, indicating that the model produces more reliable predictions when
###   built on heterogeneous information)

### - the distance between the mean of the explanatory variable and the value of
###   the explanatory variable at which the prediction is obtained (the greater
###   the distance from the center of the data the wider the interval, indicating
###   that the prediction is less reliable for non-typical values)

### - the sample size (the larger the sample size the smaller the width, indicating
###   that the more information available the more reliable prediction)

### - the estimate of the variance of the errors (the larger this estimate the
###   the larger the width, to account for the increased uncertainty due to the
###   the higher dispersion of the data around the regression line)

## d)
### I would expect a narrower interval for the prediction of the average debt of
### families whose television was turned on for 33 hours in a week because the
### sample size will be bigger than the last one which leads to smaller width.

### 1) 99% prediction interval with the function predict()
interval <- predict(m, newdata = xg, interval = "confidence", level = 0.99)

### 2) Show results
interval
interval[1, "lwr"]  # left side
interval[1, "upr"]  # right side

### The result is [128255.1; 138222.5] which is a much narrower interval.

## e) 
### The conclusion is entirely incorrect. While the available empirical evidence
### suggests undoubtedly a positive relationship between the number of hours the
### television is on and the amount of debt, it is possible that there are some
### factors related to both variables that explain the observed relationship. In
### fact, a high number of television hours may be related to unemployment status,
### or the presence of children in the household, or a part-time job instead of a
### a full-time job. Such factors may be related to both amount of debt and the
### number of hours the television is left on. It would be necessary to account for
### (at least) these factors in order to check whether the hypothesized relationship
### actually exists.

# EXERCISE 8.2
## a)
### The optimality criterion used to determine the coefficients' estimates in
### the linear regression model is based on minimizing the sum of squares of the
### residuals, that is of the differences between the observed and predicted
### values for the dependent variable F. Such sum quantifies the risk incurred
### when using the estimated model to explain/predict the dependent variable.

## b)
### b1) Our explanatory variable will be Salary and the dependent variable will
### be AmountSpent. To build the estimated equation we have to first obtain the
### coefficients beta0 and beta1:

m <- lm(AmountSpent ~ Salary, data = DS)
coef(m)

### The estimated equation will be equal to:
### AmountSpent = -8.03 + Salary*0.022

### b2) 
### The erratic component of a linear model satisfies the assumption of
### homoscedasticity when it can be assumed that Var(epsilon_i)=(sigma_epsilon)^2
### for each sample unit. This assumption implies that the random variable
### describing the realizations of the dependent variable, Y_i also has
### Var(Y_i)=(sigma_epsilon)^2, i.e., constant variance.
### To test whether the assumption of homoscedasticity is plausible for the
### estimated model, one can graphically evaluate the behavior of the residuals
### and in particular the plot of the residuals vs, the predictions obtained
### using the model (residuals vs. fitted plot) given below.

plot(m, which = 1)

### It is evident from the cone form of the residuals: the dispersion of the
### residuals increases as the predicted salary increases. This trend suggests
### that the variance of the residuals is not constant, a condition called
### heteroscedasticity.

### b3)
### I would not suggest using the estimated model to assess the significance of
### the slope of the regression line because there is a lot of variance in the
### the higher values of the salary variable which prevents us from making an
### accurate conclusion. In fact, to assess the significance of the coefficients
### it is necessary to refer to the estimated standard error of the least squares
### estimators, which depends on the estimated variance of the errors. Since the
### variance of the errors is not constant, the estimated residuals cannot be
### considered a homogeneous sample in terms of variance and therefore cannot be
### used to estimate the common variance.

### b4)
### Just like in b3), it is not appropriate to use the model to obtain confidence
### or prediction intervals for the same reason - variance nowhere close to 
### constant so we can not build an interval.

# EXERCISE 8.3
## a)

m <- lm(Weeks ~ Age, data = NewHired)
summary(m)


### After calculating the coefficients of the variables Weeks and Age we can
### insert them in the estimated equation.
### Weeks = -19.53 + 1.69*Age

### To assess the significance of the relationship at the population level, we
### should refer to the test that compares the two hypotheses H_0: beta_1 = 0 vs
### H_1: beta_1 != 0. The realization of the test statistic for this test is
### 15.153 (obtained from the output of the lm() and then summary() functions),
### and its p-value is close to zero, therefore the null hypothesis is rejected
### at any significance level. We can conclude that a change in Age corresponds
### to a mean change in Weeks that is significantly different from zero. On the
### basis of the estimated model, in can be concluded that for every 1 year increase
### in age corresponds, on average, to an estimated increase in the number of
### weeks needed to find a job of 1.69 weeks.

## b)

confint(m, level = 0.9)

### The obtained interval for beta1 representing the change in the average number
### of weeks needed to find a new job corresponding to a unit increase in age is 
### (1.502505; 1.877065). To compute the 90% interval for the change in the average 
### number of weeks corresponding to an increase in 5 years of age, it is sufficient
### to multiply the extremes of the interval by 5, obtaining (7.5125; 9.3853).

## c)
### The percentage of variance explained by the model is measured by the value of
### the coefficient of determination, R^2, given by the ratio between the sum of
### squares of the regression and the sum of total squares or by the summary()
### function applied to the linear regression model. In the present case, the
### linear model based on age explains about 80% of the dependent variable.

## d)

xg <- data.frame(Age = 36)
predict(m, newdata = xg, interval = "prediction", level = 0.99)

### The prediction interval for 36-year-old subject is (22.14825; 60.46381).

## e)

plot(m, which = 1)

### From the scatter plot we can conclude that the assumptions at the basis of the
### linear model are not fulfilled as the dispersion of the residuals increases
### in the middle and the variance is not constant.

# EXERCISE 8.4
## a)
### The statement is false. The determination coefficient corresponds to how much
### are the residuals dispersed around the line of regression and a lower
### coefficient would mean that the residuals are much scattered around the line.
### It has nothing to do with the slope of the line.

## b)
### The statement is false. The numerical value of the slope has nothing to do
### with the goodness of fit - this is the determination coefficient. In fact,
### the slope depends on to what extent are the measurements explanatory variable
### bigger than the ones of the dependent variable. If the explanatory ones are
### much higher than the dependent ones, then the slope will be low.

## c)
### The statement is true. Opposite to a), slope close to zero imply low correlation,
### which leads to low coefficient of determination.

## d)
### d1) 

m <- lm(revenues ~ surface, data = restaurants)
coef(m)

### The equation of the regression line is equal to:
### revenues = 246.81 + 0.41*surface
### The estimated regression line suggests that 1-square-meter increase in
### restaurant floor area corresponds to an estimated average increase in
### revenues of 0.4. This effect is to be considered significantly different
### from 0 for each level of significance, as the p-value of the test stat is
### close to zero. However the coef of determination R^2 takes a small value
### of 0.119, and indicates that a poor fit of the model to the data.

### d2)
### No, multiplying everything by 1000 will not change the estimated line or
### goodnes of fit.

### d3) 

plot(m, which=1)

### No, this model can not be used to make predictions. Judging by the high
### dispersion of the residuals in the higher revenues, the variance is not
### constant.

### d4)
boxplot(rstandard(m) ~ restaurants$evening_only)

### It can be inferred from the boxplots that the residuals have different structural 
### characteristics depending on whether or not the restaurant is opened only in the 
### evening. In particular, restaurants that serve both lunch and dinner have both 
### higher median and dispersion. This signals that the erratic component depends
### structurally (also) on this variable.	Therefore, a multiple regression model
### capable of capturing the determinants of revenues heterogeneity should be
### evaluated.

# EXERCISE 8.5
## a) 
### We should estimate a model based on already given statistics.

n <- 47
sum_salary <- 99150
s2_salary <- 345722

sum_years <- 297
s2_years <- 27.048

covar <- 2697.96

### The estimated value of the regression coefficient beta1 is obtained as the
### ratio between the covariance and the variance of the independent variable:

beta1 <- covar/s2_years

### This value is interpreted as the average change in the independent variable
### corresponding to a unit change in the explanatory variable: for each additional
### year of work experience, an average increase in the starting salary of 99.7471
### is expected.
### To determine the estimate for the intercept, it is first necessary to determine
### the sample averages of the variable considered,

xbar <- sum_years/n
ybar <- sum_salary/n

### From which, using the estimate obtained previously, we obtain:

beta0 <- ybar - beta1*xbar

### This value represents the average level of the dependent variable corresponding
### to a null value of the explanatory variable: thus, an average salary of 1479.26
### euros is expected for workers without work experience. To determine whether
### this interpretation is appropriate or not, it would be necessary to know
### whether the sample includes subjects who were hired without having any work
### experience. Only in this case, in fact, it would make sense to interpret the
### intercept.

## b) 
### To assess the goodness of fit model, it is appropriate to compute the coef of
### determination R^2, which - since the model is based on a single explanatory
### variable - coincides with the correlation coefficient squared:

R2 <- (covar^2)/(s2_salary*s2_years)

### the coefficient of determination takes on a high value of 78% of its theoretical
### maximum, indicating that the model has an excellent ability to fit the data
### and is able to explain about 78% of the variance of the dependent variable.
### Thus, based on work experience it is possible to explain "why the salaries of
### newly hired employees differ from each other."

## c)
### The high coefficient of determination (78%) suggests that the slope test will
### likely reject 0. However, we have to test it. The test will consist of:
### H0: beta1 = 0 vs H1: beta1 != 0. The realization of this test is equal to
### t = beta1/se(beta1).
### We have to find se(beta1).

### se(beta1) = sqrt((s_epsilon)^2/(n-1*(s2_years))

### Therefore, we have to find the s_epsilon
### s_epsilon = SSE/(n-2)

### So we have to find the SSE
### R^2 = 1 - (SSE/SST)

### So before anything we have to find the SST which is equal to

SST <- (n-1)*(s2_salary); SST

### So 0.778 = 1 - (SSE/15903212)
### 0.222 = SSE/15 903 212

SSE <- (1-R2)*SST

s_epsilon2 <- SSE/(n-2)

se_beta1 <- sqrt((s_epsilon2)/((n-1)*(s2_years)))

t = beta1/se_beta1           

### Therefore, we obtain that the realization of the test statistic is equal to
### 12.573 which is far from 0. The p-value of the sample realization is obtained
### by referring to a Student's t distribution with (47-2)=45 degrees of freedom,

p_value <- 2*(1-pt(12.57, 45)); p_value

### which is very close to 0, therefore the null hypothesis is rejected.

## d)
### We have to determine the 99% interval for the initial monthly salary of two
### new hired employees having respectively 5 and 7 years of work experience.

ME5 <- 2.689585*sqrt(s_epsilon2)*sqrt(1 + 1/n + ((5-6.3)*(5-6.3))/((n-1)*s2_years))

ME7 <- 2.689585*sqrt(s_epsilon2)*sqrt(1 + 1/n + ((7-6.3)*(7-6.3))/((n-1)*s2_years))

y5 <- beta0 + beta1*5

y7 <- beta0 + beta1*7

left5 <- y5 - ME5; left5
right5 <- y5 + ME5; right5

left7 <- y7 - ME7; left7
right7 <- y7 + ME7; right7

### The interval for the initial monthly salary of a new hired having 5 years 
### of work experience is [1216.688; 2739.118]. The interval for the initial
### monthly salary of a new hired having 7 years of work experience is
### [1416.721; 2938.254]. The first interval is wider since 5 is further from
### the average 6.3 years than the 7 years.

# EXERCISE 8.6
## a)
### The least squares estimators are linear combinations of the observations on
### the dependent variable. Therefore, under the weak assumptions (and only if
### these are met), it can be shown that they are both unbiased for the respective
### coefficients of the linear model in the population and that their variance
### of the random errors, tends to zero as the sample size increases. Furthermore,
### under the strong assumptions i.e., under the assumption that the random errors
### in the model have a normal distribution, the least squares estimators have a
### normal distribution, although their distribution can be approximated by a
### normal distribution even when the sample size is high.

## b)
### The properties of the least squares estimators beta0 and beta1 can be obtained
### from the lm() function in R studio.

m <- lm(Employment~Age, data = Turnover)
coef(m)

### We obtain that the intercept or beta0 is equal to 30.63 and the beta1 is
### equal to -0.1169.
### Therefore the regression line of Employment on Age will be equal to:
### Employment = 30.63 - 0.1169*Age
### beta0 is the minimum number of weeks on the job before quitting and as the
### dependent variable Age increases by 1 year, this minimum of weeks decreases
### leading to the interpretation of that the older telemarketers stay less on
### the job than the younger ones.


## c)
### To be able to conclude with 5% significance level that as age varies a
### significant variation of the average job can be expected we should test
### the hypotheses H0: beta1 = 0 vs H1: beta1 != 0. The test realization is
### t = beta1/se(beta1) and is obtainable with the function summary() used
### on the linear model.

summary(m)

### The test realization is equal to -4.255 which is different from 0. The p-value
### of the sample realization is equal to 0.0000577 which is below every significance
### level, including the required 0.05 and therefore the null hypothesis is
### rejected, so we can conclude that as age varies a significant variation of
### the average job time can be expected.

## d)
### I would assess the goodness of fit of the model by obtaining the dedication
### coefficient (R^2), again using the summary() function. It is significantly
### low at just 0.1884, meaning that the residuals are much scattered around the
### regression line.

## e)
### Since a simple linear model is estimated, it is possible to assess the
### adequacy of the model from a scatter plot.

plot(m)

### The variance of the residuals is fairly
### constant, although a slightly different dispersion is seen at higher predicted
### values, which correspond to relatively low values of age, at which fewer cases
### are observed.

## f)

xg <- data.frame(Age = 27)

predict(m, newdata=xg, interval = "prediction", level = 0.9)

### The point estimate of the number of weeks on the job for a 27 years old person
### is equal to 27.47, while the 90% interval will be [24.4; 30.55]. The more
### reliable tool is the interval as it covers the potential variation in the
### estimate with its width. Considering the fact that the dedication coefficient
### is very low it once again reinforces this decision. The interval is not
### particularly informative considering that the dependent variable takes
### values between 21 and 31. Actually, the prediction interval coincides with
### the range of value taken by Employment and is not particularly useful or
### informative. The reason for such a high width of the interval is the fact
### that the dispersion around the model is high, and the standard error is rather
### high.

# EXERCISE 8.9
### To estimate the linear model, we should use the lm() function and find the
### linear square estimates beta0 and beta1.

m <- lm(Aad ~ Rep, data = RepeatedAds)
lm(m)

### So we obtain that the linear model is equal to:

### Aad = 0.1638 + 0.01783*Rep

### The linear model can be interpreted as the following: with the increase of
### one repetition, the Aad increases by 0.01738 and the minimum amount of customer
### affection towards an ad (Aad) is equal to 0.1638.

summary(m)

### In terms of significance of the model's coefficients, we should test the
### hypotheses H0: beta1 = 0 vs H1: beta1 != 0. The realization test statistic 
### of this test is equal to t = beta1/SE(beta1), which can be obtained from the
### summary() function and is equal to 7.12, which is significantly different from
### zero. The p-value of the realization is less than 0.0000005 and is very close
### to zero, which means that for any significance level, the null hypothesis is
### rejected and beta1 is not equal to 0. Additionally, the goodness of fit of the
### model can be quantified by the R^2 or the dedication coefficient which is
### equal to roughly 0.5.

### With reference to the reported statement, before making a full evaluation,
### we should focus on the scatter plot of the model. From it we can see that
### the relationship between the variables is more quadratic than linear since
### the number of reps increase the Aad at some point and then start to decrease
### maybe due to annoyance from by consumer. Therefore the statement does is not
### true to a full extent.

#### Note: I leave 8.7, 8.8 and 8.10 for tomorrow and I will solve them only if
#### I find the time.