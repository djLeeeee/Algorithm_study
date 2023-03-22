## pypy3 통과
import sys
sys.stdin = open("input/15684.txt")
input = sys.stdin.readline

def check():
    for start in range(N):
        k = start
        for j in range(H):
            if board[j][k]:
                k += 1
            elif k > 0 and board[j][k - 1]:
                k -= 1
        if k != start:
            return False
    return True

def dfs(cnt, x, y):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return
    
    for i in range(x, H):
        k = y if i == x else 0
        
        for j in range(k, N - 1):
            if not board[i][j] and not board[i][j + 1]:
                if j > 0 and board[i][j - 1]:
                    continue
                board[i][j] = True
                dfs(cnt + 1, i, j + 2)
                board[i][j] = False


N, M, H = map(int, sys.stdin.readline().split())
board = [[False] * N for _ in range(H)] # 특정 지점 방문 여부 체크
if M == 0: # M이 0일 경우 출발점에서 도착점으로 바로 내려오므로 0 출력 후 종료
    print(0)
    exit(0)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    board[a - 1][b - 1] = True
ans = 4 # 결과값 4로 초기화
dfs(0, 0, 0)
print(ans if ans < 4 else -1)