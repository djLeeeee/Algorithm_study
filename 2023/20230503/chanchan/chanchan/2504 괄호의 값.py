# https://www.acmicpc.net/problem/2504
import sys
sys.stdin = open("./input/2504.txt")
input = sys.stdin.readline

all_stk = []
paren_stk = []

pair = {
    "]": "[",
    ")": "("
}

for t in input():
    print(all_stk)
    if t in ("[", "("):
        all_stk.append(t)
        paren_stk.append(t)
        continue

    if not paren_stk or pair[t] != paren_stk[-1]:
        print(0)
        exit()

    if type(all_stk[-1]) != int:
        all_stk.pop()
        paren_stk.pop()
        all_stk.append(2 if t == ")" else 3)
        continue
    
    num = 0
    while type(all_stk[-1]) == int:
        num += all_stk.pop()
    num *= 2 if t == ")" else 3

    all_stk.pop()
    paren_stk.pop()
    all_stk.append(num)
    
if len(paren_stk) != 0:
    print(0)
else:
    print(sum(all_stk))