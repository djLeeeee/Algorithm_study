import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, k = map(int, input().split())
add = [list(map(int, input().split())) for _ in range(n)]
arr = [[5] * n for _ in range(n)]
trees = []
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for _ in range(m):
    x, y, z = map(int, input().split())
    heapq.heappush(trees, (z, x-1, y-1))

while k > 0:
    live = []
    die = []
    # 봄, 가을
    while trees:
        z, x, y = heapq.heappop(trees)
        if arr[x][y] >= z:
            arr[x][y] -= z
            heapq.heappush(live, (z+1, x, y))
            if not (z+1) % 5:
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        heapq.heappush(live, (1, nx, ny))
        else:
            die.append((z, x, y))

    # 여름
    for z, x, y in die:
        arr[x][y] += z // 2

    # 겨울
    for i in range(n):
        for j in range(n):
            arr[i][j] += add[i][j]

    trees = live
    k -= 1

print(len(trees))

