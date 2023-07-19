import sys
from itertools import combinations
sys.stdin = open('input.txt')

s = input().rstrip()
n = len(s)
stack = []
check = [0] * n
cnt = 1
for i in range(n):
    char = s[i]
    if char == '(':
        stack.append(i)
    elif char == ')':
        j = stack.pop()
        check[i] = check[j] = cnt
        cnt += 1

ans = set()
for i in range(1, cnt):
    cases = combinations(range(1, cnt), i)
    for case in cases:
        temp = ''
        for j in range(n):
            if check[j] not in case:
                temp += s[j]
        ans.add(temp)

for str in sorted(list(ans)):
    print(str)


