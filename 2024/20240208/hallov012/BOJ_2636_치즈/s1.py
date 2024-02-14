import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt_dict = defaultdict(int)

board = [[-1] * m for _ in range(n)]
board[0][0] = 0
que = []
heapq.heappush(que, (0, 0, 0))
while que:
    cnt, x, y = heapq.heappop(que)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == -1:
                if arr[nx][ny]:
                    board[nx][ny] = cnt+1
                    heapq.heappush(que, (cnt+1, nx, ny))
                    cnt_dict[cnt+1] += 1
                else:
                    board[nx][ny] = cnt
                    heapq.heappush(que, (cnt, nx, ny))

max_cnt = max(cnt_dict.keys())
print(max_cnt)
print(cnt_dict[max_cnt])





