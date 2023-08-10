import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    p = input()
    n = int(input())
    nums = input().strip()[1:-1].split(',')
    if nums == ['']:
        if 'D' in p:
            print('error')
            continue
    nums_lst = deque(nums)
    r_cnt = 0
    check = True
    for command in p:
        if command == 'R':
            r_cnt += 1
        elif command == 'D':
            if nums_lst:
                if not r_cnt % 2:
                    nums_lst.popleft()
                else:
                    nums_lst.pop()
            else:
                check = False
                break
    if not check:
        print('error')
    else:
        if r_cnt % 2:
            nums_lst.reverse()
        print('[' + ','.join(nums_lst) + ']')


