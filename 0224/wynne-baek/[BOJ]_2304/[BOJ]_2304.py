import sys
sys.stdin = open('input2.txt')

N = int(input())
max_H = 0
max_L = 0
pole = []
for _ in range(N):
    #L은 위치, H는 높이
    L, H = map(int, input().split())
    pole.append([L, H])
    if max_L < L:
        max_L = L
    if max_H < H:
        max_H = H
        max_index = L

pole_list = [0] * (max_L + 1)
for L, H in pole:
    pole_list[L] = H
# 결과값 초기화
total = 0
# 임시 높이
temp = 0
# 젤 높은 거 기준 좌
for i in range(max_index+1):
    # 새로 나타난 기둥 높이가 임시 높이보다 크면
    if pole_list[i] > temp:
        # 임시 높이 초기화
        temp = pole_list[i]
    #결과값에 더해줌
    total += temp
# 젤 높은 거 기준 우
#임시 높이 초기화
temp = 0
for i in range(max_L, max_index, -1):
    if pole_list[i] > temp:
        temp = pole_list[i]
    total += temp
print(total)