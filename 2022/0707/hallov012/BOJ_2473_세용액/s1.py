import sys
sys.stdin = open('input.txt')

n = int(input())
data = list(map(int, input().split()))
data.sort()
ans = []
min_sum = sys.maxsize

# 첫번째 용액을 선택
for i in range(n-2):
    # 두번째, 세번째 용액을 선택
    left, right = i+1, n-1
    while left < right:
        check = data[i] + data[left] + data[right]
        if abs(check) < min_sum:
            min_sum = abs(check)
            ans = [data[i], data[left], data[right]]
        # 세 용액의 합이 양수라면 최댓값인 data[right]를 줄여서 격차를 줄이기 위해 시도
        if check > 0:
            right -= 1
        # 세 용액의 합이 음수라면 data[i]는 고정이므로 data[left]를 더 크게 바꿔서 시도
        elif check < 0:
            left += 1
        else:
            break

print(*ans)