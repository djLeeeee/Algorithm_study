import sys, heapq

input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def do():
    heap = [(g[0][0], 0, 0)]
    while heap:
        gold, r, c = heapq.heappop(heap)
        if r == N-1 and c == N-1:
            return gold
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < N and 0 <= nc < N:
                if nr == N-1 and nc == N-1:
                    return gold + g[nr][nc]
                elif visited[nr][nc] > gold + g[nr][nc]:
                    visited[nr][nc] = gold + g[nr][nc]
                    heapq.heappush(heap, (gold + g[nr][nc], nr, nc))

N = int(input().strip())
cnt = 1
while True:
    if N == 0:
        break
    g = [tuple(map(int, input().strip().split())) for _ in range(N)]
    visited = [[125 * 125 * 9] * N for _ in range(N)]
    print(f'Problem {cnt}: {do()}')
    N = int(input().strip())
    cnt += 1

