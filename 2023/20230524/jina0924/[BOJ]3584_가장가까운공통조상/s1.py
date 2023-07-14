# 백준 3584번 가장 가까운 공통 조상

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    tree = {}
    for __ in range(N - 1):
        a, b = map(int, input().split())
        tree[b] = a
    x, y = map(int, input().split())
    px = set()
    px.add(x)
    node = x
    while tree.get(node):
        p = tree[node]
        px.add(p)
        node = p
    node = y
    while True:
        if node in px:
            print(node)
            break
        node = tree[node]