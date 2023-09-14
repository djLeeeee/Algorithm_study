import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
virus = []
arr = []
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
    for j in range(n):
        if arr[i][j]:
            heapq.heappush(virus, (arr[i][j], i, j))
s, x, y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while s:
    new_virus = []
    while virus:
        t, a, b = heapq.heappop(virus)
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not arr[nx][ny]:
                    arr[nx][ny] = t
                    heapq.heappush(new_virus, (t, nx, ny))
    virus = new_virus
    s -= 1

print(arr[x-1][y-1])
