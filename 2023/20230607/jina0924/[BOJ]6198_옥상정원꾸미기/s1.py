# 백준 6198번 옥상 정원 꾸미기

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())                        # 빌딩의 개수
stack = []
ans = 0
for _ in range(N):
    h = int(input())
    while stack and stack[-1] <= h:     # 현재 높이가 제일 위에 쌓인 높이보다 클때까지 pop
        stack.pop()
    ans += len(stack)                   # 쌓인 높이들 = 현재 높이를 볼 수 있는 빌딩의 수
    stack.append(h)
print(ans)