import sys
sys.stdin = open('input.txt')

def find(idx, cnt):
    global ans
    if idx == 11:
        ans = max(ans, cnt)
        return
    for i in range(11):
        if data[idx][i] and not visited[i]:
            visited[i] = 1
            find(idx+1, cnt+data[idx][i])
            visited[i] = 0

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    data = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    ans = 0
    find(0, 0)
    print(ans)