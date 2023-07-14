import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
nums = list(input())
stack = []
cnt = 0
for i in range(n):
    num = nums[i]
    if not stack or cnt == k:
        stack.append(num)
    else:
        while stack and stack[-1] < num:
            stack.pop()
            cnt += 1
            if cnt == k:
                break
        stack.append(num)

if cnt < k:
    print(''.join(stack[:n-k]))
else:
    print(''.join(stack))
