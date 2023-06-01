# 백준 2812번 크게 만들기

import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
num = list(input())

'''
1. 일단 ans에 숫자 넣어둠
2. 만약 지울 수 있는 횟수가 남아있고(K > 0) ans에 빼낼 숫자가 있고(ans) 마지막 숫자가 현재 살펴보는 숫자보다 작다면(ans[-1] < num[i])
3. ans에 남아있는 숫자가 현재 숫자보다 크거나 같을때까지 pop & K 1씩 줄이기
'''
ans = []
for i in range(N):
    while K and ans and ans[-1] < num[i]:
        K -= 1
        ans.pop()
    ans.append(num[i])
print(''.join(ans[:len(ans) - K]))