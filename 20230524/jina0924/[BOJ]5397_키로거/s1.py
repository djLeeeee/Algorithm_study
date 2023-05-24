# 백준 5397번 키로거 - 시간초과

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    password = ''
    string = input().rstrip()
    point = -1
    for char in string:
        if char == '<':
            if point >= 0:
                point -= 1
        elif char == '>':
            if point < len(password) - 1:
                point += 1
        elif char == '-':
            if password and point >= 0:
                password = password[:point] + password[point + 1:]
                point -= 1
        else:
            password = password[:point + 1] + char + password[point + 1:]
            point += 1
    print(password)