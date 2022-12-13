sumofmultipe = []
a = 3
while a < 20:
    if a % 3 == 0:
        sumofmultipe.append(a)
    elif a & 5 == 0:
        sumofmultipe.append(a)
    a = a + 3
print (sumofmultipe)
sums = 0
for i in sumofmultipe:
    sums = sums + i
print (sums)