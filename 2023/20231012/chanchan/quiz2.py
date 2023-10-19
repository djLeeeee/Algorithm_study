# 정복자
# https://www.acmicpc.net/problem/14950
import sys
sys.stdin = open("./input/quiz2.txt")
input = sys.stdin.readline
import heapq

# ----------------------------------------
def find(p, x):
    if p[x] == x:
        return x
    p[x] = find(p, p[x])
    return p[x]

def union(p, x, y):
    p[find(p, y)] = find(p, x)
    find(p, y)

# ----------------------------------------

def solution():
    N, M, T = map(int, input().split())
    p = [n for n in range(N + 5)]
    arr = []

    for _ in range(M):
        n1, n2, cost = map(int, input().split())
        heapq.heappush(arr, (cost, n1, n2))
        
    cnt = 0
    ans = 0

    while arr:
        cost, n1, n2 = heapq.heappop(arr)
        if find(p, n1) != find(p, n2):
            union(p, n1, n2)
            print(cost)
            ans += cost + cnt * T
            cnt += 1

    return ans

# ----------------------------------------
T = int(input())

for _ in range(T):
    my_ans = solution()

    ans = input().rstrip()
    print(f'ans = {ans}', f'my_ans = {my_ans}', sep="\t")
