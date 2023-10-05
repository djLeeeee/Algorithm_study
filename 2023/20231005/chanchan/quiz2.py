# 세 수의 합
# https://www.acmicpc.net/problem/2295'
import sys
sys.stdin = open("./input/quiz2.txt")
input = sys.stdin.readline
# ----------------------------------------

def solution():
    N = int(input())
    U = sorted([int(input()) for _ in range(N)])
    U2 = []
    for i in range(N):
        for j in range(i, N):
            U2.append(U[i] + U[j])
    
    U2 = set(U2)
    ans = 0
    for i in range(N):
        for j in range(i, N):
            rest = U[j] - U[i]
            if rest in U2:
                ans = max(ans, U[i] + rest)
    return ans


    


    

# ----------------------------------------
T = int(input())

for _ in range(T):
    my_ans = solution()

    ans = input().rstrip()
    print(f'ans = {ans}', f'my_ans = {my_ans}', sep="\t")
