# 백준 2573번 빙산

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from copy import deepcopy
from collections import deque


dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
def melting(iceberg):
    ans = 0
    finish = False
    while not finish:
        # 빙산 녹이기
        melting_iceberg = deepcopy(iceberg)
        for r in range(1, n-1):
            for c in range(1, m-1):
                if iceberg[r][c] > 0:
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if iceberg[nr][nc] <= 0:
                            melting_iceberg[r][c] -= 1
        iceberg = deepcopy(melting_iceberg)
        ans += 1

        # 빙산 개수 세기
        cnt = 0
        for r in range(1, n-1):
            for c in range(1, m-1):
                if melting_iceberg[r][c] > 0:
                    queue = deque([(r, c)])

                    while queue:
                        cr, cc = queue.popleft()
                        for d in range(4):
                            nr, nc = cr + dr[d], cc + dc[d]
                            if melting_iceberg[nr][nc] > 0:
                                melting_iceberg[nr][nc] = 0
                                queue.append((nr, nc))
                    cnt += 1
                    if cnt >= 2:
                        finish = True
        if cnt == 0:
            ans = 0
            finish = True
    return ans


n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]
print(melting(iceberg))