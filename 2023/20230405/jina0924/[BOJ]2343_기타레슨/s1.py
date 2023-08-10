# 백준 2343번 기타 레슨

import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())            # N, M: 강의의 수, 블루레이 개수
data = list(map(int, input().split()))
left, right = max(data), sum(data)          # left, right: 블루레이 크기 중 최소값, 최대값
while left <= right:
    mid = (left + right) // 2               # mid: 현재 살펴볼 블루레이 크기
    tmp, cnt = 0, 0                         # tmp, cnt: mid크기 만큼 담을 변수, mid크기일 때 블루레이 개수
    for i in range(len(data)):
        if tmp + data[i] > mid:
            cnt += 1
            tmp = 0
        tmp += data[i]
    else:                                   # for문 다 돌고 tmp값 있으면 블루레이 하나 더 만들기
        if tmp:
            cnt += 1
    if cnt > M:                             # 블루레이 개수 초과하면 mid값 키워보기
        left = mid + 1
    else:
        right = mid - 1
print(left)                                 # 블루레이 개수 맞아떨어져도 right값 갱신되므로 left가 최종값