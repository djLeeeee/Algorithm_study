# https://www.acmicpc.net/problem/21608'
import sys
sys.stdin = open("./input/21608.txt")
input = sys.stdin.readline
# ----------------------------------------

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def set_blanks(blanks, N):
    for i in range(N):
        for j in range(N):
            cnt = 0
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if (0<= ni < N and 0<= nj < N):
                    cnt += 1
            blanks[i][j] = cnt


def get_best_position(likes, board, blanks, N):
    max_like = -1
    max_blank = -1
    mi, mj = 0, 0
    for i in range(N):
        for j in range(N):
            if (board[i][j] == 0):
                cnt = 0 
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if (0<= ni < N and 0<= nj < N and board[ni][nj] in likes):
                        cnt += 1
                if (cnt > max_like):
                    max_like = cnt
                    max_blank = blanks[i][j]
                    mi, mj = i, j
                elif (cnt == max_like and blanks[i][j] > max_blank):
                    max_blank = blanks[i][j]
                    mi, mj = i, j
    return (mi, mj)

            
    

def solution():
    N = int(input())
    students = {}
    board = [[0] * N for _ in range(N)]
    blanks = [[0] * N for _ in range(N)]
    set_blanks(blanks, N)

    for _ in range(N ** 2):
        student, *likes = map(int, input().split())
        students[student] = set(likes)

    for student in students:
        likes = students[student]
        mi, mj = get_best_position(likes, board, blanks, N)
        board[mi][mj] = student
        for d in range(4):
            ni, nj = mi + di[d], mj + dj[d]
            if (0<= ni < N and 0<= nj < N):
                blanks[ni][nj] -= 1

    ans = 0
    scores = [0, 1, 10, 100, 1000]
    for i in range(N):
        for j in range(N):
            student = board[i][j]
            likes = students[student]
            cnt = 0
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if (0<= ni < N and 0<= nj < N and board[ni][nj] in likes):
                    cnt += 1
            ans += scores[cnt]
    print(ans)
                    



solution()