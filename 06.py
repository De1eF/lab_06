import math

def func(x):
    y = (2**x) / (math.fabs(x**2+1)) + math.log(2, math.fabs(math.fabs(x) + 1))
    return y

def parametrizedCycle(a, b, h):
    resultList = list()
    
    for i in range(int(a), int(b), int(h)):
        resultList.append(func(i))
    
    return resultList
        
def conditionalCycle(a, b, h):
    resultList = list()
    
    i = int(a)
    while i < int(b):
        resultList.append(func(i))
        i += int(h)
    
    return resultList

a = input("a: ")
b = input("b: ")
h = input("h: ")

print("\n")

print("parametrizedCycle values:")
for y in parametrizedCycle(a, b, h):
    print(y)

print("\n")

print("conditionalCycle values:")
for y in conditionalCycle(a, b, h):
    print(y)
    
print("\n")
    
print("sorted parametrizedCycle values:")
sortedList = sorted(parametrizedCycle(a, b, h))
for y in sortedList:
    print(y)

print("\n")

print("sorted conditionalCycle values:")
sortedList = sorted(conditionalCycle(a, b, h))
for y in sortedList:
    print(y)
