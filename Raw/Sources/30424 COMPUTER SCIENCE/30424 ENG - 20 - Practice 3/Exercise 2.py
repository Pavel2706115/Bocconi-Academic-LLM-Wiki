
import random

def overlap(number): #number = 5

    mylist1 = []
    mylist2 = []
    
    for n in range(number): #[0, 1, 2, 3, 4]
        mylist1.append(random.randint(1, 100))
        mylist2.append(random.randint(1, 100))
    print('mylist1',mylist1)
    print('mylist2',mylist2)
    newlist = []
    for num in mylist1:
        if num in mylist2:
            newlist.append(num)

    return newlist
    for num in mylist1:
        if num in mylsit2 and num not in newlist:
            newlist.append(num)
            
print(overlap(8))
