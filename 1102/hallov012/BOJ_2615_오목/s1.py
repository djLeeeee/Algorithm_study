import sys
sys.stdin = open('input.txt')

def check(x, y, d):
    temp = arr[x][y]
    visited[x][y] = temp
    cnt = 1
    nx = x + dx[d]
    ny = y + dy[d]
    while 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == temp:
        visited[nx][ny] = temp
        cnt += 1
        nx += dx[d]
        ny += dy[d]
    if cnt == 5:
        return True
    return False


input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(19)]
# 오른쪽, 아래, (우하향)대각선, (우상향)대각선
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]
ans = []
for d in range(4):
    visited = [[0] * 19 for _ in range(19)]
    if d != 3:
        for x in range(19):
            for y in range(19):
                if arr[x][y] and not visited[x][y]:
                    if check(x, y, d):
                        ans.append((arr[x][y], x, y))
    else:
        for x in range(18, -1, -1):
            for y in range(19):
                if arr[x][y] and not visited[x][y]:
                    if check(x, y, d):
                        ans.append((arr[x][y], x, y))

if len(ans) == 1:
    win, x, y = ans[0]
    print(win)
    print(x+1, y+1)
else:
    print(0)


