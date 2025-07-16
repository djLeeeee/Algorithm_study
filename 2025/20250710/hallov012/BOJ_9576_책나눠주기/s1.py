import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    needs = [tuple(map(int, input().split())) for _ in range(m)]
    needs.sort(key=lambda x: (x[1], x[0]))
    ans = 0
    visited = [0] * (n+1)
    for a, b in needs:
        for i in range(a, b+1):
            if not visited[i]:
                visited[i] = 1
                ans += 1
                break
    print(ans)