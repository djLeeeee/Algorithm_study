import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

s = int(input())
visited = [[0] * (s+1) for _ in range(s+1)]
# idx 0: 화면, 1: 클립보드
que = deque([(1, 0)])
visited[1][0] = 1

while que:
    a, b = que.popleft()
    # 클립보드에 저장
    if not visited[a][a]:
        visited[a][a] = visited[a][b] + 1
        que.append((a, a))
    # 클립보드에 있는거 붙혀넣기
    if a+b <= s and not visited[a+b][b]:
        visited[a+b][b] = visited[a][b] + 1
        que.append((a+b, b))
    # 하나 삭제
    if a-1 >= 0 and not visited[a-1][b]:
        visited[a-1][b] = visited[a][b] + 1
        que.append((a-1, b))

ans = sys.maxsize
for i in range(s+1):
    if visited[s][i]:
        ans = min(ans, visited[s][i])

print(ans-1)