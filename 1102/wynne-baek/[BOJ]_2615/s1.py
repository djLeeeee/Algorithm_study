import sys
sys.stdin = open('input.txt')

board = []
for i in range(19):
    line = list(map(int, input().split()))
    board.append(line)

dx = [1, 0, 1, -1]
dy = [1, 1, 0, 1]

for i in range(19):
    for j in range(19):
        if board[i][j]:
            num = board[i][j]
            for idx in range(4):
                cnt = 1
                nx = i + dx[idx]
                ny = j + dy[idx]

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == num:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= i - dx[idx] < 19 and 0 <= j - dy[idx] < 19 and board[i - dx[idx]][j - dy[idx]] == num:
                            break
                        if 0 <= nx + dx[idx] < 19 and 0 <= ny + dy[idx] < 19 and board[nx + dx[idx]][ny + dy[idx]] == num:
                            break
                        print(num)
                        print(i + 1, j + 1)
                        sys.exit()

                    nx += dx[idx]
                    ny += dy[idx]
print(0)


