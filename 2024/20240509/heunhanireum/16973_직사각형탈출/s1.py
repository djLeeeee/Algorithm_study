from collections import deque
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
mt = [list(map(int, input().split())) for _ in range(N)]
H, W, sr, sc, fr, fc = map(int, input().split())

visited = [[0]*M for _ in range(N)]
di = ((-1, 0), (1, 0), (0, -1), (0, 1))
queue = deque([(sr-1, sc-1)])
visited[sr-1][sc-1] = 1
walls = []

for r in range(N):
    for c in range(M):
        if mt[r][c] == 1:
            walls.append((r, c))


def is_valid(min_r, min_c):
    max_r, max_c = min_r+H-1, min_c+W-1
    if 0 <= max_r < N and 0 <= max_c < M:
        for wr, wc in walls:
            if min_r <= wr <= max_r and min_c <= wc <= max_c:
                return False
        return True


while queue:
    r, c = queue.popleft()
    if r == fr-1 and c == fc-1:
        print(visited[r][c]-1)
        break
    for dr, dc in di:
        nr, nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and is_valid(nr, nc):
            queue.append((nr, nc))
            visited[nr][nc] = visited[r][c]+1
else:
    print(-1)

