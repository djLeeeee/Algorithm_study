# 짝수와 홀수가 다름
# 2**n -1 줄로 전개됨
# 역으로 들어가는 것을 생각해보자


n = int(input())
arr = [[' '] * (2*(2**n-1)-1) for _ in range(2**n-1)]
if n == 1:
    print('*')
else:
    for k in range(2, 2**n-1):
        star(k)
