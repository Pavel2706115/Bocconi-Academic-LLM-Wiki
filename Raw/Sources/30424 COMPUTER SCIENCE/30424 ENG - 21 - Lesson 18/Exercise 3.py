def frequency(string):
    dct_freq = {}
    for char in string:
        if char in dct_freq:
            dct_freq[char] = dct_freq[char] + 1
        else:
            dct_freq[char]=1
    return dct_freq
    
