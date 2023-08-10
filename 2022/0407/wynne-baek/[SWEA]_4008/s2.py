import sys
sys.stdin = open('input.txt')

def cal(my_sum, idx):
    global max_result
    global min_result
    #종료조건
    if idx == N:
        if my_sum > max_result:
            max_result = my_sum
        if my_sum < min_result:
            min_result = my_sum
        return

    for i in range(4):
        if operator[i]:
            if i == 0:
                operator[i] -= 1
                cal(my_sum + nums[idx], idx + 1)
                operator[i] += 1
            elif i == 1:
                operator[i] -= 1
                cal(my_sum - nums[idx], idx + 1)
                operator[i] += 1
            elif i == 2:
                operator[i] -= 1
                cal(my_sum * nums[idx], idx + 1)
                operator[i] += 1
            else:
                operator[i] -= 1
                cal(int(my_sum / nums[idx]), idx + 1)
                operator[i] += 1
    return


T = int(input())
for _ in range(1, T+1):
    N = int(input())
    operator = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    max_result = -(9 ** 12)
    min_result = 9 ** 12
    cal(nums[0], 1)
    print(f'#{_} {max_result - min_result}')