from collections import deque

def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    visited = [[0] * m for _ in range(n)]
    cnt_lst = [0]
    idx = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(n):
        for j in range(m):
            if land[i][j] and not visited[i][j]:
                que = deque([(i, j)])
                cnt = 1
                visited[i][j] = idx
                while que:
                    x, y = que.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] and not visited[nx][ny]:
                                que.append((nx, ny))
                                cnt += 1
                                visited[nx][ny] = idx
                cnt_lst.append(cnt)
                idx += 1

    for j in range(m):
        tmp = [0] * idx
        for i in range(n):
            number = visited[i][j]
            if number and not tmp[number]:
                tmp[number] = cnt_lst[number]
        answer = max(answer, sum(tmp))

    return answer

datas = [
    [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]],
    [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
]

for land in datas:
    print(solution(land))