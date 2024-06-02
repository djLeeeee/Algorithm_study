import sys
sys.stdin = open('input.txt')

K = int(input())
W, H = map(int, input().split())
mt = [list(map(int, input().split())) for _ in range(H)]
visited = [[0]*W for _ in range(H)]
di = ((-1, 0), (1, 0), (0, -1), (0, 1))
horse = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
ans = W*H+1
def func(r, c, cnt, h_cnt):
    global ans
    if r == H-1 and c == W-1:
        if cnt < ans:
            ans = cnt
        return

    if h_cnt < K:
        for hr, hc in horse:
            nr, nc = r+hr, c+hc
            if 0 <= nr < H and 0 <= nc < W and mt[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                func(nr, nc, cnt+1, h_cnt+1)
                visited[nr][nc] = 0
    else:
        for dr, dc in di:
            nr, nc = r+dr, c+dc
            if 0 <= nr < H and 0 <= nc < W and mt[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                func(nr, nc, cnt+1, h_cnt)
                visited[nr][nc] = 0


func(0, 0, 0, 0)
if ans == W*H+1:
    print(-1)
else:
    print(ans)