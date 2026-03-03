import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
ans = 0

for case in range(1 << n*m):
    tmp = 0
    # 가로(비트 0)
    for i in range(n):
        r_tmp = 0
        for j in range(m):
            bit = i*m + j
            if not case & (1 << bit):
               r_tmp = r_tmp * 10 + arr[i][j]
            else:
                tmp += r_tmp
                r_tmp = 0
        tmp += r_tmp
    # 세로(비트 1)
    for j in range(m):
        c_tmp = 0
        for i in range(n):
            bit = i*m + j
            if case & (1 << bit):
                c_tmp = c_tmp * 10 + arr[i][j]
            else:
                tmp += c_tmp
                c_tmp = 0
        tmp += c_tmp
    ans = max(tmp, ans)

print(ans)