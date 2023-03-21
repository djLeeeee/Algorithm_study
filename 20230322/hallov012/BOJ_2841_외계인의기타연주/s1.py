import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, p = map(int, input().split())
orders = [list(map(int, input().split())) for _ in range(n)]
stack = [[] for _ in range(7)]
ans = 0
for a, b in orders:
    flag = False
    while stack[a] and stack[a][-1] >= b:
        temp = stack[a].pop()
        if temp == b:
            flag = True
        else:
            ans += 1
    stack[a].append(b)
    if not flag:
        ans += 1

print(ans)