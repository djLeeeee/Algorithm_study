import sys
sys.stdin = open('input.txt')

def dfs(idx):
    global ans
    if idx == n:
        ans += 1
        return
    dfs(idx+1) # 현재 재료 선택 X
    for i in range(idx):
        if selected[i] and bad[idx][i]:
            return
    selected[idx] = True
    dfs(idx+1)
    selected[idx] = False


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    bad = [[False] * n for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        bad[a][b] = True
        bad[b][a] = True

    selected = [False] * n
    ans = 0

    dfs(0)

    print(f"#{tc} {ans}")