# Problem: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=5&problemLevel=6&contestProbId=AV18NaZqIt8CFAZN&categoryId=AV18NaZqIt8CFAZN&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=6&pageSize=10&pageIndex=3
# Submission: 2026-09-16 18:39 / Python / Pass
def main():
    def dfs(idx):
        visited[idx] = True
        res = [idx]
        for adj in graph[idx]:
            if not visited[adj]:
                tmp = dfs(adj)
                if len(tmp) + 1 > len(res):
                    res = [idx] + tmp
        visited[idx] = False
        return res
 
    n = int(input())
    arr = list(map(int, input().split()))
    nodes = []
    for i in range(n):
        nodes.append((arr[2 * i], arr[2 * i + 1]))
    graph = [[] for _ in range(n)]
    for i, (x, y) in enumerate(nodes):
        for j in range(i + 1, n):
            nx, ny = nodes[j]
            if y == nx:
                graph[i].append(j)
            if x == ny:
                graph[j].append(i)
    ans = []
    for i in range(n):
        visited = [False] * n
        tmp = dfs(i)
        if len(tmp) > len(ans):
            ans = tmp
    return " ".join(" ".join(map(str, nodes[i])) for i in ans)
 
 
if __name__ == "__main__":
    for tc in range(int(input())):
        print(f"#{tc + 1} {main()}")
