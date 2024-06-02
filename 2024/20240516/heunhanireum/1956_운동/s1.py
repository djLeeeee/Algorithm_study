import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
ans = sys.maxsize
mt = [[ans]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    mt[a][b] = c

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            if mt[i][j] > mt[i][k]+mt[k][j]:
                mt[i][j] = mt[i][k]+mt[k][j]

for i in range(1, V+1):
    ans = min(ans, mt[i][i])

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)