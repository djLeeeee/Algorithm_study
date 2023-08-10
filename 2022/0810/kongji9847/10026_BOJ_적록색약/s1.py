# bfs 사용해서 그룹 나누기

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

#from pprint import pprint


from collections import deque
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 1. bfs 사용해서 그룹 나누기 - 정상인/적록색맹 colors 딕셔너리로 구분줘서 사용하기
def solution(normal):
    if normal:
       colors = {'R':1, 'G': 2, 'B': 3}
    else:
        colors = {'R':1, 'G':1, 'B':2}

    visit = [[0]*N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if not visit[r][c]:
                cnt += 1
                visit[r][c] = cnt
                color_num = colors[data[r][c]]
                Q = deque()
                Q.append((r, c))

                while Q:
                    rr, cc = Q.popleft()
                    for d in range(4):
                        nr = rr + delta[d][0]
                        nc = cc + delta[d][1]
                        if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc] and colors[data[nr][nc]] == color_num:
                            visit[nr][nc] = cnt
                            Q.append((nr, nc))

    #pprint(visit)
    return cnt


# 0. input 받기
N = int(input())
data = [list(input().strip()) for _ in range(N)]

print(f'{solution(1)} {solution(0)}')
