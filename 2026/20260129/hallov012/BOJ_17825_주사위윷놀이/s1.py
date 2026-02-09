import sys
sys.stdin = open('input.txt')

def dfs(cnt, turn):
    global ans
    if turn == 10:
        ans = max(ans, cnt)
        return
    move = nums[turn] - 1
    for i in range(4):
        now = position[i]
        if now != 21:
            next = graph[now][move]
            flag = True
            if next == 21 or not next in position:
                cnt += score[next]
                position[i] = next
                dfs(cnt, turn+1)
                cnt -= score[next]
                position[i] = now

nums = list(map(int, input().split()))

graph = {i: [i+1, i+2, i+3, i+4, i+5] for i in range(33)}

# 마지막 goal(21) 처리
for i in range(5):
    target = 16+i
    for j in range(1, i+1):
        graph[target][-j] = 21

graph[5] = [22, 23, 24, 25, 31]
graph[22] = [23, 24, 25, 31, 32]
graph[23] = [24, 25, 31, 32, 20]
graph[24] = [25, 31, 32, 20, 21]
graph[25] = [31, 32, 20, 21, 21]

graph[10] = [29, 30, 25, 31, 32]
graph[29] = [30, 25, 31, 32, 20]
graph[30] = [25, 31, 32, 20, 21]

graph[15] = [28, 27, 26, 25, 31]
graph[28] = [27, 26, 25, 31, 32]
graph[27] = [26, 25, 31, 32, 20]
graph[26] = [25, 31, 32, 20, 21]

graph[31] = [32, 20, 21, 21, 21]
graph[32] = [20, 21, 21, 21, 21]

score = [i*2 for i in range(33)]
score[21] = 0
score[22] = 13
score[23] = 16
score[24] = 19
score[25] = 25
score[26] = 26
score[27] = 27
score[28] = 28
score[29] = 22
score[30] = 24
score[31] = 30
score[32] = 35

ans = 0
position = [0] * 4
dfs(0, 0)
print(ans)
