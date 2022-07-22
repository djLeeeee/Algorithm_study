# 백준 3649번 로봇 프로젝트

import sys
sys.stdin = open('input2.txt')
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
    except ValueError or EOFError:
        break
    n = int(input())
    blocks = [int(input()) for _ in range(n)]
    blocks.sort()
    l1, l2 = 0, len(blocks) - 1
    found = False
    while l1 < l2:
        if blocks[l1] + blocks[l2] == x:
            print(f'yes {blocks[l1]} {blocks[l2]}')
            found = True
            break
        elif blocks[l1] + blocks[l2] > x:
            l2 -= 1
        elif blocks[l1] + blocks[l2] < x:
            l1 += 1
    if not found:
        print('danger')