def permutation(n, cnt, amt):
    global mins
    if cnt == N:
        if arr[n][i]:
            mins = min(mins, amt + arr[n][i])
            return

    if amt >= mins:
        return

    for a in range(N):
        if arr[n][a] and not visited[a]:
            visited[a] = 1
            permutation(a, cnt+1, amt + arr[n][a])
            visited[a] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
mins = float('inf')

for i in range(N):
    visited = [0] * N
    visited[i] = 1
    permutation(i, 1, 0)
print(mins)