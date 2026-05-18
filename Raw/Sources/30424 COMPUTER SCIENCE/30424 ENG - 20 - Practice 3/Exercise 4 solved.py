

economics = ["market", 150, "economy", "money", 10, "price", "cost", 142.6, "demand", "supply", "profit", "investment", "capital", "trade", 4, "inflation", "interest", 34.67, "growth", "policy", 52.4, "risk", 14, "debt", "wealth", "credit"]



def string_count(mylist):
    strings = 0
    for elem in mylist:
        if type(elem) == str:
            strings = strings + 1		
    return strings


def strings(mylist):
    newlist = []
    for elem in mylist:
        if type(elem) == str:
            newlist.append(elem)	
    return newlist



def analysis(mylist):
    strings, numbers = 0,0 
    for elem in mylist:
        if type(elem) == str:
            strings = strings + 1
        else:
            numbers = numbers + elem
    newlist = [strings, numbers]
    return newlist
