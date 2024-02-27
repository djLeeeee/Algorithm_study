from collections import deque
import sys
sys.stdin = open('input.txt')

S = input()
cnt = 0

alst = deque()
blst = deque()
for i in range(len(S)):
    if S[i] == 'A':
        alst.append(i)
    elif S[i] == 'B':
        blst.append(i)
    elif S[i] == 'C':
        if len(blst) > 0 and i > blst[0]:
            blst.popleft()
            cnt += 1

while len(blst) > 0 and len(alst) > 0:
    if alst[0] < blst[0]:
        alst.popleft()
        blst.popleft()
        cnt += 1
    else:
        blst.popleft()

print(cnt)