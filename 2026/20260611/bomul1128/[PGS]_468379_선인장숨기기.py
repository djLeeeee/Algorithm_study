# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/468379
# Submission: 2026-06-11 18:23:51 Python3 정답 100 /
def solution(n, m, h, w, drops):
    from collections import deque

    def compress(line, size):
        dq = deque()
        for i in range(size):
            v = line[i]
            while dq and dq[-1][1] > v:
                dq.pop()
            dq.append((i, v))
        result = [dq[0][1]]
        for i in range(size, len(line)):
            while dq and dq[0][0] + size <= i:
                dq.popleft()
            v = line[i]
            while dq and dq[-1][1] > v:
                dq.pop()
            dq.append((i, v))
            result.append(dq[0][1])
        return result
        
    ld = len(drops)
    board = [[ld] * m for _ in range(n)]
    for i, (x, y) in enumerate(drops):
        board[x][y] = i
    b1 = [compress(l, w) for l in board]
    b2 = list(map(list, zip(*b1)))
    b3 = [compress(l, h) for l in b2]
    b4 = list(map(list, zip(*b3)))
    ans = [0, 0]
    v = b4[0][0]
    for i, l in enumerate(b4):
        for j, tmp in enumerate(l):
            if tmp > v:
                v = tmp
                ans = [i, j]
    return ans
