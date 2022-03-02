
lst = []
for i in range(1, 10000):
    num = str(i)
    nself = i
    for n in num:
        nself += int(n)
    if nself not in lst and nself <= 10000:
        lst.append(nself)

for k in range(1, 10000):
    if k not in lst:
        print(k)
