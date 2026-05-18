### LECTURE 11&12 SCRIPT ###

### COMPUTING PROBABILTIES OF A NORMAL DISTRIBUTION
# Assume you have X~N(2,9) # note that 9 is the variance
# What is Prob(X<2)?
0.5 # as a normal distribution is symmetric around its mean
# Prob(X<1) (i.e. cdf evaluated at 1)
pnorm(1,mean=2,sd=3)
# the command above computes the cdf of a N(2,9) evaluated at 1
# Pr(X>1) = 1-Pr(X<1)
1-pnorm(1,2,3)
# Pr(1<X<3) = Pr(X<3)-P(X<1)
pnorm(3,2,3)-pnorm(1,2,3)

### EXAMPLE: INCOME OF A FREELANCER
# Assume Income ~ N(71K,324K)
mu = 71; sigma = sqrt(324);
# Compute the probability of an income less than 20K
# Pr(Income<20K)
pnorm(20,mu,sigma)

# Compute the probability of an income between 20K e 80K
# Pr(20K<Income<80K)
pnorm(80,71,sqrt(324))-pnorm(20,71,sqrt(324))

# Compute the probability of an income higher than 90K
# Pr(Income>90K)
1-pnorm(90,71,sqrt(324))

# How much is (at least) the income of a top 10% earner?
# Here we are asked for the 90th percentile of the Income r.v.
# that is the value (we call it Income_0.10) such that
# P(Income>Income_0.10)=0.10 and of course P(Income<Income_0.10)=0.90
qnorm(0.9,mu,sigma)
# 94.06793 is the 90% percentile of our Normal distribution.
# 90% of people have an income lower than 94.06793
# 10% of people have an income higher than 94.06793

# Provide an interval including the 90% of "standard" incomes?
qnorm(0.05,71,sqrt(324))
# P(Income<41.39263) = 0.05
qnorm(0.95,71,sqrt(324))
# P(Income>100.60737) = 0.05
# Hence P(41.39263<Income<100.60737)=0.90
# i.e. the interval [41.39263,100.60737] represents the 90% standard incomes

# A declared income exceeded only by the 10% of the population
# entitles to a certain tax advantage.
# What is the minimum income threshold to benefit from the tax relief?
qnorm(0.90,mu,sigma)

# A systematic tax control is in place for individuals declaring an income
# in the lowest 5% declared incomes
# What level of declared income leads to tax control?
qnorm(0.05,mu,sigma)

# Declaring an income lower than the declared income exceeded by the 70% 
# of the freelancers raises the risk of tax control
# What levels of declared income expose to such risk?
qnorm(0.30,mu,sigma)
# Levels of income below 61.56079 expose you to such risk! As
# this level is exceeded with 70% probability