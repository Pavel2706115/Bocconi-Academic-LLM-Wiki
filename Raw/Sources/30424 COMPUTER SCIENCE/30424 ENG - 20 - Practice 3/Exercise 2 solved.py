
import random


def overlap(number):

    mylist1 = []
    mylist2 = []
    results_list = []
    
    for x in range(number):
        mylist1.append(random.randint(1,100))
        mylist2.append(random.randint(1,100))
  
    for element in mylist1:
        if element in mylist2:
            results_list.append(element)
            
    return results_list




