# 세 알칼리 존재
# 세 제곱으로 문제를 접근하려 했으나 시간초과
# 투 포인터 알고리즘 적용
# 방식은 첫번째 부터
n = int(input())
arr = sorted(list(map(int, input().split()))) # 오름차순 정렬

cnt = float('inf')
for i in range(n-2):
    b = i + 1   # 크기가 작은 포인터
    c = n-1     # 크기가 큰 포인터
    while b != c:
        value = arr[i] + arr[b] + arr[c]
        if abs(value) < cnt:
            cnt = abs(value)
            ans = sorted([arr[i], arr[b], arr[c]])
            if not value:
                print(*ans)
                exit()
        if value > 0:
            c -= 1
        elif value < 0:
            b += 1
print(*ans)