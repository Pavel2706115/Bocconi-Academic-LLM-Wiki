### LECTURE 7 SCRIPT ###

### SUMMARY MEASURES: DISPERSION ###
### RANGE,INTERQUARTILE RANGE, VARIANCE,
### STANDARD DEVIATION, COEFFICIENT OF VARIATION
# Variance calculations "BY HAND" for a small sample
x = c(35,25,54,60,44,61,27,55,62)
n = length(x)
xbar = sum(x)/n
# standard method
s2 = sum((x-xbar)^2)/(n-1); s2
# indirect calculation formula
s2 =(n)/(n-1)*(sum(x^2)/n-xbar^2); s2

# Dispersion measures calculations with distr.summary.x
distr.summary.x(x,stats="dispersion")
distr.summary.x(x=Age,stats=c("central","dispersion"),
                data = Loyalty)
distr.summary.x(x=Profitability,stats="dispersion", data=Loyalty)
distr.summary.x(x=Nr_visits,stats="dispersion", data=Loyalty)
distr.summary.x(x=Income,stats="dispersion", data=Loyalty)