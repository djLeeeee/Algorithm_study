import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    p[find(y)] = find(x)

input = sys.stdin.readline

n, m, k = map(int, input().split())
money = list(map(int, input().split()))
p = list(range(n+1))
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)   # union, find를 이용해 친구관계에 았는 사람끼리 묶음
friend = [[] for _ in range(n+1)]
for i in range(1, n+1):  # 같은 부모를 가진 사람들의 친구비를 list로 저장
    friend[find(i)].append(money[i-1])

ans = 0
for group in friend:
    if group:
        ans += min(group)  # group 중 한명에게만 친구비를 지급하면 되는 것이므로 가장 친구비가 낮은 사람에게 지급

if ans <= k:
    print(ans)
else:
    print('Oh no')

