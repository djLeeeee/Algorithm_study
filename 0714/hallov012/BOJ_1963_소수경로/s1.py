import sys, math
from collections import deque
sys.stdin = open('input.txt')

# 에라토스테네스의 체를 이용해 max값인 9999까지의 소수를 체크해줌
m = 10000
nums = [1] * m
for i in range(2, int(math.sqrt(m))+1):
    if nums[i]:
        for j in range(2*i, m, i):
            nums[j] = 0

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    visited = [0] * m
    que = deque([a])
    visited[int(a)] = 1
    while que:
        now = que.popleft()
        if visited[b]:
            break
        # 일의 자리부터 숫자 바꿔보기
        for i in range(4):
            # 1033 을 1000으로 나눈 경우 나머지는 033이 아닌 33으로 나오기 때문에 오류 발생
            if now % (10 ** (i + 1)) < 10 ** i:
                origin = 0
            else:
                origin = int(str(now % (10 ** (i + 1)))[0])
            for j in range(10):
                if origin != j:
                    diff = j - origin
                    temp = now + diff * (10**i)
                    if temp >= 1000 and nums[temp] and not visited[temp]:
                        visited[temp] = visited[now] + 1
                        que.append(temp)

    if visited[b] == 0:
        print('Impossible')
    else:
        print(visited[b]-1)




