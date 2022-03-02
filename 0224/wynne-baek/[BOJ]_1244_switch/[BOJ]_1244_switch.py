def switch_boy(switch):
    # switch의 배수
    for idx in range(switch, N+1, switch):
        if light[idx] == 1:
            light[idx] = 0
        else:
            light[idx] = 1

def switch_girl(switch):
    # 일단 스위치 바꿔부러
    if light[switch] == 1:
        light[switch] = 0
    else:
        light[switch] = 1
    L = switch - 1
    R = switch + 1
    #좌 우가 같은 동안, 인덱스 에러 방지
    while (L > 0 and R <= N) and light[L] == light[R]:
        if light[L] == 1:
            light[L], light[R] = 0, 0
        else:
            light[L], light[R] = 1, 1
        L -= 1
        R += 1

    # switch의 좌우 대칭 비교

import sys
sys.stdin = open('input1.txt')

#스위치 갯수 N
N = int(input())
# 스위치 상태(1 : 켜짐, 0: 꺼짐)
light = [-1] + list(map(int, input().split()))
S = int(input())
for _ in range(S):
    gender, switch = map(int, input().split())
    if gender == 1:
        switch_boy(switch)
    if gender == 2:
        switch_girl(switch)
#출력형식 지정
for i in range(1, N+1):
    print(light[i], end=' ')
    if i % 20 == 0:
        print()
