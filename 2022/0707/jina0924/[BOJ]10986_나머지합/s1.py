# 백준 10986번 나머지 합

import sys
sys.stdin = open('input1.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
data = list(map(int, input().split()))

remainder = [0] * M                 # 나머지는 0 ~ M-1

remainder[data[0] % M] += 1         # 누적합 하기 전에 맨 처음 값의 나머지 먼저 카운팅 해놓기

for i in range(1, N):
    data[i] += data[i-1]            # 첫 번째 값부터 현재 위치 값까지 누적합
    remainder[data[i] % M] += 1     # 누적합의 나머지 카운팅

cnt = remainder[0]                  # 누적합의 나머지가 0인 부분 먼저 카운팅에 올려둠

'''
위에서 구한 누적합 : 0 ~ i까지 전부 더한 값
나머지가 같은 누적합 중 2개 고름 ex) 0 ~ 1, 0 ~ 4 누적합 고름
=> 두 누적합을 빼게 되면 나머지가 0인 구간 합이 됨 ex) 1 ~ 4 구간합이 0이 됨
=> remainder에서 두 개를 조합하면 구간합 0 만들어짐
'''
for r in remainder:
    cnt += r * (r-1) // 2

print(cnt)