import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)                                  # 재귀 깊이 설정
N = int(input().strip())
g = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def do(r, c):
    my_list = [0]                                               # 네 방향 중 값을 넣기 위한 리스트
    for w in range(4):                                          # 나중에 최대값에 1을 더해서
        nr = r + dr[w]                                          # 방문체크하고 return할 것이므로 0을 넣어준다
        nc = c + dc[w]
        if 0 <= nr < N and 0 <= nc < N and g[nr][nc] > g[r][c]:
            if visited[nr][nc]:
                my_list.append(visited[nr][nc])
            else:
                my_list.append(do(nr, nc))
    else:
        visited[r][c] = max(my_list) + 1                        # 갈 수 있는 길들 중 최대값 + 1이 현재 위치에서
        return visited[r][c]                                    # 갈 수 있는 최대 깊이이므로 갱신

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

ans = 0

for i in range(N):
    for j in range(N):
        do(i, j)                                  # i, j의 값은 이후 갱신될 가능성이 없으므로
        ans = max(visited[i][j], ans)             # ans와 비교해서 최대값을 갱신해준다.

print(ans)