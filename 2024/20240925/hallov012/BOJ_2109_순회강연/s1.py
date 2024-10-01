import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x: x[1])
q = []
for p, d in data:
    heapq.heappush(q, p)
    # 못가면 갈 수 있는 것 중 제일 싼거 빼기
    if len(q) > d:
        heapq.heappop(q)
print(sum(q))