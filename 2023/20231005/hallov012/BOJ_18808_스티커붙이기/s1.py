import sys
sys.stdin = open('input.txt')

def find_position(sticker, r, c):
    for i in range(n-r+1):
        for j in range(m-c+1):
            flag = True
            for a in range(r):
                for b in range(c):
                    if sticker[a][b] and arr[i+a][j+b]:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                return i, j
    return -1, -1

def rotate_stiker(sticker, r, c):
    new_sticker = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            new_sticker[j][r-i-1] = sticker[i][j]
    return new_sticker

input = sys.stdin.readline

n, m, k = map(int, input().split())
# 왼쪽에서 오른쪽으로 스티커 부착 가능
arr = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    for t in range(4):
        x, y = find_position(sticker, r, c)
        if (x, y) != (-1, -1):
            for i in range(r):
                for j in range(c):
                    arr[x+i][y+j] += sticker[i][j]
            break
        else:
            sticker = rotate_stiker(sticker, r, c)
            r, c = c, r

cnt = 0
for line in arr:
    cnt += sum(line)

print(cnt)
