import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

direction = {'<': 0, '>': 1, '^': 2, 'v': 3}

T = int(input())
for tc in range(1, T+1):
    r, c = map(int, input().split())
    arr = [input().strip() for _ in range(r)]

    visited = [[[[0] * 16 for _ in range(4)] for _ in range(c)] for _ in range(r)]

    que = deque()
    que.append((0, 0, 1, 0))
    visited[0][0][1][0] = 1

    flag = False
    while que:
        x, y, d, mem = que.popleft()
        cmd = arr[x][y]
        if cmd == '@':
            flag = True
            break

        if cmd in direction:
            d = direction[cmd]
        elif cmd == '_':
            d = 1 if mem == 0 else 0
        elif cmd == '|':
            d = 3 if mem == 0 else 2
        elif cmd == '+':
            mem = (mem + 1) % 16
        elif cmd == '-':
            mem = (mem - 1) % 16
        elif cmd.isdigit():
            mem = int(cmd)

        if cmd == '?':
            directions = range(4)
        else:
            directions = [d]

        for nd in directions:
            nx = (x + dx[nd]) % r
            ny = (y + dy[nd]) % c

            if not visited[nx][ny][nd][mem]:
                visited[nx][ny][nd][mem] = 1
                que.append((nx, ny, nd, mem))

    print(f"#{tc} {'YES' if flag else 'NO'}")




