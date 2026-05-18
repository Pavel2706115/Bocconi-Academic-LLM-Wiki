


def FirstLast(s):
    myfirst = s[0]
    mylast = s[-1]
    p = "First character: " + myfirst.upper() + ", last character: " + mylast.upper()
    return p



def FirstLast2(s, start=0, stop=1):
    myslice = s[start:stop+1]
    p = myslice.upper()
    return p



def FirstLast3(s):
    mylist = s.split()
    myfirst = mylist[0]
    mylast = mylist[len(mylist)-1]  # Can also be used: mylist[-1]
    p = "First word: " + myfirst.upper() + ", last word: " + mylast.upper()
    return p
