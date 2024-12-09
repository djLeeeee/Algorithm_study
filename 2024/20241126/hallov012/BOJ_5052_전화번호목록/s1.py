import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [input().strip() for _ in range(n)]
    numbers.sort()
    for i in range(1, n):
        if numbers[i].startswith(numbers[i-1]):
            print('NO')
            break
    else:
        print('YES')
