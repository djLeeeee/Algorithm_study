import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
h_lst = [int(input()) for _ in range(n)]
ans = 0
stack = []
for h in h_lst:
    # 해당 빌딩을 못보는 요소를 pop
    while stack and stack[-1] <= h:
        stack.pop()
    stack.append(h)
    # 가장 나중에 append 된 빌딩을 이 전에 추가된 빌딩이 볼 수 있음
    ans += len(stack)-1

print(ans)

