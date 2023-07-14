import sys
from itertools import permutations
from collections import deque

sys.stdin = open('input.txt')
# 의뢰자 음수 몬스터 양수

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dic = {}
    monster = 0
    nums = []
    ans = 10000
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                dic[arr[i][j]] = [i, j]
                nums.append(arr[i][j])
                if arr[i][j] > monster:
                    monster = arr[i][j]
    cases = list(permutations(nums, monster * 2))
    result = []
    for _ in range(len(cases)):
        case = cases.pop(0)
        stack = []
        check = True
        for num in case:
            if num > 0:
                stack.append(num)
            elif num < 0:
                if abs(num) not in stack:
                    check = False
                    break
        if check:
            result.append(case)

    for root in result:
        root = deque(root)
        a, b = dic[root[0]]
        cnt = a + b
        while len(root) > 1:
            now = root.popleft()
            next = root.popleft()
            x, y = dic[now]
            nx, ny = dic[next]
            cnt += abs(x - nx) + abs(y - ny)
            if cnt > ans:
                break
            root.appendleft(next)
        ans = min(ans, cnt)

    print(f'#{tc} {ans}')
