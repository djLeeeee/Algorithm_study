import sys
sys.stdin = open('input.txt')

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

case = 1
while True:
    # 입력
    N, M = map(int, input().split())
    # 종료 조건
    if N == 0 and M == 0:
        break
    # 계산
    tree = 0
    ## 연결리스트
    cycle = []
    ## 분리집합
    parent = [i for i in range(N + 1)]
    for i in range(M):
        A, B = map(int, input().split())
        a = find(parent, A)
        b = find(parent, B)
        if a != b:
            union(parent, A, B)
        else:
            cycle.append(a)
    # print(parent)
    for i in range(N + 1):
        find(parent, i)
    # print(parent)
    # print(cycle)
    group = set()
    for spot in cycle:
        group.add(parent[spot])

    parent = list(set(parent))
    for i in parent:
        if i != 0 and i not in group:
            tree += 1
    # print(tree)
    # 출력
    if tree >= 2:
        print(f'Case {case}: A forest of {tree} trees.')
    elif tree == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: No trees.')
    case += 1