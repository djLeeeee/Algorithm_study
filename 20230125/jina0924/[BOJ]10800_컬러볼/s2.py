# 백준 10800번 컬러볼

import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline

N = int(input())
balls = [[i] + list(map(int, input().split())) for i in range(N)]   # 공 번호 포함하여 정보 저장
balls.sort(key=lambda x: x[2])                                      # 크기 오름차순으로 정렬
ans = [0] * N                                                       # 해당 공으로 잡을 수 있는 공들의 크기 합 저장할 배열
i = 0
total = 0                                                           # 누적합을 담을 변수
color = [0] * (N + 1)                                               # 같은 색 누적합 담을 변수
for j in range(1, N):
    while balls[i][2] < balls[j][2]:                                # 현재 살펴보는 공보다 작은 공일때만 반복
        total += balls[i][2]
        color[balls[i][1]] += balls[i][2]
        i += 1
    ans[balls[j][0]] += total - color[balls[j][1]]                  # 현재 공보다 작은 크기들 합에서 같은 색깔 공은 빼기
print(*ans, sep='\n')