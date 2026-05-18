import random

heads = 0
tails = 0

tries = int(input("Enter the number of tosses: "))
for i in range(tries):
    random_nr = random.randint(0,1)
    if random_nr == 0:
        heads = heads + 1
    else:
        random_nr == 1
        tails = tails + 1
print('Number of heads tosses: ', heads,'\n Number of tails tosses: ',tails)
