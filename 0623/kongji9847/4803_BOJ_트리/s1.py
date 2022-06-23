'''
연결된 노드가 1개라면 leaf이자 root!
연결 노드가 1개인 곳을 root로 지정해서 dfs로 탐색하며 tree를 구성하는 자손 노드들과 cycle 여부 확인하기
top-down 형태로 내려감
'''

import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

# 4-1. 해당 node를 root로 하는 트리인지 확인: tree를 구성하는 자손 노드와, cycle 여부를 확인한다.
# 부모 -> 자식 으로 top-down 형태로 내려가므로 이전에 확인한 노드는 부모 노드로 확정된 상황이고, 해당 노드가 다시 호출되는 상황은 cycle 상황이다.
def dfs(root):
    stack = []
    for second_node in link[root]:
        stack.append((root, second_node))               # stack에 root와 연결된 자손 노드들을 추가한다.

    while stack:
        parent, child = stack.pop()
        nodes[child] = 2                                # root가 아닌 자손이므로 '2'로 방문 표시 -> root는 아니지만 어떤 자손의 부모 노드라는 뜻
        for grand_child in link[child]:                 # 자손 노드의 자손 확인하면서 stack에 넣어주기
            if grand_child != parent:                   # 부모가 아닌 자손(손자)라면
                if nodes[grand_child] == 0:             # 아직 방문한 적이 없다면 stack에 넣어주기
                    stack.append((child, grand_child))

                else:                                   # 이미 전에 방문한 적이 있다면, 이미 누군가의 부모가 해당 노드의 자손이 되는 모양이다.(cycle이 형성된 것)
                    nodes[child] = 2
                    nodes[root] = 3                     # root는 더 이상 root가 아니게 된다.


# 0. input 받기
tc = 0
while True:
    # 1. 노드 수, 간선 개수 input 받기
    n, m = map(int, input().split())
    # 0, 0으로 종료되기 전까지
    if n == 0 and m == 0:
        break

    # 2. 하나의 테스트 케이스 시작
    else:
        tc += 1
        link = [[] for _ in range(n + 1)]
        tree_cnt = 0

        # 3. 2차원 배열에 연결된 노드 모두 저장하면서 input 받기(인접 배열)
        for i in range(m):
            node1, node2 = map(int, input().split())
            link[node1].append(node2)
            link[node2].append(node1)

        # 4. 각 노드들을 모두 탐색하며 tree 개수 세기
        nodes = [0]*(n+1)
        for j in range(1, n+1):
            if len(link[j]) == 1 and not nodes[j]:                  # 연결된 노드가 1개이고, 아직 방문하지 않은 노드라면
                nodes[j] = 1                                        # 해당 노드를 root로 지정해서 이 노드를 root로 하는 tree 확인하기
                dfs(j)
                if nodes[j] == 1:                                   # tree를 확인한 후에도 여전히 root 노드로 남아있다면 tree 개수 갱신
                    tree_cnt += 1

            elif len(link[j]) == 0 and not nodes[j]:                # 연결된 노드가 없고 방문하지 않은 노드라면
                nodes[j] = 1                                        # 자기 자신을 root로 하는 노드로, tree 이다.
                tree_cnt += 1

        # 5. 해당 case의 최종 tree 개수 세기
        if tree_cnt == 0:
            print(f'Case {tc}: No trees.')
        elif tree_cnt == 1:
            print(f'Case {tc}: There is one tree.')
        else:
            print(f'Case {tc}: A forest of {tree_cnt} trees.')