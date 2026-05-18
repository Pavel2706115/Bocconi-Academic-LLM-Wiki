


# SLIDE 7 Methods of dictionaries

phonebook = {'Mario':'555-1111', 'Julia':'555-2345', 'Anna':'555-6789'}




# SLIDE 8 Traversing dictionaries

phonebook2 = {'Mario':'555-1111', 'Julia':'555-2345', 'Anna':'555-6789', 'Emma':'555-3528', 'John':'555-8341', 'Frank':'555-6789' }


for K in phonebook2:  # traversing keys
    print(K)


for K in phonebook2.keys():  # traversing keys
    print(K)


for K in phonebook2:  # traversing values
    print(phonebook2[K])


for Val in phonebook2.values():  # traversing values
    print(Val)


for K, Val in phonebook2.items():  # traversing items (couples)
    print (K, '\t', Val)


for K in phonebook2:
    question = input('Do you want to change the phone number of ' + str(K) + '? (yes/no) ')
    if question == 'yes':
        phonebook2[K] = input('Enter a new number: ')








