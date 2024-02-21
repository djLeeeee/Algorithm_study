import sys
from collections import deque
sys.stdin = open('input.txt')

def move_dice(dir):
    # 아랫면의 위치
    x, y = 3, 1
    # 동쪽
    if dir == 0:
        a, b, c, d = dice[1][0], dice[1][1], dice[1][2], dice[x][y]
        dice[1] = [d, a, b]
        dice[x][y] = c
    # 남쪽
    elif dir == 1:
        a, b, c, d = dice[0][1], dice[1][1], dice[2][1], dice[x][y]
        dice[0][1] = d
        dice[1][1] = a
        dice[2][1] = b
        dice[x][y] = c
    # 서쪽
    elif dir == 2:
        a, b, c, d = dice[1][0], dice[1][1], dice[1][2], dice[x][y]
        dice[1] = [b, c, d]
        dice[x][y] = a
    # 북쪽
    else:
        a, b, c, d = dice[0][1], dice[1][1], dice[2][1], dice[x][y]
        dice[0][1] = b
        dice[1][1] = c
        dice[2][1] = d
        dice[x][y] = a
    return dice[x][y]

def score():
    global ans, dir
    A = move_dice(dir)
    B = arr[x][y]
    # 다음 방향 정하기
    if A > B:
        dir = (dir + 1) % 4
    elif A < B:
        dir = (dir - 1) % 4

    visited = [[0] * m for _ in range(n)]
    C = 1
    visited[x][y] = 1
    que = deque([(x, y)])
    while que:
        p, q = que.popleft()
        for i in range(4):
            np = p + dx[i]
            nq = q + dy[i]
            if 0 <= np < n and 0 <= nq < m:
                if not visited[np][nq] and arr[np][nq] == B:
                    visited[np][nq] = 1
                    C += 1
                    que.append((np, nq))
    ans += B * C



"""
A: 주사위 아랫면의 숫자
B: 주사위가 위치한 칸의 숫자
C: 현재 위치에서 사방향 탐색으로 갈 수 있는 숫자(B와 같은 칸)
"""
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dice = [
    [0, 2, 0],
    [4, 1, 3],
    [0, 5, 0],
    [0, 6, 0]
]

# 동, 남, 서, 북으로 시계방향으로
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = 0
dir = 0
x, y = 0, 0
while k:
    nx, ny = x + dx[dir], y + dy[dir]
    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny
    else:
        dir = (dir + 2) % 4
        x += dx[dir]
        y += dy[dir]
    score()
    k -= 1

print(ans)


