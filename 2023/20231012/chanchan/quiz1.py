# 올바른 괄호
# https://www.acmicpc.net/problem/24552
import sys
sys.stdin = open("./input/quiz1.txt")
input = sys.stdin.readline
# ----------------------------------------

def solution():
    p_check = {"(": 0, ")": 0}
    cnts = 0

    P = input().rstrip()

    for p in P:
        p_check[p] += 1
        cnts += 1 if p == "(" else -1
        
        if cnts < 0:
            return p_check[")"]
        if cnts == 0:
            p_check["("] = 0

    if cnts:
        return p_check["("]
    
    return 0
        


# --------------------------------------------
T = int(input())

for _ in range(T):
    my_ans = solution()

    ans = input().rstrip()
    print(f'ans = {ans}', f'my_ans = {my_ans}', sep="\t")
