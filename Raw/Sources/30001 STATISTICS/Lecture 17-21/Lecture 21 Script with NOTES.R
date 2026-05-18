### LECTURE 21 SCRIPT ###

### CHISQUARED GOODNESS OF FIT TEST

# Brand Preferences
O = c(151,117,140,162); O # observed abs freq
# We test 
# H0: p1=0.25,p2=0.25,p3=0.25,p4=0.25
# vs
# H1: at least one equality in H0 does not hold
n = sum(O); n # sample size
p = rep(0.25,4); p # rel. freq. under H0

### COMPUTATIONS
E = p*n; E # expected freq. under H0
# WE CAN PROCEED WITH THE TEST IF ALL THE EXPECTED
# FREQUENCIES IN E ARE >= 5
chi2score = sum((O-E)^2/E); chi2score
# under H0 the chi2score ~ chi2(df=3)
# degrees of freedom are: (number of categories) - 1
# calculate the critical region for alpha = 0.01
qchisq(0.99,df=3) # NOTE the function chisq.test
# does not calculate the rejection region!!!
# R0.01 = {chi2score>11.34487}
# chi2score = 7.782456 -> DO NOT REJECT H0!!!!!
# alternatively
pvalue = 1-pchisq(chi2score,df=3); pvalue
# pvalue = 3.773923e-06 super small. REJECT H0!
### END OF COMPUTATIONS

# Note that the computations above are carried over by the
# R function chisq.test (not in UBSTATS):
chisq.test(x = O,p = p) # same results obv!

# Clients of a bank: goodness of fit 
# H0: p1=0.05,p2=0.28,p3=0.17,p4=0.35,p5=0.15
# vs
# H1: at least one equality in H0 does not hold
O = c(56,389,267,526,159)
chisq.test(x = O,p=c(0.05,0.28,0.17,0.35,0.15))
# EQUIVALENTLY:
O = table(Bank$Education_Level)
chisq.test(x = O,p=c(0.05,0.28,0.17,0.35,0.15)) # same but faster
# p-value = 0.0002606 < 0.01 -> REJECT H0
# the observed absolute freq. are NOT consistent with respect to
# the rel. freq. under H0

### CHISQUARE TEST FOR INDEPENDENCE OF
### TWO CATEGORICAL VARIABLES 

# Clients' class and number of campaigns

# We used to check independence between variables by
# looking at the conditional relative frequencies and
# their corresponding stacked bar-charts!
distr.plot.xy(x=Class,y=Num, freq="prop", freq.type="y|x",
              plot.type="bars", 
              color=c("red","orange","green","darkgreen"),
              data=Class_Campaign)
# Now we can be more rigorous and run the 
# CHI SQUARED TEST FOR INDEPENDENCE! WOW!
# H0: Class and Nr of Campaigns are INDEPENDENT
# vs
# H1: Class and Nr of Campaigns are DEPENDENT

### COMPUTATIONS ARE OPTIONAL, PRO LEVEL ###
### Pier recommendation: DO NOT pass tables in R at the exam!
### You will not be given such big tables!
O = matrix(c(15,20,6,
             7,30,10,
             6,15,20,
             6,10,20),nrow = 4,ncol=3, byrow = TRUE)
rsums = rowSums(O); rsums
csums = colSums(O); csums
E = rsums%*%t(csums)/165; E
rowSums(E)
colSums(E)
chi2score = sum((O-E)^2/E)
### END OF OPTIONAL COMPUTATIONS ###

# All the calculations above are carried over
# with the following code:
chisq.test(x=Class_Campaign$Num,y=Class_Campaign$Class)
# as the p-value is small, we reject H0!
# The variables are NOT independent!

# equivalently we can check that the chi2score = 27.921
# belongs to the rejection region defined
# (alpha = 0.001, df = 6)
qchisq(0.999,6)
# R0.001 = {chi2score>22.45774}
# 27.921 is in the rejection region therefore we reject H0!