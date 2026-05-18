

def delete(dct, seq):
    for K in seq:
        if K in dct:          #or if K in dct.keys():
            x = dct.pop(K)
            print('Deleted the key', K, 'and the value', x)
    return dct







