# 백준 13975번 파일 합치기3

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

T = int(input())                        # T: 테스트 케이스 개수
for tc in range(T):
    K = int(input())                    # K: 소설 장 수
    data = sorted(list(map(int, input().split())))
    ans = 0
    while len(data) > 1:                # 합칠 수 있는 파일이 있을 때까지 반복
        a = heapq.heappop(data)
        b = heapq.heappop(data)
        ans += a + b
        heapq.heappush(data, a + b)
    print(ans)