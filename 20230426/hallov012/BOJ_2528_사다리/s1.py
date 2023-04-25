import sys
sys.stdin = open('input.txt')

def stick_move():
    for i in range(n):
        if sticks[i][2] == 0:
            sticks[i][0] += 1
            sticks[i][1] += 1
            if sticks[i][1] == l:
                sticks[i][2] = 1
        else:
            sticks[i][0] -= 1
            sticks[i][1] -= 1
            if sticks[i][0] == 0:
                sticks[i][2] = 0

def move(now):
    while True:
        next = now + 1
        if min(sticks[now][1], sticks[next][1]) >= max(sticks[now][0], sticks[next][0]):
            now += 1
            if now == n-1:
                break
        else:
            break
    return now

input = sys.stdin.readline

n, l = map(int, input().split())
sticks = []
for _ in range(n):
    a, d = map(int, input().split())
    if d == 0:
        sticks.append([0, a, d])
    else:
        sticks.append([l-a, l, d])
if n == 1:
    print(0)
    exit()

ans = 0
now = 0

while True:
    now = move(now)
    if now == n-1:
        break
    stick_move()
    ans += 1

print(ans)

