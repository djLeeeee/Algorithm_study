from itertools import permutations
def solution(expression):
    answer = 0
    my_lst = []
    sub = ''
    exp = []
    for char in expression:
        if char in '0123456789':
            sub += char
        elif char in '+-*':
            my_lst.append(sub)
            sub = ''
            my_lst.append(char)
            if char not in exp:
                exp.append(char)
    my_lst.append(sub)
    n = len(exp)
    order_lst = range(n)
    cases = list(permutations(order_lst, n))
    for case in cases:
        result = []
        isp = dict(zip(exp, case))
        stack = []
        for char in my_lst:
            if char in '+-*':
                if stack:
                    while stack and isp[char] <= isp[stack[-1]]:
                        result.append(stack.pop())
                    stack.append(char)
                else:
                    stack.append(char)
            else:
                result.append(char)
        while stack:
            result.append(stack.pop())
        stack = []
        for ch in result:
            if ch in '+-*':
                b = int(stack.pop())
                a = int(stack.pop())
                if ch == '+':
                    stack.append(a + b)
                elif ch == '-':
                    stack.append(a - b)
                elif ch == '*':
                    stack.append(a * b)
            else:
                stack.append(ch)
        answer = max(answer, abs(stack[0]))
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))