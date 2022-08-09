'''
100+1+ => 1001, 10:000:111
01

생각보다 경우의 수가 많다... -> 함수 하나로 표현하니까 헷갈려서 엣지케이스에서 걸린다. => 작은 기능도 함수를 사용해서 혼란 줄이기
'''

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


from collections import deque

# 1. 전체를 판별하는 함수
def solution(signal):
    while len(signal) >= 2:
        first = signal.popleft()
        second = signal.popleft()

        # 1001
        if first == 1 and second == 0 and len(signal) >= 2:
            ans = check1001(signal)
            if ans == 1:
                return
        # 01
        elif first == 0 and second == 1:
            if not signal:
                print('YES')
                return

        else:
            print('NO')
            return
    print('NO')
    return


# 2. 1000001111(=100+1+)을 판별하는 함수 -> return 0: 다음 신호 확인하기 / return 1 확인 완료
def check1001(signal):
    third = signal.popleft()
    if third == 0:                                                          # 100
        if check0(signal) == 1:                                             # 1000001
            signal.popleft()
            if signal and signal[0] == 1:                                   # 1000001/1
                ans = check1(signal)
                if ans == 0:                                                # 1000001/1111
                    print('YES')
                    return 1
                else:                                                       # 1000001/11110
                    if len(signal) >= 2 and signal[1] == 0:                 # 1000001/111100
                        signal.appendleft(1)                                # 1000001111/100
                        return 0
                    else:                                                   # 10000011111/01 or 10000001111/0
                        return 0


            elif signal and signal[0] == 0:                                 # 1000001/0
                return 0

            elif not signal:                                                # 1000001/_
                print('YES')
                return 1

        else:                                                               # 100_
            print('NO')
            return 1

    print('NO')                                                             # 101
    return 1




# 2-1. 연속된 0이 끝나는 지점을 확인하는 함수
def check0(signal):
    while signal:
        if signal[0] == 0:
            signal.popleft()
        else:
            return 1            # 0000001: 계속 진행하다 1을 만났을 때
    return 0                    # 0000000 or _: 끝이 결국 0으로 끝날 때

# 2-2. 연속된 1이 끝나는 지점을 확인하는 함수
def check1(signal):
    while signal:
        if signal[0] == 1:
            signal.popleft()
        else:
            return 1            # 111110
    return 0                    # 111111 or _


# 0. input 받기
T = int(input())
for _ in range(T):
    tc = deque(map(int, list(input().strip())))
    solution(tc)