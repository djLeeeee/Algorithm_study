# https://www.acmicpc.net/problem/2617
import sys
sys.stdin = open("./input/2617.txt")
input = sys.stdin.readline
from collections import deque
# ----------------------------------------

def count_child(arr, n):
    vst[n] = 1
    que = deque([n])
    cnt = 1
    while que:
        cur = que.popleft()
        for next in arr[cur]:
            if not vst[next]:
                cnt += 1
                que.append(next)
    return cnt > MID
    

# ----------------------------------------
N, M = map(int, input().split())
MID = (N + 1) // 2
top_down = [[] for _ in range(N + 1)]
bottom_up = [[] for _ in range(N + 1)]
for _ in range(M):
    n1, n2 = sorted(map(int, input().split()))
    top_down[n2].append(n1)
    bottom_up[n1].append(n2)


ans = 0
for n in range(1, N + 1):
    vst = [0] * (N + 1)
    ans += count_child(top_down, n)
    vst = [0] * (N + 1)
    ans += count_child(bottom_up, n)
print(ans)