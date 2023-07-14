import sys
sys.stdin = open('input.txt')

che = [1]* 1000001
che[0], che[1] = 0, 0
for idx in range(2, 1001):
    if che[idx]:
        for j in range(idx+idx, 1000001, idx):
            che[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, len(che)):
        if che[i] and che[n-i]:
            print(f"{n} = {i} + {n-i}")
            break
