import sys
sys.stdin = open('input.txt')

N = int(input())
ans = abs(100 - N)
M = int(input())
if M:
    broken = list(input().split())
else:
    broken = []

for num in range(1000001):
    for i in str(num):
        if i in broken:
            break
    else:
        ans = min(ans, (len(str(num)) + abs(num-N)))

print(ans)