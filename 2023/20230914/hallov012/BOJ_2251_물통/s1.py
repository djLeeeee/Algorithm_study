import sys
from collections import deque
sys.stdin = open('input.txt')

bucket = list(map(int, input().split()))
n = 200
ans = set()
# A, B 물통의 상황을 기록
visited = [[False] * (n+1) for _ in range(n)]
que = deque([[0, 0, bucket[2]]])

while que:
    data = que.popleft()
    a, b, c = data
    if visited[a][b]:
        continue
    visited[a][b] = True
    if not a:
        ans.add(c)
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            # j번째를 i번째로 쏟아 부움
            x, y = data[i], data[j]
            k = bucket[i]
            tmp = data[::]
            if x + y > k:
                tmp[i], tmp[j] = k, y-(k-x)
            else:
                tmp[i], tmp[j] = x+y, 0
            que.append(tmp)

ans = sorted(list(ans))
print(*ans)



