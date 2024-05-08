import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx8 = [0, -1, -1, -1, 0, 1, 1, 1]
dy8 = [-1, -1, 0, 1, 1, 1, 0, -1]

dx4 = [-1, 1, -1, 1]
dy4 = [-1, -1, 1, 1]

cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for _ in range(m):
    d, s = map(int, input().split())
    d -= 1
    # 구름 이동
    move = set()
    for x, y in cloud:
        nx = (x + dx8[d] * s) % n
        ny = (y + dy8[d] * s) % n
        arr[nx][ny] += 1
        move.add((nx, ny))

    # 물복사버그 마법 시전
    for x, y in move:
        cnt = 0
        for i in range(4):
            nx = x + dx4[i]
            ny = y + dy4[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]:
                cnt += 1
        arr[x][y] += cnt

    # 구름 생성
    cloud = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and not (i, j) in move:
                arr[i][j] -= 2
                cloud.append((i, j))

ans = 0
for row in arr:
    ans += sum(row)
print(ans)


