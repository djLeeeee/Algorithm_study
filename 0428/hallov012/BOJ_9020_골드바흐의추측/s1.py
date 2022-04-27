import sys, math
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

m = 10000
numbers = [0, 0] + [1] * (m-1)
for i in range(2, int(math.sqrt(m)) + 1):
    if numbers[i]:
        for j in range(i * 2, m+1, i):
            numbers[j] = 0

for tc in range(T):
    n = int(input())
    a, b = n//2, n//2
    if not numbers[a]:
        for i in range(a-1, -1, -1):
            if numbers[i]:
                a = i
                break
    if not numbers[b]:
        for j in range(b+1, n+1):
            if numbers[j]:
                b = j
                break
    while True:
        if a + b == n:
            ans = [a, b]
            print(*ans)
            break
        if a + b > n:  # 만약 두 값의 합이 n 보다 크다면 a를 더 작은 수로 바꿔줌
            for i in range(a-2, -1, -2):
                if numbers[i]:
                    a = i
                    flag = 1
                    break
        else:
            for j in range(b+2, n+1, 2):
                if numbers[j]:
                    b = j
                    flag = 0
                    break


