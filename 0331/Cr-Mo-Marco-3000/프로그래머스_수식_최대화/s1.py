def solution(expression):
    from itertools import permutations
    from collections import deque

    def do(operator, left, right):
        if operator == '+':
            return [left + right]
        elif operator == '-':
            return [left - right]
        elif operator == '*':
            return [left * right]


    # "100-200*300-500+20"
    temp = ['+', '-', '*']
    oper_list = tuple(permutations(temp, 3))
    my_list2 = []
    start = 0
    i = 0

    while i < len(expression):
        if expression[i] in '+-*':
            my_list2.append(int(expression[start:i]))
            my_list2.append(expression[i])
            start = i + 1
        i += 1

    my_list2.append(int(expression[start:]))
    answer = 0
    for oper_set in oper_list:
        my_list = my_list2
        # "100-200*300-500+20"
        for i in range(3):
            oper = oper_set[i]
            j = 0
            while j < len(my_list):
                if my_list[j] == oper:
                    my_list = my_list[0:j-1] + do(oper, my_list[j-1], my_list[j+1]) + my_list[j+2:]
                    j -= 1
                j += 1
        if abs(my_list[0]) > answer:
            answer = abs(my_list[0])

    return answer


print(solution("100-200*300-500+20"))
a = 1