### LECTURE 19 SCRIPT ###

### TIME SPENT ON SOCIAL ### (slides 48-49)
### Test whether the mean is greater than 34
# after the change in algorithm
#PEPUS I# <3 <3 <3
# H0: mu=34 (status quo)
# H1: mu>34 (I would like to show if enough evidence)
TEST.mean(x=Time,mu0=34,alternative="greater",data=Time_Social)
# Note that:
# xbar = 35.6
# s = 7.82
# t-score = 15.87
# the p-value is lower than any usual significance level
# (alpha = 0.05 or 0.01 or 0.10)
# therefore we reject H0!
# We have enough statistical evidence to say that H0 is not plausible and
# the average time on social is > 34 after the change in the algorithm!
pvalue = 1-pt(15.97,5976-1); pvalue # the p value is numerically zero

### TIME SPENT ON SOCIAL ### (slides 56-58)
### Test whether areas A and B are homogeneous 
### as for the time spent on platform
time.A = Time_Social$Time[Time_Social$Area=="A"]
time.B = Time_Social$Time[Time_Social$Area=="B"]

# Test for H0:muA-muB=0 vs H1:muA-muB≠0
# Let's construct a confidence interval on the 
# difference first
CI.diffmean(time.A,time.B,type="independent",conf.level = 0.95)
# NOTE THAT: with alpha = 0.05 the CI does NOT contain 0.
# hence 0 does not seem a plausible value with this significance
CI.diffmean(time.A,time.B,type="independent",conf.level = 0.99)
# NOTE THAT: with alpha = 0.01 the CI DOES contain 0.
# hence 0 is a plausible value with this significance

# Let's run the test:
TEST.diffmean(x=time.A,y=time.B,mdiff0=0,
              type="independent",alternative="two.sided")
# As we expected, the null hypothesis would be:
# H0 rejected if alpha = 0.05
# H0 NOT rejected if alpha = 0.01

### Test whether push notifications lead to an increase  
### of average time spent on platform (slides 59-60)
# Test for H0:muPUSH=muNOPUSH vs H1:muPUSH>muNOPUSH
time.push = Time_Social$Time[Time_Social$Push=="Yes"]
time.nopush = Time_Social$Time[Time_Social$Push=="No"]
TEST.diffmean(x=time.push,y=time.nopush,mdiff0=0,type = "independent",
              alternative="greater",digits=5)
# reject the null hypotheses H0 at any common significance level alpha
# we have statistical evidence to say that users who receive 
# push notifications spend a higher time on the social (alternative hypothesis H1)

### TRANSITION TO A NEW SOFTWARE ### (slides 61-62)
### Test increase in efficiency
# H0:muPost-muPre<=5 vs H1:muPost-muPre>5

TEST.diffmean(x=Post,y=Pre,mdiff0=5,type="paired",
              alternative="greater",data=Transition)

# how was the p-value obtained?
1-pnorm((55.8-46.52-5)/(12.6/sqrt(65)))

### Test difference between the average improvement
### in two groups
# Let's define a variable measuring how much each employee has improved
Transition$Improve = Transition$Post-Transition$Pre
# and extract the two groups
Impr1 = Transition$Improve[Transition$Department =="Dept1"]
Impr2 = Transition$Improve[Transition$Department=="Dept2"]

TEST.diffmean(x=Impr1,y=Impr2,mdiff0=0,type = "independent",
              alternative="two.sided",var.test=T)
# we rejct H_0 if alpha = 0.05
# we do not rejecty H_0 if alpha = 0.01
# note that the p-value is different depending
# on assumption on equality of variances

# If we set: var.test=T, then also a hypotheses test on the equality of the
# two variances is run! (it's called: Levene's test for homogeneity of variance)
# The p-value of this test is 0.02.
# therefore at the usual alpha = 0.05 significance we reject H0,
# i.e. the two variances seems different!
# We can use the result of the test
# for "Unknown variances assumed to be different"

### DRUG vs PLACEBO (slides 65-69)
nP = 42
xbarP = 0.06
sdP = 0.48
nF = 44
xbarF = 0.16
sdF = 0.35
alpha = 0.025
t.025 = qt(0.975,df=nP+nF-2)
s2pool = ((nP-1)*sdP^2 +
          (nF-1)*sdF^2)/(nP+nF-2)
se = sqrt(s2pool/nP + s2pool/nF)
tscore = (xbarF-xbarP)/se; tscore
1-pt(tscore,nP+nF-2)
