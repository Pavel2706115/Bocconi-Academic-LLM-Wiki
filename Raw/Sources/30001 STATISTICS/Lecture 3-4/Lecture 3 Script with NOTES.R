### LECTURE 3 SCRIPT ###

### UBStats INSTALLATION ###
# To download and install the package UBStats
# run the following code, one at a time
install.packages("devtools")
library(devtools)
install.packages("UBStats") # DOWNLOADS UBStats package
library(UBStats) # INSTALL UBStats package

# to make sure that the UBStats package is loaded,
# go to the Packages tab and
# put a tick on the box to the left of UBStats

### TABLES AND PLOTS FOR QUALITATIVE VARIABLES ###
Loyalty$Dept # qualitative nominal variable

### FREQUENCY TABLES
# Load the file Loyalty.RData for this session
# dist.table.x() function for frequency tables/distributions
distr.table.x(x=Dept,data=Loyalty)
# The variable Dept assumes K = 6 different values. There are K=6
# categories for this qualitative nominal variable
# There are n=125 observations
# Under the column Count the ABSOLUTE FREQUENCIES (f) are reported, 
# i.e. number of observations in each category
# Under the column Prop the RELATIVE FREQUENCIES (p) are report,
# i.e. ABSOLUTE FREQ divided by the sample size n
distr.table.x(x=Dept,freq=c("counts","prop","perc"),total=T,data=Loyalty)

### PIE AND BARCHART
# dist.plot.x() function for pies
distr.plot.x(x=Dept, freq="proportions",plot.type="pie",data=Loyalty)
# In a pie chart each sector width is proportional to the
# absolute (or relative) freq of the corresponding category

# ATTENTION! With a pie chart
# 1) it is not easy to compare the frequencies of categories
# 2) we cannot give the categories a clear ordering
# therefore for these reasons we usually prefer BARPLOTS,
# in particular for QUALITATIVE ORDINAL variables
# we always use barplots to have a clear display of the orders
# of the categories

distr.plot.x(Recommend.F,plot.type = "pie",data=Loyalty)
# OK but order is not as clear as in a barchart!

# Frequency table for the FACTOR variable Recommend.F,
# qualitative ordinal variable
distr.table.x(x=Recommend.F,data=Loyalty)
# Note that we use the factor variable Recommend.F,
# where categories are ordered
# dist.plot.x() function for barcharts
distr.plot.x(x=Recommend.F, freq="perc", plot.type="bars",data=Loyalty)
# categories have the natural ordering! Nice!

### EXERCISE ###
# Hint: use the Help tab to solve the exercise ;)
# a) Produce a frequency table of the variable Dept
# which shows 3 decimal digits for the relative frequencies (proportions)
distr.table.x(x=Dept, freq="proportions",plot.type="bars",data=Loyalty,
             f.digits=3)

# b) Represent graphically the variable Dept using a bar chart such that
# the bars are RED and they are displayed in DECREASING ORDER
distr.plot.x(x=Dept, freq="proportions",plot.type="bars",data=Loyalty,
             ord.freq = "decreasing", col = "red")
### END OF EXERCISE ###