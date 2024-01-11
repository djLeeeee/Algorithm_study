# 백준 16934번 게임 닉네임

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
nickname = defaultdict(int)
byname = defaultdict(set)

for _ in range(n):
    username = input().rstrip()
    tmp = ''
    isFound = False
    for i in range(len(username)):
        tmp += username[i]
        if not isFound and tmp not in byname[i+1]:
            print(tmp)
            isFound = True
        byname[i + 1].add(tmp)
    if not isFound:
        if username in nickname:
            print(f'{username}{nickname[username] + 1}')
        else:
            print(username)
    nickname[username] += 1