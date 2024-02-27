from collections import deque
import sys
# 기준 블록: 무지개 블록이 아닌 블록 중에서 행의 번호가 제일 작은 블록, 열의 번호가 가장 작은 블록
# 크기가 가장 큰 블록 그룹, 포함된 무지개 블록의 수가 가장 많은 경우, 기준블록의 행이 가장 큰 경우, 기준블록의 열이 가장 큰 경우

di = ((-1, 0), (1, 0), (0, -1), (0, 1))
ans = 0

# mt[br][bc] 블록이 포함된 블록 그룹 구하기
def block_group(br, bc, color):
    cnt = 1
    res = set()
    rainbow = set()
    res.add((br, bc, mt[br][bc]))
    while queue:
        r, c, tmp = queue.popleft()
        for dr, dc in di:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and (mt[nr][nc] == color or mt[nr][nc] == 0) and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                if mt[nr][nc] == 0:
                    rainbow.add((nr, nc))
                queue.append((nr, nc, mt[nr][nc]))
                res.add((nr, nc, mt[nr][nc]))

    # 무지개 블록은 다른 블록 그룹에 중복으로 들어갈 수 있으므로 방문체크 해제
    for rr, rc in rainbow:
        visited[rr][rc] = 0

    if len(res) > 1 and len(res)-len(rainbow) > 0:
        return sorted(list(res), key=lambda x: (-x[2], x[0], x[1]))+[len(rainbow)]
    else:
        return []


# ----------------------------------------------------------------------------------
N, M = map(int, input().split())
mt = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
queue = deque()


# ----------------------------------------------------------------------------------
# 가장 큰 블록그룹 찾기
def find_biggest_group():
    group = []
    for r in range(N):
        for c in range(N):
            if mt[r][c] != '' and mt[r][c] > 0 and visited[r][c] == 0:
                queue.append((r, c, mt[r][c]))
                visited[r][c] = 1
                res = block_group(r, c, mt[r][c])
                # 블록 그룹 목록에 담기
                if len(res) > 0:
                    group.append(res)

    if len(group) == 0:
        return group

    group.sort(key= lambda x : (-len(x), -x[-1], -x[0][0], -x[0][1]))

    return group[0][:-1]


# ----------------------------------------------------------------------------------
# 블록 제거
def delete_block(grp):
    for r, c, tmp in grp:
        mt[r][c] = ''


# ----------------------------------------------------------------------------------
# 중력 작용
def gravity():
    for c in range(N):
        cnt = 0
        for r in range(N-1, -1, -1):
            if mt[r][c] == '':                                  # 블록이 비어있는경우
                cnt += 1                                        # 내려가야 할 칸수 1 증가
            elif mt[r][c] >= 0 and cnt > 0:                     # 무지개 or 일반블록이고, 내려가야 할 칸수 존재 시
                mt[r][c], mt[r+cnt][c] = mt[r+cnt][c], mt[r][c] # 중력 적용
            elif mt[r][c] == -1:                                # 남은 경우의 수 1: 무지개 or 일반블록인데 내려가야 할 칸수 미존재 -> pass
                cnt = 0                                         # 남은 경우의 수 2: 검은색블록일 경우 -> 내려가야 할 칸수 초기화


# ----------------------------------------------------------------------------------
while True:
    # 점수 합산
    biggest_group = find_biggest_group()
    if len(biggest_group) == 0:
        break
    ans += len(biggest_group)**2

    delete_block(biggest_group)
    gravity()
    mt = list(map(list, zip(*mt)))[::-1]
    gravity()
    visited = [[0]*N for _ in range(N)]


print(ans)