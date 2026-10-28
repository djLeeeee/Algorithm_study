import sys
sys.stdin = open('input.txt')

def check(limit):
    idx = 0
    for s in s_lst:
        cnt = 0
        while idx < n:
            if w_lst[idx] <= limit:
                cnt += 1
            else:
                cnt = 0
            idx += 1
            if cnt == s:
                break
        if cnt < s:
            return False
    return True

T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    w_lst = list(map(int, input().split()))
    s_lst = list(map(int, input().split()))

    left, right = min(w_lst), max(w_lst)

    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1

    print(f"#{tc} {left}")
