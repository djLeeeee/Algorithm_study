import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

di = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))

N, M = map(int, input().split())
mt = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
ans = 0

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1
    for i in range(len(clouds)):
        clouds[i] = ((clouds[i][0]+di[d][0]*s)%N, (clouds[i][1]+di[d][1]*s)%N)
        mt[clouds[i][0]][clouds[i][1]] += 1

    for i in range(len(clouds)):
        cnt = 0
        for j in range(1, 8, 2):
            nr, nc = clouds[i][0]+di[j][0], clouds[i][1]+di[j][1]
            if 0 <= nr < N and 0 <= nc < N and mt[nr][nc] > 0:
                cnt += 1
        mt[clouds[i][0]][clouds[i][1]] += cnt

    new_clouds = []
    for r in range(N):
        for c in range(N):
            if (r, c) not in clouds and mt[r][c] >= 2 and (r, c):
                new_clouds.append((r, c))
                mt[r][c] -= 2
    clouds = new_clouds


for r in range(N):
    for c in range(N):
        ans += mt[r][c]

print(ans)