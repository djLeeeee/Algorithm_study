import sys


sys.stdin = open('input.txt')

S = int(input())
my_list = list(map(int, input().split()))
N = len(my_list)
s_num = int(input())
# 1은 남성, 2는 여성
# 학생들 리스트로 만든다.
s_list = [list(map(int, input().split())) for _ in range(s_num)]

for std in s_list:
    if std[0] == 1: # 남자면
        i = std[1] - 1 # 인덱스가 1부터 시작하므로, 적용할 i에 -1을 해 주어야 한다.
        while i < N: # 여기서 조금 헷갈렸는데, 어차피 i는 라인 마지막까지 순환해주어야 하므로 평범하게 범위 설정을 해 준다.
            my_list[i] = int(not my_list[i]) # int를 안 붙여주면 True, False로 나온다.
            i += std[1]
    elif std[0] == 2:
        i = std[1] - 1
        k = 0
        while i + k < N and i - k >= 0:
            if my_list[i + k] == my_list[i - k]:
                my_list[i + k] = my_list[i - k] = int(not my_list[i + k])
            elif my_list[i + k] != my_list[i - k]:
                break
            k += 1
j = 0
while j < N:
    if (j + 1) % 20 == 0:
        print(my_list[j])
    else:
        print(my_list[j], end=' ')
    j += 1
