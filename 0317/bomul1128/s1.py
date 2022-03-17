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