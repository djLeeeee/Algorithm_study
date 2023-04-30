import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, h, t = map(int, input().split())
q = []
for _ in range(n):
    heapq.heappush(q, -int(input()))

ans = 0
flag = False
while True:
    tmp = -heapq.heappop(q)
    if tmp < h:
        flag = True
        break
    ans += 1
    if ans == t+1 or tmp == 1:
        heapq.heappush(q, -tmp)
        break
    else:
        heapq.heappush(q, -(tmp//2))

if flag:
    print('YES')
    print(ans)
else:
    print('NO')
    print(-q[0])







