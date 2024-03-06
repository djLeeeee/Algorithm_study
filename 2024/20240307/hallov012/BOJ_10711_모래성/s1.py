import sys
sys.stdin = open('input.txt')

"""
8방향 중, 모래성이 없는 부분의 수가 자신의 수보다 많거나 같으면 무너질 수 있음
일단 9는 절대 안무너짐

=> 시간초과
"""

input = sys.stdin.readline

h, w = map(int, input().split())
arr = [[0] * w for _ in range(h)]
send = []

for i in range(h):
    data = input().rstrip()
    for j in range(w):
        if data[j] != '.':
            arr[i][j] = int(data[j])
            if data[j] != '9':
                send.append((i, j))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
ans = 0
while True:
    remain = []
    destroy = []
    for x, y in send:
        cnt = 0
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if not arr[nx][ny]:
                cnt += 1
        if cnt < arr[x][y]:
            remain.append((x, y))
        else:
            destroy.append((x, y))
    if destroy:
        send = remain
        ans += 1

        for x, y in destroy:
            arr[x][y] = 0
    else:
        break

print(ans)

