import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
k = int(input())
check = [0] * n

ans = 0
for i in range(n):
    if check[i]:
        continue
    cnt = 0
    for j in range(m):
        if arr[i][j] == '0':
            cnt += 1
    # 1개를 켜야 행을 완성시킬 수 있을 때, k는 총 3, 5, 7 (홀수)여야 함
    if cnt <= k and cnt % 2 == k % 2:
        temp = 0
        for x in range(n):
            if arr[x] == arr[i]:
                check[x] = 1
                temp += 1
        ans = max(ans, temp)

print(ans)