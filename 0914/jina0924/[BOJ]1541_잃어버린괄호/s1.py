# 백준 1541번 잃어버린 괄호

import sys
sys.stdin = open('input3.txt')

data = input()
number = '0123456789'
operator = '+-'
stack = []                          # 앞자리 0을 제거한 숫자와 연산자를 담을 배열
idx = start = 0                     # idx: data의 값을 하나하나 살펴볼 인덱스 / start: 수의 시작 인덱스
while idx < len(data):
    if data[idx] in operator:       # 만약 해당 값이 연산자라면
        stack += [data[start:idx].lstrip('0'), data[idx]]       # 변형한 수와 연산자를 stack에 담아줌
        start = idx + 1             # 연산자 다음 index가 다음 수의 첫 시작 인덱스가 됨
    idx += 1
stack.append(data[start:idx].lstrip('0'))                       # 마지막에 남은 수도 stack에 담아줌
invert = False                      # 괄호를 칠 부분 = +를 -로 바꿀 부분
for j in range(1, len(stack), 2):
    if stack[j] == '-':             # 연산자가 '-'라면
        invert = True               # 괄호 시작
    else:
        if invert:                  # 만약 괄호 안에 있는 '+'라면
            stack[j] = '-'          # '-'로 값을 바꿔줌
print(eval(''.join(stack)))         # stack안에 있는 문자열을 합쳐서 수식으로 계산해줌