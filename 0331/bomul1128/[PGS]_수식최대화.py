from itertools import permutations


def solution(expression):
    answer = 0
    cal = ['+', '-', '*']
    nums = []
    cals = []
    num = ''
    for char in expression:
        if char in cal:
            cals.append(char)
            nums.append(int(num))
            num = ''
        else:
            num += char
    nums.append(int(num))
    orders = list(permutations(cal, 3))
    for order in orders:
        answer = max(answer, abs(calculation(order, nums, cals)))
    return answer


def calculation(order, nums, cals):
    for i in range(3):
        stack1 = [nums[0]]
        stack2 = []
        for j in range(len(cals)):
            if cals[j] != order[i]:
                stack1.append(nums[j + 1])
                stack2.append(cals[j])
            else:
                if order[i] == '+':
                    stack1.append(stack1.pop() + nums[j + 1])
                elif order[i] == '-':
                    stack1.append(stack1.pop() - nums[j + 1])
                else:
                    stack1.append(stack1.pop() * nums[j + 1])
        nums = stack1
        cals = stack2
    return stack1[0]
