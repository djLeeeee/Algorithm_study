# 백트래킹이지만 bfs로..
def bfs():
    queue = set((0, 0, arr[0][0]))
    ans = 1
    while queue:
        x, y, sen = queue.pop()
        for d in di:
            nx, ny = d[1] + x, d[0] + y
            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] not in sen:
                queue.add((nx, ny, arr[nx][ny] + sen))
                ans = max(ans, len(arr[nx][ny] + sen))

    return ans

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
R, C = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(list(input()))

print(bfs())