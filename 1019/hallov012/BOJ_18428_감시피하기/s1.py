import sys
sys.stdin = open('input.txt')

def find():
    visited = [[0] * n for _ in range(n)]
    for x, y in teachers:
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 'O':
                visited[nx][ny] = 1
                nx += dx[i]
                ny += dy[i]
    flag = True
    for x, y in students:
        if visited[x][y]:
            flag = False
            break
    return flag

def dfs(cnt):
    global ans
    if cnt == 3:
        flag = find()
        if flag:
            ans = 'YES'
        return
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                dfs(cnt+1)
                arr[i][j] = 'X'

input = sys.stdin.readline

n = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
students = []
teachers = []
arr = []
ans = 'NO'
for i in range(n):
    row = list(map(str, input().split()))
    arr.append(row)
    for j in range(n):
        if arr[i][j] == 'S':
            students.append((i, j))
        elif arr[i][j] == 'T':
            teachers.append((i, j))
dfs(0)
print(ans)
