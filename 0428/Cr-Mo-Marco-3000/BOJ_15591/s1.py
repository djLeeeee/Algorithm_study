from sys import stdin

def do(k, v):
    key = [1000000001] * (N + 1)
    key[v] = 0
    visited = [0] * (N+1)
    for _ in range(N):
        min_idx = -1
        min_v = 1000000001
        for i in range(1, N+1):
            if not visited[i] and key[i] < min_v:
                min_idx = i
                min_v = key[i]
        visited[min_idx] = 1
        for w in range(1, N+1):
            if not visited[w] and g[min_idx][w] < key[w]:
                key[w] = g[min_idx][w]
                for e in range(1, N+1):
                    if g[w][e] != 1000000001 and g[w][e] > key[w]:
                        g[w][e] = key[w]

    cnt = 0
    for a in range(1, N+1):
        if key[a] >= k:
            cnt += 1
    return cnt


N, Q = map(int, stdin.readline().rstrip().split())
g = [[1000000001] * (N+1) for _ in range(N+1)]

for _ in range(N-1):
    p, q, r = map(int, stdin.readline().rstrip().split())
    g[p][q] = r
    g[q][p] = r



for _ in range(Q):
    k, v = map(int, stdin.readline().rstrip().split())
    print(do(k, v))
