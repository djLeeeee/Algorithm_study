import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())
robots = [[0, 0, 0]]
arr = [[0] * a for _ in range(b)]
direction = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
# 문제 포맷에 맞춰서 저장
for i in range(1, n+1):
    y, x, dir = input().split()
    x = b - int(x)
    y = int(y) - 1
    dir = direction[dir]
    arr[x][y] = i
    robots.append([x, y, dir])

# 상, 우, 하, 좌 => L일 경우 -1, R일 경우 +1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for case in range(m):
    robot, command, turn = input().split()
    robot, turn = int(robot), int(turn)
    x, y, dir = robots[robot]
    flag = True
    # 만약 돌리는게 여러번일 때, 4의 배수만큼 돌리면 원위치니까 4의 나머지로 처리
    if command in 'LR':
        turn %= 4
    while turn > 0:
        if command == 'L':
            dir -= 1
            if dir < 0:
                dir = 3
            # 바뀐 방향 저장
            robots[robot][2] = dir
        elif command == 'R':
            dir += 1
            if dir > 3:
                dir = 0
            # 바뀐 방향 저장
            robots[robot][2] = dir
        elif command == 'F':
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < b and 0 <= ny < a:
                # 진행하는 곳에 다른 로봇이 있는 경우
                if arr[nx][ny]:
                    flag = False
                    print(f'Robot {robot} crashes into robot {arr[nx][ny]}')
                    break
                else:
                    # arr에 저장된 위치 바꿔주고, 바뀐 정보 저장
                    arr[x][y] = 0
                    arr[nx][ny] = robot
                    x, y = nx, ny
                    robots[robot] = [x, y, dir]
            else:
                flag = False
                print(f'Robot {robot} crashes into the wall')
                break
        turn -= 1
    if not flag:
        break
else:
    print('OK')



