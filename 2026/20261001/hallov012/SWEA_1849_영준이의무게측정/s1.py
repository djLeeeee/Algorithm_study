import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        parent = p[x]
        p[x] = find(parent)
        diff[x] += diff[parent]
    return p[x]

def union(a, b, w):
    pa, pb = find(a), find(b)
    if pa == pb:
        return
    # diff[a] = w[a] - w[pa]
    # diff[b] = w[b] - w[pb]
    # w[pb] - w[pa] = (w[b] - diff[b]) - (w[a] - diff[a])
    #               = diff[a] + (w[pb] - w[pa]) + diff[b]
    if size[pa] >= size[pb]:
        p[pb] = pa
        diff[pb] = diff[a] + w - diff[b]
        size[pa] += size[pb]
    else:
        p[pa] = pb
        diff[pa] = diff[b] - w - diff[a]
        size[pb] += size[pa]

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    p = list(range(n+1))
    diff = [0] * (n+1) # i번 샘플의 무게 - 부모 샘플의 무게
    size = [1] * (n+1)
    ans = []

    for _ in range(m):
        data = input().split()
        if data[0] == '!':
            a, b, w = map(int, data[1:])
            union(a, b, w)
        else:
            a, b = map(int, data[1:])
            if find(a) != find(b):
                ans.append('UNKNOWN')
            else:
                ans.append(str(diff[b] - diff[a]))
    print(f"#{tc}", *ans)

