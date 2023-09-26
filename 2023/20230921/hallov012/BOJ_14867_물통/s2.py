import sys
sys.stdin = open('input.txt')
from collections import deque, defaultdict

def convert_str(p, q):
    return '-'.join([str(p), str(q)])

a, b, c, d = map(int, input().split())
visited = defaultdict(int)
visited['0-0'] += 1
que = deque([(0, 0)])

while que:
    x, y = que.popleft()
    if (x, y) == (c, d):
        break
    cnt = visited[convert_str(x, y)]
    # A 물통을 채우기, 비우기
    if not visited[convert_str(a, y)]:
        visited[convert_str(a, y)] += cnt + 1
        que.append((a, y))
    if not visited[convert_str(0, y)]:
        visited[convert_str(0, y)] += cnt + 1
        que.append((0, y))
    # B 물통 채우기, 비우기
    if not visited[convert_str(x, b)]:
        visited[convert_str(x, b)] += cnt + 1
        que.append((x, b))
    if not visited[convert_str(x, 0)]:
        visited[convert_str(x, 0)] += cnt + 1
        que.append((x, 0))
    # A => B, B => A 옮기기
    if x <= b-y:
        if not visited[convert_str(0, x+y)]:
            visited[convert_str(0, x+y)] += cnt + 1
            que.append((0, y+x))
    else:
        if not visited[convert_str(x-(b-y), b)]:
            visited[convert_str(x-(b-y), b)] += cnt + 1
            que.append((x-(b-y), b))
    if y <= a-x:
        if not visited[convert_str(x+y, 0)]:
            visited[convert_str(x+y, 0)] += cnt + 1
            que.append((x+y, 0))
    else:
        if not visited[convert_str(a, y-(a-x))]:
            visited[convert_str(a, y-(a-x))] += cnt + 1
            que.append((a, y-(a-x)))

print(visited[convert_str(c, d)] - 1)



