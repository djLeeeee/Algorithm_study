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
            idx_x = start_x
            idx_y = start_y
            while l:
                # 맨 윗 줄
                if idx_x == start_x:
                    if idx_y == start_y:
                        alternative[idx_x][idx_y+l] = arr[idx_x][idx_y]
                        idx_y += 1
                    elif idx_y <= start_y + l:
                        alternative[idx_y][start_x+l] = arr[idx_x][idx_y]
                        idx_y += 1
                elif idx_y == start_y + l:
                    if idx_x == start_x:
                        alternative[idx_y][idx_x+l] = arr[idx_x][idx_y]
                        idx_x += 1
                    elif idx_x <= start_x + l:
                        alternative[idx_y][start_x + l - idx_x] = arr[idx_x][idx_y]
                        idx_x += 1
                elif idx_x == start_x + l:
                    if idx_y == start_y + l:
                        alternative[idx_x][start_y] = arr[idx_x][idx_y]
                        idx_y -= 1
                    elif idx_y <= start_y + l:
                        alternative[idx_x-idx_y][start_x] = arr[idx_x][idx_y]
                        idx_y -= 1
                else:
                    if idx_x == start_x + l:
                        alternative[start_x][start_y] = arr[idx_x][idx_y]
                        idx_x -= 1
                    elif idx_x <= start_x + l:
                        alternative[idx_y][start_x+l - idx_x] = arr[idx_x][idx_y]
                        idx_x -= 1
                if idx_x == start_x + 1 and idx_y == start_y:
                    start_x += 1
                    start_y += 1
                    l -= 2




di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
spells = list(map(int, input().split()))

for spell in spells:
    alternative = [[0] * (2 ** N) for _ in range(2 ** N)]
    arr = fire(spell)
print(arr)