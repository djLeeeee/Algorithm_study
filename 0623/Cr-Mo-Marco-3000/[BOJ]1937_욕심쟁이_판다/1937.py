import sys, copy

input = sys.stdin.readline

def do(r, c, cnt, stack):
    global ans
    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]
        if 0 <= nr < N and 0 <= nc < N and g[nr][nc] > g[r][c]:
            new_stack = copy.deepcopy(stack)
            new_stack.append((nr, nc))
            if not visited[nr][nc]:
                do(nr, nc, cnt + 1, new_stack)
            else:
                if visited[r][c] < visited[nr][nc] + cnt:
                    # visited[r][c] = max(visited[nr][nc] + cnt, visited[r][c])
                    count = visited[nr][nc] + cnt
                    while new_stack:
                        m, n = new_stack.pop()
                        if visited[m][n] < count:
                            visited[m][n] = count
                        count += 1

    else:
        count = 1
        while stack:
            m, n = stack.pop()
            if visited[m][n] < count:
                visited[m][n] = count
                count += 1
            else:
                return

N = int(input().strip())

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

g = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N):
        stack = [(i, j)]
        do(i, j, 1, stack)

for k in range(N):
    for l in range(N):
        ans = max(ans, visited[k][l])

print(ans)
