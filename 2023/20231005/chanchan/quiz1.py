# 사과나무
# https://www.acmicpc.net/problem/19539
import sys
sys.stdin = open("./input/quiz1.txt")
input = sys.stdin.readline
# ----------------------------------------

def solution():
    N = int(input())
    trees = list(map(int, input().split()))
    cnts = 0
    TOTAL = sum(trees)

    if TOTAL % 3:
        return "NO"
    for tree in trees : 
        cnts += tree//2

    return ("YES" if cnts >= TOTAL//3 else "NO")

# --------------------------------------------
T = int(input())

for _ in range(T):
    my_ans = solution()

    ans = input().rstrip()
    print(f'ans = {ans}', f'my_ans = {my_ans}', sep="\t")
