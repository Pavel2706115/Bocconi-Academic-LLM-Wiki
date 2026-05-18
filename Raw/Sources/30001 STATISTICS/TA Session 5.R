### EXERCISE 1
# X_i: time to complete a request 
# X_i~N(35,8^2)
mu = 35; sd = 8
# a)
# P(X_i>45)

p=1-pnorm(45,35,8)

# The probability that it will take more than 45 minutes to complete a
# request is 10.6%.

# b)
# X_1, X_2, ..., X_70 i.i.d. X_i~N(35,8^2) n = 70

# b1) 

# Y_i = 1 if X_i > 45 and 0 otherwise
# Y_i~Bernoulli(p=0.10565)
# (1/n)*sum(Y_i)~N(p,p(1-p)/n) # according to CLT as n = 70
# P((1/n)*sum(Y_i) < 0.15) = pnorm (0.15,p,sqrt(p*(1-p)/n)) = 88.6%

sd<-sqrt(p*(1-p)/n)

# The probability that the proportion of calls taking over as minutes
# is below 0.15 is 88.6%.

# THIS USES PEPUS 2, WHERE THE MEAN IS BASICALLY THE PROBABILITY FOR SUCCESS
# AND THE SD IS THE PROBABILITY FOR SUCCESS IN THIS EASY FORMULA
# SQRT(P*(P-1)/N)

# b2)

1 - (pnorm(34,35,8/sqrt(70))-pnorm(33,35,8/sqrt(70)))

# The probability that the avg time to complete a request is between 33 and 34 minutes
# is 87%.

# b3)

qnorm(0.9, 35,0.96) = 36.2

# The value exceeded by the mean time for completion of a request with probability 0.1 is 36.2

# b4)

pnorm(420, 11*35, sqrt(11)*8)

# c)

# No, because if n is below 30, we can not apply the CLT.

### EXERCISE 3

# a)
# X_1, X_2, ..., X_256 with n=256 and i.i.d X_i~N(43.1,10.95)
n = 256
SE <- sd/sqrt(n); SE = 0.68
sd = 10.95
Xbar <- mean(superstore$Age)

# It is possible to calculate the stnadart error and it is equal to 0.68.

# b)

distr.table.x(superstore$KidsAtHome)

# Y_1, Y_2, ..., Y_256 and i.i.d Y_i~N(p,sqrt(p*(1-p)/n) # n > 30
# p = 0.29
# se = 0.028

### EXERCISE 4

# X_1, X_2, ..., X_30 and i.i.d X_i~N(42,0.12)

n=30; xbar=42; sd=0.35

# a) 
# P(xbar>0.01)

qnorm(0.99,42,0.35)


