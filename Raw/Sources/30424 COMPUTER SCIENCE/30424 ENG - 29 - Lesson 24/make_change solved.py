


def change1(ch_amount):

    coins_set = (2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01)      # Available coins, sorted descending
    change = []                                                 # List to store the coins used


    # Loop to calculate which coins must be used to make change
    for x in coins_set:
        while ch_amount >= x:
            ch_amount = ch_amount - x
            change.append(x)
    
    return change



def change2(ch_amount):

    coins_set = (2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01)      # Available coins, sorted descending
    change = {}                                                 # Dictionary to store the coins used
    
    for x in coins_set:
        count = ch_amount // x            
        if count > 0:
            change[x] = int(count)
            ch_amount = ch_amount - x * count
    
    return change
