import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
level = list(map(int, input().split()))
cnt = [0] * (n+1)
for i in range(1, n):
    cnt[i] = cnt[i-1]
    if level[i-1] > level[i]:
        cnt[i] += 1

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(cnt[y-1] - cnt[x-1])