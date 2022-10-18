import sys
sys.stdin = open('input.txt')

def count():
    # 터지는 폭탄들을 담아두고 나중에 한번에 처리
    boom = []
    for i in range(r):
        for j in range(c):
            if timer[i][j] != -1:
                timer[i][j] -= 1
                if not timer[i][j]:
                    boom.append((i, j))
    for x, y in boom:
        for d in range(5):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                timer[nx][ny] = -1
                arr[nx][ny] = '.'

# 빈 곳에 폭탄 심기
def plant():
    for i in range(r):
        for j in range(c):
            if timer[i][j] == -1:
                timer[i][j] = 3
                arr[i][j] = 'O'

input = sys.stdin.readline

r, c, n = map(int, input().split())
timer = [[-1] * c for _ in range(r)]
arr = []
for i in range(r):
    line = list(input().rstrip())
    arr.append(line)
    for j in range(c):
        if line[j] == 'O':
            timer[i][j] = 2
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
t = 1
while t < n:
    count()
    if t % 2:
        plant()
    t += 1
for row in arr:
    print("".join(row))