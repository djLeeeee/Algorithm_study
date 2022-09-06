# 분리 집합
# find and union
import sys
input = sys.stdin.readline

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
parties = [list(map(int, input().split())) for _ in range(M)]
p = [0] + list(range(1, N+1))
ans = M
if len(arr) == 1 and not arr[0]:
    print(ans)
else:
    arr = arr[1::]
    for party in parties:
        minus = False
        num = False
        for i in range(1, party[0]+1):
            if party[i] in arr:
                for j in range(1, party[0]+1):
                    if p[party[j]] not in arr:
                        union(party[i], party[j])
    for party in parties:
        for i in range(1, party[0]+1):
            if p[party[i]] in arr:
                ans -= 1
                break
    print(ans)
