# 순열 사용, 시간초과!
import sys
from itertools import permutations
from collections import deque
sys.stdin = open('input.txt')

# 계산!1
def cal(nPn):
    global max_result
    global min_result
    nPn = deque(nPn)
    x = nums[0]
    for i in range(N-1):
        ope = nPn[i]
        y = nums[i+1]
        if ope == '+':
            x = x + y
        elif ope == '-':
            x = x - y
        elif ope == '/':
            x = int(x / y)
        elif ope == '*':
            x = x * y
    if x > max_result:
        max_result = x
    if x < min_result:
        min_result = x




T = int(input())
for _ in range(1, T+1):
    N = int(input())
    operator = list(map(int, input().split()))
    operator_dict = {0: '+', 1: '-',2: '*',3:'/'}
    use = []
    nums = deque(list(map(int, input().split())))
    # print(nums)
    for i in range(4):
        if operator[i]:
            for j in range(operator[i]):
                use.append(operator_dict.get(i))
    nPns = permutations(use, N-1)
    nPns = set(nPns)
    nPns = tuple(nPns)
    result = []
    max_result = -(9 ** 12)
    min_result = 9 ** 12
    for nPn in nPns:
        cal(nPn)
    print(f'#{_} {max_result - min_result}')