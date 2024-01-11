import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

def dfs(x):
    cnt = 0
    for y in tree[x]:
        cnt += dfs(y)

    cnt += nums[x]
    if cnt < 0:
        cnt = 0
    return cnt

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
nums = [0] * (n+1)
for i in range(2, n+1):
    t, a, p = input().split()
    tree[int(p)].append(i)
    if t == 'S':
        nums[i] = int(a)
    else:
        nums[i] = -int(a)

ans = dfs(1)
print(ans)
