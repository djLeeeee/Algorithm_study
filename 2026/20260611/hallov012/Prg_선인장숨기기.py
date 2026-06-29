from collections import deque

def solution(m, n, h, w, drops):
    rain = [[len(drops)+1] * n for _ in range(m)]
    for t, (x, y) in enumerate(drops):
        rain[x][y] = t+1

    # 가로 최소(row_min: (x,y) 부터 시작하는 가로 m 길이의 최소값
    cols = n-w+1
    row_min = [[0] * cols for _ in range(m)]

    for x in range(m):
        que = deque()
        for y in range(n):
            while que and rain[x][que[-1]] >= rain[x][y]:
                que.pop()
            que.append(y)

            if que[0] <= y-w:
                que.popleft()
            if y >= w-1:
                row_min[x][y-w+1] = rain[x][que[0]]

    # 세로 최소
    rows = m-h+1
    rect_min = [[0] * cols for _ in range(rows)]

    for y in range(cols):
        que = deque()
        for x in range(m):
            while que and row_min[que[-1]][y] >= row_min[x][y]:
                que.pop()
            que.append(x)

            if que[0] <= x-h:
                que.popleft()
            if x >= h-1:
                rect_min[x-h+1][y] = row_min[que[0]][y]

    min_val = -1
    ans = [0, 0]
    for x in range(rows):
        for y in range(cols):
            if rect_min[x][y] > min_val:
                min_val = rect_min[x][y]
                ans = [x, y]

    return ans
