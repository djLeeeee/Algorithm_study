from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def diikstra():
    queue = []
    heappush(queue, (arr[0][0], 0, 0))
    distance[0][0] = 0

    while queue:
        cost, x, y = heappop(queue)

        # 종료 조건
        if x == N-1 and y == N-1:
            print(f'Problem {cnt}: {distance[x][y]}')
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                new_cost = cost + arr[nx][ny]
                # 갱신 후 힙에 추가
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heappush(queue, (new_cost, nx, ny))


cnt = 1
while True:
    N = int(input())
    if N == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[987654321] * N for _ in range(N)]
    diikstra()
    cnt += 1