n = 10000
nums = range(1, n+1)
nums_cnt = [0] * (n+1)
for i in range(1, n+1):
    num = i
    while 1:
        num += i % 10
        i = i // 10
        if num > n:
            break
        if not i:
            nums_cnt[num] += 1
            break

for i in range(1, n+1):
    if not nums_cnt[i]:
        print(i)