my_set = set()
for i in range(10000, 0, -1):
    for j in range(i-1, -1, -1):
        copy = j
        a = copy // 10000
        b = (copy % 10000) // 1000
        c = ((copy % 10000) % 1000) // 100
        d = (((copy % 10000) % 1000) % 100) // 10
        e = (((copy % 10000) % 1000) % 100) % 10
        if i == j + a + b + c + d + e:
           break
    else:
        my_set.add(i)
my_list = list(my_set)
my_list.sort()
for k in my_list:
    print(k)
