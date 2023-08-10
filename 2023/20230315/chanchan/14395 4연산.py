# https://www.acmicpc.net/problem/14395
import sys
from collections import deque
sys.stdin = open("input/14395.txt")
input = sys.stdin.readline

def calculate(opr, num):
    if (opr == 0):
        return (num * num)
    elif (opr == 1):
        return (num + num)
    elif (opr == 2):
        return 1

operator = list("*+/")
    
ans = -1
s, t = map(int, input().split())

if (s == t):
    print(0)
else:  
    check = set()
    check.add(s)
    que = deque()
    que.append((s, ""))

    while que:
        cn, opr = que.popleft()
        if (cn == t):
            ans = opr
            break
        
        for d in range(3):
            nn = calculate(d, cn)
            if (0<= nn <= 10 ** 9 and nn not in check):
                check.add(nn)
                que.append((nn, opr + operator[d]))

    print(ans)