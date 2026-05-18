def SelectionSort(MyList):
    
    for i in range(len(MyList)):
        min_idx = i
        for j in range(i+1, len(MyList)):
            if MyList[min_idx] > MyList[j]:
                min_idx = j
        MyList[i], MyList[min_idx] = MyList[min_idx], MyList[i]

    return MyList
