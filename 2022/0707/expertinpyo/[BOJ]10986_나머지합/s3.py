N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 나머지를 담는 배열 생성
reminder = [0] * M
# 초깃값 설정
reminder[arr[0] % M] = 1

for i in range(1, N):
    arr[i] += arr[i-1] # 누적합
    reminder[arr[i] % M] += 1   # 해당 나머지 값 추가

ans = reminder[0]   # 나머지가 없을 때의 값 더해주기
for re in reminder:
    ans += re * (re-1) // 2 # nC2 조합으로 답 갱신
print(ans)