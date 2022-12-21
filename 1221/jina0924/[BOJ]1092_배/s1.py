# 백준 1092번 배

import sys
sys.stdin = open('input4.txt')

N = int(input())    # N: 크레인 수
crane = sorted(list(map(int, input().split())), reverse=True)     # 크레인의 무게 제한
M = int(input())    # M: 박스 수
box = sorted(list(map(int, input().split())), reverse=True)       # 각 박스의 무게

if crane[0] < box[0]:               # 제일 무거운 걸 들 수 있는 크레인도 못 옮기는 박스면 모든 박스를 옮길 수 있는 상황x => -1 출력
    print(-1)
    sys.exit()

cnt = 0
while len(box):
    for c in crane:                 # 크레인 하나 당
        for b in box:               # 박스를 전체 순회하면서
            if c >= b:              # 크레인이 옮길 수 있는 박스면 리스트에서 해당 박스 제거
                box.remove(b)
                break
    cnt += 1                        # 크레인 for문이 다 돌면 1분 경과됨
print(cnt)