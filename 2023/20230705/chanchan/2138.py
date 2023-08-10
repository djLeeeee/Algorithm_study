# https://www.acmicpc.net/problem/2138
import sys
input = sys.stdin.readline
sys.stdin = open("./input/2138.txt")
# ----------------------------------------
N = int(input())
bf = list(map(int, input().rstrip()))
af = list(map(int, input().rstrip()))


def switch(A, B):
    tmp = A[:]
    press = 0
    for i in range(1, N):
        
        if tmp[i - 1] == B[i - 1]:
            continue
        
        press += 1
        for j in range(i - 1, i + 2):
            if j < N:
                tmp[j] = 1 - tmp[j]
    if tmp == B:
        return press 
    else:
        return sys.maxsize

res = switch(bf, af)

bf[0] = 1 - bf[0]
bf[1] = 1 - bf[1]

res = min(res, switch(bf, af) + 1)
if res != sys.maxsize:
    print(res)
else:
    print(-1)
