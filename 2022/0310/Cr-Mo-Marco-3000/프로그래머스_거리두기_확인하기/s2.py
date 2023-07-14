def solution(places):
    def do2(r, c, visited):
        # 자기 자신은 거르기 위해, 기준점 설정
        sr, sc = r, c
        # 자기는 방문햇다고 치고
        visited[r][c] = 1
        # bfs로 만들자
        Q = [[r, c]]
        while Q:
            v = Q.pop(0)
            r, c = v[0], v[1]
            # 만약 자기 자신이 아닌데, P라면
            # 이거 안 묶어주면 틀리는데, 왜 이러지?
            if (r != sr or c != sc) and g[r][c] == "P":
                # 거리두기 안 지킨 경우 0을 반환
                if visited[r][c] <= 3:
                    return 0
            # P가 아닌 경우 사방을 검사
            for w in range(4):
                nr = r + dr[w]
                nc = c + dc[w]
                if (
                    0 <= nr < 5
                    and 0 <= nc < 5
                    and g[nr][nc] in "OP"
                    and not visited[nr][nc]
                ):
                    Q.append([nr, nc])
                    visited[nr][nc] = visited[r][c] + 1
        return 1

    def do():
        for r in range(5):
            for c in range(5):
                if g[r][c] == "P":
                    # 어떤 변수를 들고 다닐지 생각하는 게, 초기화 관련 문제인 경우도 있었다.
                    visited = [[0] * 5 for _ in range(5)]
                    # 한 케이스라도 격리 망했으면, return 0
                    a = do2(r, c, visited)
                    if a == 0:
                        return 0

        # 격리가 잘 지켜졌으면, return 1
        return 1

    # 답 리스트
    answer = []
    # visited 초기화

    # 방향 초기화: 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 그래프 초기화
    g = []
    for i in range(5):
        for j in range(5):
            g.append(list(map(str, places[i][j])))
        answer.append(do())
        # 끝나고 나면 그래프와 visited 초기화
        g = []

    return answer


print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    )
)
