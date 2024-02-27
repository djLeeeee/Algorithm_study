from collections import deque
import sys
sys.stdin = open('input.txt')

N = int(input())
nlst = list(map(int, input().split()))

stack = deque()
ans = [0]*N
for i in range(N):
    if len(stack) == 0:
        ans[i] = 0
        stack.append((i, nlst[i]))
    else:
        idx = len(stack)-1
        while idx >= 0:
            if stack[idx][1] > nlst[i]:
                ans[i] = stack[idx][0]+1
                break
            else:
                stack.pop()
            idx -= 1
        stack.append((i, nlst[i]))
print(' '.join(map(str, ans)))