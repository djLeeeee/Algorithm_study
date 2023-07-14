import sys
sys.stdin = open('input.txt')

def check():
    global ans
    # 행 검사
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
        ans = max(ans, cnt)
    # 열 검사
    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if arr[i][j] == arr[i-1][j]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
        ans = max(ans, cnt)

input = sys.stdin.readline

n = int(input())
arr = [list(input()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        for dx, dy in [(0, 1), (1, 0)]:
            nx = i + dx
            ny = j + dy
            if 0 <= nx < n and 0 <= ny < n:
                arr[i][j], arr[nx][ny] = arr[nx][ny], arr[i][j]
                check()
                arr[i][j], arr[nx][ny] = arr[nx][ny], arr[i][j]

print(ans)

