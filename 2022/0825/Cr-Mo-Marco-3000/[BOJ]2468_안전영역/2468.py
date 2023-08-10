import sys, collections

input = sys.stdin.readline

N = int(input().strip())

g = []

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

flood = [[] for _ in range(101)]

visited = [[0] * N for _ in range(N)]

# 정답 초기화
ans = 1

for i in range(N):
    temp = list(map(int, input().strip().split()))
    for j in range(N):
        flood[temp[j]].append((i, j))
    g.append(temp)

for tc in range(len(flood)):
    grid = flood[tc]
    if grid:
        while grid:
            r, c = grid.pop()
            g[r][c] = -1
        temp = 1
        for i in range(N):
            for j in range(N):
                # tc는 현재 검사하고 있는 높이
                if visited[i][j] != tc and g[i][j] != -1:
                    temp += 1
                    visited[i][j] = tc
                    Q = collections.deque([(i, j)])
                    while Q:
                        r, c = Q.popleft()
                        for w in range(4):
                            nr = r + dr[w]
                            nc = c + dc[w]
                            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] != tc and g[nr][nc] != -1:
                                visited[nr][nc] = tc
                                Q.append((nr, nc))
        if temp > ans:
            ans = temp
if ans == 1:
    print(1)
else:
    print(ans-1)
