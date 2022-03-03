
T = 4
square_list = []
for _ in range(T):
    square_list.append(list(map(int, input().split())))
max_x = 0
max_y = 0
# 각 좌표들을 돌면서, 구현할 최대 넓이를 구하기 위한 최대 좌표를 찾는다.
for square in square_list:
    if square[2] > max_x:
        max_x = square[2]
    if square[3] > max_y:
        max_y = square[3]

# 좌표가 아니라, 면을 행렬의 인자로 삼는다.
my_list = [[0] * max_x for _ in range(max_y)]

for i in range(T):      # 사각형의 목록을 순환
    for j in range(square_list[i][1], square_list[i][3]):
        for k in range(square_list[i][0], square_list[i][2]):   # square_list[i][0] : 좌하방 x좌표
            my_list[j][k] = 1                                   # square_list[i][1] : 좌하방 y좌표
                                                                # square_list[i][2] : 우상방 x좌표
                                                                # square_list[i][3] : 우상방 y좌표
cnt = 0
for i in range(max_y):
    for j in range(max_x):
        if my_list[i][j] == 1:
            cnt += 1
print(cnt)

