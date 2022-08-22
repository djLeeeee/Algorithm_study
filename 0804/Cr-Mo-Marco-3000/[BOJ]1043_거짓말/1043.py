import sys

input = sys.stdin.readline

# 사람의 수 N, 파티의 수 M

N, M = map(int, input().strip().split())\

true_list = list(map(int, input().strip().split()))
true_length = len(true_list)

p = [i for i in range(N+1)]

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    p[y] = p[find(x)]

for _ in range(M):
    temp = list(map(int, input().strip().split()))
    length = len(temp)
    for i in range(1, length):
        union(temp[1], temp[i])

for j in range(1, N+1):
    find(j)

avoid_set = set()

for k in range(1, true_length):
    avoid_set.add(find(true_list[k]))

ans = N

for l in range(1, N+1):
    if p[l] in avoid_set:
        ans -= 1

print(ans)