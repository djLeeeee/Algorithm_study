
""" https://www.acmicpc.net/problem/1747
---------------------------------------------------------------------
메모리 (39,300 KB) | 시간 (320 ms) |
---------------------------------------------------------------------
decimal: 크기가 1,030,001인 array | index에 해당하는 숫자가 소수인지 표시
1) 1,030,001 의 제곱근 값까지 소수 체크 (for문 X for문)
    - 1,000,001 은 index error 발생
2) answer = N (∵ N 보다 크거나 같은 값이기 때문에)
3) 소수값이 아니거나 펠린드롬이 아니라면 => answer += 1
4) 만족할 때까지 과정 2~3 반복
"""

import sys
sys.stdin = open("input/1747.txt")
input = sys.stdin.readline

N = input()

arr_range = 1_030_001
decimal = [1] * (arr_range)
decimal[0] = decimal[1] = 0
for num in range(2, int(pow(arr_range, 1/2)) + 1):
    if decimal[num]:
        for num2 in range(num * 2, arr_range, num):
            decimal[num2] = 0

ans = int(N)
while not decimal[ans] or str(ans) != str(ans)[::-1]:
    ans += 1


print(ans)
