import sys
from collections import deque
sys.stdin = open('input.txt')

n, k = map(int, input().split())
ans = []
que = deque([])
str_n_list = list(map(str, str(n)))
que.append((str_n_list, 0))
l = len(str_n_list)

visited = set()
while que:
    now, cnt = que.popleft()
    if cnt == k:
        ans = max(ans, now)
        continue
    for i in range(l-1):
        for j in range(i+1, l):
            if i == 0 and now[j] == 0:
                continue
            now[i], now[j] = now[j], now[i]
            temp = (now[::], cnt+1)
            temp_key = ('').join(now)
            if (temp_key, cnt+1) not in visited:
                visited.add((temp_key, cnt+1))
                que.append(temp)
            now[i], now[j] = now[j], now[i]

print(int(('').join(ans)) if ans else -1)
