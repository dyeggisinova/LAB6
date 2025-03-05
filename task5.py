import random

def x(num):
    return True if num > 0 else False

n = int(input("Kol-vo elem: "))
tuple1 = tuple(x(random.randint(-100,100)) for i in range(n))
k = all(tuple1)

for i in tuple1:
    print(i, end=" ")
print()
print(k)