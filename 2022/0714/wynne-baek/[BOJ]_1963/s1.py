import sys
from collections import deque
sys.stdin = open('input.txt')

#에라토스테네스의 체
T = int(input())
a = [True] * 10000
a[0], a[1] = False, False
for i in range(2, 10000):
    if a[i]:
        for j in range(i + i, 10000, i):
            a[j] = False

def bfs():
    visited = [-1] * 10000
    visited[first] = 0
    queue = deque([(first, 0)])

    while queue:
        now, cnt = queue.popleft()
        now_str = str(now)
        # 종료 조건
        if now == last:
            return cnt
        # 각 자릿수를 0~9까지 변환한 후,
        for i in range(4):
            for j in range(10):
                temp = int(now_str[:i] + str(j) + now_str[i + 1:])
                # 방문 전 and 소수 and 1000보다 클 때, queue에 추가
                if visited[temp] == -1 and a[temp] == True and temp > 1000:
                    visited[temp] = cnt + 1
                    queue.append((temp, cnt + 1))

for _ in range(T):
    first, last = map(int, input().split())
    result = bfs()
    if result != None:
        print(result)
    else:
        print('Impossible')
