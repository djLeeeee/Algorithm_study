import sys
from collections import deque
sys.stdin = open('input.txt')

def can_go(gold_pepero):
    have_to_visit = deque([s])
    visited = [0] * (N + 1)
    visited[s] = 1
    while have_to_visit:
        x = have_to_visit.popleft()
        if x == e:
            return True
        for island, limit in connection[x]:
            if not visited[island] and gold_pepero <= limit:
                visited[island] = 1
                have_to_visit.append(island)
    return False

N, M = map(int, input().split())
s, e = map(int, input().split())
connection = [[] for _ in range(N+1)]
# print(connection)
for _ in range(M):
    h1, h2, max = map(int, input().split())
    connection[h1].append((h2, max))
    connection[h2].append((h1, max))
left = 1
right = 1000000
answer = 0
while left <= right:
    mid = (left + right) // 2
    if can_go(mid):
        left = mid + 1
        answer = mid
    else:
        right = mid -1
print(answer)
