word1 = "100-200*300-500+20"    # 60420
word2 = "50*6-3*2"              # 300

from itertools import permutations

def calculate(num1, num2, operator):
    if operator == '+':
        return str(int(num1) + int(num2))
    elif operator == '-':
        return str(int(num1) - int(num2))
    else:
        return str(int(num1) * int(num2))

def order(expression, ops):
    nums = []
    temp = ''
    for char in expression:
        if char not in ops:
            temp += char
        elif char in ops:
            nums.append(temp)
            temp = ''
            nums.append(char)
    nums.append(temp)

    for op in ops:
        temp_list = []
        while len(nums) != 0:
            thing = nums.pop(0)
            if thing == op:
                temp_list.append(calculate(temp_list.pop(), nums.pop(0), thing))
            else:
                temp_list.append(thing)
        nums = temp_list
    return abs(int(nums[0]))

def solution(expression):
    operator = ('+', '-', '*')
    nPn = permutations(operator)
    result = []
    for ops in nPn:
        result.append(order(expression, ops))
    answer = max(result)
    return answer

print(solution(word1))