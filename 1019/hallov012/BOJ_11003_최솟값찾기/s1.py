import sys
from collections import deque
sys.stdin = open('input.txt')

n, l = map(int, input().split())
data = list(map(int, input().split()))
ans = [0] * n

que = deque()
for i in range(n):
    # 현재의 값보다 큰 앞의 값들은 제거 후 현재 값을 추가(어차피 최솟값만 필요하니까)
    while que and que[-1][0] > data[i]:
        que.pop()
    que.append((data[i], i))
    # 주어진 범위를 벗어난 경우는 제거
    if i-l >= 0 and que[0][1] == i-l:
        que.popleft()
    ans[i] = que[0][0]
print(*ans)