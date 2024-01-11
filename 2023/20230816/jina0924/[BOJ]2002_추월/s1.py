# 백준 2002번 추월

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N = int(input())
tunnel_in = deque([input().rstrip() for _ in range(N)])     # 터널에 들어가는 순으로 저장
tunnel_out = deque([input().rstrip() for _ in range(N)])    # 터널 밖으로 나오는 순으로 저장

cnt = 0
car1, car2 = tunnel_in.popleft(), tunnel_out.popleft()
alreay_out = set()                                          # tunnel_out에서 이미 살펴본 번호 저장
while tunnel_out and tunnel_out:
    # 이미 tunnel_out에서 살펴본 차량이면 다음 차량 살펴보기 위해 popleft & continue
    if car1 in alreay_out:
        car1 = tunnel_in.popleft()
        continue
    # 현재 살펴보는 차량이 서로 같지 않다 = car2가 추월한 차
    if car1 != car2:
        cnt += 1
        alreay_out.add(car2)
        car2 = tunnel_out.popleft()
    else:
        car1 = tunnel_in.popleft()
        car2 = tunnel_out.popleft()
print(cnt)