import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    l = int(input())
    n = int(input())
    times = [list(map(int, input().split())) for _ in range(n)]
    prefix = [0] * (n+1)

    for i in range(n):
        s, e = times[i]
        prefix[i+1] = prefix[i] + e - s

    ans = 0
    j = 0

    for i in range(n):
        # 광고 방영 시간
        s = times[i][0]
        e = s + l
        j = max(i, j)

        # 완전히 겹치는 시간 찾기
        while j < n and times[j][1] <= e:
            j += 1

        tmp = prefix[j] - prefix[i]
        if j < n and times[j][0] < e:
            tmp += e - times[j][0]

        ans = max(ans, tmp)

    print(f"#{tc} {ans}")