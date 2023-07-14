import sys
sys.stdin = open('input.txt')

def dfs(temp_sum, cnt):
    global max_score
    if cnt == 11:
        max_score = max(max_score, temp_sum)

    for i in range(11):
        if check[i] or not player[cnt][i]:
            continue
        check[i] = 1
        dfs(temp_sum + player[cnt][i], cnt + 1)
        check[i] = 0

T = int(input())
for _ in range(T):
    player = [list(map(int, input().split())) for _ in range(11)]
    # print(player)
    check = [0]*11

    max_score = 0
    dfs(0, 0)
    print(max_score)
