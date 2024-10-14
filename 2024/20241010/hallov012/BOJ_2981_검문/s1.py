import sys, math
sys.stdin = open('input.txt')

open = sys.stdin.readline
"""
두 양의 정수 a, b(a > b)에 대해서 a = bq + r 이라 했을 때,
a, b의 최대 공약수는 b, r의 최대 공약수와 같음
gcb(a, b) = gcd(b, r)

n0 = s0*m + r
n1 = s1*m + r
n2 = s2*m + r
----------------
n1 - n0 = m(s1 - s0) => s1 - s0은 n1 - n0의 약수
n2 - n1 = m(s2 - s1) => s2 - s1은 n2 - n1의 약수
m은 공통으로 들어가는 부분이니, s'i - s'i-1 들의 최대 공약수를 찾는다
"""
n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

gab = []
for i in range(1, n):
    gab.append(nums[i] - nums[i-1])

tmp = gab[0]
for i in range(1, n-1):
    tmp = math.gcd(tmp, gab[i])

ans = set()
for i in range(2, int(tmp**0.5)+1):
    if not tmp % i:
        ans.add(i)
        ans.add(tmp // i)
ans.add(tmp)

print(*sorted(list(ans)))