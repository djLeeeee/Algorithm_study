import sys
from itertools import permutations

sys.stdin = open('sample_input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    # 각 연산자의 개수 '+' 2 개, '-' 1 개, '*' 0 개, '/' 1 개
    oper = (['+'], ['-'], ['*'], ['//'])
    oper_temp = tuple(map(int, input().split()))
    oper_list = []
    for i in range(4):
        oper_list += oper_temp[i] * oper[i]
    oper_set = set(permutations(oper_list, len(oper_list)))
    num_list = tuple(map(int, input().split()))
    max_ans = -100000000
    min_ans = 100000000
    for oper in oper_set:
        i = 0
        ans = num_list[0]
        while i < N - 1:
            if oper[i] == '+':
                ans = ans + num_list[i + 1]
            elif oper[i] == '-':
                ans = ans - num_list[i + 1]
            elif oper[i] == '*':
                ans = ans * num_list[i + 1]
            else:
                if ans // num_list[i + 1] == -1:
                    ans = abs(ans) // num_list[i + 1]
                else:
                    ans = ans // num_list[i + 1]
            i += 1
        if ans > max_ans:
            max_ans = ans
        if ans < min_ans:
            min_ans = ans
    print('#{} {}'.format(tc, max_ans-min_ans))

