import sys, collections
input = sys.stdin.readline
N, K = map(int, input().strip().split())
belt = collections.deque(map(int, input().strip().split()))
robots = collections.deque([0] * N)

cnt = 0
level = 1
while cnt < K:
    # 회전
    belt.rotate(1)
    robots.rotate(1)
    # 빼기
    if robots[N-1]:
        robots[N-1] = 0
    # 한 칸 이동
    for i in range(N-1, -1, -1):
        if robots[i] and not robots[i+1] and belt[i+1]:
            robots[i+1] = 1
            robots[i] = 0
            belt[i+1] -= 1
            if belt[i+1] == 0:
                cnt += 1
    # 빼기
    if robots[N-1]:
        robots[N-1] = 0

    if belt[0]:
        robots[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1
    level += 1
print(level-1)