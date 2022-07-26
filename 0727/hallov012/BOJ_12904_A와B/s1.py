import sys
sys.stdin = open('input.txt')

s = list(input())
t = list(input())
flag = False
while len(t) >= len(s):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if t == s:
        flag = True
        break
print(1 if flag else 0)




