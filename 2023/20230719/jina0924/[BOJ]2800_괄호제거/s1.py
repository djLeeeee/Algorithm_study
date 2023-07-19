# 백준 2800번 괄호 제거

import sys
sys.stdin = open('input.txt')
from itertools import combinations as C

data = input()
brackets = []

stack = []
for i in range(len(data)):
    if data[i] == '(':
        stack.append(i)
    elif data[i] == ')':
        s = stack.pop()
        brackets.append((s, i))

ans = set()
cnt = len(brackets)
for n in range(1, cnt + 1):
    comb = C(brackets, n)
    for c in comb:
        result = list(data)
        for s, e in c:
            result[s], result[e] = '', ''
        ans.add(''.join(result))

for a in sorted(ans):
    print(a)