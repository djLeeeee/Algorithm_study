# 백준 10904번 A와 B

import sys
sys.stdin = open('input2.txt')

S = input()
T = input()
while len(S) < len(T):      # T가 S만큼 줄어들때까지
    if T[-1] == 'A':        # 끝 문자가 A라면
        T = T[:-1]          # 끝 문자 빼고 저장
    elif T[-1] == 'B':      # 끝 문자가 B라면
        T = T[-2::-1]       # 끝 문자 빼고 뒤집기
if S == T:
    print(1)
else:
    print(0)
