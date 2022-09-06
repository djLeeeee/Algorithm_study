# 정답 풀이

A, B = map(int, input().split())    # A 가로 / B 세로
N, M = map(int, input().split())
robots = []
arr = [[0] * (A+1) for _ in range(B+1)]
left = {
    'N': 0,
    'S': 2,
    'E' : 3,
    'W' : 1,
    0 : 'N',
    2: 'S',
    3: 'E',
    1: 'W'
}
right = {
    'N': 0,
    'S': 2,
    'E' : 1,
    'W' : 3,
    0: 'N',
    2:'S',
    1:'E',
    3:'W'
}

for i in range(1, N+1):
    x, y, direction = input().split()
    x, y = int(x), int(y)
    arr[B-y][x] = i
    robots.append([x, y, direction])

di = {
    'N': [0, 1],    # 위로
    'S': [0, -1],   # 아래로
    'E' : [1, 0],   # 오른쪽으로
    'W' : [-1, 0],  # 왼쪽으로
}
for i in range(M):
    number, command, trials = input().split()
    number, trials = int(number), int(trials)
    robot = robots[number - 1]
    if command == 'F':
        x, y = robot[0], robot[1]
        for t in range(trials):
            nx, ny = x + di[robot[2]][0], y + di[robot[2]][1]
            if 1 <= nx <= A and 1 <= ny <= B:
                if arr[B-ny][nx]:
                    print(f'Robot {number} crashes into robot {arr[B-ny][nx]}')
                    exit()
                x, y = nx, ny
            else:
                print(f'Robot {number} crashes into the wall')
                exit()
        arr[B-robots[number-1][1]][robots[number-1][0]] = 0
        robots[number-1][0], robots[number-1][1] = x, y
        arr[B-y][x] = number

    elif command == 'L':
         robots[number-1][2] = left[(left[robot[2]] + trials) % 4]
    else:
        robots[number-1][2] = right[(right[robot[2]] + trials) % 4]
print('OK')