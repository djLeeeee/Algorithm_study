import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def sub_sum(lst, l):
    cnt_dict = defaultdict(int)
    keys = set()
    for i in range(l):
        cnt = 0
        for j in range(i, l):
            cnt += lst[j]
            cnt_dict[cnt] += 1
            keys.add(cnt)
    sort_keys = sorted(list(keys))
    return cnt_dict, sort_keys

input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

a_sum, a_keys = sub_sum(A, n)
b_sum, b_keys = sub_sum(B, m)

ans = 0
l, r = 0, len(b_keys)-1
while l < len(a_keys) and r >= 0:
    tmp = a_keys[l] + b_keys[r]
    if tmp == T:
        ans += a_sum[a_keys[l]] * b_sum[b_keys[r]]
        l += 1
        r -= 1
    elif tmp > T:
        r -= 1
    else:
        l += 1

print(ans)
