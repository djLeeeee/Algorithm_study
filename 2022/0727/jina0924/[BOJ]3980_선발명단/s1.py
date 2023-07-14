# 백준 3980번 선발 명단

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def pick(c, total):
    global ans
    if c == 11:             # 모든 포지션을 다 돌아봤으면
        if ans < total:     # 최대값인지 판별하고 갱신해주기
            ans = total
        return
    for r in range(11):     # 모든 선수들을 순회
        if not picked[r] and data[r][c]:        # 아직 선발되지 않았고, 능력치 값이 있다면
            picked[r] = 1
            pick(c+1, total + data[r][c])       # 해당 선수 선발하고 다음 포지션 보러 감
            picked[r] = 0                       # 선발 여부를 초기화 하고 다른 선수 값 살펴보러 감


T = int(input())            # T: 테스트 케이스 개수
for tc in range(T):
    data = [list(map(int, input().split())) for _ in range(11)]
    picked = [0] * 11       # 선발된 선수인지 판별할 배열
    ans = 0                 # 능력치의 합의 최댓값을 담을 변수
    pick(0, 0)
    print(ans)