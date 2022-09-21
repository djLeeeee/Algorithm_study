import sys
sys.stdin = open('input.txt')
from collections import deque

N = int(input())
nums = list(map(int, input().split()))

# 오큰수가 없을 경우 -1을 출력해야 하므로, -1로 초기화
answer = [-1] * N
stack = deque()

for i in range(N):
    # 스택에 원소가 있고, 스택의 마지막 원소가 지금 보는 숫자보다 작으면
    # 지금 보는 숫자가 오큰수가 됨
    while stack and nums[stack[-1]] < nums[i]:
        # 오큰수를 찾았으므로, pop해서
        idx = stack.pop()
        # 정답 배열에 갱신해줌
        answer[idx] = nums[i]
    # 그 외의 경우에는 아직 오큰수를 못찾았으므로, 스택에 추가
    stack.append(i)
print(*answer)