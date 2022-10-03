from itertools import permutations as ps

N = int(input())
arr = list(map(int, input().split()))
check = list(ps(range(N), N))
ans = 0
for c in check:
    cnt = 0
    for i in range(N-1):
        cnt += abs(arr[c[i]]-arr[c[i+1]])
    ans = max(cnt, ans)
print(ans)