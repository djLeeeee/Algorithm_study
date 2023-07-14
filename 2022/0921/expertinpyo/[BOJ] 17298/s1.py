# 오큰수
# 오른쪽에 있으면서 Ai보다 큰 수중에 가장 왼쪽에 있는 수
# stack

N = int(input())
arr = list(map(int,input().split()))
stack = [arr[-1]] # 크기 비교를 위한 것
ans = [-1] * N
for i in range(N-2, -1, -1):
    while stack:
        if arr[i] < stack[-1]:
            ans[i] = stack[-1]
            break
        stack.pop()
    stack.append(arr[i])
print(*ans)
