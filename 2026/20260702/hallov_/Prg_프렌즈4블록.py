def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0
    while True:
        remove = set()
        for i in range(m-1):
            for j in range(n-1):
                block = board[i][j]
                if block == '':
                    continue
                a, b, c, d = board[i][j], board[i+1][j], board[i][j+1], board[i+1][j+1]
                if a == b == c == d:
                    remove.update([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])
        if not remove:
            break
        answer += len(remove)
        for i, j in remove:
            board[i][j] = ''
        for j in range(n):
            stack = []
            # 위에서부터 담고
            for i in range(m):
                if board[i][j] != '':
                    stack.append(board[i][j])
            # 아래부터 꺼내기
            for i in range(m-1, -1, -1):
                if stack:
                    board[i][j] = stack.pop()
                else:
                    board[i][j] = ''
    return answer

input_lst = [
    [4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]],
    [6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]
]

for a, b, c in input_lst:
    print(solution(a, b, c))