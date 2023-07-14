# 백준 11559번 Puyo Puyo

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
def puyoPop():
    visited = [[0] * 6 for _ in range(12)]
    for key, value in spot.items():
        color = key
        if value:
            queue = [(value[0][0], value[0][1], 1)]
            visited[value[0][0]][value[0][1]] = 1

            while queue:
                cr, cc, cnt = queue.pop(0)
                if cnt >= 4:
                    field[cr][cc] = '.'
                for d in range(4):
                    nr, nc = cr + dr[d], cc + dc[d]
                    if 0 <= nr < 12 and 0 <= nc < 6 and field[nr][nc] == color and not visited[nr][nc]:
                        queue.append((nr, nc, cnt + 1))
                        visited[nr][nc] = visited[cr][cc] + 1

    print(field)


def puyoDown():
    for c in range(6):
        if field[11][c] == '.':
            pass


field = []
top = 12
spot = {'R': [], 'G': [], 'B': [], 'P': [], 'Y': []}
# spot = []
for r in range(12):
    data = list(input().rstrip())
    if data.count('.') != 6:
        for c in range(6):
            # if data[c] != '.':
            #     spot.append((r, c))
            if data[c] == 'R':
                spot['R'].append((r, c))
            elif data[c] == 'G':
                spot['G'].append((r, c))
            elif data[c] == 'B':
                spot['B'].append((r, c))
            elif data[c] == 'P':
                spot['P'].append((r, c))
            elif data[c] == 'Y':
                spot['Y'].append((r, c))
        if top > r:
            top = r
    field.append(data)
puyoPop()

