### LECTURE 25 SCRIPT ###
### MULTIPLE LINEAR REGRESSION
# [slides 11-16]
# Motivational Example: Sales and Prices
# Simple linear regression of Sales on Price
distr.plot.xy(x=Price,y=Sales,plot.type="scatter",
              data=Sales,fitline=T)
m1 = lm(Sales ~ Price, data = Sales)
summary(m1)
# Linearity and Homoschedasticity Check
plot(m1,1) # both Linearity and Homoscedasticity are reasonably met
# Normality Check
hist(rstandard(m1)) # Normality is reasonably met

# Residuals vs Price.Comp (just MOTIVATIONAL!)
distr.plot.xy(Sales$Price.Comp,m1$residuals,
              plot.type="scatter")
# there is a linear association between the price set by the competitor
# and the residuals of the model!
# when Price.Comp is high, residuals are positive (obs above fitted values)
# when Price.Comp is low, residuals are negative (obs are below fitted values)

# Simple linear regression of Sales on Price.Comp
distr.plot.xy(x=Price.Comp,y=Sales,plot.type="scatter",
              fitline=T,data=Sales)
m2 = lm(Sales ~ Price.Comp, data = Sales)
summary(m2)

# Regression of Sales on Price and Price.Comp
m = lm(Sales ~ Price + Price.Comp, data = Sales)
summary(m) 

# Analysis of residuals
plot(m,which=1) # linearity and homoschedasticity are met!
distr.plot.x(rstandard(m),plot.type="histogram")
# normality ALLRIGHT!

# Predicting sales corresponding to
# Price=50 and Price.Comp=25,50,75
# [SLIDE 36]
xg = data.frame(Price=50,Price.Comp=c(25,50,75))
# confidence interval for expected sales from multiple days
predict(m,newdata=xg,
        interval="confidence",level=0.95)
# prediction interval for sales of and individual day
predict(m,newdata=xg,
        interval="prediction",level=0.95)

# Confidence intervals for the model coefficients. Same as Simple Linear Regression!
confint(m,level=0.95)

# By how much does the Sales change ON AVERAGE if I increase the price by 5
# if the price of the competitor is FIXED???
5*-1.284 # for a 5 unit increase in price, the AVERAGE sales go down by -6.42,
# Price.Comp being fixed

# provide a 95% confidence interval for your point estimate
confint(m,level=0.95)
[-1.543,-1.024] # This is the 95% ci for the coefficient of Price
# the ci for the change in AVERAGE sales (Price.Comp fixed) corresponding
# to an increase in Price of 5 unit is:
5*c(-1.543,-1.024) # [-7.72,-5.12]

# Retention, Loyalty, SalesPersons
# SLIDES [37-42]
# Simple linear regressions
distr.plot.xy(x=Loyalty,y=Retention,plot.type="scatter",
              fitline=T,data=Retention)
distr.plot.xy(x=SalesPersons,y=Retention,plot.type="scatter",
              fitline=T,data=Retention)
summary(lm(Retention ~ Loyalty, data = Retention))
summary(lm(Retention ~ SalesPersons, data = Retention))

# Multiple linear regression
m = lm(Retention ~ Loyalty+SalesPersons, data = Retention)
summary(m)
confint(m)