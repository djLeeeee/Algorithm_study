import sys
sys.stdin = open('input.txt')

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
represent = [_ for _ in range(N+1)]

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j]:
            arr[i+1].append(j+1)
            represent[j+1] = represent[i+1]

journey = tuple(map(int, input().split()))
for idx in range(len(journey)-1):
    if represent[journey[idx]] != represent[journey[idx+1]]:
        print('NO')
        break
else:
    print('YES')