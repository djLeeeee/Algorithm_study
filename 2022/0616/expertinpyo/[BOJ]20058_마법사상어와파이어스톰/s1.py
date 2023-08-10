# 축이 생긴다고 생각해보기

def rotate(n):
    alternative = [[0] * (2 ** N) for _ in range(2 ** N)]
    num = 2**n
    for i in range(2**N):
        for j in range(2**N):
            for k in range(2**n, 0, -1):
                if i % num < num - 1 and j % num < num - 1:
                    x, y = di[0][1] + i, di[0][0] + j
                elif i % num < num -1 and j % num >= num -1:
                    x, y = di[1][1] + i, di[1][0] + j
                elif i % num >= num -1 and j % num >= num -1:
                    x, y = di[2][1] + i, di[2][0] + j
                else:
                    x, y = di[3][1] + i, di[3][0] + j
            alternative[x][y] = arr[i][j]

    return alternative

    rotate(n//2)
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
spells = list(map(int, input().split()))

for spell in spells:
    arr = rotate(spell)
print(arr)