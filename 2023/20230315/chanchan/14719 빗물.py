# https://www.acmicpc.net/problem/14719

import sys
sys.stdin = open("input/14719.txt")
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

top_ind = 0
for w in range(W):
    if blocks[w] >= blocks[top_ind]:
        top_ind = w

top, tot, temp = 0, 0, 0
for i in range(0, top_ind + 1):
    if blocks[i] >= top:
        top = blocks[i]
        tot += temp
        temp = 0
    else:
        temp += (top - blocks[i])

top, temp = 0, 0 
for i in range(W - 1, top_ind - 1, -1):
    if blocks[i] >= top:
        top = blocks[i]
        tot += temp
        temp = 0
    else:
        temp += (top - blocks[i])

print(tot)