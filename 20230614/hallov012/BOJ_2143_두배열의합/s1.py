import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def sub_sum(lst, sum_dict, length):
    for i in range(length):
        cnt = 0
        for j in range(i, length):
            cnt += lst[j]
            sum_dict[cnt] += 1

input = sys.stdin.readline

t = int(input())
n = int(input())
a_lst = list(map(int, input().split()))
m = int(input())
b_lst = list(map(int, input().split()))

a_sum = defaultdict(int)
b_sum = defaultdict(int)
sub_sum(a_lst, a_sum, n)
sub_sum(b_lst, b_sum, m)

# ans = 0
# for key, value in a_sum.items():
#     if b_sum[t-key]:
#         ans += value * b_sum[t-key]
# print(ans)

ans = 0
a_key = sorted(a_sum.keys())
b_key = sorted(b_sum.keys())
left, right = 0, len(b_key) - 1
while left < len(a_key) and right >= 0:
    temp = a_key[left] + b_key[right]
    if temp == t:
        ans += a_sum[a_key[left]] * b_sum[b_key[right]]
        left += 1
        right -= 1
    elif temp > t:
        right -= 1
    else:
        left += 1

print(ans)

