### R STUDIO PRACTICAL ###

# y = basket; x = income
# Estimate a linear regression model that explain
# the quality of the basket (y)
# form the customer income (x)
m = lm(basket ~ income, data = Basket)
summary(m) # full summary of the estimated model

### OUTPUT INTERPRETATION 

# Residuals:
# In this case the five number summary for the residuals DO NOT show skewness
# residuals seem pretty symmetric
# We can also plot the residuals:
boxplot(m$residuals) # residuals look symmetric
hist(m$residuals) # reasonably bell shaped distribution

# Coefficients:
b0 = 3.1638282; b1 = 0.0109748;
se = 0.0006467 # se(betahat_1): estimate of standard error of betahat_1
tscore = b1/se; tscore
# For the test H0: beta_1=0 vs H1: beta_1≠0
t-score # 16.97047
# and the corresponding p-value<2e-16 ***
# We REJECT H0 and say that the coefficient of INCOME is SIGNIFICANT

# Other info
s_epsilon = 9.793 # residual standard error
# 97 corresponds to the n-2 degrees of freedom
R2 = 0.748; # coefficient of determination

# Confidence intervals for the COEFFICIENTS of the model
confint(m,level=0.90) # provides confidence intervals for beta0 and beta1

# Confidence interval for the expected basket quality
# of  customers with income = 5000. Confidence = 0.99
boxplot(Basket$income) # 5000 belongs to the observed range
xg = data.frame(income = 5000)
predict(m,xg,interval = "confidence",level = 0.99)
 
# Prediction interval for the basket quality
# of a specific customer with income = 5000. Confidence = 0.99
predict(m,xg,interval = "predict",level = 0.99)


### ANALYSIS OF RESIDUALS (ONLY R-STUDIO TOPIC)
# # this covers SLIDES 78-END
# Recall:
# WEAK ASSUMPTIONS:
# 1) LINEARITY
# 2) HOMOSCHEDASTICITY
# 3) UNCORRELATED RESIDUALS
# STRONG ASSUMPTIONS ALSO INCLUDE:
# 4) NORMALITY

# We learn how DETECT MAJOR DEVIATIONS FROM THE ASSUMPTIONS OF:
# 1) LINEARITY, 2) HOMOSCHEDASTICITY and 4) NORMALITY
# with the EMPIRICAL ANALYSIS OF RESIDUALS

# Check LINEARITY AND HOMOSCHEDASTICITY
# In SIMPLE LINEAR REGRESSION we can spot DEVIATION FROM LINEARITY and
# HOMOSCHEDASTICITY by looking at the scatterplot of y against x
distr.plot.xy(income,basket,plot.type="scatter",data=Basket,fitline = TRUE)
# the scatterplot evidences a linear relationship
# the points fluctuate around the regression line
# with constant variance

# However this is NOT POSSIBLE in MULTIPLE LINEAR REGRESSION
# In MULTIPLE LINEAR REGRESSION instead we use the command plot(m,1) to
# display the MODEL RESIDUALS against the FITTED VALUES yhat_i
plot(m,1)
# the residuals do not follow a particular
# non-linear pattern (LINEARITY OK!)
# the residuals fluctuate with
# constant variance (HOMOSCHEDASTICITY OK)

# Check NORMALITY
# IN SIMPLE AND MULTIPLE LINEAR REGRESSION we can spot DEVIATION FROM
# NORMALITY by looking at the distribution (histogram) of the
# (standardised) RESIDUALS
rstd = rstandard(m)
distr.plot.x(rstd,plot.type = "hist")
# the distribution of the residuals is
# reasonably BELL-SHAPED
# hence there is NO OBVIOUS DEVIATION
# FROM NORMALITY <3

# EXAMPLE (Advertising: sales ~ facebook)
m = lm(sales ~ facebook, data = Advertising)
summary(m)
# (interpretation of slope) for each extra euro spent on Facebook ad
# on average the sales go up by 0.20250
# (interpretation of intercept) if the amount spent on Facebook ad is 0
# the expcted sales is equal to 11.17
min(Advertising$facebook)
# 0 belong to the range of the data so it seems like a reliable interpretation

# Linearity and Homoschedasticity Check
distr.plot.xy(facebook,sales,plot.type="scatter",
              data=Advertising,fitline = TRUE) # only for SIMPLE LR
plot(m,1) # also for MULTIPLE LR
# The red line is basically flat
# hence LINEARITY OK
# residuals fluctuate with
# non homogeneous variability
# this indicates DEVIATION FROM
# HOMOSCHEDASTICITY
# so e.g. prediction intervals will be
# VERY UNRELIABLE

# Normality Check
distr.plot.x(rstandard(m),plot.type = "hist")
# the distribution is mildly left skewed
# this indicates minor deviation from 
# NORMALITY

# EXAMPLE (Restaurants: Revenues ~ Income)
m = lm(Revenue ~ Income, data = Restaurants)
summary(m)

# Linearity and Homoschedasticity Check
distr.plot.xy(Income,Revenue,plot.type="scatter",
              data=Restaurants,fitline = TRUE) # only for SIMPLE LR
plot(m,1) # also for MULTIPLE LR
# MAJOR DEVIATION FROM LINEARITY!
# as the residuals follow a 
# NON LINEAR PATTERN

# Normality Check
distr.plot.x(rstandard(m),plot.type = "hist")
# slight left skewed minor deviation from
# normality as well! :(