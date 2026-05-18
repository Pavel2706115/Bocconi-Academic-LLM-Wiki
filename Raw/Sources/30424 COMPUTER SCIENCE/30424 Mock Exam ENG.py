# --------------------------------------------------------------------
#   Section 1 - PERSONAL INFORMATION
# --------------------------------------------------------------------  
#
#   Name:           Pavel
#   Surname:        Andreev     
#   Student ID:     36614
#
# --------------------------------------------------------------------  



# --------------------------------------------------------------------
#   Section 2 - Variables that can be used to test the functions
# --------------------------------------------------------------------   

a1 = ('Italy','United States','UK','France','China','Argentina','Spain','Russia','Japan','Portugal','Canada','Iceland','Kenia','Mexico','Thailand','Germany','Australia')
a2 = [3, 5, 2, 6, 0, 10]
a3 = [60, 2, 11, 4, 2]
a4 = [45, 0.0, 'France', 23.6, 3, True, 'UK', 10, 2.2, 5, 'Spain', 4]


# --------------------------------------------------------------------
#   Section 3
#   Exercise1: Create the requested function below 
# --------------------------------------------------------------------
def operation(seq):
    result = []
    i = 0
    while i < len(seq):
        element = seq[i]
        if (type(element) == int or type(element) == float) and element != 0:
            result.append(element)

        i = i + 1
    return result[::-1]
# --------------------------------------------------------------------
#   Section 4
#   Exercise 2: Complete the following function 
# --------------------------------------------------------------------

import random
def create_dct(seq, num=4):
    dct = {}
    keys = 1




    return dct





