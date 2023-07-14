import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

g = []

ans = N*M

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

cam_list = []
cam_5 = []

for i in range(N):
    temp = list(map(int, input().strip().split()))
    for j in range(M):
        if temp[j] == 6:
            ans -= 1
        elif temp[j] == 5:
            cam_5.append((i, j))
            ans -= 1
        elif temp[j] == 0:
            continue
        else:
            ans -= 1
            cam_list.append((i, j))
    g.append(temp)

while cam_5:
    r, c = cam_5.pop()
    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]
        while 0 <= nr < N and 0 <= nc < M and g[nr][nc] != 6:
            if g[nr][nc] == 0:
                g[nr][nc] = '#'
                ans -= 1
            nr = nr + dr[w]
            nc = nc + dc[w]

length = len(cam_list)

def do(cnt, temp_ans):
    global ans
    minus_list = []
    if cnt == length:
        if temp_ans < ans:
            ans = temp_ans
        return
    r = cam_list[cnt][0]
    c = cam_list[cnt][1]
    # 1일때
    if g[r][c] == 1:
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            while 0 <= nr < N and 0 <= nc < M and g[nr][nc] != 6:
                if g[nr][nc] == 0:
                    g[nr][nc] = '#'
                    temp_ans -= 1
                    minus_list.append((nr, nc))
                nr = nr + dr[w]
                nc = nc + dc[w]
            # 다 했으면 넘어가자
            do(cnt + 1, temp_ans)
            while minus_list:
                nr, nc = minus_list.pop()
                g[nr][nc] = 0
                temp_ans += 1
    # 2일때
    elif g[r][c] == 2:
        for w in range(2):
            dir1 = w
            dir2 = w+2
            # dir 1 방향
            nr = r + dr[dir1]
            nc = c + dc[dir1]
            while 0 <= nr < N and 0 <= nc < M and g[nr][nc] != 6:
                if g[nr][nc] == 0:
                    g[nr][nc] = '#'
                    temp_ans -= 1
                    minus_list.append((nr, nc))
                nr = nr + dr[dir1]
                nc = nc + dc[dir1]
            # dir 2 방향
            nr = r + dr[dir2]
            nc = c + dc[dir2]
            while 0 <= nr < N and 0 <= nc < M and g[nr][nc] != 6:
                if g[nr][nc] == 0:
                    g[nr][nc] = '#'
                    temp_ans -= 1
                    minus_list.append((nr, nc))
                nr = nr + dr[dir2]
                nc = nc + dc[dir2]
            # 다 했으면 넘어가자
            do(cnt + 1, temp_ans)
            while minus_list:
                nr, nc = minus_list.pop()
                g[nr][nc] = 0
                temp_ans += 1
    elif g[r][c] == 3:
        for w in range(0, 4):
            dir1 = w
            dir2 = (w + 1) % 4
            # dir 1 방향
            nr = r + dr[dir1]
            nc = c + dc[dir1]
            while 0 <= nr < N and 0 <= nc < M and g[nr][nc] != 6:
                if g[nr][nc] == 0:
                    g[nr][nc] = '#'
                    temp_ans -= 1
                    minus_list.append((nr, nc))
                nr = nr + dr[dir1]
                nc = nc + dc[dir1]
            # dir 2 방향
            nr = r + dr[dir2]
            nc = c + dc[dir2]
            while 0 <= nr < N and 0 <= nc < M and g[nr][nc] != 6:
                if g[nr][nc] == 0:
                    g[nr][nc] = '#'
                    temp_ans -= 1
                    minus_list.append((nr, nc))
                nr = nr + dr[dir2]
                nc = nc + dc[dir2]
            # 다 했으면 넘어가자
            do(cnt + 1, temp_ans)
            while minus_list:
                nr, nc = minus_list.pop()
                g[nr][nc] = 0
                temp_ans += 1
    elif g[r][c] == 4:
        for w in range(0, 4):
            dir1 = w - 1
            dir2 = w % 4
            dir3 = (w + 1) % 4
            # dir 1 방향
            nr = r + dr[dir1]
            nc = c + dc[dir1]
            while 0 <= nr < N and 0 <= nc < M and g[nr][nc] != 6:
                if g[nr][nc] == 0:
                    g[nr][nc] = '#'
                    temp_ans -= 1
                    minus_list.append((nr, nc))
                nr = nr + dr[dir1]
                nc = nc + dc[dir1]
            # dir 2 방향
            nr = r + dr[dir2]
            nc = c + dc[dir2]
            while 0 <= nr < N and 0 <= nc < M and g[nr][nc] != 6:
                if g[nr][nc] == 0:
                    g[nr][nc] = '#'
                    temp_ans -= 1
                    minus_list.append((nr, nc))
                nr = nr + dr[dir2]
                nc = nc + dc[dir2]
            # dir 3 방향
            nr = r + dr[dir3]
            nc = c + dc[dir3]
            while 0 <= nr < N and 0 <= nc < M and g[nr][nc] != 6:
                if g[nr][nc] == 0:
                    g[nr][nc] = '#'
                    temp_ans -= 1
                    minus_list.append((nr, nc))
                nr = nr + dr[dir3]
                nc = nc + dc[dir3]
            do(cnt + 1, temp_ans)
            while minus_list:
                nr, nc = minus_list.pop()
                g[nr][nc] = 0
                temp_ans += 1

do(0, ans)

print(ans)