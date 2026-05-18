### LECTURE 13 SCRIPT ###
### THE FANTASTIC PEPUS ###

### PEPUS 1 (slide 11)
# We want to estimate the
# population mean mu.
# mu is the average duration
# of a call 
# X_1,X_2,...,X_n i.i.d.
# (call durations)
# E[X_i]=mu; Var(X_i)=sigma^2
n = length(CallCenter.P$TimeTalk)
n #n =300
xbar = mean(CallCenter.P$TimeTalk)
# xbar
# xbar = 254.3733
# xbar is the estimate of mu
# the population mean

# To estimate the standard error
# of the ESTIMATOR, first we
# calculate the sample standard
# deviation of TimeTalk
s = sd(CallCenter.P$TimeTalk); s
# s is an estimate of sigma
# which is the standard deviation
# of the population
se = s/sqrt(n); se
# se is an estimate of the
# STANDARD ERROR of the
# ESTIMATOR Xbar
# Recall that the STANDARD ERROR
# of an estimator is its
# STANDARD DEVIATION
# IMPORTANT!
# INTERPRETATION OF STANDARD ERROR:
# the SE is an indicator of how
# precise our ESTIMATOR is.
# the lower the SE the more precise
# the ESTIMATOR.
# se is the ESTIMATE OF THE SE.
# The SE represents the
# EXPECTED DISTANCE OF THE ESTIMATOR
# FROM THE PARAMETER mu
# however the STANDARD ERROR
# DOES NOT TELL US ANYTHING
# about the distance of our
# ESTIMATE xbar = 254.3733 from
# the true value mu of
# the population mean
# I could have an estimator with 
# very small SE, however becasue I'm
# unlucky :'( I get an estimate
# very far from the parameter mu

# ANOTHER EXAMPLE!
# Estimate the mean time of calls
# for people who call on Saturdays.
# Also report the standard error! Of Course!
xSat = CallCenter.P$TimeTalk[CallCenter.P$WeekDay=="Sat"]
xbarSat = mean(xSat); xbarSat # estimate of muSat
# we cannot calculate the exact SE!
# Because we are not given sigma
s = sd(xSat); s # s in an estimate of sigma
nSat = length(xSat); nSat
seSat = s/sqrt(nSat); seSat
# the estimate of the standard error is se = 30
# that's an estimate of the expected distance
# of the estimator from muSat, the parameter of interest

# We could do the same for the average time of calls on fridays
xFri = CallCenter.P$TimeTalk[CallCenter.P$WeekDay=="Fri"]
xbarFri = mean(xFri); xbarFri # estimate of muSat
# we cannot calculate the exact SE because we are
# not given with sigma
s = sd(xFri); s
nFri = length(xFri); nFri
seFri = s/sqrt(nFri); seFri

# Recall the lower the standard error the more efficient 
# the estimator. 
# However the standard error cannot be used to assess
# how good specific estimates are! 
# So we cannot say xbarFri is closer to its parameter
# than xbarSat is to its parameter

### PEPUS 2 (slide 17)
# We want to estimate the
# population proportion p.
# p is the proportion of calls
# being solved for the whole
# population
CallCenter.P$Solved
# categorical variable with
# two levels
# indicates whether the call was
# solved
distr.table.x(CallCenter.P$Solved)
phat = 0.91 # this is the sample
# proportion estimate
# the sample proportion phat = 0.91
# it is our estimate of the 
# population proportion p

# the estimate of the standard
# error of the estimator Phat is:
se = sqrt(phat*(1-phat)/n); se
# se = 0.01652271

# ANOTHER EXAMPLE!
table(CallCenter.P$Topic)
# Estimate the proportion of solved calls
# among those related to payment
# Report the standard error of the corresponding estimator
xPay = CallCenter.P$Solved[CallCenter.P$Topic=="Payment related"]
distr.table.x(xPay)
phatPay = 76/80; phatPay
se =  sqrt(phatPay*(1-phatPay)/80); se

### PEPUS 3 [SLIDE 25]
# We want to estimate the difference
# between two population means
# mux - muy
# mux: mean refund for Smokers in
# the population (with no children)
# muy: mean refund for Non-Smokers
# in the pop (with no children)
# First we extract the relevant
# samples:
# RefundSmokers: the refunds for
# smokers with no children
RefundSmokers = Insurance$refund[
  Insurance$smoker=="yes"&
  Insurance$children==0]
# RefundNONSmokers: the refunds for
# NON smokers with no children
RefundNONSmokers = Insurance$refund[
  Insurance$smoker=="no"&
  Insurance$children==0]
nx = length(RefundSmokers); nx
# sample size of smokers sample
ny = length(RefundNONSmokers); ny
# sample size of NON smokers sample
xbar = mean(RefundSmokers); xbar
# sample mean refund for smokers
ybar = mean(RefundNONSmokers); ybar
# sample mean refund for non smokers
dbar = xbar - ybar; dbar
# difference between the two sample
# means
# dbar = 23729.57 is our estimate
# of mux - muy

# estimate the standard error of
# the estimator Xbar - Ybar
# 1] under the assumption that
# sigma_x is different from sigma_y
sx = sd(RefundSmokers); sx
sy = sd(RefundNONSmokers); sy
se = sqrt(sx^2/nx+sy^2/ny); se
# 2] under the assumption that
# sigma_x = sigma_y
spool2 =
  ((nx-1)*sx^2+(ny-1)*sy^2)/
  (nx+ny-2)
spool2
se = sqrt(spool2/nx+spool2/ny); se

# Note that we choose between [1]
# and [2] depending on the question.
# Typically if you are explicitly
# told that sigma_x = sigma_y,
# use [2], otherwise use [1].
# In the exam paper, specify the
# assunption [1] or [2] that you
# used!

### PEPUS 4 (slide 27)
# We want to estimate the average
# difference between pairs of
# measurements
# We are given with:
n = 44; xbar = 155; ybar = 122;
# Our estimate of mux - muy =: mud
# (average drop in cholesterol)
dbar = xbar - ybar; dbar
# We estimate the standard error
# of the estimator
sx = 19.9; sy = 24.5; sxy = 23.4;
se = sqrt(sx^2+sy^2-2*sxy)/sqrt(n)
se
# Note that if we had the dataset
# with the actual differences in the 
# measurements, we could calculate
# the standard error of the 
# differences here instead to get
# s_d!

### PEPUS 5 (slide 31)
# We want to estimate the difference
# in proportions: pA-pB
# Banner A was clicked by 19.29%
# of people who saw it
# Banner B was clicked by 26.30%
# of people who saw it
phatA = 456/2364; phatA
phatB = 611/2323; phatB
nA = 2364; nB = 2323;
phatA-phatB #phatA-phatB = -0.0701
# is our estimate of the difference
# between the proportion pA-pB

# let's estimate the standard error
# of our estimator
se = sqrt(phatA*(1-phatA)/nA+
          phatB*(1-phatB)/nB); se
# se = 0.01221878