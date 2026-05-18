### LECTURE 4 SCRIPT ###

### TABLES AND PLOTS FOR NUMERICAL VARIABLES ###
# Different cases
distr.table.x(x=Nr_visits,data=Loyalty) 
distr.table.x(x=Age,data=Loyalty) 
distr.table.x(x=Amount,data=Loyalty) 

### NUMERICAL VARIABLES WITH FEW POSSIBLE VALUES
# Representations for a discrete variable with FEW POSSIBLE VALUES
distr.table.x(x=Nr_visits, freq= c("counts","prop","perc"),data=Loyalty)
distr.plot.x(x=Nr_visits, freq="perc", plot.type="bars",data=Loyalty)
# Spike (or Stick) Plot
distr.plot.x(x=Nr_visits, freq="perc", plot.type="spike",data=Loyalty)

### NUMERICAL VARIABLES WITH MANY POSSIBLE VALUES
# Define a numerical discrete variable with many values
Ticket<-c(24,35,17,21,24,37,26,46,58,30,32,13,12,38,41,43,44,27,53,27)
# Frequency distribution
distr.table.x(x=Ticket,freq= c("counts","prop","perc")) #not looking good!
distr.plot.x(x=Ticket,plot.type="bars") #bleah
distr.plot.x(x=Ticket,plot.type="spike") #double bleah
# Frequency distribution for class intervals
distr.table.x(x=Ticket,freq=c("counts","prop","dens"),breaks=5)
distr.table.x(x=Ticket,freq=c("counts","prop","dens"),
              breaks=c(10,20,30,40,50,60))
distr.plot.x(x=Ticket,freq= c("dens"),plot.type="hist",
             breaks=c(10,20,30,40,50,60))
# Variable amount: how many classes?
distr.plot.x(x=Amount,freq="densities",plot.type="histogram",
             breaks=3,data=Loyalty)
distr.plot.x(x=Amount,freq="densities",plot.type="histogram",
             breaks=10,data=Loyalty)
distr.plot.x(x=Amount,freq="densities",plot.type="histogram",
             breaks=50,data=Loyalty)

### EXERCISE ###
# Load the dataset contained in CPS1985.Rdata
# For the following variables say whether their distribution
# i) is symmetric, right skewed, left skewed or none
# ii) has long or short tails

# a) wage

# b) education

# c) experience

# d) age

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
# If classes have equal widths then it is FINE to have relative or absolute
# frequencies in the y-axis

# Note that UBStats can produce frequency distributions and histograms,
# for a numerical variable already divided into intervals
distr.table.x(x=Income,freq=c("counts","prop","perc","dens"),
              interval=T,f.digits = 3,d.digits = 3,data=Loyalty)
distr.plot.x(x=Income,plot.type="histogram",
             interval=T,data=Loyalty)

### CUMULATIVE FREQUENCIES, STEP DIAGRAM, OGIVE ###
# Cumulated frequencies and step diagram
distr.table.x(x=Nr_visits,freq=c("prop","cum"),data=Loyalty)
distr.plot.x(x=Nr_visits,plot.type="cumulative",data=Loyalty)
# Cumulated frequencies
distr.table.x(x=Recommend.F,freq=c("prop","cum"),data=Loyalty)
distr.plot.x(x=Recommend.F,plot.type="cumulative",data=Loyalty)
# Numerical variable with plot of cumulative freq. based on raw data 
# and on ogive plots based on different categorization 
distr.plot.x(x=Age,freq="prop",plot.type="cumulative",data=Loyalty)
distr.plot.x(x=Age,freq="prop",breaks=c(25,35,45,55,65,80),plot.type="cumulative",data=Loyalty)
distr.plot.x(x=Age,freq="prop",breaks=c(25,45,60,80),plot.type="cumulative",data=Loyalty)