# Problem: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=5&problemLevel=6&contestProbId=AV5PNx_KACIDFAUq&categoryId=AV5PNx_KACIDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=6&pageSize=10&pageIndex=3
# Submission: 2026-08-27 21:49 / Python / Pass
def main():
    def line():
        tmp = input()
        return [int(c) if c.isdigit() else 0 for c in tmp]
 
    n, m = map(int, input().split())
    board = [line() for _ in range(n)]
    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    empty_count = [[0] * m for _ in range(n)]
    queue = []
    for x in range(n):
        for y in range(m):
            if not board[x][y]:
                continue
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and not board[nx][ny]:
                    empty_count[x][y] += 1
            if empty_count[x][y] >= board[x][y]:
                queue.append((x, y))
    turn = 0
    while queue:
        gone = []
        while queue:
            x, y = queue.pop()
            if board[x][y]:
                board[x][y] = 0
                gone.append((x, y))
        turn += 1
        for x, y in gone:
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if not board[nx][ny]:
                    continue
                empty_count[nx][ny] += 1
                if empty_count[nx][ny] == board[nx][ny]:
                    queue.append((nx, ny))
    return turn
 
 
if __name__ == "__main__":
    for tc in range(int(input())):
        print(f"#{tc + 1} {main()}")
