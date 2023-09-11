import math

def listSum(list: int):
    return sum(list)

def listProd(list: int):
    prod = 1
    for i in range(0,len(list)):
        prod *= list[i]

    return prod

inString = input("Input a comma separated list of numbers:")
stringList = inString.split(',')
nums = [int(x) for x in stringList]

print("Sum: {}".f, listSum(nums))
print("Product: {}".f, listProd(nums))