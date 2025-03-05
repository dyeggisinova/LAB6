import math

list1 =[]
n = int(input("the amount of the n umbers in the list?"))

for i in range(n):
    i = int(input("The number:"))
    list1.append(i)
result = math.prod(list1)
print(result)