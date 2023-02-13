# https://www.acmicpc.net/problem/10800

import sys
# sys.stdin = open('10800.txt')
input = sys.stdin.readline

N = int(input())
colors = [0] * (N + 1)
players = [0] * N

balls = []

for n in range(N):
    color, size = map(int, input().split())
    balls.append([n, size, color])

balls.sort(key = lambda x: (x[1], x[2]))

sum_ = 0
a, b = 0, 0

while a < N:
    ball_a = balls[a]
    ball_b = balls[b]

    while ball_b[1] < ball_a[1]:
        sum_ += ball_b[1]
        colors[ball_b[2]] += ball_b[1]

        b += 1
        ball_b = balls[b]
    
    a += 1
    players[ball_a[0]] = sum_ - colors[ball_a[2]]

for n in range(N):
    print(players[n])