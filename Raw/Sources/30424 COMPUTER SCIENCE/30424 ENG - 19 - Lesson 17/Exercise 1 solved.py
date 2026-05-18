
import random


# This function creates a list that can contain duplicate elements

def random_list(num):
    mylist = []
    for x in range(num):
        rnd_number = random.randint(1, 100)
        mylist.append(rnd_number)
    return mylist


# These functions create a list with no duplicate elements

def random_list2a(num):
    mylist = []
    while len(mylist) < num:
        rnd_number = random.randint(1, 100)
        if rnd_number not in mylist:
            mylist.append(rnd_number)
    return mylist


def random_list2b(num):
    mylist = []
    while len(mylist) < num:
        rnd_number = random.randint(1, 100)
        if rnd_number in mylist:
            continue
        else:
            mylist.append(rnd_number)
    return mylist
