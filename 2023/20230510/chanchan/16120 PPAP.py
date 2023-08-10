# https://www.acmicpc.net/problem/16120
import sys
sys.stdin = open("./input/16120.txt")
input = sys.stdin.readline
# ----------------------------------------

word = input().rstrip()
stack = []
PPAP = list("PPAP")
for w in word:
    stack.append(w)
    if stack[-4:] == PPAP:
        for _ in range(3):
            stack.pop()
    
ans = "PPAP" if "".join(stack) == "P" else "NP"
print(ans)