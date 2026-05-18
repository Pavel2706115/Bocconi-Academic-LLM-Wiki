# EXERCISE 7.1
# a)

# a1) 

# The 47 workers in the sample should be representative of the population we
# are interested to. Thus, the estimate can refer only to the time taken by workers
# looking for a job in the same position as that of the workers in the sample.
# The sample size is not particularly high; even so it is high enough to apply
# the central limit theorem and to approximate the distribution of the (random)
# sample mean with a normal distribution, without any specific assumptions on
# the distribution in the population.

# a2)

# We want to test a hypothesis on the time needed to find a new job. Such
# hypothesis should be set as the alternative: we want to verify whether there
# is enough empirical evidence supporting the hypothesis. Therefore, the contrasted
# hypotheses are H0: mu >= 45 vs H1: mu < 45. Actually, also from the point of
# view of a worker who wants to change her job, the most serious error consists
# in concluding that the average time needed to find a new job is lower than 45
# weeks when it is higher.
# The test statistic used to verify hypotheses on the mean when the variance is
# unknown is the sample mean standardized under the null hypothesis using the
# correct sample variance to estimate the variance:

# sqrt(n)*(Xbar - mu0)/S

n <- 47
Xbar <- mean(NewHired$Weeks)
mu0 <- 45
S <- sd(NewHired$Weeks)

result <- sqrt(n)*(Xbar - mu0)/S

# where Xbar is the point estimate of the mean of variable Weeks and S is the
# estimate of the standard error of the sample mean, obtained by dividing the
# estimate of the standard deviation, 17.2206, by the square root of the sample
# size, n = 47. 

# The p-value of the sample realization is 

# The result is also obtainable through the UBStats function TEST.mean in R Studio:

TEST.mean(NewHired$Weeks, mu0 = 45, alternative = "less")

# The p-value of the sample realization is 0.0309 if one refers to a Student's t
# distribution with 46 df(n-1) or 0.0278 if one uses the normal approximation.
# The p-value is lower than 0.05 in both cases, and therefore the null hypothesis
# is rejected and there is enough empirical evidence to conclude that the average
# time needed to find a new job is lower than 45 weeks,

# a3)

# If the significance level drops 0.05 to 0.01, then the null hypothesis will
# not be rejected. The p-value would have been greater than the significance
# level and the conclusion reached would have been the opposite.

# a4)

# The significance level determines how extreme a sample result must be under
# H0 ti justify its rejection; in the rejection-region approach it defines the
# critical values, while in the p-value approach it acts as the threshold for
# decision-making.

# b)

# If the variance is assumed to be known and equal to 16, the normal approximation
# can be used. The rejection is based on the sample mean, and results in:

# R: xbar < mu0 - z*sigma/sqrt(n) = 45 - 1.28*4/sqrt(47)

# Or equivalently:

# R: (xbar - mu0)/(sigma/sqrt(n)) = (xbar - 45)/(4/sqrt(47)) < -1.28

# Where 1.28 is the percentile of order 0.9 of a standardized normal obtained
# using the function qnorm(0.9)

# b1) 

# The probability of concluding that the average time needed to find a new
# job is lower than 45 weeks when it is 50 weeks is the probability of rejecting
# the null hypothesis when it is true, because the value 50 is included in the
# set of values specified by the null hypothesis.
# Therefore, it is the probability of a type 1 error:
# Pr(Xbar < 44.25|mu = 50) = Pr(Z<(44.25-50)/(4/sqrt(47)))
# Using pnorm(44,25, mean=50, sd=4/sqrt(47)) we obtain a value close to zero.

# b2)

# The probability of concluding that the average time needed to find a new
# job is higher than 45 weeks when it is 43 weeks is the probability of rejecting
# the null hypothesis when it is true, because the value 43 is included in the
# set of values specified by the null hypothesis.
# Therefore, it is the probability of a type 1 error:
# Pr(Xbar > 44.25|mu = 43) = Pr(Z<(44.25-43)/(4/sqrt(47)))
# Using pnorm(44.25, mean=43, sd=4/sqrt(47)) we obtain a probability of 0.016.

1- pnorm(44.25, mean=43, sd=4/sqrt(47))

# c) 

# For the agency, the worker's claim "should be tested and verified" and
# clearly the most serious error will consist that the percentage is higher
# than 10% when in fact it is lower. Therefore, the hypotheses to test are
# H0: p =< 0.1 vs H1: p > 0.1, where p is the proportion of workers who
# needed more than 52 weeks to find a new job.

# 
TEST.mean(propose, mu0 = 0.1, alternative = "less")

propose <- sum(NewHired$Weeks > 52)
n <- length(NewHired$Weeks)
phat <- propose/n

# The sample proportion is about 0.15 (phat); nonetheless, such value does not
# provide an empirical evidence sufficient to support the claim that the considered
# proportion is higher than 0.1 at the population level. 

# Under H0 using p0 = 0.1, the standard error is:

# SE = sqrt(p0(1-p0)/n) = sqrt((0.1*0.9)/47) = 0.04
# z = (phat - p0)/SE = (0.15 - 0.1)/0.04 = 1.12

# Indeed, the realization of the test statistic is 1.12, and its p-value, 0.13, 
# is higher than any standard. Since H1: p > 0.1, "more extreme" means larger
# phat, hence larger z. So:

# p-value = P(Z >= 1.12) = 1 - pnorm(1.12) = 0.13

# At the 5% significance level, the data do not provide enough evidence to support
# the worker's claim that the proportion taking more than 52 weeks is greater than
# 10%.

# EXERCISE 7.2

# a) 
# a1)

# Since we do not want to favor either side, we compare the hypotheses
# H0: mu = 2200 against H1: mu != 2200, which correspond to a two-sided test.
# Because the sample size is large enough, we can use the sample data to estimate
# the variance and rely on asymptotic results. In particular, we can either use
# the normal approximation, which is justified by the central limit theorem (the
# sample mean is approximately normally distributed and the sample variance
# approximates the population variance), or use the Student's t distribution,
# which explicitly accounts for the additional uncertainty introduced by
# estimating the variance from the sample. Although the sample size is not very
# large, it is sufficient to apply the CLT, making both approaches reasonable.
# The estimates of the mean and the variance are:

# H0: mu = 2200 vs H1: mu != 2200

mu0 <- 2200

# Sample size:

n <- 47

# Sum of salaries:

sum_x <- 99150

# Sum of squared salaries:

sum_x2 <- 225067500

# From these, we can compute:
# 1. the sample mean xbar
# 2. the sample variance s2

# 1. Compute the sample mean

xbar <- sum_x/n

# 2. Compute the sample variance from aggregates
# A key identity:

 s2 <- (sum_x2 - n*(xbar)*(xbar))/(n-1)

# Then:

 s <- sqrt(s2)

# So salaries vary with a standard deviation around €588

# Next, variance is unknown, so the "correct" finite-sample test uses Student's t:

t <- ((xbar - mu0)*sqrt(n))/s

# Degrees of freedom:

df <- n - 1 # = 46

# Interpretation:

# The sample mean is about 1.05 standard errors below 2200.

# Compute the p-value (two-sided)
# Because H1: mu != 2200, we use both tails:

# p-value = 2*P(T =< - |t|)

# So:

p <- 2*pnorm(-1.0543) # = 0.2972

# Decision:
# At any standard level (0.1, 0.05, 0.01):

# p = 0.2972 > 0.05

# Do not reject H0

# Based on the sample, there is not enough evidence to conclude that the
# average monthly salary differs from €2200.

# a2)

qnorm(0.975)

left <- 2109.57 - 1.96*s
right <- 2109.57 + 1.96*s

# Yes, we can conclude that 2200 is included in the 95% confidence interval for
# the mean of the salary without doing any calculations because we already
# know that the estimated average or the middle of the interval is equal to
# 2109.57 which is a very close value to 2200.

# The null hypothesis H0: mu = 2200 is not rejected against the two-sided
# alternative whatever the level of significance among the common ones and thus
# in particular at the 0.05 level. Since the region of acceptance or 
# non-rejection of the null hypothesis at the level alpha is related (in the
# case of bilateral alternative hypotheses) to the confidence interval at level
# 1-alpha and in particular the null hypothesis is not rejected when the value
# specified by its belongs to the confidence interval, we can conclude that the
# 95% confidence interval includes the value 2200.

# a3)

# The two different parties have different opinions; therefore they would conduct
# a unilateral test either to the right or to the left. For example, the job agency
# would set H0: mu >= 2000 vs H1: mu < 2000, thus highlighting that its assumption
# could only be challenged by empirical evidence strongly against it. New hires
# would adopt the opposite reasoning. In both cases, the test statistic would
# remain the same but the test would be one-tailed instead of two-tailed.

# b)

# The null hypothesis H0 would be equal to mu = 2032 and the alternative hypothesis
# would be equal to mu > 2032. The average of the current salaries is equal to
# 99150/47 = 2109.57, while the previous average was equal to 2032, so the sample
# mean of the difference is (2109.57-2032) = dbar = 77.57. The variance of the
# difference between salaries is unknown and must be estimated, using the sample
# standard deviation of differences, sd = 96.04. Under the assumption of jointly
# normal distribution the distribution of the test statistic is a Student's t
# with 46 degrees of freedom. To determine the p-value, it is necessary to
# compute the value of the standardized test statistic. The realization of the
# test statistic is:

sd <- 96.04
prev_xbar <- 2032

t <- ((xbar - prev_xbar)*sqrt(n))/sd

# And the p-value is obtained through the function 1 - pt(t, df)

p_value <- 1 - pt(t, df)

# Equal to 0.0000007. We therefore reject the null hypothesis for any level of
# significance and conclude that the average salaries of newly hired employees
# have significantly increased with new job.

# EXERCISE 7.3

stops_df <- data.frame(
  Nr_Stops = 0:8,
  pre_promotion  = c(32, 43, 14, 10, 18, 13, 5, 0, 5),
  post_promotion = c(32, 36, 18, 14, 22, 17, 6, 5, 9)
)

stops_df

# a)
# It is necessary to compare the proportions of customers who visited the
# cafeteria at least once before and after the promotion. The hypotheses to be
# tested are H0: p_pre = p_post vs H1: p_post > p_pre, as the most severe error
# is to extend an ineffective promotion to other bookstores, thus giving up gains
# unnecessarily. Since the sample size is sufficiently large in both samples,
# the test can be conducted by referring to the normal distribution. The two
# samples - independent - are characterized by n_pre = 140, n_post = 159, and by
# pbar_pre = (140-32)/140 = 0.7714 and pbar_post = (159-32)/159 = 0.7987. Under
# the null hypothesis, the two proportions are equal, and pooled estimation is
# used to estimate the common proportion. Under the null hypothesis, the two
# proportions are equal, and pooled estimation is used to estimate the common
# proportion.

pbar_pre <- (140-32)/140 
pbar_post <- (159-32)/159

n_pre <- 140
n_post <- 159

pbar <- (n_pre*pbar_pre + n_post*pbar_post)/(n_pre + n_post)

# The p-value is the probability of observing a difference greater than that
# observed under the null hypothesis, i.e., being pbar_post - pbar_pre =
# = 0.7987 - 0.7714 = 0.0273 which can be calculated using the normal
# approximation by replacing the standard error of the difference between
# proportions with the estimate of the standard error under the null
# hypothesis that the two proportions are equal:

se <- sqrt((pbar*(1-pbar)/n_pre)+(pbar*(1-pbar)/n_post))

# Using the function:

1 - pnorm(0.0273, mean=0, sd=0.0475)

# We obtain that the p-value is 0.2827, which leads to not rejecting the null
# hypothesis for any level of standard significance (typically no higher than 0.1).
# Thus, it is concluded that with the promotion we do not expect a significant
# increase in the propensity to visit the cafeteria once a month.

# b) 
# It is necessary to compare the proportions of customers who visited the
# cafeteria more than 4 times a month before and after the promotion. The hypotheses to be
# tested are H0: p_pre = p_post vs H1: p_post > p_pre, as the most severe error
# is to extend an ineffective promotion to other bookstores, thus giving up gains
# unnecessarily. Since the sample size is sufficiently large in both samples,
# the test can be conducted by referring to the normal distribution. The two
# samples - independent - are characterized by n_pre = 140, n_post = 159, and by
# pbar_pre = (140-117)/140 = 0.1643 and pbar_post = (159-122)/159 = 0.2327. Under
# the null hypothesis, the two proportions are equal, and pooled estimation is
# used to estimate the common proportion. Under the null hypothesis, the two
# proportions are equal, and pooled estimation is used to estimate the common
# proportion.

pbar <- (n_pre*pbar_pre + n_post*pbar_post)/(n_pre + n_post)

# The p-value is the probability of observing a difference greater than that
# observed under the null hypothesis, i.e., being pbar_post - pbar_pre =
# = 0.2327 - 0.1643 = 0.0684 which can be calculated using the normal
# approximation by replacing the standard error of the difference between
# proportions with the estimate of the standard error under the null
# hypothesis that the two proportions are equal:

sd <- sqrt((pbar*(1-pbar)/n_pre)+(pbar*(1-pbar)/n_post))
pbar_diff <- pbar_post - pbar_pre

1-pnorm(pbar_diff, 0, sd)

# We obtain that the value that the p-value is 0.07 which again leads to not
# rejecting the null hypothesis, unless we use a significance level of 0.1, thus
# being less conservative toward the hypothesis that the promotion is ineffective
# and therefore more likely to risk launching a promotional campaign that doesn't
# actually lead to an increase in the propensity of customers to visit the
# cafeteria more than 4 times per month.

### EXERCISE 7.4 
# a)

# To assess whether it can be concluded that the values of the variable History
# are uniformly distributed in the population, it is necessary to use a goodness
# of fit test, which compares the observed frequencies with the expected
# frequencies under the assumption that all frequencies are equal in the
# population, i.e., that the frequencies of the 4 values are all equal to 0.25.
# Thus, the hypotheses to be tested are H0: p_low = p_medium = p_high = p_none =
# = 0.25 vs H1: at least one of p_low, p_medium, p_high, and p_none is different
# from 0.25.

n_none <- as.numeric(sum(DS$History == "None"))
n_low <- as.numeric(sum(DS$History == "Low"))
n_medium <- as.numeric(sum(DS$History == "Medium"))
n_high <- as.numeric(sum(DS$History == "High"))

prop_none <- n_none/750
prop_low <- n_low/750
prop_medium <- n_medium/750
prop_high  <- n_high/750

# The chi square test on goodness of fit is based on the comparison between the
# observed absolute frequencies and the expected frequencies under H0 (which
# should all equal 0.25*750 = 187.5). Using the function

chisq.test(x=table(DS$History), p=c(0.25,0.25,0.25, 0.25))
