import sys
from collections import deque
sys.stdin = open('input.txt')

def check():
    visited = [0] * 25
    visited[group[0]] = 1
    que = deque([group[0]])
    cnt = 1
    while que:
        x = que.popleft()
        for i in range(4):
            # 우측으로 이동할 때 제일 오른쪽에 있는 거면 취소
            if i == 2:
                if x % 5 == 4:
                    continue
            elif i == 3:
                if not x % 5:
                    continue
            nx = x + d[i]
            if 0 <= nx < 25 and not visited[nx] and nx in group:
                que.append(nx)
                visited[nx] = 1
                cnt += 1
    return True if cnt == 7 else False

def dfs(idx, cnt, y_cnt):
    global ans
    # 임다솜파가 다수거나, 앞으로 7명을 채울 수 없을 때
    if y_cnt >= 4 or 25 - idx + cnt < 7:
        return
    if cnt == 7:
        if check():
            ans += 1
        return
    group.append(idx)
    if arr[idx] == 'S':
        dfs(idx+1, cnt+1, y_cnt)
    else:
        dfs(idx+1, cnt+1, y_cnt+1)
    group.pop()
    dfs(idx+1, cnt, y_cnt)

input = sys.stdin.readline

arr = ''
for _ in range(5):
    line = input().rstrip()
    arr += line
d = [5, -5, 1, -1]
ans = 0
group = []
dfs(0, 0, 0)
print(ans)