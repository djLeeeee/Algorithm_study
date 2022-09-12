a, b = map(int, input().split())
board = [[0] * b for _ in range(a)]
n, m = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
di = {'E': 0, 'W': 2, 'N': 1, 'S': 3}
direction = [0] * (n + 1)
position = [0] * (n + 1)
for i in range(1, n + 1):
    x, y, d = input().split()
    x = int(x) - 1
    y = int(y) - 1
    d = di[d]
    board[x][y] = i
    position[i] = (x, y)
    direction[i] = d
ans = 'OK'
orders = [input().split() for _ in range(m)]
for i, o, v in orders:
    i = int(i)
    v = int(v)
    if o == 'L':
        direction[i] += v
        direction[i] %= 4
    elif o == 'R':
        direction[i] -= v
        direction[i] %= 4
    else:
        flag = True
        x, y = position[i]
        board[x][y] = 0
        d = direction[i]
        for _ in range(v):
            x += dx[d]
            y += dy[d]
            if 0 <= x < a and 0 <= y < b:
                if board[x][y]:
                    flag = False
                    ans = f'Robot {i} crashes into robot {board[x][y]}'
                    break
            else:
                flag = False
                ans = f'Robot {i} crashes into the wall'
                break
        if flag:
            board[x][y] = i
            position[i] = (x, y)
        else:
            break
print(ans)
