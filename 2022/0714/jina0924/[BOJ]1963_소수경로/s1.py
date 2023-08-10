# 백준 1963번 소수 경로

import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def change(num):
    heap = [(0, num)]                           # cnt 낮은 순으로 보기 위해 heap 사용
    used = set(num)                             # 이미 살펴본 소수 담을 set

    while heap:
        cnt, num = heapq.heappop(heap)
        if num == end:                          # 원하는 소수 발견 시 함수 끝냄
            return cnt
        for p in prime:
            str_p = str(p)                      # 자리 바꿔서 비교하기 위해 문자열로 변환
            if not str_p in used:
                diff = 0                        # 한 자리만 바뀐 수인지 판별하기 위한 변수
                for i in range(4):
                    if num[i] != str_p[i]:
                        diff += 1
                if diff == 1:
                    heapq.heappush(heap, (cnt + 1, str_p))
                    used.add(str_p)
    else:                                       # 안적어도 통과됨(?)
        return 'Impossible'


number = [True for _ in range(10001)]

for n in range(2, 101):                         # 10000의 제곱근인 100까지만 살펴봐도 됨
    if number[n]:                               # 소수라면
        for m in range(2 * n, 10001, n):        # 해당 소수의 배수를 False 처리
            number[m] = False

prime = [i for i in range(1000, 10001) if number[i]]    # 소수만 저장한 배열

T = int(input())
for tc in range(T):
    start, end = input().split()
    print(change(start))