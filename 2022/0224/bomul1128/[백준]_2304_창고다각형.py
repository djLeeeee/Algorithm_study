from sys import stdin as s

column = [0] * 1001
n = int(s.readline())
for _ in range(n):
    a, b = map(int, s.readline().split())
    column[a] = b
Max_height = max(column)
Max_location = column.index(Max_height)
M = 0
for i in range(1, Max_location):
    if M < column[i]:
        M = column[i]
    else:
        column[i] = M
M = 0
for i in range(1000, Max_location, - 1):
    if M < column[i]:
        M = column[i]
    else:
        column[i] = M
print(sum(column))
