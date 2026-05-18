'''
def character_count(text, character = 'a'):
    count = 0
    for mychar in text:
        if mychar == character:
            count = count + 1
    return count




It is also possible to use the .count() method of the strings


def character_count(text, character = 'a'):
    mycount = text.count(character)
    return mycount

'''
def character_count(text, looking = 'a'):
    count = text.count(looking)
    return count
    









































