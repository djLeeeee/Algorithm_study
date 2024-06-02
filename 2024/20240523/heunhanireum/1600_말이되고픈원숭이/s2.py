from collections import deque
import sys
sys.stdin = open('input.txt')

K = int(input())
W, H = map(int, input().split())
mt = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0]*(K+1) for _ in range(W)] for __ in range(H)]
di = ((-1, 0), (1, 0), (0, -1), (0, 1))
horse = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
queue = deque()
ans = -1
visited[0][0][0] = 1

def bfs():
    global ans
    while queue:
        r, c, k_cnt = queue.popleft()
        if r == H-1 and c == W-1:
            ans = visited[r][c][k_cnt] -1
            return

        if k_cnt < K:
            for dr, dc in horse:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and visited[nr][nc][k_cnt+1] == 0 and mt[nr][nc] == 0:
                    visited[nr][nc][k_cnt+1] = visited[r][c][k_cnt]+1
                    queue.append((nr, nc, k_cnt+1))

        for dr, dc in di:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and visited[nr][nc][k_cnt] == 0 and mt[nr][nc] == 0:
                visited[nr][nc][k_cnt] = visited[r][c][k_cnt]+1
                # print(nr, nc)
                queue.append((nr, nc, k_cnt))

queue.append((0, 0, 0))

bfs()
print(ans)