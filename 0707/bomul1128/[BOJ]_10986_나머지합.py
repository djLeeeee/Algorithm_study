n, m = map(int, input().split())
status = [0] * m
status[0] = 1
ans = 0
total = 0
for num in map(int, input().split()):
    total += num
    total %= m
    ans += status[total]
    status[total] += 1
print(ans)
