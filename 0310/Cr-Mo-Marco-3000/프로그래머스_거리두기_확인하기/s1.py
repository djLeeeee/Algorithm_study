import sys

sys.stdin = open("input.txt")


def do2(r, c):
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
                # 한 케이스라도 격리 망했으면, return 0
                a = do2(r, c)
                if a == 0:
                    return 0
    # 격리가 잘 지켜졌으면, return 1
    return 1


def solution(places):
    # 입력 받기: 2차원 문자열 배열이랍신다 ㅅㅂ
    my_list = places
    # 그래프 초기화
    g = []
    temp = []
    i = 0
    # 답 리스트
    answer = []
    # visited 초기화
    visited = [[0] * 5 for _ in range(5)]

    # 방향 초기화: 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # g 만들기
    while i < len(my_list):
        if my_list[i] in '"':
            # i + 1 부터 i + 5 까지
            g.append(list(map(str, my_list[i + 1 : i + 6])))
            i += 8
        i += 1
        if len(g) == 5:
            answer.append(do())
            # 끝나고 나면 그래프와 visited 초기화
            g = []
            visited = [[0] * 5 for _ in range(5)]
    return answer


# 아래는 출력용 답


# # 입력 받기
# my_list = list(input())
# # 그래프 초기화
# g = []
# temp = []
# i = 0
# # 답 리스트
# answer = []
# # visited 초기화
# visited = [[0] * 5 for _ in range(5)]

# # 방향 초기화: 상 우 하 좌
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]

# # g 만들기
# while i < len(my_list):
#     if my_list[i] in '"':
#         # i + 1 부터 i + 5 까지
#         g.append(list(map(str, my_list[i + 1 : i + 6])))
#         i += 8
#     i += 1
#     if len(g) == 5:
#         answer.append(do())
#         # 끝나고 나면 그래프와 visited 초기화
#         g = []
#         visited = [[0] * 5 for _ in range(5)]
# print(answer)
