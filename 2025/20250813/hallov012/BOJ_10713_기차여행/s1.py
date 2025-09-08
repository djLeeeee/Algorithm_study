import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
path = list(map(int, input().split()))
fee = [[]] + [list(map(int, input().split())) for _ in range(n-1)]

acc = [0] * (n+1)
for i in range(m-1):
    x, y = path[i], path[i+1]
    if x > y:
        x, y = y, x
    # 구매 해야 하는 쪽 노선 시작에 += 1, 끝에 -= 1
    acc[x] += 1
    acc[y] -= 1

ans = 0
cnt = 0
for i in range(1, n):
    cnt += acc[i]
    ticket = fee[i][0] * cnt
    card = fee[i][2] + fee[i][1] * cnt
    ans += min(ticket, card)
print(ans)