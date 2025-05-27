import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = [[0] * n for _ in range(n)]
revers_arr = [[0] * n for _ in range(n)]
ans = 0
for i in range(n):
    row = input().rstrip()
    for j in range(n):
        if row[j] == 'T':
            arr[i][j] = 1
            ans += 1
        else:
            revers_arr[i][j] = 1

temp = []
ans = 0
for i in range(n):
    if sum(arr[i]) < sum(revers_arr[i]):
        temp.append(arr[i])
    else:
        temp.append(revers_arr[i])

for j in range(n):
    cnt = 0
    for i in range(n):
        cnt += arr[i][j]
    ans += min(cnt, n-cnt)

print(ans)