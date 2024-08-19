import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    l, n = map(int, input().split())
    min_ans, max_ans = 0, 0
    for _ in range(n):
        ant = int(input())
        min_ans = max(min_ans, min(ant, l - ant))
        max_ans = max(max_ans, ant, l - ant)
    print(min_ans, max_ans)