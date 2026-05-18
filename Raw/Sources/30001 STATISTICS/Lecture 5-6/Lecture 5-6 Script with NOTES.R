### LECTURE 5-6 SCRIPT ###

### SUMMARY MEASURES: LOCATION ###
### CENTRAL TENDENCY MEASURES
# Only the mode is displayed for QUALITATIVE NOMINAL data
distr.summary.x(x=Payment,stats="central", data=Loyalty)
# the mode is Credit Card, with 0.408 relative freq.

# Mode and median are displayed for QUALITATIVE ORDINAL data
distr.summary.x(x=Recommend.F,stats="central", data=Loyalty)
distr.plot.x(x=Recommend.F,plot="bars", data=Loyalty)

# Mode, median and mean can be computed for QUANTITATIVE data
distr.summary.x(x=Age,stats="central", data=Loyalty)
# here the mode is not very useful/meaningful because it's relative freq
# is pretty low (less than 5%)
# the mode is more meaningful when we have few values/levels of the variable

# Calculate quickly the mean of a vector of raw data (slide 21)
x = c(4,3,3,1,0,1,2,3,3,4,2,5,4,3,4,5)
distr.summary.x(x,stats = "central")

# Calculate quickly the mean of a variable presented in a freq table
value = 0:5
f = c(1,2,2,5,4,2) # absolute freq.
n = sum(f) # sample size
p = f/n # relative freq.
mean = sum(value*f)/n # mean
mean

### QUARTILES
Profit = c(81.8,82.6, 85.7,86.8,88.9,91.5,91.7,92.8,94.3,96.2,103.8)
distr.summary.x(Profit,stats="quartiles")
distr.summary.x(x=Amount_V,stats=c("central","quartiles"), data=Loyalty)

### PERCENTILES
distr.summary.x(x=Profitability,
                stats=c("q1","q2","mean","q3","p90","p95","p99"), 
                data=Loyalty)
# What is the interval containing the Profitability of the 80% 
# most standard customers?
distr.summary.x(x=Profitability,
                stats=c("p10","p90"), #10th and 90th percentiles
                data=Loyalty)
# The interval [106.44,434.84] contains the profitability measurements
# of the 80% "most common" customers.
# Note that 10% of the customers have profitability lower than 106.44
# and 10% of the customers have profitability higher than 434.84

### BOXPLOT
# The boxplot is an effective representation of a numerical variable
# It describes the distribution's main features:
# CENTRE, LOCAL DISPERSION, GLOBAL DISPERSION, SHAPE, OUTLIERS (when shown)
# Boxplot is a very effective graphical tool
# for comparing distributions
distr.plot.x(x=Profitability,plot.type="boxplot", data=Loyalty)

# The box extends from the first quartile Q1 to the
# third quartile Q3. The line in the middle is the Median
distr.summary.x(x=Profitability,stats=c("central","quartiles"), data=Loyalty)
Q1 = 139.1; Median = 178.8; Q3 = 280.4

IQR = Q3-Q1; IQR # interquartile range
# If an obs is above Q3+1.5*IQR it is considered an UPPER OUTLIER
UOlimit = Q3+1.5*IQR; UOlimit
# Obs over the Upper Outlier limit are UPPER OUTLIERS
# and are drawn as points in a boxplot
# Obs that are NOT outliers, are called REGULAR OBSERVATIONs
# The upper whisker extends from Q3 to the maximum
# of the regular obs
max(Loyalty$Profitability[Loyalty$Profitability<UOlimit])
# So the upper whisker extends from Q3 to 478.6 in this case

# Note that the limit for LOWER OUTLIERS is Q1-1.5*IQR
LOlimit = Q1-1.5*IQR; LOlimit
# No customer has profitability under -72 therefore
# there are no LOWER OUTLIERS in the distribution
# The lower whisker here extends from Q1 to the minimum value observed
# that is:
min(Loyalty$Profitability) #81.8