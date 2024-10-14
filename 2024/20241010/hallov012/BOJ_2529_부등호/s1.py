import sys
sys.stdin = open('input.txt')

def find(tmp, cnt, last):
    global max_ans, min_ans
    if cnt == k:
        if not min_ans:
            min_ans = tmp
        else:
            max_ans = tmp
        return
    if orders[cnt] == '>':
        for i in range(last):
            if not visited[i]:
                visited[i] = 1
                find(tmp+str(i), cnt+1, i)
                visited[i] = 0
    else:
        for i in range(last+1, 10):
            if not visited[i]:
                visited[i] = 1
                find(tmp+str(i), cnt+1, i)
                visited[i] = 0

k = int(input())
orders = list(map(str, input().split()))
visited = [0] * 10
max_ans, min_ans = '', ''
for i in range(10):
    visited[i] = 1
    find(str(i), 0, i)
    visited[i] = 0
print(max_ans)
print(min_ans)