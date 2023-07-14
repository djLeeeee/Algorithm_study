from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[a] = b


n = int(input())
m = int(input())
parent = list(range(n + 1))
for i in range(n):
    connection = list(map(int, input().split()))
    for j in range(i + 1, n):
        if connection[j] == 1:
            union(i + 1, j + 1)

tour_list = list(map(int, input().split()))
arrival = tour_list.pop()
while tour_list:
    latest = tour_list.pop()
    if find(latest) != find(arrival):
        print('NO')
        exit(0)
    arrival = latest
print('YES')
