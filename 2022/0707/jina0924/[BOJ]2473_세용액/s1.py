# 백준 2473번 세 용액 - 41% 시간초과 => pypy 통과

import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline

N = int(input())
data = sorted(list(map(int, input().split())))          # 데이터값 정렬해두기

ans = ()                                                # 세 용액 담을 변수
solution = 3000000000                                   # 혼합된 용액 값 담을 변수

for start in range(N - 2):
    mid, end = start + 1, N - 1
    while mid < end:                                    # 중간 값이 끝 값을 넘어서지 않을 때까지 반복
        ssum = data[start] + data[mid] + data[end]
        if solution > abs(ssum):
            ans = (data[start], data[mid], data[end])
            solution = abs(ssum)
        if ssum < 0:                                    # 용액의 합이 0보다 작다면
            mid += 1                                    # 좀 더 큰 값 더해서 0에 가깝게 만들어보기
        elif ssum > 0:                                  # 위의 과정의 반대
            end -= 1
        elif ssum == 0:
            print(*ans)
            sys.exit()                                  # sys 모듈의 프로그램 종료 함수 (for와 while문 한번에 끝내버리기)
print(*ans)