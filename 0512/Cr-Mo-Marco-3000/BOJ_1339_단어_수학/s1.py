from sys import stdin
from itertools import permutations

N = int(stdin.readline().rstrip())

alpha_dict = dict()

number_list = []

my_list = []
for _ in range(N):
    # 입력 받는다.
    alpha_list = tuple(map(str, stdin.readline().rstrip()))

    length = len(alpha_list)

    # alpha_dict를 순환하다가 있으면,
    for i in range(length):
        if alpha_list[i] in alpha_dict:
            alpha_dict[alpha_list[i]][-(length - i)] += 1
        else:
            # -(length - i) => 추가할 인덱스
            alpha_dict[alpha_list[i]] = [0, 0, 0, 0, 0, 0, 0, 0]
            alpha_dict[alpha_list[i]][-(length - i)] += 1

for key in alpha_dict:
    my_list.append(alpha_dict[key])

# a = list(permutations(my_list))

ans = 0
num = 9
print(my_list)

# while my_list:
#     v = my_list.pop()
#     for j in range(8):
#         if v[j]:
#             ans += v[j] * num * (10 ** (7 - j))
#     num -= 1
# print(ans)