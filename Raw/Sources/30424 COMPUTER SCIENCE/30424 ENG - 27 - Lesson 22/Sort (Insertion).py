def InsertionSort(MyList):
    
    for i in range(1, len(MyList)):
        elem = MyList[i]
        j = i-1
        while j >= 0 and elem < MyList[j] :
                MyList[j + 1] = MyList[j]
                j = j-1
        MyList[j + 1] = elem

    return MyList
