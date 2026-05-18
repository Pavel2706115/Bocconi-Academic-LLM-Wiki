# EXERCISE 6.1
# a)

mean(Developers_ITA$NrSkills)
CI.mean(Developers_ITA$NrSkills, sigma = NULL, conf.level = 0.95, digits = 2)
# The average number of computer skills of developer is the mean of the NrSkills.
# variable in the dataframe is equal to 19.22.
# The 95% interval estimate for the mean with unknown variance can be determined 
# without special assumptions about the population distribution because the sample 
# is large enough to apply the central limit theorem. The interval is [18.44, 20.01] 
# and it is the same irrespective of whether the normal or the Student's approximation 
# is used, because the number of degrees of freedom is so high that the percentiles 
# of the two distributions are almost the same. Therefore, with confidence 95% 
# we can conclude that the average number of skills of Italian developers is between 
# 18.44 and 20.01. In other words, the interval built based on the 95% of the 
# samples (with the same size as the considered one) contain the parameter. We
# can't know whether the interval built on the specific available sample leading
# to intervals not including the parameter (and this happens with probability 0.05)
# - the interval is reliable, and we can quantify the extent of our confidence in 0.95.

# b1)

(16.91 + 18.29)/2
# To calculate the point estimate of the average number of skills we should
# add up both ends of the interval and divide them in 2, to find the average value
# between the two. Moreover, knowing the avg number of skills of both German and
# Italian developers we can conclude that the Italian developers have more skills
# on average.

# b2)

(18.29-16.91)/2
# To calculate the margin of error we should calculate the half of the width of
# the interval, equal to 0.69. Increasing the confidence level would result in a
# larger margin of error and thus a wider interval, because we want to increase
# the level of confidence associated to the interval, and the width of the interval
# consequently increases.

# c)

mean(Developers_ITA$WorkingMode=="Hybrid")
CI.prop(Developers_ITA$WorkingMode=="Hybrid", sigma = NULL, conf.level = 0.95, digits = 3)
# The proportion of developers working in Hybrid mode is equal to 0.47. The 95% 
# confidence interval for the parameter of interest is equal to [0.436, 0.505].

# d)

# Even if one assumes that the sampling procedure is adequate (and it is not),
# one could only obtain a point estimate for the perimeter, because the sample
# size is too small to apply the central limit theorem.
# In addition, there are some critical issues in the procedure followed to obtain
# the sample. First, the sample  is not drawn from the entire population but from
# the sub-population of developers following the specific social channel; it is
# therefore necessary to assess if and to what extent such sub-population
# resembles the entire population. Second, results are based in the spontaneous
# answers of some developers, and therefore can't be considered as a random sample.
# Last, since it was explicitly declared that the survey aimed at proving that
# the obtained estimate (0.47) was too high, it is possible that respondents 
# were mainly the developers supporting this idea.

# EXERCISE 6.2
# a)
# The sample size of 20 is too small to apply the central limit theorem. 
# To determine the confidence interval, it is necessary to assume the normality
# of the distribution of customers' stay duration on the premises of the
# bookstore. Since the variance of the population is unknown, the confidence
# interval is constructed around the sample mean, with a margin of error given
# by the product of the estimated standard error of the sample mean and the
# percentile of order 0.975 of a Student's t distribution with 19 degrees of
# freedom:
rel_factor_t <- qt(0.975, 19)
x_bar <- 39.34
n <- 20
s2 <- 118.93
s <- sqrt(s2/n)
# Therefore, the left side of the confidence interval is:
left_20 <- x_bar-(rel_factor_t*s); left_20
# And the right side of the confidence interval is:
right_20 <- x_bar+(rel_factor_t*s); right_20
# Therefore, the confidence interval is [34.236; 44.444]
# Moreover, it is not possible to conclude that the average time spent by
# the bookstore's clients in the store is included in the interval with probability
# 0.95 because the average time spent by the bookstore's clients is a constant
# and the observed interval is not random since it is based in a specific sample;
# therefore the average either belongs or does not belong to the interval, and
# this is unknown since the average is unknown.

# b)

# The statement is false because it is not possible to compare the reliability
# of the two intervals. The different width of the two intervals depends on the
# different variance estimates, which are not given and we can't conclude anything.

# c)

# The statement is true, when we repeat the sampling many times, most confidence 
# intervals will contain the true mean, but around 5 out of every 100 intervals 
# will miss it.

# d)

# The width of a confidence interval for the mean when the variance is unknown
# is 2*reliability factor*s, implying that the required sample size should be
# n >= (2*reliability factor*s)^2/5^2. Obviously before knowing the size of the
# sample to draw it is not possible to know the degrees of freedom to be used.
# Also, before drawing the sample, one can't know what sample variance will be
# actually observed. Therefore, it is not possible to give indications about the
# sample size guaranteeing the required width. Even so, it is possible to provide
# an approximate educated indication based on the available sample. This way we
# get n >= (2*reliability factor/5)^2 * s2 = (2*2.093/5)^2 * 118.93 = 83.3,
# suggesting that a sample of size 84 or more should be used. If instead the
# variance is assumed to be known and (in this case) coinciding with the sample
# variance, the required sample size would be n >= (2*z*sigma)^2/5^2 =
# = (2*1.96/5)^2 * 118.93 = 73.1 and a sample of 74 cases or more should be drawn.

# e)

# Having a bigger sample size of 100, allows us to apply the central limit theorem,
# meaning that we can conclude that the distribution is normal and we don't need
# to assume it. Moreover, the estimation of the standard deviation will be
# smaller and more accurate as there is larger sample size - 1.09055.
se <- sqrt(s2/100); se
# The reliability factor would be the percentile of a standard normal, z = 1.98.
rel_factor_z <- qt(0.975,99)
# Therefore the left side of the confidence interval would be equal to:
left_100 <- (x_bar-rel_factor_z*se); left_100
# And the right side of the confidence interval would be equal to:
right_100 <- (x_bar+rel_factor_z*se); right_100

# EXERCISE 6.3

length(vgsales$Global_Sales[vgsales$Year == 1990])
length(vgsales$Global_Sales[vgsales$Year == 2010])
CI.mean(vgsales$Global_Sales[vgsales$Year == 1990], sigma=NULL, conf.level = 0.95, digits = 3)
CI.mean(vgsales$Global_Sales[vgsales$Year == 2010], sigma=NULL, conf.level = 0.95, digits = 3)
# Due to the fact that the sample size for the sales in 1990 is 16, we should 
# make an assumption that the distribution is a student-t one. Applying the 
# CI.mean function in R studio we get that the confidence interval is [0.516;5.668]. 
# On the other side, for the sales in 2010, we have a sample size of 
# interval is equal to 1259, which allows us to apply the central limit theorem,
# and conclude that the population has normal distribution. We again make an 
# assumption for the 95% confidence interval and we get that it is equal to [0.405; 0.549].
# Moreover, the two intervals obtained have significantly different widths. This
# is due to:
# 1) The reliability factor, which for 1990 is the percentile of order 0.975 of
# a student t distribution with 15 degrees of freedom, about 2.131, and for 2010
# is the percentile of the same order of a standard normal distribution with
# 1258 degrees of freedom, about 1.96.
# 2) The population variance estimates, which turn out to be 4.825 for 1990 and
# 1.295 for 2010, suggesting that there was greater variability in the past than
# there is in the recent past. Less variance in the population, again all other
# things being equal, corresponds to greater precision in estimation.
# 3) And finally, as I already mentioned, the difference in the sample sizes
# plays a role in the different widths of the confidence intervals. The larger
# sample size consisting of 1259 samples results in greater precision and lower
# standard error.

# EXERCISE 6.4
# a) 

# Non-smokers:
nonsmokers_mean <- 90.7
nonsmokers_n <- 10
nonsmokers_sd <- 5.4
nonsmokers_rel_factor_t <- qt(0.975, 9); nonsmokers_rel_factor_t
rm(smokers_right)
nonsmokers_right <- nonsmokers_mean+nonsmokers_rel_factor_t*(nonsmokers_sd)^2

# Smokers:
smokers_mean <- 87.2
smokers_sd <- 4.8
smokers_n <- 10
smokers_rel_factor_t <- qt(0.975, 9); nonsmokers_rel_factor_t
smokers_left <- smokers_mean-smokers_rel_factor_t*(smokers_sd)^2
smokers_right <- smokers_mean+smokers_rel_factor_t*(smokers_sd)^2

mean_diff <- nonsmokers_mean - smokers_mean
# Knowing that the variance is the equal for both populations, we can calculate
# the standart error of the difference:
s2_diff <- (9*5.4^2 + 9*4.8^2)/18
# The standard error estimate is therefore:
se_diff <- sqrt(s2_diff/10 + s2_diff/10)
rel_fact_diff <- qt(0.975,18)
left_diff <- mean_diff - rel_fact_diff*se_diff 
right_diff <- mean_diff + rel_fact_diff*se_diff 
# So the interval of the difference is [-1.3, 8.3]

# b)

# The standard error estimate is therefore:
se_diff_b <- sqrt(5.2*5.2/10 + 5*5/10); se_diff_b
rel_fact_diff_b <- qnorm(0.975) # When we know the standard deviations, we use qnorm() instead of qt()
left_diff_b <- mean_diff - rel_fact_diff_b*se_diff_b; left_diff_b
right_diff_b <- mean_diff + rel_fact_diff_b*se_diff_b; right_diff_b
# So the interval of the difference is [-0.97; 7.97]
# The difference comes from the fact that the width of the confidence interval
# decreases as we know the actula standard deviations of the populations.

# EXERCISE 6.5
# a)

length(DS$Salary)
CI.mean(DS$Salary, sigma = 30000, conf.level = 0.9)
# The estimate of the average salary of the company's customers is 56183.7. The
# 90% confidence interval for the mean salary with a standard deviation, equal to
# 30000, is [54381.89; 57985.58]. With a sample size of 750, we can apply the
# central limit theorem and the fact that we already know the standard deviation,
# means that there aren't any required assumptions to calculate this interval.
# Calculating the 99% confidence interval will increase the interval itself because
# this allows us to more surely guarantee that the average will be included in
# the interval.

# b)
# b.1)

CI.prop(DS$Sex == "Female", success = NULL)
# Since our sample is large enough to apply the central limit theorem, 750, we
# can conclude that the population has a normal distribution and the proportion
# of female customers in the company is equal to 0.52, or 389.

# b.2)
# The interval estimate at the 0.95 level is [0.48; 0.55]. The margin of error of
# the confidence interval on the proportion is given by: z*sqrt(phat(1-phat)n)
# and depends on the standard error (estimated) of the sample production (0.02
# from output obtained with Rstudio) and the percentile of the sample
# distribution of the estimator, in this case z equals approximately 1.96.

# c)

# In order to calculate the 90% confidence interval with a margin of error not
# exceeding 0.11, we have to first find the appropriate sample size that will
# allow such margin of error. Moreover, we do not know the proportion of the
# customers living close to a competing store but we know that the maximum
# margin of error will be achieved when p = 0.5. Therefore, we will have to
# first find the reliability factor z:
z <- qnorm(0.95)
# And then plug in the inequality
# ME = z * sqrt(p(1-p)/n) =< 0.11
# 1.6445*sqrt(0.5(1-0.5)/n) =< 0.11
# ((1.6445*0.5)/0.11)^2 =< n
# n >= 56
# So I would recommend the sample size required to achieve such margin of error
# to be at least equal to 56.

# d)

spent_close <- DS$AmountSpent[DS$Location == "Close"]

spent_far <- DS$AmountSpent[DS$Location == "Far"]

CI.diffmean(spent_close, spent_far, sigma.x = NULL, sigma.y = NULL, conf.level = 0.9)

# Using the function CI.diffmean, we can easily calculate the difference between
# the spending averages of the customers which live far and close, and it is 
# equal to -657.43. The 90% confidence interval for this difference is [-778.86, -535.99]
# which was obtained after applying the CLT and concluding that the distribution
# is normal because the sample size is sufficient enough. Because the entire CI
# is negative, with 90% confidence customers living close to a competitor spend
# less on average than customers living far away (by about 536-779 under equal
# variances). If, however, we assumed that  the variances are different, the 90% 
# confidence interval will increase its width and will be [-800.03, -514.82] due 
# to the differences in standard errors (Equal variances: SE = 73.83; Unequal
# variances: SE = 86.70). Unequal variances give larger standard error, hence
# larger margin of error, and therefore wider CI.

# e)

high_married <- (DS$History == "High")[DS$Married == "Married"]
high_unmarried <- (DS$History == "High")[DS$Married == "Single"]

CI.diffprop(high_married, high_unmarried, conf.level = 0.99)

# The 99% confidence interval for the difference between the proportions of 
# customers who make high-frequency purchases among married and single customers 
# is [0.25; 0.4]. The estimated difference between the proportions being equal to
# 0.33 with the proportion of the married customers with high-frequency purchases
# being higher. This would suggest that the married customers are more prone
# to making frequent purchases. The margin of error of the interval depends on:

# 1. The estimated standard error, namely 0.03, which depends on the estimated
# proportions 0.44 and 0.11, according to the formula:
# se(PhatX - PhatY) = sqrt(phatX(1 - phatX) / nX + phatY(1 - phatY) / nY) =
# = sqrt(0.44(1-0.44) / 376 + 0.11(1-0.11) / 374) = 0.0303 

# 2. The reliability factor of the standard normal distribution, z = 2.57 (qnorm(0.995))

# f)

high_senior <- as.numeric(DS$History == "High")[DS$Age == "Senior"]

CI.mean(high_senior, sigma = NULL, conf.level = 0.95)

# The sample size is big enough so that we can apply the central limit theorem
# and conclude that the distribution is normal. The proportion of high-frequency
# purchasers among the more mature customers is equal to 0.4 and using the 
# CI.mean UBStats function we can obtain the CI which is equal to [0.32; 0.48].
# Another way of calculating the CI is by finding the reliability factor z, equal
# to 1.96: 
z <- qnorm(0.975)
# Afterwards, using the mean to find the standard of error:
se <- sqrt(0.4*(1-0.4)/144)
# And since we already know the mean we can assemble the left and the right
# side of the interval:
high_mean <- 0.4
high_left <- high_mean - z*se
high_right <- high_mean + z*se

# EXERCISE 6.6

# a)

n <- 100
p <- 0.4
se <- sqrt(p*(1-p)/n); se
z <- 1.96
left <- p - z*se
right <- p + z*se
# Interval is equal to [0.30; 0.45]

# b)

n <- 1000
p <- 0.4
se <- sqrt(p*(1-p)/n); se
z <- 1.96
left <- p - z*se; left
right <- p + z*se; right
# Interval is equal to [0.37; 0.43]. Increasing the sample to 1000 students
# decreases the standard error form 0.049 to 0.015 which decreases the margin of
# error and the width of the interval.

#c) 

n <- 100
p <- 0.4
se <- sqrt(p*(1-p)/n); se
z <- qnorm(0.95); z
left <- p - z*se; left
right <- p + z*se; right
# Interval is equal to [0.37; 0.43]. Decreasing the confidence level to 90%,
# decreases the reliability factor, leading to a decrease in the width of the
# interval.

# d)

# 1.96*sqrt(0.5(1-0.5)/n) =< 0.04
# 1.96*0.5/sqrt(n) =< 0.04
# n =< 600.4
# The minimum number of students to be interviewed to obtain a ME of below 4% os 601.

# e)

n <- 120
p <- 0.36
se <- sqrt(p*(1-p)/n); se
z <- qnorm(0.995)
left <- p - z*se
right <- p + z*se
# Interval is equal to [0.25; 0.47]
# Here the interval has bigger width because the reliability factor is much bigger,
# and the standard error is almost three times the size of the one in the first
# university. Moreover, the number of students supporting the party is larger - 43,
# compared to 40. And finally, the confidence level is 5% higher than the one
# in the other university.

# EXERCISE 6.7

# a) 

DS <- as.numeric(vgsales$Platform == "DS")
CI.mean(DS, sigma = NULL, conf.level = 0.95, digits = 4)

# The 90% confidence interval for the proportion of games that have been made
# available on the DS platform is [0.1252; 0.1354]. 

# b)

# I would quantify the precision of the interval estimation obtained in the prev.
# point via the reliability factor. Using the qnorm() function, we know that it
# is equal to 1.65. Looking at the precision that a 99% confidence level would
# have, using the same function, we can obtain that it is equal to 1.96, which
# is greater that the one of the 90% confidence level.

# c)

# ME = 0.02
# z = 1.96
# 1.96*0.5*sqrt(n) >= 0.02
# 0.98*sqrt(n) >= 0.02
# n >= 2401

# Yes, it could be based on at little as 2401 sample size

# d)

# The interval was built around the middle value between the left and the right
# sides of the interval, which is obtainable with the formula:
# MID = (L + R)/2 = 0.21
# Yes, the intervals are comparable, in terms of confidence because the confidence
# levels and the reliability factors are the same. We can not compare them in
# terms of precision, though.

# EXERCISE 6.8

# a)
# a1)
# The mean of the variable NrSkills is obtainable with the formula CI.mean and
# it is equal to 19.22.
# The interval is [18.19; 20.25]

CI.mean(Developers_ITA$NrSkills, sigma = NULL, conf.level = 0.99)

# The mean of the variable Skills.Idx is obtainable with the formula CI.mean and
# it is equal to 12.84.
# The interval is [12.44; 13.25]

CI.mean(Developers_ITA$Skills.Idx, sigma = NULL, conf.level = 0.99)

# a2)
# NrSkills:

n_ita <- 802
xbar_ita <- 19.22
s_ita<- 11.33

n_ger <- 820
xbar <- 17.6
s_ger <- 10.12

mean_diff <- 1.62
s2pool <- ((n_ita-1)*s_ita^2 + (n_ger-1)*s_ger^2)/(n_ita-1 + n_ger-1)

se_diff <- sqrt(s2pool*(1/n_ita + 1/n_ger))

z <- qnorm(0.995)

left_diff <- mean_diff - z*se_diff; left_diff
right_diff <- mean_diff + z*se_diff; right_diff

# Skills_Idx:

n_ita <- 802
xbar_ita <- 12.84
s_ita<- 4.43

n_ger <- 820
xbar <- 12.29
s_ger <- 4.13

mean_diff <- 0.55
s2pool <- ((n_ita-1)*s_ita^2 + (n_ger-1)*s_ger^2)/(n_ita-1 + n_ger-1)

se_diff <- sqrt(s2pool*(1/n_ita + 1/n_ger))

z <- qnorm(0.995)

left_diff <- mean_diff - z*se_diff; left_diff
right_diff <- mean_diff + z*se_diff; right_diff

# It is possible to estimate with a 99% confidence interval the difference between
# the means of Italian and German computer skills.The sample sizes are large enough 
# to apply the central limit theorem, and we won't need specific assumptions to
# be made. The interval for the variable NrSkill is equal to [0.25; 2.99]. And
# the interval for the variable Skills_Idx is equal to [0.002; 1.098]. In both
# cases, the obtained results suggest higher skills - on average - for Italian
# developers.

# b) 
D <- (Developers_ITA$FinSkills.Idx - Developers_ITA$Skills.Idx)
CI.mean(D, conf.level = 0.9)

# The sample is large and therefore the assumption of joint normality 0 that
# would be needed in the case of a small sample - is not necessary. The
# interval for the difference between the target and the actual average skills
# is [7.15;7.34].

# c)
# c1)
full_time <- as.numeric(Developers_ITA$Employment == "Employed, full-time")
CI.mean(full_time, sigma = NULL, conf.level = 0.95)

# The 95% confidence interval for the proportion of developers working for a
# company is [0.83;0.88].

part_time <- as.numeric(Developers_ITA$Employment == "Contractor/Freelance")
CI.mean(part_time, sigma = NULL, conf.level = 0.95) 

# The 95% confidence interval for the proportion of developers working as a
# freelance is [0.12;0.17]. Another way of obtaining the interval is through
# subtracting the interval of the developers working for a company from 1 for
# each side of the interval.

# c2) We have that the sample size of German developers is 820 and the 
# confidence interval is [0.884, 0.923]. Therefore, we can get the
# average by (L+R)/2 equal to 0.9035, and we can calculate the ME, by
# 0.9035-0.8840 = 0.02. We also know that ME = z*sqrt(p*(1-p)/n), so
# 0.02 = z*sqrt(0.903*0.097/820)
# 0.02 = z*0.0103
# z = 1.93
# Therefore, applying the pnorm() function and then subtracting the result from
# 1, we get that the confidence level is around 0.0268.

# c3)
# The interval of confidence for the German developers working as freelance is
# [0.116, 0.077]. From this we can get the mean value of the sample - 0.0965.
# Also we can find the ME, equal to 0.0965-0.077 = 0.0195. After that, we can 
# calculate the se, equal to sqrt(p*(1-p)/n), or 0.0103. Now that we have these
# two values, we can head to the Italian developers, whose mean on freelance
# developers is 0.15 and the se is equal to 0.0126. We have gathered all the
# values. Now let's calculate the s2pool

s2pool <- ((802-1)*0.0126^2 + (820-1)*0.0103^2)/(802-1 + 820-1)

se_diff <- sqrt(s2pool*(1/802 + 1/820))

z <- qnorm(0.995)

mean_diff <- 0.15 - 0.0965

left <- mean_diff - z*se_diff; left
right <- mean_diff + z*se_diff; right

# Therefore the 99% confidence interval is equal to [0.052;0.055].

#d)

employed_skills <- (Developers_ITA$Skills.Idx[Developers_ITA$Employment == "Employed, full-time"])
freelance_skills <- (Developers_ITA$Skills.Idx[Developers_ITA$Employment == "Contractor/Freelance"])

mean(employed_skills)

CI.mean(employed_skills, sigma = NULL, conf.level = 0.95)
CI.mean(freelance_skills, sigma = NULL, conf.level = 0.95)

ME_employed <- 0.33

sd <- 0.33/1.96

ME_freelance <- 0.85

sd_free <- 0.85/1.96

s2pool <- (681*4.35^2 + 119*4.78^2)/(681+119) # FOR THIS FORMULA, WE USE s_X, STANDARD DEVIATION!

se_diff <- sqrt(s2pool*(1/682+1/120))

qnorm(0.995)

left <- -1.1 - 1.96*0.437
right <- -1.1 + 1.96*0.437

# Interval -> [-1.96; -0.24]
# Judging by the interval, we can conclude that the employed developers on average
# have lower skills than the freelance ones since the average difference between
# the two groups is below the 0.

# e)
# e1)

# Master

bachelor <- (Developers_ITA$NrSkills)[Developers_ITA$Education == "Bachelor"]
master <- (Developers_ITA$NrSkills)[Developers_ITA$Education == "Master"]

CI.mean(bachelor, conf.level = 0.99)

xbar1 <- 18.91
sd1 <- 11.25
z <- 2.58
n1 <- 234

# Bachelor

CI.mean(master, conf.level = 0.99)

xbar2 <- 18.95
sd2 <- 11.26
n2 <- 225

xbar_diff <- -0.04

sd_diff <- (233*sd2^2 + 224*sd2^2)/(233+225)

se_diff <- sqrt(sd_diff*(1/234 + 1/225))

left <- xbar_diff - z*se_diff; left
right <- xbar_diff + z*se_diff; right

# The interval of the difference is  [–2.64 ; 2.67].

# e2)

# Master

bachelor <- as.numeric((Developers_ITA$DevType == "Full-stack")[Developers_ITA$Education == "Bachelor"])
master <- as.numeric((Developers_ITA$DevType == "Full-stack")[Developers_ITA$Education == "Master"])

CI.mean(bachelor, conf.level = 0.99)

xbar1 <- 0.45
sd1 <- 0.5
z <- 2.58
n1 <- 234

# Bachelor

CI.mean(master, conf.level = 0.99)

xbar2 <- 0.4
sd2 <- 0.49
n2 <- 225

xbar_diff <- 0.05

sd_diff <- (233*sd2^2 + 224*sd2^2)/(233+225)

se_diff <- sqrt(sd_diff*(1/234 + 1/225))

left <- xbar_diff - z*se_diff; left
right <- xbar_diff + z*se_diff; right

# The interval of the difference is  [–0.06 ; 0.18].

# In both cases, the intervals include both positive and negative values. In particular, with 
# reference to the variable NrSkills the interval is quite symmetric around 0; therefore, with 
# confidence 99% (very high) we can conclude that the difference between the two means 
# could be positive or negative. As for the proportion of Full‐stack developers, the interval is 
# more concentrated on positive values (higher % of developers with a bachelor degree 
# specialized in Full‐stack), but it is definitely not possible to rule out the possibility that the 
# difference is negative, even if not high.

# EXERCISE 6.9
# a)

visits_table <- data.frame(
  pre_promotion  = c(32, 43, 14, 10, 18, 13, 5, 0, 5),
  post_promotion = c(32, 36, 18, 14, 22, 17, 6, 5, 9)
)

post <- (visits_table$post_promotion)[visits_table$nr_Visits > 4]

CI.mean(pre, conf.level = 0.99)

xbar1 <- 0.1643

xbar2 <- 0.2327

mean_diff <- 0.0684

se <- sqrt(xbar1*(1-xbar1)/140 + xbar2*(1-xbar2)/159)

left <- 0.0684 - 2.58*se
right <- 0.0684 + 2.58*se

# The interval is equal to [-0.05; 0.19]

# From the 99% confidence interval we can assume that the promotion had a positive
# effect on the number of visits, even though that the left part of the interval
# is negative (-5%, 19%), the bigger proportion of the interval is positive.

# c) The statement is overly optimistic because from the interval we know that the maximum
# increase is 19%

# EXERCISE 6.10
# a)

strategy <- (vgsales$JP_Sales)[vgsales$Genre == "Strategy"]

role <- (vgsales$JP_Sales)[vgsales$Genre == "Role-Playing"]

CI.mean(strategy, conf.level = 0.9)
CI.mean(role, conf.level = 0.9)

n1 <- 681
xbar1 <- 0.07
sd1 <- 0.17

n2 <- 1488
xbar2 <- 0.24
sd1 <- 0.65

xbar_diff <- 1488-681

sd_diff <- (680*sd1^2 + 1487*sd2^2)/(680+1488)

se_diff <- sqrt(sd_diff*(1/681 + 1/1488))

qnorm(0.95)

left <- xbar_diff - se_diff*1.64; left
right <- xbar_diff + se_diff*1.64; right

# Interval is equal to [805.21; 808.79]
# No, it would not be sensible for a company to reposition itself by investing
# more in Role-Playing because the average sales of the Strategy genre is clearly
# higher.

# b) Point estimation is the process of estimating the middle of the estimated
# interval. The estimated point is usually the estimation of the mean.

# c) 

role_sales <- vgsales$Genre == "Role-Playing"
jp_RP <- vgsales$JP_Sales[role_sales]
jp_nonRP <- vgsales$JP_Sales[!role_sales]

CI.mean(jp_RP, conf.level = 0.99)
CI.mean(jp_nonRP, conf.level = 0.99)

xbar1 <- 0.24
sd1 <- 0.65
n1 <- 1488

xbar2 <- 0.06
sd2 <- 0.25
n2 <- 15110

se_diff <- sqrt(sd1^2/n1 + sd2^2/n2)

z <- qnorm(0.95)
mean_diff <- -0.18

left <- mean_diff - z*se_diff; left
right <- mean_diff + z*se_diff; right

# The interval is [-0.2237189;-0.1362811]
