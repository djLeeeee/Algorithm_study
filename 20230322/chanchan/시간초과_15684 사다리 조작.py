# https://www.acmicpc.net/problem/15684

import sys
sys.stdin = open("input/15684.txt")
input = sys.stdin.readline

class Ladder():
    answer = 4
    def __init__(self, N, H):
        self.row_size = N
        self.col_size = H
        self.board = [[0] * N for _ in range(H)]

    def add_bridge(self, i, j):
        self.board[i][j] = 1

    def del_bridge(self, i, j):
        self.board[i][j] = 0

    def isInArea(self, i, j):
        isInRow = 0 <= i and i < self.col_size
        isInCol = 0 <= j and j < self.row_size
        return isInRow and isInCol
    
    def can_add_bridge(self, i, j):
        for nj in [j - 1, j, j + 1]:
            if (self.isInArea(i, nj) and self.board[i][nj] == 1):
                return False
        return True
    
    def isIOSame(self):
        for start in range(self.row_size):
            nj = start
            for i in range(self.col_size):
                if (self.board[i][nj]):
                    nj += 1
                elif (nj > 0 and self.board[i][nj - 1]):
                    nj -= 1
            
            if (start != nj):
                return False
        return True


    def put_bridge(self, ci, cj, cnt):
        if (self.isIOSame()):
            Ladder.answer = min(Ladder.answer, cnt)
            return
        
        elif (cnt == 3 or cnt >= Ladder.answer):
            return

        for i in range(ci, self.col_size):
            k = cj if i == ci else 0
            for j in range(k, self.row_size - 1):
                if not self.board[i][j] and not self.board[i][j + 1]:
                    if j > 0 and self.board[i][j - 1]:
                        continue
                    self.add_bridge(i, j)
                    self.put_bridge(cnt + 1, i, j + 2)
                    self.del_bridge(i, j)


def solution():
    N, M, H = map(int, input().split())
    ladder = Ladder(N, H)

    for _ in range(M):
        i, j = map(int, input().split())
        ladder.add_bridge(i - 1, j - 1)
    
    ladder.put_bridge(0, 0, 0)
    print(-1 if Ladder.answer == 4 else Ladder.answer)


solution()