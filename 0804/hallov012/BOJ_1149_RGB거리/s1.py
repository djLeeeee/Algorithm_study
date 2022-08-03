import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
# 빨강: row=0, 초록: row=1, 파랑: row=2
cost = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    # 연달아 같은 색을 칠하지 못하므로, i번째 집에 빨강(0)을 칠하려면 i-1번째 집엔 초록(1) 또는 파랑(2)를 칠했어야 함
    # 따라서 이번에 칠할 비용에, 그 전까지 칠할 수 있던 cost의 최솟값을 더해서 누적합으로 만든다
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])
    cost[i][1] += min(cost[i-1][0], cost[i-1][2])
    cost[i][2] += min(cost[i-1][0], cost[i-1][1])
print(min(cost[n-1]))