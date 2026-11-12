import sys
sys.stdin = open('input.txt')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(idx, cnt, l):
    global max_cnt, min_len
    if cnt + len(cores) - idx < max_cnt:
        return
    if idx == len(cores):
        if cnt > max_cnt:
            max_cnt = cnt
            min_len = l
        elif cnt == max_cnt:
            min_len = min(min_len, l)
        return

    x, y = cores[idx]
    for d in range(4):
        nx, ny = x, y
        path = []
        while True:
            nx = nx + dx[d]
            ny = ny + dy[d]
            if not(0 <= nx < n and 0 <= ny < n):
                break
            if arr[nx][ny]:
                break
            path.append((nx, ny))
        else:
            pass

        # 가장자리 도달 확인
        if 0 <= nx < n and 0 <= ny < n:
            continue

        for px, py in path:
            arr[px][py] = 2
        dfs(idx+1, cnt+1, l + len(path))

        for px, py in path:
            arr[px][py] = 0

    # 연결 안하는 경우
    dfs(idx+1, cnt, l)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = []
    cores = []

    for i in range(n):
        row = list(map(int, input().split()))
        # 가장자리 제외
        if not i in (0, n-1):
            for j in range(1, n-1):
                if row[j]:
                    cores.append((i, j))
        arr.append(row)

    max_cnt = 0
    min_len = float('inf')

    dfs(0, 0, 0)

    print(f"#{tc} {min_len}")

