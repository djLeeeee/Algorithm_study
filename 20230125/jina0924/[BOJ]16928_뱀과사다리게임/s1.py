# 백준 16928번 뱀과 사다리 게임

import sys
sys.stdin = open('input1.txt')


def bfs():
    queue = [1]                             # 1번 칸부터 게임 시작
    visited[1] = 1

    while queue:
        s = queue.pop(0)                    # s: 현재 위치
        if s == 100:
            return visited[100] - 1         # 1번 칸에서 1로 시작했으므로 -1 해야 주사위 굴린 횟수
        for d in range(1, 7):
            # 주사위를 굴려서 나온 위치 값과 뱀 또는 사다리로 이동한 값 모두 방문하지 않았을 경우에만 방문처리
            if 0 < s + d <= 100 and not visited[s + d] and not visited[game[s + d]]:
                visited[s + d] = visited[game[s + d]] = visited[s] + 1
                queue.append(game[s + d])


N, M = map(int, input().split())            # N, M: 사다리의 수, 뱀의 수
game = [i for i in range(101)]              # 뱀 또는 사다리를 타고 이동하게 되는 칸의 정보
visited = [1] + [0] * 100                   # 방문 처리 및 주사위 굴린 횟수 저장용
for _ in range(N):
    x, y = map(int, input().split())
    game[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    game[u] = v
ans = bfs()
print(ans)