import sys
sys.stdin = open('input.txt')

# p: 내가 다음에 그릴 별의 세로 크기, q: 내가 그린 별의 세로 크기
def star(p):
    q = p // 2
    if p == 3:
        g[-3][:6] = [' '] * 2 + ['*'] + [' '] * 3
        g[-2][:6] = [' ', '*', ' ', '*', ' ', ' ']
        g[-1][:6] = ['*'] * 5 + [' ']
        return
    star(q)
    for i in range(n-p, n):
        # n-p+q 현재 그린 별의 시작 높이
        # 위에 삼각형 별 찍기
        if i < n - p + q:
            g[i][q: q+p] = g[i+q][:p]
        # 옆에 삼각형 별 찍기
        else:
            g[i][p: 2*p] = g[i][:p]

n = int(input())
g = [[' ' for _ in range(n*2)] for _ in range(n)]
star(n)
for i in range(n):
    a = ''.join(g[i])
    print(a)



