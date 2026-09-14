import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

def count_empt(x, y):
    cnt = 0
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        cnt += 1 if arr[nx][ny] == 0 else 0
    return cnt

T = int(input())
for tc in range(1, T+1):
    h, w = map(int, input().split())
    arr = []
    for _ in range(h):
        row = input().strip()
        arr.append([0 if c == '.' else int(c) for c in row])

    empt = [[0] * w for _ in range(h)]
    que = deque()
    for i in range(1, h-1):
        for j in range(1, w-1):
            if not arr[i][j]:
                continue
            empt_cnt = count_empt(i, j)
            empt[i][j] = empt_cnt
            if empt_cnt >= arr[i][j]:
                que.append((i, j))

    ans = 0
    while que:
        que_len = len(que)
        for _ in range(que_len):
            x, y = que.popleft()
            arr[x][y] = 0

            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < h and 0 <= ny < w:
                    if arr[nx][ny]:
                        empt[nx][ny] += 1
                        if empt[nx][ny] == arr[nx][ny]:
                            que.append((nx, ny))
        ans += 1

    print(f"#{tc} {ans}")



