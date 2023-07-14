from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = [0] * n
deck = deque()
for k in range(n):
    while deck and arr[deck[-1]] >= arr[k]:
        deck.pop()
    while deck and deck[0] <= k - m:
        deck.popleft()
    deck.append(k)
    ans[k] = arr[deck[0]]
print(*ans)
