import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input().strip())

teachers = []
blank = []

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

g = []
for i in range(N):
    temp = list(input().strip().split())
    for j in range(N):
        if temp[j] == 'T':
            teachers.append((i, j))
        elif temp[j] == 'X':
            blank.append((i,j))
    g.append(temp)

comb = combinations(blank, 3)

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