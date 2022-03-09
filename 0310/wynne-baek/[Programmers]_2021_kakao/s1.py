import sys
sys.stdin = open('input.txt')

def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer

def bfs(place):
    candidates = []
    for x in range(5):
        for y in range(5):
            if place[x][y] == "P":
                candidates.append((x, y))
    #1. P 기준으로 주변 탐색
    for candidate in candidates:
        x, y = map(int, candidate)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위 체크!
            if 0 <= nx < 5 and 0 <= ny < 5:
                # P 이면 방역수칙 위반!
                if place[nx][ny] == "P":
                    return 0
                # O이면 빈 테이블이므로 다시 주변 탐색!
                if place[nx][ny] == "O":
                    for i in range(4):
                        nx2 = nx + dx[i]
                        ny2 = ny + dy[i]
                        # 범위 체크!, 후보자 본인이 아닌 다른 후보자가 P이면 방역 위반!
                        if (nx2 != x and ny2 != y) and (0 <= nx2 < 5 and 0 <= ny2 < 5) and place[nx2][ny2] == "P":
                            return 0
    return 1


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))
