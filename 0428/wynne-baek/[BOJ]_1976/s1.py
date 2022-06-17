import sys
sys.stdin = open('input.txt')

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y :
        represent[y] = x
    else:
        represent[x] = y

def find(x):
    if x != represent[x]:
        represent[x] = find(represent[x])
    return represent[x]

N = int(input())
M = int(input())
represent = [_ for _ in range(N)]

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j]:
            union(i, j)

journey = tuple(map(int, input().split()))
start = represent[journey[0]-1]
for idx in range(1, M):
    if represent[journey[idx]-1] != start:
        print('NO')
        # 오타는 항상 주의하자!
        break
else:
    print('YES')