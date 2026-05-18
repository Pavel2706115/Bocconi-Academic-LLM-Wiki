### LECTURE 2 SCRIPT ###

### BASIC SYNTAX ###
# Expressions
3+5*3.5 # COMMAND (or CONTROL) + ENTER
# Expression calling a function
log(3+5*3.5)
exp(3)
# Expression based on an operator
3>0

# Create a numeric vector
x = c(1,5,8,-1,0,-2,10) # "=" is the same as "<-" for what we need
x # press control+enter to see what is inside x
# Create a character vector
s = c("F","M","F","F","M","F","M","F","M","F")
s
# Example of logic vector
l = (x>=0) # condition is checked entry wise
l
# Create a new numeric vector from x
y = x+2

# R "null" values: NULL, NA, NaN, Inf
x
log(x) # NaN stands for Not a Number
# NA: not available a.k.a. missing data

### OPERATORS AND FUNCTIONS ###
# OPERATORS
x = c(1.234,7.21,5,4.1,10.678)
y = c(1,8,3,6,2)
# Arithmetic operators
x+y
x^y
# Comparison operators
x>y # > comparison is carried over entry wise
x>=y
# the output is a logical vector (i.e. a vector of TRUEs and FALSEs)
x==y # equal to
z = c(1,2,3,4,5)
y==z
x!=y # different from
y!=z

# Logical operators !,&,|
# two dummy variables (variable with only 2 possible values)
senior = c(T,T,T,F,F) # whether the customer is senior or not
card = c(T,T,F,T,F) # whether the customer has a loyalty card
!senior # negation
senior & card # customers that are senior AND with a card
senior | card # customers that are senior OR with a card

### FUNCTIONS
log(x)
exp(x)

### R OBJECTS ###
### VECTORS
# Create a numeric vector
x = c(1,5,8,0,1,10,3)
# rep()
s = c("North","North","North","North","South","South") # TOO LONG G !
s1 = rep("North",4) # creates a vector rep-eating "North" 4 times
s2 = rep("South",3)
# Concatenate vectors
s = c(s1,s2); s #; semi colon
# names() and length()
names(x) = c("Berlin","Paris","Amsterdam","Stockholm",
            "Lisbon","Madrid","Rome") # optional
# set the names of the columns generally
length(x) # generally this is n, the sample size

# the rep function is very useful when we have a frequency table
# and want to load it in R Studio as raw data
# consider a sample of customers and the variable Number of Children
NChildren = 0:4 # variable with 5 possible values/levels: 0,1,2,3,4
f = c(45,37,23,10,4) # absolute frequency of each value
rawdata = rep(NChildren,f)
# rep creates a vector by repeating each value in NChildren as many times
# as specified in f
length(rawdata) # 119 length of the vector
table(rawdata)

# Subsetting vectors
x
s
x[3] # entry 3 of x
x.sub1 = x[c(1,4,6)] # entries 1,4,6 of x
x.sub2 = x[-c(3,6)] # remove entry 3 and 6 of x
x.sub3 = x[c(TRUE,FALSE,FALSE,TRUE,FALSE,TRUE,FALSE)] # subset x with logical vector
s.N = s=="North" # define a logical vector of cities in the north
x.sub4 = x[s.N] # use it to subset x
# extract from x only cities in the North
x[s=="North"] # subsetting x with a logical vector

### EXERCISE 1 ###
iris$Species
length(iris$Species)
table(iris$Species)
# We define the vector Species, containing
# the species of a sample of flowers
Species = iris$Species #run with cmnd+ENTER
Species
# factor is a qualitative ordinal variable

# We define the vector Petal, containing
# the lengths of the petals of the sample of flowers
Petal = iris$Petal.Length #run with cmnd+ENTER
# a) How many flowers does the sample contain?
dim(iris) # dimensions: 150 rows (obs) and 5 cols (vars)
n = length(Petal)

# b) Define the subvector of Petal lengths
# with only flowers of species "virginica"
subPetal = Petal[Species=="virginica"] # subsetting a vector with a logical condition
# also called filtering 

# c) Define the subvector of Species
# with flowers that have petals longer than 5
subSpecies = Species[Petal>5]
iris$Species[iris$Petal.Length>5]

# d) How many flowers are from the "virginica" species
# and have petals longer than 5?
sum((Species=="virginica")&(Petal>5)) # 41
# note that sum applied to a logical vector, counts the number of TRUEs

### END OF EXERCISE 1 ###

#### FACTORS (not fundamental)
char = c("F","M","F","F","M","F","M","F","M","F")
fact = factor(char) # for QUALITATIVE VARIABLES
# in a factor, also the possible levels of the variables are registered
levels(fact) # USELESS :(
# Reordering levels
char = c("Low","Medium","High","Medium","High","VeryLow","High","Medium","Low")
# char is qualitative ordinal
table(char) # the categories are in alphabetical order
# to impose an order on a vector of strings, use factor function
charOrdered = factor(char,levels=c("VeryLow","Low","Medium","High","VeryHigh"))
# factor changes the type of variable to factor
# and specifies the ordered possible levels
table(charOrdered)
# it's unlikely that we ask you to reorder factors in a dataset
# but you find this in some solutions of exercises

### MATRICES # skip this for now
v<-c(1,3,4.1,5,6.1,8,9,10.11,30,5.3)
# Create a matrix from a vector
mat<-matrix(v,nrow=2,ncol=5)
mat<-matrix(num.v,nrow=2,ncol=5,byrow=T)

#### DATAFRAMES
#??? import
Loyalty = Loyalty_2_
# Basic functions for dataframes
str(Loyalty) # not useful
head(Loyalty) # first 6 rows of the dataset. Sometimes useful
summary(Loyalty) # see this later on
dim(Loyalty) # 125 obs, 9 vars

# Extracting a variable

### EXERCISE 2 ###
#a) Find the mean age of customers in the sample
mean(Loyalty$Age) # cannot compute mean as one client did not disclose their age
mean(Loyalty$Age,na.rm=TRUE)
# na.rm = TRUE: remove all the missing values
# na.rm = FALSE: does not remove the missing values
# btw I promise you will not have missing values in the exam!

#b) Calculate the mean profitability of customers in the sample
# that are "Very Likely" to recommend
Loyalty$Recommend # customers' recommendations
Loyalty$Recommend=="Very Likely" # check which ones are == "Very Likely"
Loyalty$Profitability[Loyalty$Recommend=="Very Likely"] # customer's profitability
# only of customers very likely to recommned
mean(Loyalty$Profitability[Loyalty$Recommend=="Very Likely"])

#c) Calculate the mean profitability of customers in the sample
# that are "Very Unlikely" to recommend
mean(Loyalty$Profitability[Loyalty$Recommend=="Very Unlikely"])
### END OF EXERCISE 2 ###

### TO CLEAN THE ENVIRONMENT ###
#rm(list=ls())
#ctrl + L to clean the console