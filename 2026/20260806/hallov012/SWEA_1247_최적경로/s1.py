import sys
sys.stdin = open('input.txt')

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def dfs(now, cnt, total):
    global ans
    if cnt == n:
        total += dist(now, home)
        ans = min(ans, total)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            next_d = dist(now, customers[i])
            dfs(customers[i], cnt+1, total + next_d)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))

    company = (data[0], data[1])
    home = (data[2], data[3])

    customers = []
    for i in range(n):
        customers.append((data[4 + i*2], data[5 + i*2]))

    visited = [0] * n
    ans = float('inf')
    dfs(company, 0, 0)

    print(f"#{tc} {ans}")


