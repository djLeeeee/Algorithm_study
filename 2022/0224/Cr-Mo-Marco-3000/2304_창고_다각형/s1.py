import sys

sys.stdin = open('input.txt')

T = int(input())

my_list = [0] * 1001
N = len(my_list)
for _ in range(T):
    a, b = map(int, input().split())
    my_list[a] = b

left_list = []
right_list = []

# 왼쪽부터 더 높은 기둥이 나올 때의 인덱스를 구한다.
max_v = 0
for i in range(N):
    if my_list[i] > max_v:
        left_list.append(i)
        max_v = my_list[i]

# 오른쪽부터 더 높은 기둥이 나올 때의 인덱스를 구한다.
max_v = 0
for i in range(N-1, -1, -1):
    if my_list[i] > max_v:
        right_list.append(i)
        max_v = my_list[i]

# 가장 긴 기둥의 수가 동수일때를 구하는 것 주의!
# => 가장 큰 기둥들 사이의 값을 따로 구해주어야 한다.
area = (right_list[-1] - left_list[-1] + 1) * my_list[right_list[-1]]

# 좌측에서부터 가장 큰 기둥이 나올 때까지의 인덱스 별로 넓이를 구한다.
for i in range(len(left_list)-1):
    area += (left_list[i+1] - left_list[i]) * my_list[left_list[i]]
# 우측에서부터 가장 큰 기둥이 나올 때까지의 인덱스 별로 넓이를 구한다.
for i in range(len(right_list)-1):
    area += (right_list[i] - right_list[i+1]) * my_list[right_list[i]]
# 만나서 더러웠고 다시는 보지 말자
print(area)