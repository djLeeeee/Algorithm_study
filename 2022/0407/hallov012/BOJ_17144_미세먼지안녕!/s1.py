import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
dust = []
machine = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            machine.append([i, j])

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]
r1, c1 = machine[0]
r2, c2 = machine[1]
while t > 0:
    # 먼지 확산시키기^^
    # 이차원배열을 하나 더 만들어서 동시에 확산시킬 수 있도록 처리
    n = len(dust)
    new_arr = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if arr[x][y] > 0:
                center = arr[x][y]
                diffusion = center // 5
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and [nx, ny] not in machine:
                        center -= diffusion
                        new_arr[nx][ny] += diffusion
                new_arr[x][y] += center
    diffusion_arr = [[0] * c for _ in range(r)]
    # 공기청정기 영역 확산 시키기^^
    # 위쪽 공기청정기
    for x in range(r):
        for y in range(c):
            if x == 0:
                if y == 0:
                    diffusion_arr[1][0] = new_arr[x][y]
                else:
                    diffusion_arr[x][y-1] = new_arr[x][y]
            elif x == r1:
                if y == c-1:
                    diffusion_arr[x-1][y] = new_arr[x][y]
                else:
                    diffusion_arr[x][y+1] = new_arr[x][y]
            elif x in range(1, r1):
                if y == 0:
                    diffusion_arr[x+1][0] = new_arr[x][y]
                elif y == c-1:
                    diffusion_arr[x-1][y] = new_arr[x][y]
                else:
                    diffusion_arr[x][y] = new_arr[x][y]
            elif x == r2:
                if y == c-1:
                    diffusion_arr[r2+1][y] = new_arr[x][y]
                else:
                    diffusion_arr[x][y+1] = new_arr[x][y]
            elif x == r-1:
                if y == 0:
                    diffusion_arr[x-1][y] = new_arr[x][y]
                else:
                    diffusion_arr[x][y-1] = new_arr[x][y]
            elif x in range(r2+1, r-1):
                if y == 0:
                    diffusion_arr[x-1][y] = new_arr[x][y]
                elif y == c-1:
                    diffusion_arr[x+1][y] = new_arr[x][y]
                else:
                    diffusion_arr[x][y] = new_arr[x][y]
    arr = diffusion_arr
    arr[r1][c1] = 0
    arr[r2][c2] = 0
    t -= 1
ans = 0
for line in arr:
    ans += sum(line)
print(ans)
            




