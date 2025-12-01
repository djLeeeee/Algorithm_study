import sys
sys.stdin = open('input.txt')

n = int(input())
str = input().strip()
stack = []

ans = 0
check = [0] * n
for (i, s) in enumerate(str):
    if s == '(':
        stack.append(i)
    else:
        if stack:
            j = stack.pop()
            check[i] = check[j] = 1

for i in range(1, n):
    if check[i]:
        check[i] += check[i-1]

print(max(check))
