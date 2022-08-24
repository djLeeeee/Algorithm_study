n, k = map(int, input().split())
arr = list(map(int, input().split()))
broken = 0
robot = []
start = 0
day = 1
while broken < k:
    day += 1
    start -= 1
    if start < 0:
        start += 2 * n
    end = (start + n - 1) % (2 * n)
    l = len(robot)
    for i in range(l):
        new = (robot[i] + 1) % (2 * n)
        if new not in robot and arr[new]:
            arr[new] -= 1
            robot[i] = new
            if not arr[new]:
                broken += 1
    if start not in robot and arr[start]:
        arr[start] -= 1
        robot.append(start)
        if not arr[start]:
            broken += 1
print(day)
