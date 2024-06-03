import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x:x[1], reverse=True)
# 일을 시작할 수 있는 가장 늦은 시간...
ans = data[0][1] - data[0][0]
for i in range(1, n):
    t, s = data[i]
    # 시간 여유가 남으면 현재 더 늦게 시작
    if ans > s:
        ans = s - t
    # 아니면 바로 시작
    else:
        ans -= t
print(ans if ans >= 0 else -1)