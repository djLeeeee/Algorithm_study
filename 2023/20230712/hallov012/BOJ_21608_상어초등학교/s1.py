import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
preference = {}
for _ in range(n**2):
    student, *p = map(int, input().split())
    preference[student] = p

arr = [[0] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for s, p in preference.items():
    temp = []
    for i in range(n):
        for j in range(n):
            if not arr[i][j]:
                p_cnt = 0
                empty = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] in p:
                            p_cnt += 1
                        elif not arr[nx][ny]:
                            empty += 1
                temp.append([-p_cnt, -empty, i, j])
    # 좋아하는 친구가 많을수록 => 빈 자리가 많을수록 => 행이 작을수록 => 열이 작을 수록
    temp.sort()
    x, y = temp[0][2], temp[0][3]
    arr[x][y] = s

ans = 0
for i in range(n):
    for j in range(n):
        s = arr[i][j]
        p_cnt = 0
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] in preference[s]:
                    p_cnt += 1
        if p_cnt:
            ans += 10 ** (p_cnt-1)

print(ans)
