import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

wheels = [deque(input().rstrip()) for _ in range(4)]
k = int(input())
order = [list(map(int, input().split())) for _ in range(k)]
for idx, d in order:
    idx -= 1
    move = [(idx, d)]
    ld, rd = d, d
    for i in range(idx-1, -1, -1):
        if wheels[i][2] != wheels[i+1][6]:
            ld *= -1
            move.append((i, ld))
        else:
            break
    for j in range(idx+1, 4):
        if wheels[j][6] != wheels[j-1][2]:
            rd *= -1
            move.append((j, rd))
        else:
            break
    for num, dir in move:
        if dir == 1:
            temp = wheels[num].pop()
            wheels[num].appendleft(temp)
        else:
            temp = wheels[num].popleft()
            wheels[num].append(temp)

ans = 0
score = 1
for w in wheels:
    if w[0] == '1':
        ans += score
    score *= 2
print(ans)