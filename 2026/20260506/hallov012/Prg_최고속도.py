import sys
from collections import defaultdict


def solution(city, road):
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            p[y] = x

    def on_line(x, y, x1, y1, x2, y2):
        return x1 <= x <= x2 and y1 <= y <= y2

    def add_point(px, py, i, j):
        x1, y1, x2, y2, _ = road[i]
        a1, b1, a2, b2, _ = road[j]
        # 해당 점이 두 도로 모두 위에 있으면 교차점
        if on_line(px, py, x1, y1, x2, y2) and on_line(px, py, a1, b1, a2, b2):
            points[i].add((px, py))
            points[j].add((px, py))


    points = defaultdict(set)
    cam_limit = {}

    # 도시/카메라 추가
    for i, (x1, y1, x2, y2, limit) in enumerate(road):
        for x, y in city:
            if on_line(x, y, x1, y1, x2, y2):
                points[i].add((x, y))
        m_point = ((x1+x2)//2, (y1+y2)//2)
        points[i].add(m_point)
        if m_point not in cam_limit:
            cam_limit[m_point] = limit
        else:
            cam_limit[m_point] = min(cam_limit[m_point], limit)

    # 교차점 추가
    n = len(road)
    for i in range(n):
        x1, y1, x2, y2, _ = road[i]
        for j in range(i+1, n):
            a1, b1, a2, b2, _ = road[j]
            # 세로/가로
            if x1 == x2 and b1 == b2:
                add_point(x1, b1, i, j)
            # 가로/세로
            elif y1 == y2 and a1 == a2:
                add_point(a1, y1, i, j)
            # 같은 세로선
            elif x1 == x2 and a1 == a2 and x1 == a1:
                y_lst = [y1, y2, b1, b2]
                for y in y_lst:
                    add_point(x1, y, i, j)
            elif y1 == y2 and b1 == b2 and y1 == b1:
                x_lst = [x1, x2, a1, a2]
                for x in x_lst:
                    add_point(x, y1, i, j)

    idx = {}
    node = 0
    for s in points.values():
        for p in s:
            if p not in idx:
                idx[p] = node
                node += 1

    p = list(range(node))

    edges = []
    for i, (x1, y1, x2, y2, _) in enumerate(road):
        arr = list(points[i])
        # 세로선 -> y 정렬
        if x1 == x2:
            arr.sort(key=lambda x:x[1])
        # 가로선 -> x 정렬
        else:
            arr.sort(key=lambda x:x[0])

        for j in range(len(arr)-1):
            p1, p2 = arr[j], arr[j+1]
            u, v = idx[p1], idx[p2]

            w = sys.maxsize
            if p1 in cam_limit:
                w = min(w, cam_limit[p1])
            if p2 in cam_limit:
                w = min(w, cam_limit[p2])

            if w == sys.maxsize:
                union(u, v)
            else:
                edges.append((w, u, v))

    city_node = [idx[(x, y)] for x, y in city]
    ans = [-1] * len(city)
    s = city_node[0]
    for i in range(len(city)):
        if find(s) == find(city_node[i]):
            ans[i] = 0

    edges.sort(reverse=True)
    for w, u, v in edges:
        union(u, v)
        root = find(s)
        for i in range(1, len(city)):
            if ans[i] != -1:
                continue
            if root == find(city_node[i]):
                ans[i] = w
    return ans[1:]
