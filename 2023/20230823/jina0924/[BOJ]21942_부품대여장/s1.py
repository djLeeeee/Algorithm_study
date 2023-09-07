# 백준 21942번 부품 대여장

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import defaultdict
from datetime import datetime, timedelta

N, L, F = input().split()       # 정보의 개수, 대여기간, 벌금
N, F = int(N), int(F)
L = timedelta(days=int(L[:3]), hours=int(L[4:6]), minutes=int(L[7:]))
book = {}
member = defaultdict(int)
m = timedelta(minutes=1)
for _ in range(N):
    date, time, P, M = input().split()      # 시각, 부품 이름, 회원 닉네임
    dt = datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
    if book.get((P, M)):
        l = dt - book.get((P, M))
        if l > L:
            member[M] += ((l - L) // m) * F
        del book[(P, M)]
    else:
        book[(P, M)] = dt
if not member:
    print(-1)
    sys.exit()
member = sorted(member.items())
for name, penalty in member:
    print(name, penalty)