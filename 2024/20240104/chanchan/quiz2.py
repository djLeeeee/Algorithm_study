# 입국심사
# https://www.acmicpc.net/problem/3079
import sys
sys.stdin = open("./input/quiz2.txt")
input = sys.stdin.readline

# ----------------------------------------

# ----------------------------------------

def solution():
    N, M = map(int, input().split())
    times =[int(input()) for _ in range(N)]

    s, e = min(times), max(times) * M
    ans = e

    while s <= e:
        tot = 0
        mid = (s + e) // 2

        for time in times:
            tot += mid // time

        if tot >= M:
            e = mid - 1
            ans = min(mid, ans)
        else:
            s = mid + 1
        
    return ans

# ----------------------------------------

for _ in range(2):
    res = solution()
    print(res)