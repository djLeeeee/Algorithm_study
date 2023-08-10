def dfs(x, cnt):
    global ans
    if x == 11:
        ans = max(cnt, ans)
        return
    if players[x] >= 0:
        dfs(x+1, cnt + arr[x][players[x]])
    else:
        for pos in possible[x]:
            if not players.count(pos):
                players[x] = pos
                dfs(x+1, cnt + arr[x][pos])
                players[x] = -1

T = int(input())
for tc in range(T):
    arr = [list(map(int, input().split())) for _ in range(11)]
    players = [-1] * 11
    possible = [[] for _ in range(11)]
    for i in range(11):
        for j in range(11):
            if arr[i][j]:
                possible[i].append(j)
        if len(possible[i]) == 1:
            players[i] = possible[i][0]
    ans = 0
    dfs(0, 0)
    print(ans)