import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
moves = [tuple(map(int, input().split())) for _ in range(m)]
c_arr = [[0] * n for _ in range(n)]

dx8 = (0, -1, -1, -1, 0, 1, 1, 1)
dy8 = (-1, -1, 0, 1, 1, 1, 0, -1)

dy4 = (-1, -1,  1, 1)
dx4 = (-1,  1, -1, 1)

clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for i in range(1, m+1):
    d, s = moves[i-1]
    d -= 1

    moved_cloud = set()
    for x, y in clouds:
        nx = (x + dx8[d] * s) % n
        ny = (y + dy8[d] * s) % n
        arr[nx][ny] += 1
        c_arr[nx][ny] = i
        moved_cloud.add((nx, ny))

    for x, y in moved_cloud:
        cnt = 0
        for k in range(4):
            nx = x + dx4[k]
            ny = y + dy4[k]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]:
                cnt += 1
        arr[x][y] += cnt

    clouds = []
    for a in range(n):
        for b in range(n):
            if arr[a][b] >= 2 and c_arr[a][b] != i:
                arr[a][b] -= 2
                clouds.append((a, b))

ans = 0
for row in arr:
    ans += sum(row)

print(ans)

