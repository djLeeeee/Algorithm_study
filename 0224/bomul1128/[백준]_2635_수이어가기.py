from sys import stdin as s

n = int(s.readline())
result = [n, n, 0, n]
for i in range(1, n + 1):
    my_list = [n, i]
    while my_list[- 1] <= my_list[- 2]:
        my_list.append(my_list[-2] - my_list[-1])
    if len(result) < len(my_list):
        result = my_list
print(len(result))
print(*result)
