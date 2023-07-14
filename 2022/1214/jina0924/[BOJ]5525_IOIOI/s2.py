# 백준 5525번 IOIOI

import sys
sys.stdin = open('input2.txt')

N = int(input())                    # 패턴 번호
M = int(input())                    # 문자열의 길이
S = input()                         # 살펴볼 문자열
cnt = 0                             # 패턴이 몇 번 나오는지 저장할 변수
i = 1                               # 'IOI'를 살펴보기 위한 인덱스값
p = 0                               # 'IOI'가 반복되는 값 저장할 변수
while i < M - 1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        p += 1
        if p == N:                  # 주어진 패턴 길이만큼 살펴봤다면
            p -= 1                  # 반복된 'IOI'로 다음 패턴이 이어지는지 보기 위해 -1만큼만 해줌
            cnt += 1
        i += 1                      # 'IOI'를 만났다면 퐁당퐁당보기 위해 i에 1 더해줌
    else:
        p = 0
    i += 1                          # 패턴과 상관없이 다음 인덱스 살펴보기

print(cnt)