# Problem: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LnipaDvwDFAXc&categoryId=AV5LnipaDvwDFAXc&categoryType=CODE&problemTitle=1855&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# Submission: 2026-08-12 21:59 / Python / Pass
def main():
    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a
        while depth[a] > depth[b]:
            a = parents[a]
        while a != b:
            a = parents[a]
            b = parents[b]
        return a
 
    n = int(input())
    parents = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    for i, p in enumerate(parents, start=2):
        graph[p].append(i)
    parents = [0, 0] + parents
    depth = [0] * (n + 1)
    for i in range(2, n + 1):
        depth[i] = depth[parents[i]] + 1
    que = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    for idx in que:
        for adj in graph[idx]:
            if not visited[adj]:
                visited[adj] = True
                que.append(adj)
    ans = 0
    for i in range(1, n):
        idx, adj = que[i - 1], que[i]
        ans += depth[idx] + depth[adj] - 2 * depth[lca(idx, adj)]
    return ans
 
 
if __name__ == "__main__":
    for tc in range(int(input())):
        ans = main()
        print(f"#{tc + 1} {ans}")
