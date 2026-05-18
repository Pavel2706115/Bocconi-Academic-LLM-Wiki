# Slide 9
numeri = [10, 34, 27, 145,18] 
destination = 'Los Angeles' 



# Slide 13
numbers = [10, 34, 27, 145,18] 
for elem in range(len(numbers)): 
    print(numbers [elem]*2/3)  


destination = 'Los Angeles'  
index = 0 
while index < len(destination): 
    print(destination[index]) 
    index = index + 1


destination = 'Los Angeles'  
index = -1 
while index >= -len(destination): 
    print(destination[index]) 
    index = index - 1


numbers = [10, 34, 27, 145,18] 
for x in range(len(numbers)): 
    numbers [x] = numbers [x] / 2 
print(numbers) 



# Slide 15
quote = 'The best way to predict the future is to implement it' 
mylist = quote.split() 
for elem in range(len(mylist)): 
    if len(mylist[elem]) > 5:
        mylist[elem] = mylist[elem].upper() 
myseparator = ' ' 
quote2 = myseparator.join(mylist) 



# Slide 16
# append
list_a = [1, 10, 21, 3, 15, 8, 13, 21, 34, 55, 89] 
list_b = [1, 2, 35, 4, 15, 6, 21, 8, 63, 10, 11, 12, 13] 
list_c = []		 
for i in list_a:
    if i in list_b and i not in list_c:
        list_c.append(i)


# pop, remove
univ = ['Bocconi', 'IULM', 'Statale']

'''
# IndexError
numbers = [117, 34, 235, 15] 
for i in range(len(numbers)):
    if numbers[i] % 5 == 0: 
        numbers.pop(i)
'''

numbers = [117, 34, 235, 15] 
new_list = [] 
for i in range(len(numbers)): 
    if numbers [i] % 5 == 0: 
        new_list.append(numbers[i]) 
for elem in new_list: 
    numbers.remove(elem) 
