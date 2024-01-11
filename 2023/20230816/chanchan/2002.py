# https://www.acmicpc.net/problem/2002
import sys
sys.stdin = open("./input/2002.txt")
input = sys.stdin.readline
# ----------------------------------------
info, out = {}, []
N = int(input())
for n in range(N):
    info[input().rstrip()] = n

for n in range(N):
    out.append(input().rstrip())

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        car1, car2 = out[i], out[j]
        if info[car1] > info[car2]:
            ans += 1
            break

print(ans)