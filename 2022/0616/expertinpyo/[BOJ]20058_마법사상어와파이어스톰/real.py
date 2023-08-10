# 상대 좌표 느낌으로 접근할 예정
def fire(x, y, n):
    # 시작점 x, y, 돌리기 . fire를 재귀로 사용 할 수 있을 듯
    # x, x + n-1 / y, y + n-1
    if not n:
        return
    btn = 0
    nx, ny = x, y
    while True:
        if btn == 0:
            target[x+ny-y][y+n-1] = arr[nx][ny]
            if ny < y+n-2:
                ny += 1
            else:
                ny = y+n-1
                btn += 1
        elif btn == 1:
            target[x+n-1][y+n-1-nx+x] = arr[nx][ny]
            if nx < x+n-2:
                nx += 1
            else:
                nx = x+n-1
                btn += 1
        elif btn == 2:
            target[x+ny-y][y] = arr[nx][ny]
            if ny > y + 1:
                ny -= 1
            else:
                ny = y
                btn += 1
        else:
            target[x][y+n-1-nx+x] = arr[nx][ny]
            if nx > x + 1:
                nx -= 1
            else:
                nx = x
                break
    fire(nx+1, ny+1, n-2)

def melt():
    minus = []
    for i in range(2 ** N):
        for j in range(2 ** N):
            cnt = 0
            for d in di:
                ni, nj = d[1] + i, d[0] + j
                if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N and arr[ni][nj]:
                    cnt += 1
            if cnt < 3:
                if arr[i][j]:
                    minus.append([i, j])
    for mx, my in minus:
        arr[mx][my] -= 1

def dfs(x, y):
    stack = [(x, y)]
    cnt = 1
    while stack:
        x, y = stack.pop()
        for d in di:
            nx, ny = x + d[1], y + d[0]
            if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N and not visited[nx][ny] and arr[nx][ny]:
                visited[nx][ny] = 1
                cnt += 1
                stack.append((nx, ny))
    return cnt

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
spells = list(map(int, input().split()))

for spell in spells:
    if spell:
        n = 2 ** spell
        target = [[0] * (2 ** N) for _ in range(2 ** N)]
        for i in range(2 ** (N-spell)):
            for j in range(2 ** (N-spell)):
                x, y = i * n, j * n
                fire(x, y, n)
        arr = target
    melt()

visited = [[0] * 2**N for _ in range(2**N)]
total = 0
maxs = 0
for i in range(2 ** N):
    total += sum(arr[i])
    if maxs < (2**N)**2:
        for j in range(2**N):
            if not visited[i][j] and arr[i][j]:
                visited[i][j] = 1
                maxs = max(maxs, dfs(i, j))
print(total)
print(maxs)
