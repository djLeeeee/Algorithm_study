A, B = map(int, input().split())
N, M = map(int, input().split())
di = {
    'N': [-1, 0],
    'S': [1, 0],
    'E' : [0, 1],
    'W' : [0, -1],
}
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
r = []

arr = [[0] * A for _ in range(B)]
for i in range(1, N+1):
    y, x, d = input().split()
    y, x = int(y), int(x)
    arr[B-x][y-1] = i
    r.append([x, y, d])

for i in range(1, M+1):
    num, command, trials = input().split()
    num, trials = int(num), int(trials)
    robot = r[num-1]
    if command == 'F':
        x, y = robot[0], robot[1]
        for j in range(trials):
            nx, ny = x + di[robot[2]][0], y + di[robot[2]][1]
            if 1 <= nx <= B and 1 <= ny <= A:
                if arr[B-nx][ny-1]:
                    print(f'Robot {num} crashes into robot {arr[B-nx][ny-1]}')
                    exit()
                x, y = nx, ny
            else:
                print(f'Robot {num} crashes into the wall')
                exit()
        arr[B-robot[0]][robot[1]-1] = 0
        arr[B-x][y-1] = num

    elif command == 'L':
        r[num-1][2] = left[(left[robot[2]] + trials) % 4]

    else:
        r[num-1][2] = right[(right[robot[2]] + trials) % 4]
print('OK')