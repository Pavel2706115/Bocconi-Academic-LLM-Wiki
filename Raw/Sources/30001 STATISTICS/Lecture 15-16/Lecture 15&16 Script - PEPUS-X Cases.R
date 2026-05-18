# Lecture 15 and 16 Script

### PEPUS CASE 1 ###
### CONFIDENCE INTERVAL FOR THE POPULATION MEAN ###
### [KNOWN VARIANCE]

# Q1) (slides 12-13) data: CallCenter.P
# Determine a 0.95 Confidence interval for the average call duration (mu)
# (computations "by hands", from summary statistics)
n = length(CallCenter.P$TimeTalk); n
xbar = mean(CallCenter.P$TimeTalk); xbar # point estimator of mu
sigma = 150 # standard deviation (sigma known)
SE = sigma/sqrt(n); SE
alpha = 0.05
z.025 = qnorm(0.975)
ME = z.025*sigma/sqrt(n); ME # margin of error
ci = c((xbar-ME),(xbar+ME)); ci
# (computations with RStudio, from raw data)
CI.mean(x=TimeTalk,sigma=150,conf.level = 0.95,data=CallCenter.P)
# Interpretation and comment:
# We are 95% CONFIDENT that mu is within [237.4,271.35]
# IMPORTANT! mu is a parameter and [237.4,271.35] is fixed,
# therefore we CANNOT say that [237.4,271.35] contains mu
# with probability 0.95 as PROBABILITY IS ONLY DEFINED FOR R.V.!
# Q2) (slides 14-15) data: CallCenter.P
# Find the minimum sample size n needed to obtain a 0.99 CI with width 20
CI.mean(x=TimeTalk,sigma=150,conf.level = 0.99,data=CallCenter.P)
# the ci has a width of:
276.68-232.07 # 44.61. Too larga!
# To have a narrower interval we could consider a lower CONFIDENCE
# If confidence is FIXED, then we need to INCREASE the sample size
# WIDTH < 20
# WIDTH = 2*ME hence we want ME=10 at most
# ME = z.005*sigma/sqrt(n)
# n = (z0.005*sigma/ME)^2
ME = 10 # the required ME to have a width of 20 is of course 10
z.005 = qnorm(0.995); z.005
nmin = (z.005*sigma/ME)^2; nmin
# n = 1493 is the minimum sample size to have a ci of width<20
### [UNKNOWN VARIANCE]

# Q1) (slides 12-13, but for unknown variance) data: CallCenter.P
# Determine a 0.95 Confidence interval for the average call duration (mu)
# (computations "by hands", from summary statistics)
xbar
t.025 = qt(0.975,df=299); t.025 #97.5th percentile of t-student
s = sd(CallCenter.P$TimeTalk)
ME = t.025*s/sqrt(n);
ci = c(xbar-ME,xbar+ME); ci
# (computations with RStudio, from raw data)
CI.mean(x=TimeTalk,conf.level = 0.95,data=CallCenter.P) # sigma unknown

### PEPUS CASE 2 ###
### CONFIDENCE INTERVAL FOR THE POPULATION PROPORTION ###
### [VARIANCE ALWAYS UNKNOWN]

# Q1) (slide 27) data: CallCenter.P
# Estimate the proportion p of telephone calls concerning the contract
# (Topic="Contract related") with a 90% confidence interval.
# (from summary statistics)
distr.table.x(CallCenter.P$Topic,p.digits=5)
n = 300;
phat = 82/300
z.05=qnorm(0.95); z.05
ME = z.05*sqrt(phat*(1-phat)/n)
ci = c(phat-ME,phat+ME); ci
# (from raw data)
CI.prop(Topic,success="Contract related",
        conf.level=0.9,data=CallCenter.P,digits=10)

# Q2) (slide 28)
# Estimate the proportion of telephone calls lasting more than 6 minutes,
# with a 90% confidence interval.
long.call = CallCenter.P$TimeTalk>(6*60) # extract data
# (from row data)
CI.prop(x=long.call,conf.level=0.9,digits=100)
# Q3) (slides 29-31) data: CallCentre.p
# Find the sample size needed to obtain a ci for the calls
# longer than 6 minutes with width <=0.05
# ME = z.05*sqrt(phat*(1-phat)/n)
# Want to find n such that ME<0.025
n = z.05^2*(phat*(1-phat))/ME^2 # note that phat*(1-phat)<= 0.5^2!!!
z.05 = qnorm(0.95); ME = 0.025;
n = z.05^2*0.5^2/ME^2; n

### PEPUS CASE 3 ###
### CONFIDENCE INTERVAL FOR THE DIFFERENCE BETWEEN ###
### POPULATION MEANS: INDEPENDENT SAMPLES ###
### [UNKNOWN VARIANCES]

# Q1) (slides 39-41) data: Insurance
# Estimate the difference in the average amount of expenditure reimbursed
# to smokers and non-smokers using a 99% confidence interval,
# assuming that the variances are equal
# (from summary statistics)
refund.smoke = Insurance$refund[Insurance$smoker=="yes"]
refund.nosmoke = Insurance$refund[Insurance$smoker=="no"]
xbar = mean(refund.smoke); ybar = mean(refund.nosmoke)
sx2 = var(refund.smoke); sy2 = var(refund.nosmoke)
nx = length(refund.smoke); ny = length(refund.nosmoke);
spool2 = ((nx-1)*sx2+(ny-1)*sy2)/(nx+ny-2)
t.005 = qt(0.995,df=nx+ny-2); t.005
ME = t.005*sqrt(spool2/nx+spool2/ny); ME
ci = c(xbar-ybar-ME,xbar-ybar+ME); ci
# (from raw data)
CI.diffmean(refund.smoke,refund.nosmoke,type="independent",
            conf.level=0.99,digits=10)
### [KNOWN VARIANCES]
# Now assume in Q1 we know the variances are equal to 50'000'000
sigmax = sigmay = sqrt(50000000)
CI.diffmean(refund.smoke,refund.nosmoke,type="independent",
            sigma.x = sigmax, sigma.y = sigmay,
            conf.level=0.99,digits=10)
# Check slides 44-45 for another example

### PEPUS CASE 4 ###
### CONFIDENCE INTERVAL FOR THE DIFFERENCE BETWEEN ###
### POPULATION MEANS: PAIRED SAMPLES ###
### [UNKNOWN VARIANCE]

# Q1) (slides 49) data: given summary statistics
# Estimate the average reduction in cholesterol level following treatment
# using a 90% confidence interval.
# (from summary statistics only)
xbar_ini = 155; s_ini = 19.9; # sample mean and sd before the treatment
xbar_8w = 122; s_8w = 24.5; # sample mean and sd after the tratment (8 weeks)
cov_ini_8w = 23.4 # covariance between the levels before and after the treatment
n = 44 # sample size
dbar = xbar_ini - xbar_8w; dbar # estimate of average reduction
sd = sqrt(s_ini^2+s_8w^2-2*cov_ini_8w); # sample standard error of d
t.05 = qt(0.95,df = n-1)
ME = t.05*sd/sqrt(n); ME
ci = c(dbar-ME,dbar+ME); ci

# Q2) (slides 50) data: Fatalities_US
# Evaluate the reduction in the average number of alcohol-related accidents
# as a result of the campaign using a 95% confidence interval.
### [UNKNOWN VARIANCE]
# (from raw data)
CI.diffmean(Alcohol,AlcoholPostCampaign,
            type="paired",conf.level=0.95,data=Fatalities_US)
### [KNOWN VARIANCE]
# (from raw data)
# now assume the variance of the difference is known to be equal to 6
# (although it's weird we know the variance here)
CI.diffmean(Alcohol,AlcoholPostCampaign,sigma.d = sqrt(6),
            type="paired",conf.level=0.95,data=Fatalities_US)

### PEPUS CASE 5 ###
### CONFIDENCE INTERVAL FOR THE DIFFERENCE BETWEEN ###
### POPULATION PROPORTIONS ###
### [VARIANCE ALWAYS UNKNOWN]
# Q1) (slides 56-57) data: Banner
# Build a 90% confidence interval for the difference between the CTRs
# of Banner A and Banner B
# (from raw data)
banner_A = Banner$Click[Banner$Banner=="A"]
banner_B = Banner$Click[Banner$Banner=="B"]
CI.diffprop(x=banner_A,y=banner_B,success.x="Yes",success.y="Yes",
            conf.level=0.90,digits=4)
# (from summary statistics)
phatx = mean(banner_A=="Yes"); phatx
phaty = mean(banner_B=="Yes"); phaty
z.05 = qnorm(0.95); z.05
nx = length(banner_A); ny = length(banner_B)
ME = z.05*sqrt(phatx*(1-phatx)/nx+phaty*(1-phaty)/ny); ME
ci = c(phatx-phaty-ME,phatx-phaty+ME); ci