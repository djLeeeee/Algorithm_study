import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
inclination = set()

for i in range(n-1):
    for j in range(i+1, n):
        # 기울기
        a = (nums[j] - nums[i]) / (j - i)
        if int(a) == a:
            # y = ax + b
            b = nums[i] - a * i
            inclination.add((a, b))

ans = sys.maxsize
for (a, b) in inclination:
    cnt = 0
    for i in range(n):
        if nums[i] != a * i + b:
            cnt += 1
    ans = min(ans, cnt)

print(ans)