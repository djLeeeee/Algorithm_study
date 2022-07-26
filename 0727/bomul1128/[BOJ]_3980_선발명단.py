from sys import stdin

input = stdin.readline


def dfs(idx, s):
    if idx == 11:
        global ans
        if ans < s:
            ans = s
    else:
        for pos in range(11):
            if not visited[pos] and board[idx][pos]:
                visited[pos] = True
                dfs(idx + 1, s + board[idx][pos])
                visited[pos] = False


for _ in range(int(input())):
    board = [list(map(int, input().split())) for _ in range(11)]
    ans = 0
    visited = [False] * 11
    dfs(0, 0)
    print(ans)
