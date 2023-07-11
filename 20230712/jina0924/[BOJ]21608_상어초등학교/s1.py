# 백준 21608번 상어 초등학교

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def find(s):
    maxCnt = [0, 0]                             # 0번: max(좋아하는 학생수), 1번: 0번 동일할 때 max(빈자리수)
    tmp = deque([])                             # 현재 학생이 앉을 수 있는 자리 담을 공간
    for r in range(N):
        for c in range(N):
            friend, empty = 0, 0
            if classroom[r][c] == 0:
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        if classroom[nr][nc] in data[s]:
                            friend += 1
                        elif classroom[nr][nc] == 0:
                            empty += 1
                if friend > maxCnt[0]:
                    maxCnt = [friend, empty]
                    tmp.appendleft((r, c))
                elif friend == maxCnt[0] and empty > maxCnt[1]:
                    tmp.appendleft((r, c))
                    maxCnt[1] = empty
                else:
                    tmp.append((r, c))

    rr, cc = tmp.popleft()
    classroom[rr][cc] = s
    if maxCnt[0] > 0:                           # 좋아하는 학생 수 0, 1, 2, 3, 4 => 만족도 0, 1, 10, 100, 1000
        score[rr][cc] = 10 ** (maxCnt[0] - 1)
    for d in range(4):                          # 상하좌우에 앉은 학생이 현재학생(s) 좋아하는지 살펴보기
        nr, nc = rr + dr[d], cc + dc[d]
        if 0 <= nr < N and 0 <= nc < N and classroom[nr][nc] and s in data[classroom[nr][nc]]:
            if score[nr][nc] > 0:
                score[nr][nc] *= 10
            else:
                score[nr][nc] = 1


N = int(input())
classroom = [[0] * N for _ in range(N)]             # 자리 배치표
score = [[0] * N for _ in range(N)]                 # 각 자리에 앉은 학생의 만족도 조사
data = {}                                           # 학생 별 선호도 조사
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
for _ in range(N ** 2):
    s, *preference = map(int, input().split())
    data[s] = preference
    find(s)
ans = 0
for row in score:
    ans += sum(row)
print(ans)