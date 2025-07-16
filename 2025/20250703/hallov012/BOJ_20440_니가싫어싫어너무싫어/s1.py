import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

enter_exit = defaultdict(int)
n = int(input())
for _ in range(n):
    e, x = map(int, input().split())
    enter_exit[e] += 1
    enter_exit[x] -= 1

times = sorted(enter_exit.keys())

ans_cnt = -1
ans_range = [None, None]

cnt = 0
flag = True
for t in times:
    cnt += enter_exit[t]
    if cnt > ans_cnt:
        ans_cnt = cnt
        ans_range[0] = t
        flag = True
    elif cnt < ans_cnt and flag:
        ans_range[1] = t
        flag = False

print(ans_cnt)
print(*ans_range)