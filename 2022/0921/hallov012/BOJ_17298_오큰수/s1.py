import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
ans = [0] * n
stack = []
for i in range(n):
    if not stack:
        stack.append(i)
    else:
        # 이전에 나온 수가 현재보다 작다면 현재의 값이 이전 수의 오큰수가 된다
        if nums[stack[-1]] < nums[i]:
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        # 이전에 나온 수가 현재보다 크면 답이 될 수 없으므로 그냥 append
        else:
            stack.append(i)

for i in range(n):
    # 맨 마지막 수는 항상 오큰수가 없음
    if i == n-1:
        print(-1)
    else:
        if not ans[i]:
            print(-1, end=" ")
        else:
            print(ans[i], end=" ")