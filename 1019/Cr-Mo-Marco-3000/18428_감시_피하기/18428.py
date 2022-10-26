import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input().strip())

students = []
teachers = []

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

g = []
for i in range(N):
    temp = list(input().strip().split())
    for j in range(N):
        if temp[j] == 'S':
            students.append((i, j))
        elif temp[j] == 'T':
            teachers.append((i, j))
    g.append(temp)

visited = [[0] * N for _ in range(N)]
cross_point = []

# 교차점 구하기
for k in teachers:
    r, c = k
    for w in range(4):
        cross_stack = []
        nr = r + dr[w]
        nc = c + dc[w]
        while 0 <= nr < N and 0 <= nc < N:
            if g[nr][nc] == 'X' and not visited[nr][nc]:
                cross_stack.append(((nr, nc)))
            elif g[nr][nc] == 'S':
                while cross_stack:
                    point = cross_stack.pop()
                    visited[point[0]][point[1]] = 1
                    cross_point.append(point)
                break
            elif g[nr][nc] == 'T':
                while cross_stack:
                    point = cross_stack.pop()
                break
            nr += dr[w]
            nc += dc[w]

def do():
    # 선생에서부터 뽑아 돌리기
    for k in teachers:
        r, c = k
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            while 0 <= nr < N and 0 <= nc < N:
                if g[nr][nc] == 'O' or g[nr][nc] == 'T':
                    break
                elif g[nr][nc] == 'S':
                    return 'NO'
                nr += dr[w]
                nc += dc[w]
    else:
        return 'YES'

# 교차점 중 3개 뽑기
comb = combinations(cross_point, 3)
if len(cross_point) >= 3:
    for l in comb:
        # 3 지점 잡기
        for m in l:
            i, j = m
            g[i][j] = 'O'
        ans = do()
        if ans == 'YES':
            print('YES')
            break
        for m in l:
            i, j = m
            g[i][j] = 'X'
    else:
        print('NO')
else:
    print('NO')