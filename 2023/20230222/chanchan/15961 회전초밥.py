# https://www.acmicpc.net/problem/15961
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

sushi = [0] * N
for n in range(N):
    sushi[n] = int(input())

max_val = 0
for ind in range(N):
    sushi_list = set(sushi[ind: ind + k])
    kinds = len(sushi_list)

    if not (c in sushi_list):
        kinds += 1

    if kinds > max_val:
        max_val = kinds

print(max_val)
