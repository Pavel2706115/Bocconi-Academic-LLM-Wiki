### LECTURE 4 SCRIPT ###

### TABLES AND PLOTS FOR NUMERICAL VARIABLES ###
# Different cases
distr.table.x(x=Nr_visits,data=Loyalty) # LOOKING GREAT
distr.table.x(x=Age,data=Loyalty) # UNREADABLE
distr.table.x(x=Amount,data=Loyalty) # UNREADABLE
# distinguish numerical variables depending on whether they assume 
# few values or
# many distinct values

### NUMERICAL VARIABLES WITH FEW POSSIBLE VALUES
# Representations for a discrete variable with FEW POSSIBLE VALUES
# for these variables frequency tables are GOOD!
distr.table.x(x=Nr_visits, freq= c("counts","prop","perc"),data=Loyalty)
distr.plot.x(x=Nr_visits, freq="perc", plot.type="bars",data=Loyalty)
# !!! WARNING !!! we should not use barplots for numerical variables!
# as the distances between values are not respected!
# we use Stick charts instead!
# Spike (or Stick) Plot
distr.plot.x(x=Nr_visits, freq="perc", plot.type="spike",data=Loyalty)

### NUMERICAL VARIABLES WITH MANY POSSIBLE VALUES
# Define a numerical discrete variable with many values
Ticket = c(24,35,17,21,24,37,26,46,58,30,32,13,12,38,41,43,44,27,53,27) 
# Frequency distribution
distr.table.x(x=Ticket,freq= c("counts","prop","perc")) #not looking good!
distr.plot.x(x=Ticket,plot.type="bars") #bleah
distr.plot.x(x=Ticket,plot.type="spike") #double bleah
# Frequency distribution for class intervals
distr.table.x(x=Ticket,freq=c("counts","prop","dens"),breaks=5) # create 5 interval classes
# the classes have the same width obtained by dividing
# the range of the data (max-min) by the number of classes (breaks)
distr.table.x(x=Ticket,freq=c("counts","prop","dens"),
              breaks=c(10,20,30,40,50,60))
distr.plot.x(x=Ticket,freq= c("dens"),plot.type="hist",
             breaks=c(10,20,30,40,50,60))
# the density of a class is its relative frequency divided by
# the class width
# e.g. 0.015 = 0.15/(20-10)
# the frequency density of a class represents the "concentration
# of relative frequency in that class"
# Note! When a histogram is constructed with freq. densities
# in the y-axis (I advice to ALWAYS construct it this way)
# then the area of a bar corresponds to the RELATIVE
# FREQUENCY of the corresponding class

# Variable amount: how many classes?
distr.plot.x(x=Amount,freq="densities",plot.type="histogram",
             breaks=3,data=Loyalty) # not enough classes, 
# cannot see the shape of the distribution
distr.plot.x(x=Amount,freq="densities",plot.type="histogram",
             breaks=10,data=Loyalty) # looking good!
distr.plot.x(x=Amount,freq="densities",plot.type="histogram",
             breaks=50,data=Loyalty) # too much detail, lose on the 
# big picture

### EXERCISE ###
# Load the dataset contained in CPS1985.Rdata
# For the following variables say whether their distribution
# i) is symmetric, right skewed, left skewed or none
# ii) has long or short tails

# a) wage
distr.plot.x(wage,plot.type="hist",
             breaks = c(0,5,10,15,20,25,50),
             data = CPS1985)
# quite long right tail (not super long)
# right/positive skewed distribution (right symmetry)

# b) education
distr.plot.x(education,plot.type="hist",
             data = CPS1985)
# right tail non existent, left tail not very long
# the symmetry is not clear, if anything, slightly left 
# skewed

# c) experience
distr.plot.x(experience,plot.type="hist",
             data = CPS1985)
# right skewed 
# quite short right tail

# d) age
distr.plot.x(experience,plot.type="hist",
             data = CPS1985)
# super slightly right skewed?
# short right tail

### END OF EXERCISE ###

# When most data cluster in a narrow range of values and 
# few values are spread in a larger range, use intervals of different widths
distr.plot.x(x=Profitability,freq="densities",plot.type="histogram",
             breaks=20,data=Loyalty)
distr.plot.x(x=Profitability,freq="densities",plot.type="histogram",
             breaks=c(80,100,140,180,220,350,600,850),data=Loyalty)
distr.table.x(x=Profitability,freq = c("count","prop","dens"),
              breaks=c(80,100,140,180,220,350,600,850),data=Loyalty)
# With classes of different widths, ALWAYS have FREQUENCY DENSITIES
# on the y-axis, so that the areas of the bars correspond to relative frequencies
# and their heights represent frequency concentrations (densities!)
# (if classes have equal widths then it is FINE to have relative or absolute
# frequencies in the y-axis, because their heights will be proportional
# to the respective frequency densities)

# Note that UBStats can produce frequency distributions and histograms,
# for a numerical variable already divided into intervals
table(Loyalty$Income)
# if a numerical variable is given to you collected in classes already,
# you can still produce a histogram from it, by setting interval = TRUE
distr.table.x(x=Income,freq=c("counts","prop","perc","dens"),
              interval=TRUE,f.digits = 3,d.digits = 3,data=Loyalty)
distr.plot.x(x=Income,plot.type="histogram",
             interval=TRUE,data=Loyalty)
# useful! Thank you UBStats! :P

### CUMULATIVE FREQUENCIES, STEP DIAGRAM, OGIVE ###
# Cumulated frequencies and step diagram
distr.table.x(x=Nr_visits,freq=c("count","prop","cumulative"),
              f.digits=5,data=Loyalty)
# for a numerical or qualitative ordinal variable
# we can calculate cumulative frequencies as well
# the cumulative frequency of a class represents the proportion
# of observations that fall in that class AND IN THE CLASSES BEFORE

# we do not calculate cumulative freq for QUALITATIVE NOMINAL variables!
# because it would not make sense. There is no natural ordering!

# OPTIONAL PLOTS of CUMULATIVE FREQUENCIES
# a step chart is a representation of cumulative frequencies
distr.plot.x(x=Nr_visits,freq="prop",plot.type="cumulative",data=Loyalty)
# cumulated frequencies
distr.table.x(x=Recommend.F,freq=c("prop","cum"),data=Loyalty)
# we can produce a step chart of a qualitative ordinal variable
# HOWEVER steps are not connected, to evidence that distances between
# categories are not meaningful here
distr.plot.x(x=Recommend.F,plot.type="cumulative",data=Loyalty)

# For a numerical variable with many different values, the step chart 
# is very messy!
distr.plot.x(x=Age,freq="prop",plot.type="cumulative",data=Loyalty)
# if we display the cumulative freq of a numerical var grouped into classes
# the step chart is smoothed out into a OGIVE!
# this is consistent with the assumption that observations are
# uniformly distributed within each classe
distr.plot.x(x=Age,freq="prop",breaks=c(25,35,45,55,65,80),plot.type="cumulative",data=Loyalty)
distr.plot.x(x=Age,freq="prop",breaks=c(25,45,60,80),plot.type="cumulative",data=Loyalty)