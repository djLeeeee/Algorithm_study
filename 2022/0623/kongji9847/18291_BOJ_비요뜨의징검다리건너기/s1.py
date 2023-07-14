'''
실수한 부분:
1) 메모리 초과: N = 1일 때, power 함수에서 k가 음수일 때, 무한 recursion 일어난다.
2) 시간 초과 방지: power 연산할 때마다 1000000007로 나눈 나머지를 return 하여 사용하기
나머지를 구하는 것이라면, 거듭제곱을 계산할 때마다 나머지를 구해서 나머지끼리 곱해도 답은 같다.

11 * 11 = 121 -> 7로 나눈 나머지: 2
11을 7로 나눈 나머지 : 4
4 * 4 = 16 -> 7로 나눈 나머지 : 2

증명:
(7 + 4) * (7 + 4) = (7)**2 + 8*(7) + 16(=4*4: 나머지 끼리)
7로 나누면 어차피 나머지끼리 곱해진 값 남음 -> 여기서 나머지를 결정함
따라서 11*11을 7로 나눈 나머지나 4*4를 7로 나눈 나머지는 같다.
'''

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 거듭제곱 분할정복 -> 재귀함수 사용
def power(n, k):
    # 종료
    if k == 0:
        return 1

    # 진행
    half = power(n, k // 2) % A
    if k % 2:
        return n * half * half % A
    else:
        return half * half % A


T = int(input())
A = 1000000007
for tc in range(1, T+1):
    N = int(input())
    if N == 1:
        print(1)
    else:
        print(power(2, N-2) % A)