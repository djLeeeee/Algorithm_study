# https://www.acmicpc.net/problem/2528
import sys
sys.stdin = open("./input/2528.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
sticks = []
if N == 1:
    print(0)
    exit()
    
for _ in range(N):
    d, i = map(int, input().split())
    s = 0 if i == 0 else M - d
    e = d if i == 0 else M
    sticks.append([i, s, e])

def can_move(position):
    _, cs, ce = sticks[position]
    _, ns, ne = sticks[position + 1]
    if (cs <= ne and ns <= ce):
        return 1

    return 0 

def move_sticks(N, M):
    for n in range(N):
        i, s, e = sticks[n]
        s += (-1) ** i
        e += (-1) ** i
        if (s == 0 or e == M):
            i = abs(i - 1)
        sticks[n] = (i, s, e)

position = 0
time = -1
while position < N - 1:
    time += 1
    while position < N - 1 and can_move(position):
        position += 1
    move_sticks(N, M)

print(time)