# 백준 3649번 로봇 프로젝트 - 시간초과

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
    except ValueError or EOFError:
        break
    n = int(input())
    blocks = []
    ans = []
    for _ in range(n):
        block = int(input())
        for b in blocks:
            if b + block == x:
                if b <= block:
                    ans.append((b, block))
                else:
                    ans.append((block, b))
        blocks.append(block)
if len(ans):
    ans.sort()
    print('yes', *ans[0])
else:
    print('danger')