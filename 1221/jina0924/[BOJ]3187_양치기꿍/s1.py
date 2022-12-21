# 백준 3187번 양치기 꿍

import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
def bfs(r, c):
    queue = [(r, c)]
    wolf, sheep = 0, 0
    if data[r][c] == 'v':                               # 해당 울타리 안에 있는 늑대와 양의 수를 셈
        wolf += 1
    elif data[r][c] == 'k':
        sheep += 1
    data[r][c] = '#'                                    # 살펴본 위치의 값은 '#'으로 채워넣음(다시 보지 않기 위해)

    while queue:
        cr, cc = queue.pop(0)
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < R and 0 <= nc < C and data[nr][nc] != '#':
                queue.append((nr, nc))
                if data[nr][nc] == 'v':
                    wolf += 1
                elif data[nr][nc] == 'k':
                    sheep += 1
                data[nr][nc] = '#'
    return wolf, sheep


R, C = map(int, input().split())                        # R, C: 영역의 세로, 가로
data = [list(input().rstrip()) for _ in range(R)]
total_v, total_k = 0, 0                                 # total_v, total_k: 살아남은 늑대, 양의 수
for r in range(R):
    for c in range(C):
        if data[r][c] == 'k' or data[r][c] == 'v':      # 울타리 안에서 양이나 늑대를 발견한다면
            v, k = bfs(r, c)                            # bfs로 울타리 탐색
            if k > v:                                   # 남은 개수가 많은 쪽만 살아남음
                total_k += k
            else:
                total_v += v
print(total_k, total_v)