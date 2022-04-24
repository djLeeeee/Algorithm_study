from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    arr = input().strip()
    lr = 0
    result = 'YES'
    for i in arr:
        if i == '(':
            lr += 1
        else:
            lr -= 1
            if lr < 0:
                break
    if lr:
        result = 'NO'
    print(result)
