import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

height = 0
ans = sys.maxsize
# 모든 높이 탐색
for i in range(257):
    max = 0
    min = 0
    for x in range(n):
        for y in range(m):
            if arr[x][y] < i:
                min += i - arr[x][y]
            else:
                max += arr[x][y] - i
    rest = max + b
    if rest < min:
        continue
    time = 2 * max + min
    if time <= ans:
        ans = time
        height = i

print(ans, height)