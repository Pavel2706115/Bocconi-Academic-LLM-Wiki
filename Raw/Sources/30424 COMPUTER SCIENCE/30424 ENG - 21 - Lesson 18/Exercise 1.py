def create(number):
    output = dict()
    for n in range(1, number + 1):
        output[n] = (n / 2)**3
    return output

def show(MyDictionary):
    print("Key\tValue")
    for K in MyDictionary:
        print(str(K) + "\t" + str(MyDictionary[K]))
