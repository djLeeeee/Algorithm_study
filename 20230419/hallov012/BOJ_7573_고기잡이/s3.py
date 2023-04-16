import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(sx, sy, ex, ey):
    global ans
    cnt = 0
    for a, b in fish:
        if sx <= a <= ex and sy <= b <= ey:
            cnt += 1
    if cnt > ans:
        ans = cnt

n, l, m = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(m)]
case = []
for i in range(1, l//2):
    j = (l - 2*i) // 2
    if i < n and j < n:
        case.append((i, j))

ans = 0

for i, j in fish:
    for x, y in case:
        # 물고기가 윗변, 아랫변에 있을 때
        for sy in range(j-y, j+1):
            find(i, sy, i+x, sy+y)
            find(i-x, sy, i, sy+y)
        # 물고기가 좌변, 우변에 있을 때
        for sx in range(i-x, i+1):
            find(sx, j-y, sx+x, j)
            find(sx, j, sx+x, j+y)
print(ans)