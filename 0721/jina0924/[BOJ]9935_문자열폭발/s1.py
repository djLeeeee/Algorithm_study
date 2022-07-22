# 백준 9935번 문자열 폭발 - 시간초과

import sys
sys.stdin = open('input2.txt')

string = input()
bomb = input()
ans = ''
i = 0
while i < len(string) - 1:
    j = 0
    while j < len(bomb):
        if string[i] == bomb[j]:
            j += 1
        i += 1
    if j == len(bomb):
        i -= len(bomb) + 1
        string = string.replace(bomb, '')
if string:
    print(string)
else:
    print('FRULA')