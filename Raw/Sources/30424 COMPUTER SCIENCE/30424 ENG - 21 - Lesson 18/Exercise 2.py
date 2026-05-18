def delete(K, Val):
    a1 = {'a':61,'b':22,'c':53,'d':19,
          'e':54,'f':34,'z':71,'h':26,
          'l':3,'p':64,'y':5,'u':54
    }

    if K in a1 and a1[K] == Val:
        removed = a1.pop(K)
        print(f"Deleted: {K} \ {removed}")
    else:
        print ("No matching key-value pair found.")

    return a1
