# 가로 세로
X, Y = map(int , input().split()) 

T = int(input())

my_list = [list(map(int, input().split())) for _ in range(T)]

# 동근이의 방향 d, 동근이의 위치 h

d, h = map(int, input().split())

total = 0

if d == 2:
    for i in range(len(my_list)):
        if my_list[i][0] == 2:
            total += abs(h - my_list[i][1])
        elif my_list[i][0] == 3:
            total += h
            total += Y - my_list[i][1]
        elif my_list[i][0] == 4:
            total += X - h
            total += Y - my_list[i][1]
        elif my_list[i][0] == 1:
            total += min(h + my_list[i][1], X - h + (X - my_list[i][1]))
            total += Y
elif d == 1:
    for i in range(len(my_list)):
        if my_list[i][0] == 1:
            total += abs(h - my_list[i][1])
        elif my_list[i][0] == 3:
            total += h
            total += my_list[i][1]
        elif my_list[i][0] == 4:
            total += X - h
            total += my_list[i][1]
        elif my_list[i][0] == 2:
            total += Y
            total += min(h + my_list[i][1], X-h + (X - my_list[i][1]))
elif d == 3:
    for i in range(len(my_list)):
        if my_list[i][0] == 3:
            total += abs(h - my_list[i][1])
        elif my_list[i][0] == 1:
            total += h
            total += my_list[i][1]
        elif my_list[i][0] == 2:
            total += Y - h
            total += my_list[i][1]
        elif my_list[i][0] == 4:
            total += X
            total += min(h + my_list[i][1], Y-h + (Y - my_list[i][1]))
elif d == 4:
    for i in range(len(my_list)):
        if my_list[i][0] == 4:
            total += abs(h - my_list[i][1])
        elif my_list[i][0] == 1:
            total += h
            total += X - my_list[i][1]
        elif my_list[i][0] == 2:
            total += Y - h
            total += X - my_list[i][1]
        elif my_list[i][0] == 3:
            total += X
            total += min(h + my_list[i][1], Y-h + (Y - my_list[i][1]))
print(total)
