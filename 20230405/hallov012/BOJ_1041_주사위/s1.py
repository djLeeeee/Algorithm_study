import sys
sys.stdin = open('input.txt')

n = int(input())
data = list(map(int, input().split()))
if n == 1:
    print(sum(data) - max(data))
    exit()
counter = {(0, 5), (2, 3), (1, 4)}
min_nums = []
for a, b in counter:
    min_nums.append(min(data[a], data[b]))
min_nums.sort()
m1 = min_nums[0]
m2 = sum(min_nums[:2])
m3 = sum(min_nums)

n1 = (n-2) * (n-2) + 4 * (n-2) * (n-1)
n2 = (n-1) * 4 + (n-2) * 4
n3 = 4

ans = m1 * n1 + m2 * n2 + m3 * n3
print(ans)