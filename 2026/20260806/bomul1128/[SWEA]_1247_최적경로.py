# Problem: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=5&problemLevel=6&contestProbId=AV15OZ4qAPICFAYD&categoryId=AV15OZ4qAPICFAYD&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=6&pageSize=10&pageIndex=1
# Submission: 2026-08-12 20:44 / Python / Pass
from collections import deque
 
 
def main():
    def dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
 
    n = int(input())
    raw = map(int, input().split())
    pts = []
    start = (next(raw), next(raw))
    end = (next(raw), next(raw))
    for _ in range(n):
        pts.append((next(raw), next(raw)))
    que = deque()
    dp = [[-1] * (1 << n) for _ in range(n)]
    for i, p in enumerate(pts):
        dp[i][1 << i] = dist(start, p)
        que.append((i, 1 << i))
    while que:
        i, mask = que.popleft()
        for j, p in enumerate(pts):
            if mask & (1 << j):
                continue
            new_mask = mask | (1 << j)
            new_dist = dp[i][mask] + dist(pts[i], p)
            old_dist = dp[j][new_mask]
            if old_dist == -1:
                dp[j][new_mask] = new_dist
                que.append((j, new_mask))
            elif new_dist < old_dist:
                dp[j][new_mask] = new_dist
    return min(dp[i][-1] + dist(pts[i], end) for i in range(n))
 
 
if __name__ == "__main__":
    for tc in range(int(input())):
        ans = main()
        print(f"#{tc + 1}: {ans}")
