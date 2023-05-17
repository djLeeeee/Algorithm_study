# 백준 6137번 문자열 생성

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
string = ''
for _ in range(N):
    string += input().rstrip()
l, r = 0, N - 1
T = ''
while l <= r:
    if string[l] < string[r]:
        T += string[l]
        l += 1
    elif string[l] > string[r]:
        T += string[r]
        r -= 1
    else:
        tl, tr = l + 1, r - 1
        flag = 0
        while tl <= tr:
            if string[tl] < string[tr]:
                flag = 1
                break
            elif string[tl] > string[tr]:
                flag = 2
                break
            tl += 1
            tr -= 1
        if flag == 2:
            T += string[r]
            r -= 1
        else:
            T += string[l]
            l += 1
for i in range(len(T)):
    print(T[i], end='')
    if i % 80 == 79:
        print()