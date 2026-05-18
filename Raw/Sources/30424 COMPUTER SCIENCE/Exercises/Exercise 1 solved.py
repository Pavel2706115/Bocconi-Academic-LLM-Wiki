
def harmonic_sum(N, a):
    
    total = 0
    
    for n in range(1, N+1):
        total = total + 1/n**a
        
    return total

