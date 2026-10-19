# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/17679
# Submission: 2026-07-02 14:59:51 Python3 정답 100 /
def solution(n, m, board):
    def transfer(char):
        return ord(char) - 64
    
    def empty_board():
        return  [[0] * m for _ in range(n)]
    
    def check(board, x, y):
        if board[x][y] == 0:
            return False
        return board[x][y] == board[x][y + 1] == board[x + 1][y] == board[x + 1][y + 1]
    
    def pop_box(board, x, y):
        board[x][y] = 0
        board[x + 1][y] = 0
        board[x][y + 1] = 0
        board[x + 1][y + 1] = 0
    
    def drop(board):
        for y in range(m):
            column = []
            for x in range(n):
                if v := board[x][y]:
                    column.append(v)
                board[x][y] = 0
            for i, v in enumerate(column[::-1], start=1):
                board[n - i][y] = v            
        
    board = [list(map(transfer, line)) for line in board]
    while True:
        pop_targets = []
        for i in range(n - 1):
            for j in range(m - 1):
                if check(board, i, j):
                    pop_targets.append((i, j))
        if not pop_targets:
            break
        for i, j in pop_targets:
            pop_box(board, i, j)
        drop(board)
    return sum(line.count(0) for line in board)
