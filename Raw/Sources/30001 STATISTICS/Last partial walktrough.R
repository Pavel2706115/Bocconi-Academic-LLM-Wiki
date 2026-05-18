### EXERCISE 1

# a)

# a1)

distr.plot.xy(Paid, Impressions, plot.type = "boxplot", data=Metrics2)

# I used side-by-side boxplots and the one corresponding to "Yes" has a much
# higher range and IQR, meaning that the the variability of the numbers of
# impressions is much higher there. Both boxplots have equal minimum values and
# left whiskers start from the same number of impressions and are both 
# right skewed, with the boxplot of "Yes" having much longer right tail. Both
# of the boxplots have a lot of upper outliers, reaching the same extreme values.

# a2)

# I would use Min, Q1, Median, Q3, Max which will help to make a define difference between
# the two graphs by comparing their IQR, range.

distr.summary.x(Impressions, by1 = Paid, stats = "fivenumbers", data = Metrics2)

# b)

distr.summary.x(Engagement, stats = "fivenumbers", data = Metrics2)

outliers <- Metrics2$Engagement[Metrics2$Engagement > 10.155]

Q3 + 1.5*(Q3-Q1) = 10.155

length(outliers)

(45/550)*100
  
Q1 <- 2.73

Q3 <- 5.7

# The posts with anomalously good performance are those with over 10.155 clicks in hundereds.
# They are the ones over the value that we get from the formula Q3 + 1.5*IQR.
# Yes, the outlier account for 8.18% of the posts.

# c)

distr.plot.xy(Reach, Engagement, plot.type = "scatter", fitline = T, data = Metrics2)
cor(Metrics2$Reach, Metrics2$Engagement)

# From the scatter plot, we can clearly observe that there is strong linear relationship,
# between the two variables and this can be confirmed by the correlation coefficient equal
# to 0.73.

# d)

Metrics2$Shares_recode <-  factor(Metrics2$Shares, levels = c("verylow", "low", "high", "veryhigh"))

distr.plot.xy(Shares_recode, Content, plot.type = "bars", bar.type = "beside", data = Metrics2)

distr.table.xy(Content, Shares_recode, freq.type = "col", freq = "perc", data = Metrics2)

# The sentence is not correct as the posts that promote offers, tend to have the higher levels
# proportion of the levels High and VeryHigh of the variable shares 86%, compared to the Nobrand's 68%.

# e)

distr.table.x(Out.Engage, freq = "counts", data = Metrics2)
mids <- c(0.5, 2.5, 7.5,30, 125)
counts <- c(110,231,88,110,11)
mids.1 <- rep(mids, counts)

mean(mids.1)
var(mids.1)

# f)

p=1-pnorm(15,12,80)
xbar=12; var=380; n=80
sd = 19.5

### EXERCISE 2

# a) The estimatior is used to estimate different values

# b) Consider the variable Shares. Obtain the estimate of the proportion 
# of posts with Shares=high and that of the proportion of posts with Shares=low 
# [round results to 2 decimals]. Evaluate the standard errors

# c) Explain if and why it is possible to say what follows “Given the standard errors, 
# one can conclude that the distance between the calculated estimate and the 
# corresponding population proportion is lower for posts with Shares=low than 
# for posts with Shares=high” [Only if you did answer to the previous point, 
# assume that the two standard errors are 0.025 for posts with Shares=low and 
# 0.041 for posts with Shares=high. Note that these numbers have nothing to do 
# with the values obtained at the previous points] of the corresponding estimators, 
# illustrating the procedure. 