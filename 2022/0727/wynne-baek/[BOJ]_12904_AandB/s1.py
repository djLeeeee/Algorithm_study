import sys
sys.stdin = open('input.txt')

S = list(input())
T = list(input())

while len(S) != len(T):
    char = T.pop()
    if char == 'B':
        T.reverse()

if S == T:
    print(1)
else:
    print(0)
