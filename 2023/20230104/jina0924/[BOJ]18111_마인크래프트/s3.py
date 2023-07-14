# 백준 18111번 마인크래프트

import sys
sys.stdin = open('input4.txt')
input = sys.stdin.readline


def flatten(height):
    global ans, top
    lack, overflow = 0, 0                               # lack, overflow: height보다 부족한/넘치는 블록 개수

    for r in range(N):
        for c in range(M):
            if ground[r][c] > height:
                lack += ground[r][c] - height
            elif ground[r][c] < height:
                overflow += height - ground[r][c]
    if B + lack - overflow < 0:                         # 인벤토리에 있을 블록 개수보다 많이 써야 한다면 함수 끝냄
        return
    if lack * 2 + overflow <= ans:                      # 걸리는 시간의 최소값 갱신
        ans = lack * 2 + overflow
        top = height                                    # 0~256 순으로 돌므로 top을 비교할 if문 필요 없음


N, M, B = map(int, input().split())                     # N, M, B: 세로, 가로, 인벤토리에 있는 블록 수
ground = [list(map(int, input().split())) for _ in range(N)]
ans, top = 987987987, 0                                 # ans, top: 땅을 고르는 데 걸리는 시간, 그 때의 최대 높이
for h in range(257):                                    # 높이가 256이하이므로 0~256 순회
    flatten(h)
print(ans, top)