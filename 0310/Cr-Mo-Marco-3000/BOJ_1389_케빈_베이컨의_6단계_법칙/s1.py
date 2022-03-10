def do(i):
    # 들어갈 때 마다 초기화
    visited = [0] * (V + 1)
    # visited[i] = 1
    Q = [i]
    total = 0
    while Q:
        v = Q.pop(0)
        for w in range(1, V + 1):
            if not visited[w] and g[v][w]:
                visited[w] = visited[v] + 1
                total += visited[w]
                Q.append(w)
    # 자기 자기 자신이 2로 들어가기 때문에 2를 빼준다.
    return total - 2


# 첫 번째 줄 V, E
V, E = map(int, input().split())

# 그래프 초기화: 방향 없음
g = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    r, c = map(int, input().split())
    g[r][c] = 1
    g[c][r] = 1

# ans_list 초기화
ans_list = []

# 최소값 구해서 인덱스 반환
for i in range(1, V + 1):
    ans_list.append(do(i))
min_v = min(ans_list)

# 인덱스이므로 +1 해서 출력
print(ans_list.index(min_v) + 1)
