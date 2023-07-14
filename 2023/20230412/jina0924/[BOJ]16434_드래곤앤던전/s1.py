# 백준 16434번 드래곤 앤 던전

import sys
sys.stdin = open('input.txt')
from math import ceil                       # 올림: ceil, 내림: floor, 버림: trunc

N, ATK = map(int, input().split())          # 던전 방의 개수, 초기 공격력
MaxHP = 1                                   # 최대 생명력
CurHP = MaxHP                               # 현재 생명력
for _ in range(N):
    t, a, h = map(int, input().split())
    if t == 1:                              # 몬스터일 때, a: 몬스터 공격력, h: 몬스터 생명력
        cnt = ceil(h / ATK)                 # 몬스터 공격 횟수
        tmp = a * (cnt - 1)                 # 몬스터 공격량
        if CurHP - tmp <= 0:
            MaxHP += tmp - CurHP + 1        # 죽지 않을 만큼 최대 생명력 증폭
            CurHP = 1                       # 게임 이어나가도록 1 남김
        else:                               # 포션일 때, a: 공격력 증가, h: 현재 생명력 증가
            CurHP -= tmp
    else:
        ATK += a
        CurHP = min(MaxHP, CurHP + h)
print(MaxHP)