import sys
sys.stdin = open('input.txt')

n = int(input())
S = input().rstrip()
if len(S) <= n:
    print(len(S))
    exit()

left, right = 0, 1
tmp = set()
tmp.add(S[left])
ans = 0
while left <= right:
    if right == len(S):
        ans = max(ans, right-left)
        break
    tmp.add(S[right])
    if len(tmp) == n:
        ans = max(ans, right-left+1)
        right += 1
    elif len(tmp) > n:
        tmp = set()
        left += 1
        right = left + 1
        tmp.add(S[left])
    else:
        right += 1

print(ans)