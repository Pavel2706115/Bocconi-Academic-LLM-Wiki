### LECTURE 8&9 SCRIPT ###

### TWO CATEGORICAL VARIABLES ###
### JOINT FREQUENCY DISTRIBUTIONS
# Dataframe Health is in Lesson 8-9_Data.RData
# Cross table with absolute frequencies
Health$Age # numerical variable grouped into interval classes
Health$Interest # categorical ordinal variable
distr.table.xy(x = Age, y = Interest,
               freq.type="joint",
               freq="count",data = Health) 
# cross-tab with joint absolute frequencies
# 97 is the number of people with age in [31,45] AND with
# LOW interest in healthy food

# Let's look at the distribution of Interest
distr.table.x(Interest,prop = "count",data = Health)
# The absolute frequencies of Interest are:
#Fr("Low") = 345; Fr("Medium")=654; Fr("High")=225
# In a bivariate setting these are called
# MARGINAL ABSOLUTE FREQUENCIES of the variable INTEREST
# they represent the MARGINAL DISTRIBUTION of INTEREST

# Joint Relative Frequencies
# Massively more interesting than absolute
distr.table.xy(x = Age, y = Interest,freq.type="joint",
               freq="prop",data = Health) 

# Side-by-side bar chart
distr.plot.xy(x = Age, y = Interest,freq.type="joint",
               freq="prop",data = Health,
              plot.type = "bars",bar.type = "beside")
# here the joint relative frequencies of individual
# combinations of values are easily comparable

# Stacked bar chart
distr.plot.xy(x = Age, y = Interest,freq.type="joint",
              freq="prop",data = Health,
              plot.type = "bars",bar.type = "stacked")
# here the marginal relative frequencies of AGE
# are easily comparable

# - side-by-side bar plots are better for comparing
# individual joint frequencies
# - stacked bar plots are better for comparing
# marginal frequencies

### CONDITIONAL FREQUENCY DISTRIBUTIONS
# Cross table with conditional frequencies
# of INTEREST given
# different values of the variable AGE
distr.table.xy(x = Age, y = Interest,freq.type="y|x",
               freq="prop",data = Health)
# - e.g. 0.36 is the proportion of individuals with
# a LOW interest in healthy food AMONG THE INDIVIDUALS
# in the [18,30] category
# - e.g. what is the prop. of young ([18-30]) people among
# people with a high interest in healthy food?
distr.table.xy(x = Age, y = Interest,freq.type="x|y",
               freq="prop",data = Health) # answer: 22%
# - e.g. what is the prop. people that are young ([18-30]) and
# have with a high interest in healthy food in the sample?
distr.table.xy(x = Age, y = Interest,freq.type="joint",
               freq="prop",data = Health) # answer: 4%
# - exam like question: what is the conditional frequency of
# the variable INTEREST GIVEN (|) the age class [31-45]?
distr.table.xy(x = Age, y = Interest,freq.type="y|x",
               freq="prop",data = Health)
# Freq(Interest="Low"|Age=[31,45])=0.29 #(=97/333)
# Freq(Interest="Medium"|Age=[31,45])=0.5
# Freq(Interest="High"|Age=[31,45])=0.20

# Conditional frequencies of AGE given INTEREST
distr.table.xy(x = Age, y = Interest,freq.type="x|y",
               freq="prop",data = Health)
# e.g. 0.53 is the proportion of young people [18-30]
# within the group of people with LOW interest in healthy food

# TBH side-by-side barplots and stacked barplots are MASSIVELY
# more insightful if constructed on CONDITIONAL FREQUENCIES
# Side-by-side bar chart for conditional frequencies
distr.plot.xy(x = Age, y = Interest,freq.type="y|x",
              freq="prop",data = Health,
              plot.type = "bars",bar.type = "beside")
# Stacked bar chart for conditional frequencies <- choose this
distr.plot.xy(x = Age, y = Interest,freq.type="y|x",
              freq="count",data = Health,
              plot.type = "bars",bar.type = "stacked")
# ARE INTEREST and AGE ASSOCIATED?
# - 2 categorical variables x,y are ASSOCIATED if the conditional
# frequencies of y|x are very different depending on the value
# of x
# INTERPRETATION: the higher the age
# the higher the interest in healthy food
# IN PRACTICE: if the stacked bars show very different 
# conditional distributions, this indicates ASSOCIATION
# between x and y.
# This shows also from the table of conditional freq. of
# interest given age! The conditional distributions
# are very different! 
# (note that you can swap x and y here)
# generally we choose x as the variable that 
# can have an impact of y (in this case age can have an impact
# on interest)

### ONE CATEGORICAL VARIABLE AND ONE NUMERICAL VARIABLE ###
distr.table.x(Tweets$Company)
distr.plot.x(Tweets$Time,plot.type="hist")
# Joint frequency table looks AWFUL!
# The numerical variable assumes too many values
distr.table.xy(x=Time,y=Company,freq="counts",freq.type="joint",data=Tweets)
# APPROACH I: group the numerical var in interval classes
# (not ideal as we lose a lot of info by grouping in classes
# and it is a subjective representation)
# Joint frequency table with interval classes
distr.table.xy(x=Time,y=Company,freq="counts",freq.type="joint",
               breaks.x=c(600,1000,2000,3500),data=Tweets)
# APPROACH II: multiple hist with conditional distributions
# (sometimes not ideal, cumbersome to compare too many hist)
# plot the conditional distributions of Time for each Company
distr.plot.x(Tweets$Time[Tweets$Company=="Airplane"],
             plot.type="hist")
distr.plot.x(Tweets$Time[Tweets$Company=="Courier"],
             plot.type="hist")
# APPROACH III: multiple boxplot with conditional distributions
# (make sure you know! IMPORTANT!)
# Side-by-side boxplots
distr.plot.xy(x=Company,y=Time,
              plot.type="boxplot",data=Tweets)
# boxplots represents the conditional  distributions of
# Time given the different Companies
# Let's examine the main features of the boxplots and compare them
# LOCATION (compare where the boxes are, the medians and quartiles)
# the Airplane company has typically slowest response, as the boxplot is in the
# highest location and with the highest median, followed by the companies
# Products and then Tour, Telecom and Courier in order.
# DISPERSION (compare range and IQR)
# the conditional distribution of Time has the highest dispersion in 
# correspondence to the Products company, as measured by the RANGE.
# It is followed by Airplane and then Tour. Finally Telecom and Courier
# have a similar range if we include the outliers of the Courier
# The local dispersion as measured by the IQR, i.e. the boxes heights
# is the highest for Products, pretty similar for Airplane, Telecom and Tour,
# and the lowest for Courier
# OUTLIER
# the conditional distribution of Time given Courier shows some outliers
# in correspondence to Products only one upper outlier and 
# there are no outliers for the other distributions
# SYMMETRY
# the conditional distributions for Airplane, Courier and Tour
# seem pretty symmetric. For Telecom the distribution is slightly right skewed.
# For Company the distr. is markedly right skewed.
# ASSOCIATION
# location, dispersion and skewness of the conditional distributions of time
# CLEARLY depends on the Company. Hence we can say that there is an association
# between Time and Company.
# In particular, the Airplane company seems to be much slower than the others,
# and the Product company shows a very high
# dispersion/variability in time taken to reply.

# APPROACH IV: conditional summary measures
# (another great approach!)
# Conditional summary measures
# The following function calculates conditional mean, median,...
# of the variable time in correspondence to each company subsample 
distr.summary.x(x=Time,by1=Company,# conditioning variable is Company
                stats=c("summary","cv"),data=Tweets)
# by setting the parameter by1 = Company 
# we calculate CONDITIONAL SUMMARY MEASURES of TIME
# given different values of COMPANY

### TWO NUMERICAL VARIABLES ###
### THE SCATTERPLOT
distr.plot.xy(x=livingArea,y=price,plot.type = "scatter",data=House_Price)
distr.plot.xy(x=rooms,y=price,plot.type = "scatter",data=House_Price)
distr.plot.xy(x=lotSize,y=price,plot.type = "scatter",data=House_Price)
distr.plot.xy(x=rooms,y=price,plot.type = "box",data=House_Price)
### MEASURE OF LINEAR ASSOCIATION
# COVARIANCE
cov(House_Price$livingArea,House_Price$price)
cov(House_Price$rooms,House_Price$price)
cov(House_Price$lotSize,House_Price$price)
# To ignore missing values: use="complete" 
cov(House_Price$lotSize,House_Price$price,use="complete")
# positive covariance indicates positive LINEAR ASSOCIATION
# negative covariance indicates negative LINEAR ASSOCIATION
# however we cannot interpret the abs.value of COVARIANCE!
# CORRELATION
cor(House_Price$livingArea,House_Price$price)
cor(House_Price$rooms,House_Price$price)
# To ignore missing values: use="complete"
cor(House_Price$lotSize,House_Price$price,use="complete")
