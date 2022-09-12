import sys, collections
sys.stdin = open('input.txt')
input = sys.stdin.readline
M, N = map(int, input().strip().split())
g = []
visited = [[0] * M for _ in range(N)]

# 남동북서
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

for i in range(N):
    temp = list(map(int, input().strip().split()))
    temp_list = []
    for j in range(M):
        binary = bin(temp[j])[2:]
        length = len(binary)
        if length != 4:
            binary = '0' * (4 - length) + binary
        temp_list.append(binary)
    else:
        g.append(temp_list)

room_number = 1
largest = 0
largest_break = 0
room_dict = {}

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            temp_number = 0
            Q = collections.deque([(i, j)])
            while Q:
                r, c = Q.popleft()
                if not visited[r][c]:
                    visited[r][c] = room_number
                    temp_number += 1
                    now = g[r][c]
                    length = len(g[r][c])
                    for w in range(4):
                        if now[w] == '0':
                            nr, nc = r + dr[w], c + dc[w]
                            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                                Q.append((nr, nc))
            if temp_number > largest:
                largest = temp_number
            room_dict[room_number] = temp_number
            room_number+=1

for r in range(N):
    for c in range(M):
        if visited[r][c]:
            for w in range(4):
                nr = r + dr[w]
                nc = c + dc[w]
                if 0 <= nr < N and 0 <= nc < M and visited[r][c] != visited[nr][nc] and visited[nr][nc]:
                    if room_dict[visited[nr][nc]] + room_dict[visited[r][c]] > largest_break:
                        largest_break = room_dict[visited[nr][nc]] + room_dict[visited[r][c]]
            else:
                visited[r][c] = 0

print(room_number-1)
print(largest)
print(largest_break)