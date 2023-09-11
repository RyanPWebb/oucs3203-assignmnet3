import math

def listSum(list: int):
    return sum(list)

def listProd(list: int):
    prod = 1
    for i in range(0,len(list)):
        prod *= list[i]

    return prod

