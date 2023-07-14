# 방의 개수
# 가장 넓은 방의 너비
# 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
# 이진수로 해결하기
# dfs

def move(x, y):
    binary = format(arr[x][y], 'b')
    binary = '0'*(4-len(binary)) + binary
    for k in range(4):
        nx, ny = x+di[k][0], y+di[k][1]
        if binary[k] == '0' and not visited[nx][ny]:
            visited[nx][ny] = len(room) - 1
            room[-1] += 1
            move(nx, ny)

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
room = [0]
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            room.append(1)
            visited[i][j] = len(room) - 1
            move(i, j)
wall = 0
for i in range(M):
    for j in range(N):
        for d in di:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < M and 0 <= nj < N and visited[i][j] != visited[ni][nj] and room[visited[i][j]] + room[visited[ni][nj]] > wall:
                wall = room[visited[i][j]] + room[visited[ni][nj]]
print(len(room)-1)
print(max(room))
print(wall)
