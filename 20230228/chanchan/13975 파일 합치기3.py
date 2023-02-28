''' https://www.acmicpc.net/problem/13975
---------------------------------------------------------------------
메모리 (152,944KB) | 시간 (5,356 ms) | 채점 결과 나오기까지 5분이나 걸리네
---------------------------------------------------------------------
최소힙을 활용해서 숫자 중 가장 작은 두 숫자를 활용한다.
1) 두 숫자를 heap_pop 한다 => n1(가장 작은 숫자), n2(다음으로 작은 숫자)
2) n1 + n2 를 heap_push 한다.
3) n1 + n2 값을 answer 에 더한다.
4) heap에 원소가 하나만 남을 때까지 과정 1 ~ 3을 반복한다.
'''
import sys
import heapq
sys.stdin = open("input/13975.txt")
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    N = int(input())
    nums = []
    for num in map(int, input().split()):
        heapq.heappush(nums, num)  # 기본 세팅

    ans = 0
    while len(nums) != 1:
        n1 = heapq.heappop(nums)        # 1)
        n2 = heapq.heappop(nums)        # 1)
        heapq.heappush(nums, n1 + n2)   # 2)
        ans += (n1 + n2)                # 3)

    print(ans)
