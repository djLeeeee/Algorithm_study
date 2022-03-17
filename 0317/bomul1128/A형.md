```python
# 1번
def sol(t, lr):
    gate, person = fishing[t]
    gate -= 1
    result = 0
    for _ in range(person):
        pointer = 0
        if lr:
            while True:
                if gate - pointer >= 0 and seat[gate - pointer] == 0:
                    seat[gate - pointer] = 1
                    break
                elif gate + pointer < n and seat[gate + pointer] == 0:
                    seat[gate + pointer] = 1
                    break
                else:
                    pointer += 1
        else:
            while True:
                if gate + pointer < n and seat[gate + pointer] == 0:
                    seat[gate + pointer] = 1
                    break
                elif gate - pointer >= 0 and seat[gate - pointer] == 0:
                    seat[gate - pointer] = 1
                    break
                else:
                    pointer += 1
        result += pointer + 1
        if result > ans:
            return 10000
    return result


for tc in range(1, int(input()) + 1):
    n = int(input())
    fishing = [list(map(int, input().split())) for _ in range(3)]
    orders = [
        (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)
    ]
    flag = [
        (0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
        (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)
    ]
    ans = 10000
    for i, j, k in orders:
        for f1, f2, f3 in flag:
            seat = [0] * n
            ans = min(ans, sol(i, f1) + sol(j, f2) + sol(k, f3))
    print(f'#{tc} {ans}')
```

```python
# 2번
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
        elif idx > 0:
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
            point[line[j]] = (i, j)
        board.append(line)
    orders = itertools.permutations(list(point.keys()))
    ans = 10000
    for order in orders:
        ans = min(ans, sol(order))
    print(f'#{tc} {ans}')
```

