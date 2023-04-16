import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
g = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a] += 1
    g[b] += 1
q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if g[k] > 1:
            print('yes')
        else:
            print('no')
    # 사이클이 없으므로 단절선이 없음
    else:
        print('yes')

