

def sum_digits():
    num = input('Insert an integer number: ')
    total = 0
    for digit in num:
        total = total + int(digit)
    return total



# Possible alternative:

def sum_digits_2():
    num = input('Insert an integer number: ')
    total = 0
    for digit in range(len(num)):
        total = total + int(num[digit])
    return total



