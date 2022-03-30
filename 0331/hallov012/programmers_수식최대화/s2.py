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
    order_lst = range(1, n+1)
    cases = list(permutations(order_lst, n))
    for case in cases:
        isp = dict(zip(exp, case))
        now_lst = my_lst[:]
        for i in range(n, 0, -1):
            m = len(now_lst)
            stack = []
            j = 0
            while j < m:
                if now_lst[j] in '+-*':
                    if isp[now_lst[j]] == i:
                        a = int(stack.pop())
                        b = int(now_lst[j+1])
                        if now_lst[j] == '+':
                            stack.append(str(a + b))
                        elif now_lst[j] == '-':
                            stack.append(str(a - b))
                        elif now_lst[j] == '*':
                            stack.append(str(a * b))
                        j += 2
                    else:
                        stack.append(now_lst[j])
                        j += 1
                else:
                    stack.append(now_lst[j])
                    j += 1
            now_lst = stack[:]
        answer = max(answer, abs(int(now_lst[0])))
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
