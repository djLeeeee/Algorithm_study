# 물통
# https://www.acmicpc.net/problem/14867
import sys
sys.stdin = open("./input/quiz1.txt")
input = sys.stdin.readline
from collections import deque
# 골2 ----------------------------------------

def get_and_set_que(que, a, b, cnt):
    if not check.get((a, b)):
        check[(a, b)] = cnt + 1
        que.append((a, b))

def empty(que: list, a: int, b: int):
    cur_cnt = check[(a, b)]
    for na in [0, A_LIMIT]:
        get_and_set_que(que, na, b, cur_cnt)

    for nb in [0, B_LIMIT]:
        get_and_set_que(que, a, nb, cur_cnt)


def fill(que: list, a: int, b: int):
    cur_cnt = check[(a, b)]
    for (na, nb) in [(a, B_LIMIT), (A_LIMIT, b)]:
        get_and_set_que(que, na, nb, cur_cnt)

def pour(a, b):
    ret_val = []
    a_avail, b_avail = A_LIMIT - a, B_LIMIT - b

    if a <= b_avail:
        ret_val.append((0, a + b))
    else:
        ret_val.append((a - b_avail, B_LIMIT))

    if b <= a_avail:
        ret_val.append((a + b, 0))
    else:
        ret_val.append((A_LIMIT, b - a_avail))
    
    return ret_val


def move(que: list, a: int, b: int):
    cur_cnt = check[(a, b)]
    
    for (na, nb) in pour(a, b):
        if na < 0 or nb < 0:
            continue
        get_and_set_que(que, na, nb, cur_cnt)

# --------------------------------------------
A_LIMIT, B_LIMIT, A_GOAL, B_GOAL = map(int, input().split())

check = {}
check[(0, 0)] = 0

que = deque([(0, 0)])
while que:
    a, b= que.popleft()
    if a == A_GOAL and b == B_GOAL:
        break
    
    empty(que, a, b)
    fill(que, a, b)
    move(que, a, b)

ans = check.get((A_GOAL, B_GOAL), -1)
print(ans)
