from collections import deque
import sys
sys.stdin = open('input.txt')
di = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
      (1, -1), (1, 0), (1, 1))
N, M = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = 0

def is_bwr(R, C):
    bwr = farm[R][C]
    flag = True
    queue = deque([(R, C)])
    while queue:
        r, c = queue.popleft()
        for dr, dc in di:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M:
                if farm[nr][nc] == bwr and visited[nr][nc] == 0:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
                elif farm[nr][nc] > bwr:
                   flag = False
    return flag


for r in range(N):
    for c in range(M):
        if visited[r][c] == 0:
            visited[r][c] = 1
            if is_bwr(r, c):
                ans += 1

print(ans)