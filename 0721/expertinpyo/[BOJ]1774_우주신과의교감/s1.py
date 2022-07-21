# 우주신과의 교감
# kruskal로 접근

def kruskal(x):
    ans = 0.0
    for i in range(len(distance)):
        if x == N-1:
            return ans
        a, b, dis = distance[i]
        if find_set(a) != find_set(b):
            union(a, b)
            ans += dis
            x += 1

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

N, M = map(int, input().split())
arr = [0]
p = list(range(N+1))
distance = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
cnt = 0
for _ in range(M):
    a, b = map(int, input().split())
    if find_set(a) != find_set(b):
        union(a, b)
        cnt += 1
for i in range(1, N+1):
    for j in range(i+1, N+1):
        distance.append((i, j, ((arr[i][0]-arr[j][0])**2 + (arr[i][1]-arr[j][1])**2)**0.5))
distance.sort(key=lambda x:x[2])
if cnt < N-1:
    print('%.2f' % kruskal(cnt))
else:
    print('%.2f' % 0)