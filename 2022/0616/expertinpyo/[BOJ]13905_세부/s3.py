# kruskal로 경로 설정
# 빼빼로를 못가져가는 경우가 있을 수 있다 = > 진짜 화나네 아니 ;

def kruskal():
    cnt = 1
    for i in range(M):
        x, y, w = arr[i][0], arr[i][1], arr[i][2]
        if find_set(x) != find_set(y):
            union(x, y)
            cnt += 1
            if find_set(s) == find_set(e):
                print(w)
                return
    else:
        print(0)
        return

def find_set(x):
    while x != p[x]:
         x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

N, M = map(int, input().split())
s, e = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
arr.sort(key=lambda x:x[2], reverse=True)
routes = [[] for _ in range(N+1)]
p = list(range(N+1))
kruskal()

