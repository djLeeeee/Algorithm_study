from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
ans = 0
for p in permutations(arr):
    temp = 0
    for i in range(1, n):
        temp += abs(p[i] - p[i - 1])
        if temp > ans:
            ans = temp
print(ans)
