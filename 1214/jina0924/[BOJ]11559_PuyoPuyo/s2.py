# 백준 11559번 Puyo Puyo

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
def puyoPop():
    visited = [[0] * 6 for _ in range(12)]
    combo = 0                               # 이번에 연쇄가 일어났는지 알려줄 변수

    for puyo in spot:
        queue = [puyo]
        color = field[puyo[0]][puyo[1]]
        isPop = False                       # 큐를 순회할 때 연쇄작용이 있었는지 판별할 변수
        temp = []                           # 연쇄 여부와 상관없이 임시로 뿌요 위치값을 담아둘 리스트
        visited[puyo[0]][puyo[1]] = 1
        cnt = 0                             # 모여있는 뿌요 개수

        while queue:
            cr, cc = queue.pop(0)
            temp.append((cr, cc))
            cnt += 1
            if cnt >= 4:                    # 뿌요가 4개 이상 모여있으면 => 터짐
                isPop = True
            for d in range(4):
                nr, nc = cr + dr[d], cc + dc[d]
                if 0 <= nr < 12 and 0 <= nc < 6 and field[nr][nc] == color and not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1

        if isPop:                           # 이번에 뿌요가 터졌다면
            combo = 1                       # 1연쇄 시작
            for t in temp:                  # temp에 저장해둔 뿌요 위치를 순회하면서 터진 뿌요 자리 '.'으로 채움
                field[t[0]][t[1]] = '.'
    return combo


def puyoDown():
    new_spot = []

    for c in range(6):                          # 세로 기준으로 살펴봄
        queue = []
        for r in range(11, top-1, -1):          # 아래에서 위로 살펴봄
            if field[r][c] != '.':
                queue.append(field[r][c])       # 뿌요가 있다면 큐에 저장해둠
        for r in range(11, top-1, -1):          # 다시 아래에서 위로 살펴보면서
            if queue:                           # 저장한 뿌요가 있다면 아래쪽부터 채워넣음
                field[r][c] = queue.pop(0)
                new_spot.append((r, c))
            else:                               # 저장된 뿌요가 없다면 해당 공간을 빈 값으로 저장
                field[r][c] = '.'
    return new_spot


field = []
top = 12
spot = []                                       # 뿌요들의 위치값 저장할 리스트
for r in range(12):
    data = list(input().rstrip())
    if data.count('.') != 6:
        for c in range(6):
            if data[c] != '.':
                spot.append((r, c))
        if top > r:                             # 비어있는 공간 탐색하지 않기 위해 제일 위에 있는 뿌요의 r값 저장
            top = r
    field.append(data)

result = 0
while True:
    if puyoPop():                               # 뿌요가 터졌다면
        spot = puyoDown()                       # 아래 빈 공간으로 내리고 새 뿌요 위치 저장
        result += 1                             # 연쇄 + 1
    else:
        print(result)
        break
