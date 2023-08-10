# https://www.acmicpc.net/problem/10800

import sys
sys.stdin = open('10800.txt')
input = sys.stdin.readline

N = int(input())
max_color, max_size = 0, 0
players = []
for _ in range(N):
    color, size = map(int, input().split())
    if (max_color < color):
        max_color = color

    if (max_size < size):
        max_size = size

    players.append([color, size])

board = [[0] * (max_size + 2) for _ in range(max_color + 2)]
for player in players:
    color, size = player
    board[color][size] = size

for i in range(1, max_color + 1):
    for j in range(1, max_size + 1):
        board[i][j] += board[i][j - 1]

for player_ind in range(N):
    color, size = players[player_ind]
    result = 0
    for c in range(max_color + 1):
        result += board[c][size - 1] if c != color else 0

    print(result)