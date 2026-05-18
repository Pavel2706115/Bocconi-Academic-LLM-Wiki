import random

cities = ['Milan','New York','London','Paris','Singapore','Buenos Aires','Madrid','Lisbon','Tokio','San Antonio','Seattle','Amsterdam','Boston','Athens','Berlin','Dublin','Florence','Rome','Prague','Dubai','Cape Town','Bruges','Sao Paulo','Toronto','Beijing']


def create(seq, num):
    
    results = {}
    
    while len(results) < num:
        K = random.randint(1,100)
        Val = random.choice(seq)
        if K not in results and Val not in results.values():
            results[K] = Val
            
    return results






