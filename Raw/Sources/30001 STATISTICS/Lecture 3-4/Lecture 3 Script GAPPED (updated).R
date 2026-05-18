### LECTURE 3 SCRIPT ###
[#slides 1-14]

### UBStats INSTALLATION ###
# Download and install the package UBStats

### TABLES AND PLOTS FOR CATEGORICAL VARIABLES ###
### FREQUENCY TABLES
# Load the file Loyalty.RData for this session
# dist.table.x() function for frequency tables/distributions
distr.table.x(x=Dept,freq=c("counts","prop","perc"),total=T,data=Loyalty)
distr.table.x(x=Dept,data=Loyalty)

### PIE AND BARCHART
# dist.plot.x() function for pies
distr.plot.x(x=Dept, freq="proportions", plot.type="pie",data=Loyalty)
# Frequency table for the FACTOR variable Recommend.F,
# qualitative ordinal variable
distr.table.x(x=Recommend.F,data=Loyalty)
# Note that we use the factor variable Recommend.F,
# where categories are ordered
# dist.plot.x() function for barcharts
distr.plot.x(x=Recommend.F, freq="perc", plot.type="bars",data=Loyalty)
distr.plot.x(x=Recommend, freq="perc", plot.type="bars",data=Loyalty) #unordered :/

### EXERCISE ###
# Hint: use the Help tab to solve the exercise ;)
# a) Produce a frequency table of the variable Dept
# which shows 3 decimal digits for the relative frequencies (proportions)

# b) Represent graphically the variable Dept using a bar chart such that
# the bars are RED and they are displayed in DECREASING ORDER

### END OF EXERCISE ###