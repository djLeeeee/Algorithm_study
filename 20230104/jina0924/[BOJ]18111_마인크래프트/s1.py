# 백준 18111번 마인크래프트 - x

import sys
sys.stdin = open('input4.txt')


def flatten(height):
    global ans, top
    cnt, block = 0, B
    isFlatten = True
    for r in range(N):
        for c in range(M):
            if ground[r][c] > height:
                cnt += 2 * (ground[r][c] - height)
                block += ground[r][c] - height
            elif ground[r][c] < height:
                cnt += height - ground[r][c]
                if block < height - ground[r][c]:
                    isFlatten = False
                    flatten(height - 1)
                else:
                    block -= height - ground[r][c]
    if isFlatten and ans >= cnt:
        ans = cnt
        if top < height:
            top = height


N, M, B = map(int, input().split())
ground = []
total = 0
ans, top = 987987987, 0
for r in range(N):
    data = list(map(int, input().split()))
    total += sum(data)
    ground.append(data)
total /= (N * M)
flatten(int(total))
flatten(int(total) + 1)
print(ans, top)

