# https://www.acmicpc.net/problem/9466
import sys
from collections import deque
sys.stdin = open("./input/9466.txt")
input = sys.stdin.readline
# ----------------------------------------
def play(n):
        global checked
        vst = [0] * (N + 1)
        vst[n] = 1
        que = deque([(n, n)])

        while que:
            prev, cur = que.popleft()
            for next in edges[cur]:
                if next != prev and not checked[next]:
                    if not vst[next]:
                        vst[next] = 1
                        que.append((cur, next))
                    else:
                        for ind in range(1, N + 1):
                            if vst[ind]:
                                checked[ind] = 1
                        return


for _ in range(int(input())):
    N = int(input())

    edges = [[] for _ in range(N + 1)]
    picks = [0] + list(map(int, input().split()))
    checked = [0] * (N + 1)

    for n in range(1, N + 1):
        m = picks[n]
        if n == m:
            checked[n] = 1
    
    for n in range(1, N + 1):
        if checked[n]:
            continue
        m = picks[n]
        edges[m].append(n)
        edges[n].append(m)
        
    for n in range(1, N + 1):
        if checked[n]:
            continue
        
        play(n)




    print(checked.count(0) - 1)
