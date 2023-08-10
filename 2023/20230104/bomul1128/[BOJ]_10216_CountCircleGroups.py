from sys import stdin

input = stdin.readline


def find(idx):
    if idx == parents[idx]:
        return idx
    parents[idx] = find(parents[idx])
    return parents[idx]


for _ in range(int(input())):
    n = int(input())
    enemy = [tuple(map(int, input().split())) for _ in range(n)]
    parents = list(range(n))
    ans = n
    for i in range(n):
        x, y, r = enemy[i]
        fi = find(i)
        for j in range(i):
            z, w, d = enemy[j]
            if (x - z) ** 2 + (y - w) ** 2 <= (r + d) ** 2:
                fj = find(j)
                if fi != fj:
                    ans -= 1
                    parents[fj] = fi
    print(ans)
