import sys, pprint

input = sys.stdin.readline

R, C, N = map(int, input().strip().split())

g = []

for i in range(R):
    temp = list(map(str, input().strip()))
    for j in range(C):
        if temp[j] == 'O':
            temp[j] = 0
        else:
            temp[j] = -1
    g.append(temp)

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

for tc in range(0, N):
    # 폭탄 설치 단계
    if tc % 2:
        for i in range(R):
            for j in range(C):
                if g[i][j] == -1:
                    g[i][j] = tc
    else:
        stack = []
        for i in range(R):
            for j in range(C):
                if g[i][j] >= 0 and g[i][j] <= tc-2:
                    stack.append((i, j))
                    for w in range(4):
                        nr = i + dr[w]
                        nc = j + dc[w]
                        if 0 <= nr < R and 0 <= nc < C:
                            stack.append((nr, nc))
        while stack:
            r, c = stack.pop()
            g[r][c] = -1

for i in range(R):
    for j in range(C):
        if g[i][j] == -1:
            print('.', end='')
        else:
            print('O', end='')
    print()

