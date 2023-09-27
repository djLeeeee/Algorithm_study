# 물통
# https://www.acmicpc.net/problem/14867
import sys
sys.stdin = open("./input/quiz1.txt")
input = sys.stdin.readline
from collections import deque
# 골2 ----------------------------------------

def empty(que: list, a: int, b: int):
    cur_cnt = check[a][b]
    for na in [0, A_LIMIT]:
        if check[na][b] > cur_cnt + 1:
            check[na][b] = cur_cnt + 1
            que.append((na, b))

    for nb in [0, B_LIMIT]:
        if check[a][nb] > cur_cnt + 1:
            check[a][nb] = cur_cnt + 1
            que.append((a, nb))


def fill(que: list, a: int, b: int):
    cur_cnt = check[a][b]
    for (na, nb) in [(a, B_LIMIT), (A_LIMIT, b)]:
        if check[na][nb] > cur_cnt + 1:
            check[na][nb] = cur_cnt + 1
            que.append((na, nb))

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
    cur_cnt = check[a][b]
    
    for (na, nb) in pour(a, b):
        if na < 0 or nb < 0:
            continue
        if check[na][nb] > cur_cnt + 1:
            check[na][nb] = cur_cnt + 1
            que.append((na, nb))

# --------------------------------------------
A_LIMIT, B_LIMIT, A_GOAL, B_GOAL = map(int, input().split())

check = [[sys.maxsize] * (B_LIMIT + 1) for _ in range(A_LIMIT + 1)]
check[0][0] = 0

que = deque([(0, 0)])
while que:
    a, b= que.popleft()
    if a == A_GOAL and b == B_GOAL:
        break
    
    empty(que, a, b)
    fill(que, a, b)
    move(que, a, b)

ans = check[A_GOAL][B_GOAL]
print(ans if ans != sys.maxsize else -1)
