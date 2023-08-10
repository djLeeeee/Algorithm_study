# bfs로 모든 경우를 확인한다.
# cctv가 없을 때도 고려해주기 -> 런타임 에러
from copy import deepcopy
from collections import deque
# 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다.
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]      # 상하좌우
CCTV = {1 : [(0), (1), (2), (3)],
        2 : [(0, 1), (2, 3)],
        3 : [(0, 2), (0, 3), (1, 2), (1, 3)],
        4 : [(0, 2, 3), (1, 2, 3), (2, 0, 1), (3, 0, 1)],
        5 : [(0, 1, 2, 3)]}

def monitor(data):
    # 마지막에 모든 경우가 고려된 arr를 넣을 통 -> 이후 0의 개수 세서 최소 사각지대 개수 구하기
    ans = []
    # cctv의 위치 및 cctv 종류를 담을 통
    cctvs = []
    for r in range(N):
        for c in range(M):
            if data[r][c] != 0 and data[r][c] != 6:
                cctvs.append((r, c, data[r][c]))

    # cctv가 있다면 -> bfs
    if cctvs:
        Q = deque([ [cctvs[0], data, 0] ])
        while Q:
            # k는 cctvs의 인덱스 -> 다음 단계의 cctv를 확인하기 위해 필요하다.
            [(sr, sc, indx), arr, k] = Q.popleft()

            # cctv의 종류에 따라 회전 가능한 방향이 여러개 이다. -> 2번 cctv는 2개, 1번 cctv는 4개
            for i in range(len(CCTV[indx])):
                new_arr = deepcopy(arr)             # 새로운 회전 방향을 볼때마다 deepcopy로 new_arr초기화해주기

                if indx == 1:                       # 1번 cctv는 j가 나올 수 없다. -> len(CCTV[1][0]) => 오류
                    going(sr, sc, CCTV[indx][i], new_arr)

                else:
                    for j in range(len(CCTV[indx][0])):     # 한번 회전했을때, cctv에서 한번에 볼 수 있는 방향 개수 -> 3번 CCTV는 3개
                        going(sr, sc, CCTV[indx][i][j], new_arr)

                # Q에 다음 단계를 넣어주는 것 -> 특정 방향에서의 한 cctv를 보고 cctv를 회전하기 전에
                if k == len(cctvs) - 1:                    # 만약에 마지막 cctv였다면 ans에 arr 넣어주고
                    ans.append(new_arr)

                elif k+1 < len(cctvs):                      # 아직 봐야할 cctv가 남아있으면
                    Q.append([cctvs[k+1], new_arr, k+1])    # 현재 new_arr를 Q에 저장하고 다음 cctv를 불러준다. -> [cctvs[k+1] : 미래, new_arr: 현재, k+1: 미래]

        # 모든 경우를 따졌다면 각 경우에서 0의 개수를 세어주고 가장 작은 애 확인
        answer = []
        for info in ans:
            cnt = 0
            for r in range(N):
                for c in range(M):
                    if info[r][c] == 0:
                        cnt += 1
            answer.append(cnt)

    else:
        cnt = 0
        for r in range(N):
            for c in range(M):
                if data[r][c] != 6:
                    cnt += 1
        return cnt

    return min(answer)


# 시작지점에서 어떠한 방향으로 감시 영역을 표시하는 함수
# 시작지점, 방향(상하좌우), data
def going(sr, sc, d, data):
    nr, nc = sr + delta[d][0], sc + delta[d][1]
    while 0 <= nr < N and 0 <= nc < M:
        if data[nr][nc] == 0:
            data[nr][nc] = '#'
        elif data[nr][nc] == 6:
            break
        nr += delta[d][0]
        nc += delta[d][1]



import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N: 행의 수, M:열의 수
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(monitor(data))