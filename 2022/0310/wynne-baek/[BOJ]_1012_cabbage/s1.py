import sys
sys.stdin = open('input.txt')

def worm(field):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for idx_1 in range(N):
        for idx_2 in range(M):
            if field[idx_1][idx_2] == 1:
                for i in range(4):
                    nx = idx_1 + dx[i]
                    ny = idx_2 + dy[i]
                    if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1:
                        field[nx][ny] = 0
    for list in field:
        cnt += list.count(1)
    return cnt

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    field = [[0]*M for ___ in range(N)]
    for __ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1
    cnt = 0
    print(field)
    print(worm(field))
    #print(field)