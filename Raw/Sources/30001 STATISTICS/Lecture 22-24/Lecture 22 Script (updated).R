# Lecture 22 Script
# [Slide 70]
# In the dataset Basket the variable INCOME represents
# the household income of a customer
distr.plot.x(Basket$income,plot.type="hist",breaks=10)
# the variable BASKET represents the quality of the
# basket of good purchased by the customer
distr.plot.x(Basket$basket,plot.type="hist",breaks=10)
# let's explore the relationship between these two variables
x = Basket$income
y = Basket$basket
distr.plot.xy(x,y,plot.type="scatter",fitline = TRUE)
# the relationship looks linear and positive
# let's try and fit a linear model!
sxy = cov(x,y); sxy
sx2 = var(x); sx2
b1 = sxy/sx2; b1
xbar = mean(x); ybar = mean(y);
b0 = ybar-b1*xbar; b0
# The fitted model has equation:
# yhat_i = b0 + b1*x_i
# yhat_i = 3.16 + 0.01097*x_i

# INTERPRETATION OF THE ESTIMATED COEFFICIENTS b0 AND b1
# b0 is the forecast for the response (basket quality) for a value of
# the independent variable equal to zero i.e. x=0
# (customer with household income equal to 0)

# Note that we can only make predictions for values of the 
# independent variable x that are WITHIN THE RANGE OF THE
# OBSERVED DATA for x
# as we do not know if the relationship extends beyond such range
# In this case 0 does not belong to the data range,
# so we cannot give a meaningful interpretation

# b1 interpretation:
b1
# for a unit increase household income, the AVERAGE quality of
# the basket increase by (all other variables fixer): 0.01097483

# In R, linear model are estimated with the function lm()
m = lm(basket~income,data = Basket)
m