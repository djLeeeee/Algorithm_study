import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def able_to_attach(x1, x2, y1, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if not arr[i][j]:
                return False
    return True

def attach(x1, x2, y1, y2, val):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            arr[x][y] = val

def find(num, cnt):
    global ans
    if cnt >= ans:
        return
    if num == n*n:
        ans = min(ans, cnt)
        return
    x = num // n
    y = num % n
    if arr[x][y]:
        flag = False
        for s in range(5):
            if paper[s]:
                nx, ny = x+s, y+s
                if 0 <= nx < n and 0 <= ny < n:
                    if able_to_attach(x, nx, y, ny):
                        flag = True
                        paper[s] -= 1
                        attach(x, nx, y, ny, 0)
                        find(num+1, cnt+1)
                        paper[s] += 1
                        attach(x, nx, y, ny, 1)
        if not flag:
            return
    else:
        find(num+1, cnt)


n = 10
arr = [list(map(int, input().split())) for _ in range(n)]
paper = [5] * 5
ans = 26
find(0, 0)

print(ans)



