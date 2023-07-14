# 백준 2504번 괄호의 값

import sys
sys.stdin = open('input.txt')

data = list(input())
stack = []
for char in data:
    if char == '(' or char == '[':
        stack.append(char)
    elif char == ')':
        if not stack:
            print(0)
            sys.exit()
        result = 0
        while stack:
            tmp = stack.pop()
            if tmp == '(':
                if result == 0:
                    result += 1
                stack.append(result * 2)
                break
            elif tmp == '[':
                print(0)
                sys.exit()
            else:
                result += tmp
        if result:
            print(0)
            sys.exit()
    elif char == ']':
        if not stack:
            print(0)
            sys.exit()
        result = 0
        while stack:
            tmp = stack.pop()
            if tmp == '[':
                if result == 0:
                    result += 1
                stack.append(result * 3)
                break
            elif tmp == '(':
                print(0)
                sys.exit()
            else:
                result += tmp
        if result:
            print(0)
            sys.exit()
    else:
        print(0)
        sys.exit()
if type(stack[0]) != int or type(stack[-1]) != int:
    print(0)
else:
    print(sum(stack))