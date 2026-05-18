def sum_digits():
    strNumber = input("Enter an integer: ")
    
    mysum = 0

    for char in strNumber:
        mysum = mysum + int(char)

    return mysum 
