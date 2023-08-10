# 축이 생긴다고 생각해보기
# 현재 좌표 기준으로 기준을 넘어가면 마이너스, 기준 전이면 플러스
#
def fire(n):
    if not n:
        return arr
    num = 2 ** n
    for i in range(2**(N-n)):
        for j in range(2**(N-n)):
            start_x = i * num
            start_y = j * num
            l = 2 * n - 1
            x = start_x
            y = start_y
            btn = 0
            while l:
                nx, ny = x + di[btn][1], y + di[btn][0]
                if start_x <= nx <= start_x + l and start_y <= ny <= start_y + l:
                    if btn == 0:    # 오른쪽으로 이동
                        alternative[ny][start_x+l] = arr[nx][ny]
                        if ny == start_y + l:
                            btn += 1
                    elif btn == 1:  # 아래로 이동
                        alternative[ny][start_x+l-nx] = arr[nx][ny]
                        if nx == start_x + l:
                            btn += 1
                    elif btn == 2:  # 왼쪽으로 이동
                        alternative[nx-ny][start_y] = arr[nx][ny]
                        if ny == start_y + l:
                            btn += 1
                    else:
                        alternative[ny][start_x + l - nx] = arr[nx][ny]
                        if nx == start_x + l:
                            btn = 0
                    x, y = nx, ny

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
spells = list(map(int, input().split()))

for spell in spells:
    alternative = [[0] * (2 ** N) for _ in range(2 ** N)]
    arr = fire(spell)
print(arr)