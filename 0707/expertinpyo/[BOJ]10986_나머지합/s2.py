# 누적합 알고리즘
N, M = map(int, input().split())
arr = list(map(int, input().split()))
cal = [0] * N
cal[0] = arr[0]
for i in range(1, N):
    cal[i] = (cal[i-1] + arr[i]) % M
ans = cal.count(0)
for i in range(1, N):
    if not cal[i]*cal[i-1]:
        ans += 1
print(cal)
print(ans)