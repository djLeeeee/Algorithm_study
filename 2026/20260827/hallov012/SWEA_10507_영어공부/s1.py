import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, p = map(int, input().split())
    days = list(map(int, input().split()))

    left = 0
    ans = 0
    for right in range(n):
        # 실제 공부하지 않은 날의 수가 p보다 작을 때, 그 기간을 채우면 된다
        while days[right] - days[left] - (right - left) > p:
            left += 1
        ans = max(ans, (right - left + 1) + p)
    print(f"#{tc} {ans}")