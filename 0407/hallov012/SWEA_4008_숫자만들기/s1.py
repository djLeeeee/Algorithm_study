import sys
sys.stdin = open('input.txt')

def dfs(cnt, result):
    if cnt == n-1:
        cases.append(result)
        return
    for i in range(4):
        if exp[i] > 0:
            exp[i] -= 1
            dfs(cnt + 1, result + exp_dic[i])
            exp[i] += 1

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    exp = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    exp_dic = {0: '+', 1: '-', 2: '*', 3: '/'}
    max_ans = (-1) * (10 ** 8)
    min_ans = 10 ** 8
    cases = []
    dfs(0, '')
    for case in cases:
        i = 1
        ans = nums[0]
        while i < n:
            if case[i-1] == '+':
                ans += nums[i]
            elif case[i-1] == '-':
                ans -= nums[i]
            elif case[i-1] == '*':
                ans *= nums[i]
            else:
                ans = int(ans / nums[i])
            i += 1
        max_ans = max(ans, max_ans)
        min_ans = min(ans, min_ans)
    print(f'#{tc} {max_ans-min_ans}')
