import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    x_lst = data[:N]
    m_lst = data[N:]

    ans = []

    for i in range(N-1):
        left, right = x_lst[i], x_lst[i+1]
        while True:
            mid = (left + right) / 2
            if mid in (left, right):
                break
            force = 0
            for j in range(N):
                f = m_lst[j] / (mid - x_lst[j]) ** 2
                if x_lst[j] < mid:
                    force -= f
                else:
                    force += f

            if force > 0:
                right = mid
            else:
                left = mid

        ans.append(f"{(left + right) / 2:.10f}")

    print(f"#{tc} ", *ans)


