# 백준 19638번 센티와 마법의 뿅망치

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq


def sol(top):
    if centi > top:
        print('YES')
        print(cnt)
        sys.exit()
    elif cnt == T or (top == 1 and centi == 1):
        print('NO')
        print(top)
        sys.exit()


N, centi, T = map(int, input().split())
giants = []
for _ in range(N):
    height = int(input())
    heapq.heappush(giants, -height)                 # 최대힙 만들기 위해 음수로 바꿔넣음
cnt = 0
while cnt <= T:                                     # 뿅망치 횟수만큼 돌고 난 맨 마지막 top 보기 위해 <=
    top = heapq.heappop(giants)
    top = -top
    sol(top)
    top //= 2                                       # 현재 키 / 2보다 작거나 같은 정수(⌊ top / 2 ⌋)
    cnt += 1
    heapq.heappush(giants, -top)