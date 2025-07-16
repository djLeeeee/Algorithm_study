import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N, A, B = map(int, input().split())
dots = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N-1):
    x1, y1, s1 = dots[i]
    for j in range(i+1, N):
        x2, y2, s2 = dots[j]
        if abs(x1 - x2) < A and abs(y1 - y2) < B:
            ans = max(ans, abs(s1 - s2))
print(ans)
