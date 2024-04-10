from math import sqrt
def variance(lengths) -> float:
    n = len(lengths)
    mean = sum(lengths) / n
    
    diff = [x - mean for x in lengths]
    
    return sqrt(sum([x * x for x in diff]) / n)
    
    
print(variance([10, 12, 10, 11, 10, 11, 12]))