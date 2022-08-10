from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10000)


def solve(g, a, b, R):
    if 0 <= a < N and 0 <= b < N and g[a][b] == R:
        g[a][b] = ''
        solve(g, a - 1, b, R)
        solve(g, a, b - 1, R)
        solve(g, a + 1, b, R)
        solve(g, a, b + 1, R)


N = int(input())
A = []
B = []
for _ in range(N):
    x = input().rstrip()
    y = x.replace('G', 'R')
    A.append(list(x))
    B.append(list(y))
r = 0
l = 0
for i in range(N):
    for j in range(N):
        if A[i][j]:
            solve(A, i, j, A[i][j])
            r += 1
        if B[i][j]:
            solve(B, i, j, B[i][j])
            l += 1
print(r, l)
