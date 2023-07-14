import sys
input = sys.stdin.readline

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union_set(x, y):
    p[find_set(y)] = find_set(x)


def do(v):
    global ans
    v_set = set()                       # 탐색 중 사이클이 만들어지는지 확인 위해
    stack = [(v, v)]                    # 스택 생성
    while stack:
        v, before_v = stack.pop()       # 어떤 노드와, 그 노드가 스택에 들어갈 때 타고 온 노드
        if not visited[v]:              
            visited[v] = 1
            v_set.add(v)                # 노드 방문 체크
            for w in g[v]:
                if w != before_v:       # 노드에 연결된 노드들 체크 중, 타고 온 노드를 제외하고
                    if w in v_set:      # 예전에 방문한 노드와 연결되어 있으면 싸이클 존재
                        ans -= 1        # 집합 하나를 빼주고 리턴
                        return
                    else:               # 아니면 dfs 돌리기
                        stack.append((w, v))


cnt = 0
while True:
    cnt += 1
    V, E = map(int, input().strip().split())
    if V == 0 and E == 0:
        break
    # 그래프
    g = [[] for _ in range(V+1)]
    # 부모 표시
    p = [i for i in range(V + 1)]
    for _ in range(E):
        start, end = map(int, input().strip().split())
        g[start].append(end)
        g[end].append(start)
        union_set(start, end)

    for j in range(1, V+1):         # 이거 해줘야 할 것 같다.
        find_set(j)                 # 중간 노드가 변경되지 않는 경우 방지

    my_set = set(p)
    ans = len(my_set) - 1
    visited = [0] * (V+1)
    
    for k in my_set:
        if k != 0:              # 1번 노드부터 dfs를 돌려서 답을 찾는다
            do(k)

    if ans > 1:
        print(f'Case {cnt}: A forest of {ans} trees.')
    elif ans == 1:
        print(f'Case {cnt}: There is one tree.')
    else:
        print(f'Case {cnt}: No trees.')

# 유니온 파인드 문제에서, 부모 노드를 찾는 두 가지 방법 중 대표노드만 저장하는 방법을 쓸 경우
# 시간은 절약되지만중간에 대표 노드가 제대로 저장되지 않는 값들이 생기는 단점이 있다.
# 따라서 작업이 끝나고 난 뒤, 전체적으로 find_set(x)를 돌려줘서 
# 모든 parent 리스트에 대표 노드들이 저장되도록 한다.