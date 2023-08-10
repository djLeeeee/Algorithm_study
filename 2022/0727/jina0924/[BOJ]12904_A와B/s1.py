# 백준 10904번 A와 B - 메모리 초과

import sys
sys.stdin = open('input1.txt')

S = input()
T = input()
result = [[S]]
idx = 0
length = len(S)
while length < len(T):
    result.append([])
    for word in result[idx]:
        new1 = word + 'A'
        if new1 == T:
            print(1)
            sys.exit()
        result[idx+1].append(new1)
        new2 = word[::-1] + 'B'
        if new2 == T:
            print(1)
            sys.exit()
        result[idx+1].append(new2)
    idx += 1
    length += 1
print(0)