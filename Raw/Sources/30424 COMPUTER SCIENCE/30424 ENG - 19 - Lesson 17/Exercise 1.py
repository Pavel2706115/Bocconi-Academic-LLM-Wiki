import random

def random_list(x):
    Rand_list = []
    for i in range(1,x+1):
        rand_int= random.randint(1,5)
        if rand_int not in Rand_list:
            Rand_list.append(rand_int)
    return Rand_list
