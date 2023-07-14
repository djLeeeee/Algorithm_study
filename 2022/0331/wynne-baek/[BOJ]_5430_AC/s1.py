import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    p = input()
    N = int(input())
    arr = input()
    nums = []
    temp = ''
    nums_str = '1234567890'
    for char in arr:
        if char in nums_str:
            temp += char
        if temp and char not in nums_str:
            nums.append(int(temp))
            temp = ''
    # 정순 - 왼쪽에서 제거
    flag = True
    # 역순 = 오른쪽에서 제거
    for char in p:
        if char == 'R':
            if flag:
                flag = False
            else:
                flag = True
        elif char == 'D':
            if flag and nums:
                nums.pop(0)
            elif not flag and nums:
                nums.pop()
            elif not nums:
                print('error')
                break
    else:
        if not flag:
            nums = reversed(nums)
        print('['+','.join(str(_) for _ in nums)+']')