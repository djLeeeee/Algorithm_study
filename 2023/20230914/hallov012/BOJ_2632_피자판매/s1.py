import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def sub_sum(lst, l):
    sum_dict = defaultdict(int)
    sum_dict[0] += 1
    sum_dict[sum(lst)] += 1
    for i in range(l):
        cnt = lst[i]
        sum_dict[cnt] += 1
        for j in range(1, l-1):
            cnt += lst[(i+j) % l]
            sum_dict[cnt] += 1
    return sum_dict

input = sys.stdin.readline

t = int(input())
m, n = map(int, input().split())
A = list(int(input()) for _ in range(m))
B = list(int(input()) for _ in range(n))

a_sum = sub_sum(A, m)
b_sum = sub_sum(B, n)

ans = a_sum[t] + b_sum[t]
for i in range(1, t):
    if a_sum[i] and b_sum[t-i]:
        ans += a_sum[i] * b_sum[t-i]
print(ans)