# 반복으로 풀기

N = int(input())
max_list = [N, N+1]
max_length = 2
for i in range(N, 0, -1):
    my_list = [N, i]
    j = 0
    # 이건 내 잘못이 맞다. >= 대신 >을 썼다.
    # 문제를 잘 읽자
    while my_list[j] - my_list[j+1] >= 0:
        my_list.append(my_list[j] - my_list[j+1])
        j += 1
    if len(my_list) > len(max_list):
        max_length = len(my_list)
        max_list = my_list
print(max_length)
print(*max_list)