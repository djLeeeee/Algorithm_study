from sys import stdin

input = stdin.readline


def chicken_distance(remain):
    ans = 0
    for x, y in house:
        dist = 2 * n
        for r in remain:
            dist = min(dist, abs(x - shop[r][0]) + abs(y - shop[r][1]))
        ans += dist
    return ans


def check_nums(num):
    ans = 0
    while num > 0:
        if num & 1:
            ans += 1
        num >>= 1
    return ans


n, m = map(int, input().split())
shop = []
house = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            house.append((i, j))
        elif line[j] == 2:
            shop.append((i, j))
result = int(1e6)
for k in range(1 << len(shop)):
    if check_nums(k) == m:
        chicken = []
        for bit in range(len(shop)):
            if k & (1 << bit):
                chicken.append(bit)
        result = min(result, chicken_distance(chicken))
print(result)
