def main():
    def set_height(idx):
        h = heights[idx]
        if h != 0:
            return h
        nh = set_height(parents[idx])
        heights[idx] = nh + 1
        return nh + 1
    
    def set_size(idx):
        s = sizes[idx]
        if s != 0:
            return s
        ns = 1
        for adj in graph[idx]:
            ns += set_size(adj)
        sizes[idx] = ns
        return ns

    n, m, ini, fin = map(int, input().split())
    edges = map(int, input().split())
    parents = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        x, y = next(edges), next(edges)
        parents[y] = x
        graph[x].append(y)
    heights = [0] * (n + 1)
    heights[1] = 1
    sizes = [0] * (n + 1)
    for idx in range(1, n + 1):
        set_height(idx)
        set_size(idx)
    hi, hf = heights[ini], heights[fin]
    if hi > hf:
        ini, fin = fin, ini
        hi, hf = hf, hi
    for _ in range(hf - hi):
        fin = parents[fin]
    while ini != fin:
        ini = parents[ini]
        fin = parents[fin]
    return ini, sizes[ini]
    

if __name__ == '__main__':
    for tc in range(int(input())):
        idx, size = main()
        print(f"#{tc + 1} {idx} {size}")
