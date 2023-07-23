import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

q_data = list(map(int, input().split()))
q_num = q_data[0]
q_lst = []
for i in range(1, len(q_data), 2):
    x, y = q_data[i]-1, q_data[i+1]-1
    q_lst.append((x, y))
    arr[x][y] = 1

k_data = list(map(int, input().split()))
k_num = k_data[0]
k_lst = []
for i in range(1, len(k_data), 2):
    x, y = k_data[i]-1, k_data[i+1]-1
    k_lst.append((x, y))
    arr[x][y] = 1

p_data = list(map(int, input().split()))
p_num = p_data[0]
p_lst = []
for i in range(1, len(p_data), 2):
    x, y = p_data[i]-1, p_data[i+1]-1
    p_lst.append((x, y))
    arr[x][y] = 1

# queen 이동
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for x, y in q_lst:
    for d in range(8):
        nx, ny = x, y
        while 0 <= nx + dx[d] < n and 0 <= ny + dy[d] < m:
            if arr[nx + dx[d]][ny + dy[d]] == 1:
                break
            else:
                arr[nx + dx[d]][ny + dy[d]] = 2
                nx += dx[d]
                ny += dy[d]

# knight 이동
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
for x, y in k_lst:
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if not arr[nx][ny]:
                arr[nx][ny] = 2

ans = 0
for line in arr:
    ans += line.count(0)

print(ans)




