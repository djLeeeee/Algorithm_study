import itertools


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def sol(arr):
    now = (0, 0)
    get = []
    result = 0
    for idx in arr:
        if idx < 0:
            if -idx not in get:
                return 10000
            result += dist(now, point[idx])
            now = point[idx]
        else:
            result += dist(now, point[idx])
            now = point[idx]
            get.append(idx)
        if result > ans:
            return 10000
    return result


for tc in range(1, int(input()) + 1):
    n = int(input())
    board = []
    point = {}
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(n):
            if line[j]:
                point[line[j]] = (i, j)
        board.append(line)
    orders = itertools.permutations(list(point.keys()))
    ans = 10000
    for order in orders:
        ans = min(ans, sol(order))
    print(f'#{tc} {ans}')