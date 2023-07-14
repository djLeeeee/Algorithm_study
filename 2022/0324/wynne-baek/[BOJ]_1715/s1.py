import heapq
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
cards = []
heapq.heapify(cards)
for _ in range(N):
    card = int(sys.stdin.readline())
    heapq.heappush(cards, card)
result = 0
# heap 내부에 1개가 남을 때까지
while len(cards) != 1:
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    z = x + y
    result += z
    heapq.heappush(cards, z)
print(result)
