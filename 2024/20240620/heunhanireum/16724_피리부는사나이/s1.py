import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
mt = [list(input()) for _ in range(N)]
di = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
visited = [[0]*M for _ in range(N)]
cnt = 1

def dfs(r, c):
    global N, M, cnt
    visited[r][c] = cnt
    dr, dc = di[mt[r][c]]
    nr, nc = r+dr, c+dc
    if 0 <= nr < N and 0 <= nc < M:
        if visited[nr][nc] != 0:
            if visited[nr][nc] != cnt:
                for resr, resc in result:
                    visited[resr][resc] = visited[nr][nc]
            else:
                cnt += 1
            return
        else:
            result.append((nr, nc))
            dfs(nr, nc)

for r in range(N):
    for c in range(M):
        if visited[r][c] == 0:
            result = [(r, c)]
            dfs(r, c)

print(cnt-1)