# 6987번 월드컵

import sys
sys.stdin = open('input.txt')
from itertools import combinations


def check(i):
    global result

    # 6개 팀이 총 15경기 마쳤다면 결과 확인
    if i >= 15:
        # 아직 살펴보지 않은 경기가 있다면 불가능한 결과
        for row in data:
            if sum(row):
                result = 0
                return
        else:
            result = 1
        return

    # 현재 살펴볼 경기
    a, b = match[i]
    # x: a팀의 승무패 -> 살펴볼 수 있는 경기가 있으면 다음 경기 go, 없으면 return
    for x, y in (0, 2), (1, 1), (2, 0):
        if data[a][x] and data[b][y]:
            data[a][x] -= 1
            data[b][y] -= 1
            check(i + 1)
            data[a][x] += 1
            data[b][y] += 1


# 경기 매치 순서
match = list(combinations(range(0, 6), 2))
for _ in range(4):
    data = []
    tmp = list(map(int, input().split()))
    # a팀의 [승, 무, 패] 수 저장
    for i in range(0, 18, 3):
        data.append([tmp[i], tmp[i + 1], tmp[i + 2]])
    result = 0
    check(0)
    print(result, end=' ')