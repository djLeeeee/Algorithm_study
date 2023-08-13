import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(n)]
    ex, ey = map(int, input().split())
    visited = [0] * n
    que = deque([(sx, sy)])
    flag = False
    while que:
        x, y = que.popleft()
        # 20병을 가지고 도착지에 갈 수 있는 경우
        if abs(ex - x) + abs(ey - y) <= 20 * 50:
            flag = True
            break
        for i in range(n):
            nx, ny = stores[i]
            if not visited[i] and abs(nx - x) + abs(ny - y) <= 20 * 50:
                visited[i] = 1
                que.append((nx, ny))
    if flag:
        print('happy')
    else:
        print('sad')
