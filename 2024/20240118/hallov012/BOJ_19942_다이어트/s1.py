import sys
sys.stdin = open('input.txt')

def find(idx, cost, cnt):
    global ans, ans_lst
    if cost > ans:
       return
    if idx == n-1:
       for k in range(4):
           if cnt[k] < m_lst[k]:
               break
       else:
           lst = []
           for q in range(n):
               if visited[q]:
                   lst.append(q+1)
           if ans == cost:
               ans_lst.append(lst)
           else:
               ans_lst = [lst]
               ans = cost
       return
    for i in range(idx+1, n):
        if not visited[i]:
            visited[i] = 1
            temp = [0] * 4
            for j in range(4):
                temp[j] = cnt[j] + data[i][j]
            find(i, cost+data[i][4], temp)
            visited[i] = 0
            find(i, cost, cnt)

input = sys.stdin.readline

n = int(input())
m_lst = list(map(int, input().split()))

data = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
ans = sys.maxsize
ans_lst = []
find(-1, 0, [0] * 4)

if ans != sys.maxsize:
    print(ans)
    print(*sorted(ans_lst)[0])
else:
    print(-1)
