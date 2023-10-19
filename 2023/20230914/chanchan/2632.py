# https://www.acmicpc.net/problem/2632
import sys
sys.stdin = open("./input/2632.txt")
input = sys.stdin.readline
# 골2 ------------------------------------

def get_avail_size(pizza):
    SIZE = len(pizza)
    ret_dict = {}
    for idx in range(SIZE):
        pieces = pizza[idx:] + pizza[:idx]
        tot = 0
        for p in pieces:
            tot += p
            ret_dict[tot] = ret_dict.get(tot, 0) + 1
    ret_dict[sum(pizza)] = 1
    return ret_dict

# ----------------------------------------
GOAL_SIZE = int(input())
M, N = map(int, input().split())
PIZ1 = [int(input()) for _ in range(M)]
PIZ2 = [int(input()) for _ in range(N)]

PIZ1_AVAIL_SIZE = get_avail_size(PIZ1)
PIZ2_AVAIL_SIZE = get_avail_size(PIZ2)
# ----------------------------------------

ans = 0
for p1 in PIZ1_AVAIL_SIZE:
    rest = GOAL_SIZE - p1
    if rest > 0 and rest in PIZ2_AVAIL_SIZE:
        ans += PIZ1_AVAIL_SIZE[p1] * PIZ2_AVAIL_SIZE[rest]
        
ans += PIZ1_AVAIL_SIZE.get(GOAL_SIZE, 0) + PIZ2_AVAIL_SIZE.get(GOAL_SIZE, 0)

print(ans)
