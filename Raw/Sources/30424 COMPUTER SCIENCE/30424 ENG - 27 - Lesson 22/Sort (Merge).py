def MergeSort(MyList):      # This is a case of "recursive function"
                            # i.e. the body of the function contains
                            # a call to the function itself.
                            # Recursive functions are not part of 30424 course
    
    if len(MyList) > 1:
        mid = len(MyList)//2
        L = MyList[:mid]
        R = MyList[mid:]

        MergeSort(L)        # These are two calls to the
        MergeSort(R)        # function that we are defining
        
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                MyList[k] = L[i]
                i = i+1
            else:
                MyList[k] = R[j]
                j = j+1
            k += 1

        while i < len(L):
            MyList[k] = L[i]
            i = i+1
            k = k+1

        while j < len(R):
            MyList[k] = R[j]
            j = j+1
            k = k+1

    return MyList
