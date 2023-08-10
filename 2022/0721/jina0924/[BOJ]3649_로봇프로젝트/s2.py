# 백준 3649번 로봇 프로젝트 - 시간초과

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import combinations

while True:
    try:
        x = int(input()) * 10000000
    except ValueError or EOFError:
        break
    n = int(input())
    blocks = []
    ans = []
    for _ in range(n):
        blocks.append(int(input()))
    for comb in combinations(blocks, 2):
        if sum(comb) == x:
            l1, l2 = comb[0], comb[1]
            if l1 <= l2:
                ans.append((l1, l2))
            else:
                ans.append((l2, l1))
    if len(ans):
        ans.sort()
        print('yes', *ans[0])
    else:
        print('danger')