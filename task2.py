n = input()
bigl =0
smalll=0

for i in range(len(n)):
    if n[i].isupper():
        bigl +=1
    else:
        smalll +=1

print("BIGs: ", bigl)
print("SMALLs: ", smalll)