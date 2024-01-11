# 괄호 추가하기
# https://www.acmicpc.net/problem/16637
import sys
sys.stdin = open("./input/quiz1.txt")
input = sys.stdin.readline
# ----------------------------------------

def baseCal(opr, num1, num2):
    if (opr == "*"):
        return num1 * num2
    elif (opr == "+"):
        return num1 + num2
    elif (opr == "-"):
        return num1 - num2


def getCal(num, op):
    while op:
        num1, num2 = num.pop(0), num.pop(0)
        opr = op.pop(0)
        num.insert(0, baseCal(opr, num1, num2))

    return num[0]


# ----------------------------------------

def solution(cnt, num, op):
    global result

    if cnt == N // 2 or len(num) == 1:
        result = max(result, getCal(num, op))
        return
    solution(cnt + 1, num[:], op[:])

    try:
        n1, n2 = num.pop(cnt), num.pop(cnt)
        opr = op.pop(cnt)
        num.insert(cnt, baseCal(opr, n1, n2))
        solution(cnt + 1, num[:], op[:])
    except:
        0

# --------------------------------------------

for _ in range(int(input())):
    N = int(input())
    expression = list(input())
    num, op = [], []
    result = - float('inf')

    for ind in range(N):
        if (ind % 2):
            op.append(expression[ind])
        else:
            num.append(int(expression[ind]))

    solution(0, num, op)
    print(result)
