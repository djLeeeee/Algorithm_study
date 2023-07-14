import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
card_que = []
for card in cards:
    heapq.heappush(card_que, card)

for _ in range(m):
    a = heapq.heappop(card_que)
    b = heapq.heappop(card_que)
    heapq.heappush(card_que, a+b)
    heapq.heappush(card_que, a+b)

print(sum(card_que))
