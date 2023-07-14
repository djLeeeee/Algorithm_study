from sys import stdin

input = stdin.readline

while True:
    try:
        t = int(input()) * 10 ** 7
    except ValueError:
        break
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    p1, p2 = 0, n - 1
    while p1 < p2:
        if arr[p1] + arr[p2] < t:
            p1 += 1
        elif arr[p1] + arr[p2] > t:
            p2 -= 1
        else:
            break
    if p1 < p2:
        print(f'yes {arr[p1]} {arr[p2]}')
    else:
        print('danger')
