import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)                                          # 재귀 깊이 설정
N = int(input().strip())
g = [list(map(int, input().strip().split())) for _ in range(N)]     
visited = [[0] * N for _ in range(N)]

def do(r, c):
    if not visited[r][c]:
        visited[r][c] = 1                                               # 미방문시 방문체크
        my_list = []                                                    # 네 방향 중 값을 넣기 위한 리스트
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < N and 0 <= nc < N and g[nr][nc] > g[r][c]:     # 어차피 지나쳐 온 길은 자신보다 작으므로, 통과 불가
                my_list.append(do(nr, nc))                              # 네 방향을 체크해서 갈 수 있는 길들을 리스트에 넣음
        else:
            if my_list:                                                 # 만약 사방에 갈 수 있는 길이 있다면
                visited[r][c] = max(my_list) + 1                        # 갈 수 있는 길들 중 최대값 + 1이 현재 위치에서
            return visited[r][c]                                        # 갈 수 있는 최대 길이이므로 갱신
    else:
        return visited[r][c]                                            # 들어갔는데 이미 체크된 길이라면, 그 길에서 모든
                                                                        # 가능성이 체크 된 길이므로 그냥 그 값을 return

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

ans = 0

for i in range(N):
    for j in range(N):
        do(i, j)
        if visited[i][j] > ans:                                         # i, j의 값은 이후 갱신될 가능성이 없으므로
            ans = visited[i][j]                                         # answer와 비교해서 확인해준다.

print(ans)
