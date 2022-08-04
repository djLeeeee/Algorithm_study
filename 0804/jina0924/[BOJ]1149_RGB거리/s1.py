# 백준 1149번 RGB거리

import sys
sys.stdin = open('input.txt')


def coloring():
    i = 1
    '''
    i번째 집을 특정 색으로 칠할 때의 최소 비용
    = i-1번째 집까지 해당 색이 아닌 색으로 칠할 때의 최소 비용
    ex) 3번째 집을 R로 칠할 경우 => 2번째 집을 G or B로 칠했을 때 최소 비용
    '''
    while i < N:                                                    # N번째 집까지 최소비용 누적해감
        data[i][0] += min(data[i-1][1], data[i-1][2])
        data[i][1] += min(data[i-1][0], data[i-1][2])
        data[i][2] += min(data[i-1][0], data[i-1][1])
        i += 1
    print(min(data[N-1]))

for tc in range(5):
    N = int(input())                                                # N: 집의 개수
    data = [list(map(int, input().split())) for _ in range(N)]      # 각 집을 RGB로 칠할 때 드는 비용 데이터
    coloring()