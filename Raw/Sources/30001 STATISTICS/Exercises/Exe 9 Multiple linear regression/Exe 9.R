# EXERCISE 9.1
## a)

m <- lm(Major~Minor+Age, data = Baseball)
summary(m)
coef(m)

### To asses the goodness of fit of the model, we refer to the coefficient of
### determination defined as:

### Major = -12.42 + 0.61*Minor + 0.814*Age

### R^2 = 1-SSE/SST

### Where SSE = sum((yi - yhat_i)^2) is the sum of the squared regression errors,
### given by the squared distance between the observed and the predicted values
### of the dependent variable, and SST=sum((yi-ybar)^2) is the sum of the squared
### deviation of the measurements on the dependent variable from their mean. For
### the data at hand the index, which can be interpreted as the proportion of the
### variance of the dependent variable which is explained by the linear model and
### ranges between 0 and 1, is relatively low, about 0.3348 (in other words, 
### the coefficient of determination is equal to 0.3348). Therefore the model
### does not fit the data well.

### Even so, we can conclude that the model includes at least one significant
### explanatory variable. Indeed the realization of the F-statistic to test the
### two hypotheses: H0: beta_Minor=beta_Age=0 vs H1: at least one of the 
### coefficients beta_Minor and beta_Age != 0, defined as:

### F = (SSR/K)/(SSE/(n-K-1))

### where K is the number of the explanatory variables in the model. The F-statistic
### is 30.95 and its p-value is close to zero. Thus, even if at least one of the
### two explanatory variables is significantly related to Major, the dependent
### variable, there is high amount of dispersion around the regression plane.

## b)
### Minor is highly significant, because its t-stat equals 7.444 with a p-value
### close to zero, leading to reject the null hypothesis that the coefficient is
### zero at the population level. The value of the coefficient is 0.65112,
### indicating that, given the number of years as a professional baseball player,
### corresponding to one additional home run in the last year in the minor league,
### one can expect a variation in the average number of home runs in the first
### two years in the major league equal to 0.65112. As for the variable Age, the
### rejection of the hypothesis that its coefficient is null at the population
### level depends on the chosen level of significance : it can be concluded that
### the coefficient is significant only at a significance level higher than 0.024
### (e.g. 0.025 or 0.05). The coefficient signifies that given the number of home
### runs in the last year as a player in the minor league, an additional year of
### age corresponds to an expected increase of 0.81406 in the average number of
### home runs in the first two years as a player in the major league.
### The intercept in the model corresponds to the predicted expected value of Major
### corresponding to players with both Minor and Age equal to zero, and has
### therefore no meaning interpretation.

## c)

xg <- data.frame(Age = 25, Minor = 22)
predict(m, newdata = xg, interval = "prediction")

### The point estimate prediction for the number of home runs in the first two
### years in the major league is equal to 22.26. The interval estimate, on the
### other hand, is equal to [7.87; 36.64]. I would use interval estimate as it
### covers a wide range of values, even though that the width of the interval
### is neither useful nor informative as it almost covers the range of the Major
### variable. Also since R^2 indicates a high amount of dispersion around the 
### regression plane, prediction intervals should be referred to so as to 
### account for the high uncertainty characterizing the point prediction.

## d)
### In order to predict the difference in the average number of home runs in the
### first two years in the major league for two players with an average gap of 2
### years, we have to first "lock" the variable Minor for both of the compared
### players by assuming that the variable for both of them is equal. Secondly,
### to estimate the difference, we would simply have to multiply the Age variable
### coefficient 0.814 by the difference equal to 2 years, so the difference will
### be equal to 2*0.814, equal to 1.628 home runs. So the older player with 2
### years ahead will score 1.628 home runs more. Considering the high variability,
### I would use the confidence interval for the regression coefficient, in order
### to account for the standard error of the estimator - which is relatively high.
### Such interval is obtained by first calculating the confidence interval of
### the variable Age from the function confint(), and then multiplying it by 2
### which equals 2*(0.108; 1.52) = (0.216; 3.04).

## e)
### When the variable Years is included among the explanatory variables, the
### the model becomes:

m <- lm(Major~Age+Minor+Years, data = Baseball)
coef(m)
summary(m)

### Major = -1.97 + 0.136*Age + 0.666*Minor + 1.176*Years

### The model does change in terms of formula and significance of some of the 
### explanatory variables. To begin with, the significance of the Minor variable
### does not change, its realization statistic is very high at 7.64 and its
### respective p-value is almost equal to zero rejecting the null hypothesis at
### every significance level. Turning to the significance that change with the
### addition in the explanatory variables, the realization value of the variable
### Age fall and its p-value increases to a point which is higher than every
### significance level, not rejecting the null hypothesis and becoming insignificant.
### The variable Age's realization value is equal to 1.75 and its significance
### depends on the level chosen, since it could be significant if the test is
### only 0.1, its p-value is equal to 0.08. One can suspect that there is
### relation between the variables Age and Years, as their correlation is equal
### to 0.73 and this may be to the fact that the players start at a similar age
### and the more years of age equal more years playing. Even if we are not in a
### situation of perfect multicollinearity, it is clear that the inclusions of
### both variables in the model makes one variable mask the significance of the
### additional contribution of Age to the model is not significant; also, if a
### model already includes results, a reasonable final proposal would be considering
### a model including only Minor and Years. This model a higher adjusted R-square
### compared to the other ones, and the coefficient of Years is now significant
### at the 0.5%, implying that the null hypothesis that the coefficient if the
### variable is null at the population level would be rejected unless a very low
### value of significance (e.g. 0.001) was required.

## f)
### In order to determine whether the regressions assumptions for the model
### chosen in e) are satisfied, we have to plot the linear model and investigate
### the distribution of the residuals and their distances from the regression
### line.

m <- lm(Major~Minor+Years, data = Baseball)
plot(m, which = 1)

### By plotting the scatterplot, we observe a cone-shaped distribution of the
### residuals, which are mostly concentrated around the regression line
### in the fitted values, and as we increase their number we observe a much more
### dispersed distribution of fewer residuals. Again, the R^2 is low so we would 
### expect a bigger portion of variance, but we now also can observe that the 
### variance is not constant. To possibly identify the cause of heteroscedasticity,
### we consider the plots of standardized residuals against the two explanatory
### variables:

plot(rstandard(m) ~ Baseball$Minor)
plot(rstandard(m) ~ Baseball$Years)

### We note that the dispersion of residuals is higher corresponding to values
### of Years between 2 and 4 as well as corresponding to higher number of home
### runs during the last year as a player in the minor league.

# EXERCISE 9.2
## a) 
### To assess the goodness of fit of the model, we have to calculate the R-square,
### given by 1-SSE/SST. The SST is the numerator of the variance of the dependent
### variable, therefore:

### var_success = SST/(n-1)
### 7059.01 = SST/29

SST <- 7059.01*29; SST 

### SST = 204711.3

### The SSE is given by SSE = (s_epsilon)^2*(n-K-1)

SSE <- (63.08)^2 * (30 - 2 - 1); SSE

### Therefore, R^2 will be equal to:

R2 <- 1 - SSE/SST

### To test the significance of the model, we have to calculate the F statistic
### and its significance level (or we have to compare it with the percentile of
### the specified level the F distribution). The realization of the test
### statistic is:

### F = (SSR/K)/(SSE/(n-K-1))

K <- 2

n <- 30

F <- ((204711.3-107435.3)/2)/(107435.3/(30-2-1)); F


### It's p-value is the probability to observe a realization of the F-statistic
### higher than the observed one, and can be obtained using the function:

1 - pf(F, df1=K, df2=(n-K-1))

### The function returns p-value equal to 0.000166, which is lower than all of the
### significance levels and we can conclude that at least one of the two
### variables is significant.

## b)
### b1)
### To test the significance of the coefficient of Channel1, we need to obtain
### the realization of the t-statistic, which is 

### tstats1 = channel1_estimate/channel1_se = 0.1398/0.0.0814 = 1.7174

### And the p-value is obtainable from the function:

tstats1 <- 1.7174

2*(1-pt(abs(tstats1), df=(27)))

### Equal to 0.0974, which rejects the null hypothesis only when the significance
### level is equal to 0.1. Following the same reasoning:

### tstats2 = channel2_estimate/channel2_se = 0.0313/0.0067 = 4.6716

tstats2 <- 4.6716

### And the p-value is obtainable from the function:

2*(1-pt(abs(tstats2), df=(27)))

### Equal to 0.0000736, which rejects the null hypothesis at every significance
### level. So we know that for Channel 1 for every increase in 1-unit in the 
### expenses corresponds to an average increase of 0.14 in the success indicator, 
### and for Channel 2, an increase in 1-unit in the expenses corresponds to
### an increase of 0.03.

### b2) 

t <- qt(0.995, 27)

left_channel1 <- 0.14 - t*0.081
right_channel1 <- 0.14 + t*0.081

left_channel2 <- 0.0313 - t*0.0067
right_channel2 <- 0.0313 + t*0.0067

### So for the 99% confidence interval for Channel2 is equal to [0.0127; 0.0499].
### Therefore a 1-unit increase of the amount spent on the second channel will
### increase the indicator of success with a given value from this interval, no
### matter that the amount spent on the first channel is 150. We can not estimate
### the covariance of the two variables to conclude that there is any kind of
### relation between them. Moreover, we evaluate the change on the indicator of
### success from a change in Channel2, holding Channel1 constant.

### b3)
### The 95% confidence interval and estimate for the decrease of 50 units in the
### amount invested on Channel 1 are equal to:

t <- qt(0.975, 27)
left_channel1 <- 0.14 - t*0.081
right_channel1 <- 0.14 + t*0.081
estimate <- 0.1662

(0.3062+0.0262)/2

### So the point estimate for the amount lost from the success index due to the
### reduction by 50 unit points from the amount spent on Channel1 is equal to
### 0.1662 and the 95% confidence interval is equal to [-0.0262; 0.3062]. The
### interval is quite wide, but I would still prefer it as an estimation tool
### over the point estimate.

## c) 
### In order to state to what extent the conclusions I made are reliable, I have
### to plot a scatterplot in order to observe the dispersion of the residuals.
### However, the graph can be assessed only when I have access to the raw data,
### not only partial statistics, so it is impossible to state.

## d)
### To predict the success of the commercial campaigns, we have to insert the
### amounts spent on the two channels, 100 and 1000 respectively, in the 
### estimated equation:

Success = 164.01 + 0.14*100 + 0.03*1000

### Knowing that the determination coefficient has mid-value, it is usually
### recommended to use intervals of confidence or prediction, instead of a 
### single prediction.

## e)
### To compare two channels with a different number of explanatory variables, their
### adjusted R-squares should be compared. The adjusted R-square is defined as:

### Adj. R2 = 1 - (SSE/(n-K-1))/(SST/(n-1)) = 1 - ((s_epsilon)^2)/((s_Y)^2)

### For the model with two explanatory variables it is Adj.R2 = 1-(63.08^2)/(7059.01)=
### = 0.4363 which is higher compare to that characterizing the model including
### only Channel2 because 63.08 < 65.24.

# EXERCISE 9.3
## a) 

m <- lm(Performance~Competition, data = Competition)
coef(m)
summary(m)

### Performance = 46.5 + 0.877*Competition

### So from the model we can understand the relationship between the explanatory
### variable Competition and the dependent variable Performance. As competition
### increases by 1 unit point the overall performance increases by 0.877. In terms
### significance, the realization statistic of the Competition variable is equal
### to 8.494 and it respective p-value is very close to 0, rejecting the null
### hypothesis at any significance level. Looking at the goodness of fit,
### the model has a coefficient of determination equal to 0.41, which reveals
### a moderate to low variability around the regression line.

## b)
### The addition of the explanatory variable Quality in the linear model leads to:

m <- lm(Performance~Competition+Quality, data = Competition)
coef(m)
summary(m)

### Performance = 50.31 - 0.998*Competition + 1.997*Quality

### The first, significant change after the addition of the variable Quality
### except the model, is that the coefficient of determination increased more
### than double to 0.99, meaning that the model explain 99% of the residuals now.
### The second big change which occurred is the change of the sign of the 
### Competition coefficient, it is now negative, revealing a new relationship
### between the Competition variable and the Performance one - as competition
### increases, the company lags behind and loses out on its performance, but now
### the Quality can be increased to compensate - with an increase of 1 unit point,
### the Performance increases with 1.997. The p-values of the coefficients are
### very close to zero rejecting the null hypothesis at any significance level.
### Comparing the two models, I would choose the second one as it gives more
### insight of the dynamics in the market and in the company.

# EXERCISE 9.4
## a)
### To estimate the model we will use the lm() function:

m <- lm(MntMeatProducts ~ IncomeK + Age, data = superstore)
coef(m)
summary(m)

### Therefore the model is equal to:
### MntMeatProducts = -115.68 + 7.954*IncomeK - 2.9*Age

### a1) 
### To check whether the variable Age is significant we should use the function
### summary() to obtain its realization statistic and its p-value:

summary(m)

### We obtain that the realization statistic of the variable is equal to -3.28
### and the p-value is equal to 0.00117, therefore it will reject the null
### hypotheses for very significance level except 0.001. 

### a2)
### In terms of the coefficient of the variable Age, we observe that an increase
### of one year to the variable leads to an increase in the MntMeatProducts of
### 7.954 units.

## b)
### To estimate the model we will use the lm() function and specify for the
### first model that the variable KidsAtHome is equal to "Yes", estimating the
### model for the families which have kids and then a second time where the
### variable is equal to "NO", estimating the model for the families which do not
### have kids. However, we have to remove the variable KidsAtHome because it is
### a binary one. We now know that when a family has children, 168.093 is added.

m <- lm(MntMeatProducts~IncomeK + KidsAtHome, data = superstore)
coef(m)

### Now that we have the coefficients for both cases, we know the models:
### Families with kids:

### MntMeatProducts = -7.99 + 5.778*IncomeK

### Families without kids:

### MntMeatProducts = -176.084 + 5.78*IncomeK

### The two lines differ by exactly 168.093, meaning that the intercept increases
### as the family does have kids because they consume more meat.

## c)

m <- lm(MntMeatProducts~IncomeK+KidsAtHome, data = superstore)
summary(m)

### The model can be estimated by conducting the lm() function and then the
### summary function. The estimated equation for families with  kids looks like this:

### MntMeatProducts = 92.98 + 6.1324*IncomeK - 2.7934*Age

### And the estimated equation for families without kids looks like this:

### MntMeatProducts = -73.769 + 6.1324*IncomeK - 2.7934*Age

### From the summary function we   can also obtain the F-statistic which is equal
### to 146.8 and its respective p-value which is very low (close to zero), therefore
### it rejects the null hypothesis at any significance level and the model is
### globally significant. The hypothesis tested is whether the coefficients were
### equal to zero or not. The dedication coefficient is equal to 0.636 and therefore
### the model explains 64% of the residuals which is more than the half and
### because of this I would rely on the point prediction.

### c1)
### In order to estimate the prediction, we have to input the given values in the
### estimated equation:



### The prediction of the average amount spent on meat by clients aged 40, with
### with a family income equal to 75 who have children is about 441.173. While
### the prediction for those that do not have kids is equal to 273.08. Using the
### point forecast is not recommended because even if the R2 is medium-high (0.63),
### the confidence interval takes into account both the dispersion around the
### regression hyperplane and the distance of the case considered from the center
### of the data, with reference to the explanatory variables.
### MntMeatProducts = 92.98 + 6.1324*75 - 2.7934*40
### MntMeatProducts = 441.173

### Withouth children, the prediction is equal to:
### MntMeatProducts = 441.173 - 168.093 = 273.08



### c2)

xg <- data.frame(MntMeatProducts = 40, IncomeK = 75, KidsAtHome = "Yes")

predict(m, newdata = xg, interval = "prediction", level = 0.95)

### The interval is equal to [152.4173; 698.2271]

### c3)
### The reliability of the obtained predictions should be estimated based on the
### graphs. The variance is constant, as more and more residuals are dispersed
### around the regression line as the amount spent on meat products increases.

plot(m, which = 1)

### EXERCISE 9.5
## a)

m <- lm(revenues~seats+area+days_open+evening_only, data = restaurants)
coef(m)
summary(m)

### The model equation if the restaurant is opened only in the evening is:
### revenues = -82.7 + 1.76*seats + 38.193*areaNorthWest + 0.997*areaSouthEast + 13.015*days_open

### The model equation if the restaurant is opened not only in the evening:
### revenues = 260.7 + 1.76*seats + 38.193*areaNorthWest + 0.997*areaSouthEast + 13.015*days_open

## b)
### The coefficient of the variable days_open means that for every increase in 
### the number of days working, the revenues variable increases by 13.015. Its
### realization statistic is equal to 6.734 and its p-value is close to zero,
### rejecting the null hypothesis at every significance level.

## c)
### Based on the model, I can conclude that it is not convenient for a restaurant
### to be opened for the evening only as it loses part of the revenue.

## d)
### No, in fact Center is the reference category: the model that explains the 
### turnover for restaurants located in the center is: 
### revenues = 89 + 1.76*seats  + 13.015*days_open - 171.7

## e)
### No, in fact there are no significant differences in the turnovers of 
### restaurants in the center and in the South‐West area.

## f) 
### All other conditions being equal, restaurants located in the North‐West area 
### have on average a turnover of 38,193 hundred euros higher than restaurants in 
### the centre. 
