import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
cnt = [0] * 21
names = []
ans = 0

for i in range(n):
    val = len(input().rstrip())
    names.append(val)
    if i > k:
        cnt[names[i-k-1]] -= 1
    ans += cnt[val]
    cnt[val] += 1

print(ans)


