# 백준 9935번 문자열 폭발 - 시간초과

import sys
sys.stdin = open('input1.txt')

string = input()
bomb = input()
length = len(bomb)

ans = ''

for i in range(len(string)):
    ans += string[i]
    if string[i] == bomb[-1]:
        if ans[-length:] == bomb:
            ans = ans[:-length]

if ans:
    print(ans)
else:
    print('FRULA')