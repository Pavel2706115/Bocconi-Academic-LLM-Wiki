### EXERCISE 1

# X_1, X_2, ..., X_N with n=16 i.i.d X_i~N(87,22^2)

# a)
# The standard error is just the standard deviation equal to 22.

n=16; mu=87; sigma=22 
se = sigma/sqrt(n); se # standard error for xbar

# b)
# P(Xbar<100)

?pnorm(100,mu,sigma/sqrt(n)) # The probability that the sample mean is below 100 min is 99.1%.

# c)
# P(Xbar>80)

1-pnorm(80,mu,se) # The probability that the sample mean is more than 80 mean is 89.84%.

# d)
# P(Xbar<85 or Xbar>95)

1-(pnorm(95,mu,se)-pnorm(85,mu,se)) #The probability that the sample mean is outside the range [85,95] is 43%.

# e)
# in b) as n increases the probability gets HIGHER
# in c) as n increases the probability gets HIGHER
# in d) as n increases the probability gets LOWER

###EXERCISE 2

# Define X_i = 1 if the investor is interested. # success
# Define X_i = 0 if the investor is not interested.
# X_i can be either 1 or 0, it is a random variable
# Therefore X_i~Bernoulli(p=0.2)
# Consider a random sample of investors:
# X_1, X_2, ... X_n i.i.d with X_i~Bernoulli(p=0.2)
# Note that E[X_i]=0.2 and Var(X_i) = p(1-p) = 0.2*0.8

# a)
# The sample proportion is defined at:
# Phat = sum(X_i)/n
# As n = 130, we can use CLT, to say:
# Phat~N(p,p*(1-p)/n) #approximately
# Therefore Phat is a normal distribution with a mean
p = 0.2;
# and a variance
p*(1-p)/n;
# The STANDARD ERROR OF PHAT is:
se = sqrt(p*(1-p/n))
se = 0.44

# b)
# P(Phat>0.15):

1-pnorm(0.15,p,se) #54%

# c)
1-(pnorm(0.22,p,se)-pnorm(0.18,p,se)) #96.4%

# d) HIGHER, HIGHER

### EXERCISE 3

# PEPUS 1
#  X_1, X_2, ..., X_N with n = 25 i.i.d X_i~N(420,100^2)

n=25; mu=420; sigma=100
SE = sigma/sqrt(n)
# Standad error equals 20

# a)

pnorm(450,420,20) 
# The probability that the sample mean score is higher than 450 is 93.3%.

# b)

(pnorm(450,420,20)-pnorm(400,420,20))
# The probability that the sample score is between 400 and 450 is 77.5%.

# c)

qnorm(0.9,420,20)

# The probability 0.1 that the sample mean is higher than 445.631.

# d)

qnorm(0.1,420,20)

# The probability 0.1 that the sample mean is lower than 394.4.

### EXERCISE 4

# X_1, X_2, ... X_n with n = 9 i.i.d X_i~N(14.8,6.3^2)
n = 9; mu = 14.8; sigma = 6.3

SE = sigma/sqrt(n)
SE = 2.1

# a)

1-pnorm(19,14.8,2.1)

# The probability of the sample mean being more than 19 is 22.8%.

# b)

pnorm(19,14.8,2.1)-pnorm(10.6,14.8,2.1)

# The probability of the sample mean being between 10.6 and 19 is 95.5%.

# c)

qnorm(0.25,14.8,2.1)

#The probability of 0.25 that the sample mean percentage return is less than 13.38%.

# d)

# SMALLER