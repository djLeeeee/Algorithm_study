def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer


def check(board):
    board = [list(line) for line in board]
    starts = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'P':
                starts.append((i, j))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for x, y in starts:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if board[nx][ny] == 'O':
                    board[nx][ny] = 'P'
                elif board[nx][ny] == 'P':
                    return 0
    return 1


print(solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]))
