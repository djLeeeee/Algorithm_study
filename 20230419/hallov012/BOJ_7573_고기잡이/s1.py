import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, l, m = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
case = []
for i in range(1, l//2):
    j = (l - 2*i) // 2
    case.append((i, j))

ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for x, y in case:
            if i+x < n+1 and j+y < n+1:
                temp = 0
                for a in range(x):
                    temp += sum(arr[i+a][j:j+y])
                if ans < temp:
                    ans = temp
print(ans)