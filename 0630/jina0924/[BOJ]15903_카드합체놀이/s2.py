# 백준 15903번 카드 합체 놀이 - 92ms

import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)                        # heap을 써서 매번 정렬하던 과정 생략
for _ in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    for _ in range(2):
        heapq.heappush(cards, x + y)
print(sum(cards))