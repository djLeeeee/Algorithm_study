import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def change(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] ^= 1

n, m = map(int, input().split())
a = [list(map(int, input().rstrip())) for _ in range(n)]
b = [list(map(int, input().rstrip())) for _ in range(n)]

ans = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            change(i, j)
            ans += 1

print(ans if a == b else -1)
