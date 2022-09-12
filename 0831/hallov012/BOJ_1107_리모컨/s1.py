import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

channel = int(input())
n = int(input())
# 채널의 최댓값인 500000에 2를 곱한다
m = 1000000
now = 100
# +, - 만을 이용해 움직이는 값이 max 값이 된다
ans = abs(channel - now)

if n:
    data = list(map(int, input().split()))
else:
    data = []

# 가장 가까운 채널로 이동하기 위해 전체 탐색
for nums in range(m+1):
    nums = str(nums)
    flag = True
    # 누를 수 없는 버튼이 있다면 그 경우는 종료
    for num in nums:
        if int(num) in data:
            flag = False
            break
    # 전부 다 누를 수 있다면, 채널 숫자를 입력하는데 필요한 버튼 수와 +, -를 이용해 맞추는 버튼 수를 더해 ans 와 비교
    if flag:
        temp = abs(channel - int(nums)) + len(nums)
        ans = min(ans, temp)
print(ans)




