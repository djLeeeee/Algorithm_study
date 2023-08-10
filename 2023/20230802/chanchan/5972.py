# https://www.acmicpc.net/problem/5972'
import sys
sys.stdin = open("./input/5972.txt")
input = sys.stdin.readline
# ----------------------------------------
from collections import deque

N, M = map(int, input().split())
cows_info = [[] for _ in range(N)]
cnt_board = [sys.maxsize] * N

for _ in range(M):
    n1, n2, cow = map(lambda x: int(x) - 1, input().split())
    cows_info[n1].append((n2, cow + 1))
    cows_info[n2].append((n1, cow + 1))

cnt_board[0] = 0
que = deque([(0, 0)])
while que:
    cur, val = que.popleft()
    # 시간 초과 방지
    if cnt_board[cur] < val:
        continue
    for (next, cow) in cows_info[cur]:
        if val + cow < cnt_board[next]:
            cnt_board[next] = val + cow
            que.append((next, cnt_board[next]))

print(cnt_board[N - 1])