def BubbleSort(MyList):
    
    n = len(MyList)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if MyList[j] > MyList[j+1]:
                MyList[j], MyList[j+1] = MyList[j+1], MyList[j]

    return MyList
