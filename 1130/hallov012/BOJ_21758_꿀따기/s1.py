import sys
sys.stdin = open('input.txt')

n = int(input())
data = list(map(int, input().split()))
total = sum(data)
ans = 0

# 벌-벌-통 순서
# i는 두번째 벌의 위치
# 첫번째 벌은 무조건 0에 두는 것이 유리, 벌통은 n-1에 두는 것이 유리
temp = data[0]
for i in range(1, n-1):
    # 두번째 벌이 딸수 없는 꿀의 양
    temp += data[i]
    first = total - data[0] - data[i]
    second = total - temp
    ans = max(ans, first + second)

# 통-벌-벌 순서 (벌-벌-통의 역순)
r_data = list(reversed(data))
temp = r_data[0]
for i in range(1, n-1):
    temp += r_data[i]
    first = total - r_data[0] - r_data[i]
    second = total - temp
    ans = max(ans, first + second)

# 벌-통-벌 순서
for i in range(1, n-1):
    ans = max(ans, total - data[0] - data[-1] + data[i])

print(ans)



