
def present_value(rate, duration, CF):
    total = 0
    for year in range (1, duration + 1):
        PV = CF/(1+rate)**year
        total = total + PV
    return total


