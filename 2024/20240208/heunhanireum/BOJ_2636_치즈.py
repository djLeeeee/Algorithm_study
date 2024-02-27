from collections import deque
import sys
sys.stdin = open('input.txt')

H, W = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(H)]
di = ((-1, 0), (1, 0), (0, -1), (0, 1))
ans = []
def bfs():
    cnt = 0
    while queue:
        r, c = queue.popleft()
        for dr, dc in di:
            nr, nc = r+dr, c+dc
            if 0 <= nr < H and 0 <= nc < W and visited[nr][nc] == 0:
                if cheese[nr][nc] == 0:
                    queue.append((nr, nc))
                else:
                    cheese[nr][nc] = 0
                    cnt += 1
                visited[nr][nc] = 1
    return cnt


while True:
    visited = [[0]*W for _ in range(H)]
    queue = deque([(0, 0)])
    res = bfs()
    if res > 0:
        ans.append(res)
    else:
        break

print(len(ans))
print(ans[-1])