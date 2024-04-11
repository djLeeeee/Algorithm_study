import sys
sys.setrecursionlimit(10**6)

def solution(n, m, x, y, r, c, k):
    def find(cnt, a, b, temp):
        nonlocal answer
        # 현재 거리에서 k안에 (x, y)로 못가면 return
        if k < cnt + abs(a-r) + abs(b-c):
            return
        if a == r and b == c and cnt == k:
            answer = temp
            return
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if 0 <= na < n and 0 <= nb < m and (temp < answer or answer == ''):
                find(cnt+1, na, nb, temp + d_lst[i])

    answer = ''
    x -= 1
    y -= 1
    r -= 1
    c -= 1

    d_lst = ['d', 'l', 'r', 'u']
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    short = abs(r-x) + abs(c-y)

    if k < short or (k - short) % 2:
        return 'impossible'

    find(0, x, y, '')

    return answer

print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))