# 백준 9935번 문자열 폭발

import sys
sys.stdin = open('input2.txt')

string = list(input())
bomb = list(input())
length = len(bomb)

ans = []

for i in range(len(string)):
    ans.append(string[i])
    if string[i] == bomb[-1]:
        if ans[-length:] == bomb:
            for _ in range(length):
                ans.pop()

if ans:
    print(''.join(ans))
else:
    print('FRULA')