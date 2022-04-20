a = int(input())
for _ in range(a):
    inp = input()
    lr = 0
    result = 'YES'
    for i in inp:
        if i == '(':
            lr += 1
        else:
            lr -= 1
        if lr < 0:
            break
    if lr != 0:
        result = 'NO'
    print(result)
