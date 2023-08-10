# https://www.acmicpc.net/problem/16434
import sys
sys.stdin = open("./input/16434.txt")
input = sys.stdin.readline


N, atk = map(int, input().split())

max_hp = 1
cur_hp = 1

def battle(a, h):
    global cur_hp, max_hp
    min_atk_cnt, rest = divmod(h, atk)
    min_atk_cnt += 1 if rest else 0
    monster_atk = a * (min_atk_cnt - 1)
    if cur_hp < monster_atk:
        max_hp += (monster_atk - cur_hp + 1)
        cur_hp += (monster_atk - cur_hp + 1)
    cur_hp -= monster_atk


def buff(a, h):
    global atk, cur_hp
    atk += a
    cur_hp += h
    if (cur_hp > max_hp):
        cur_hp = max_hp


for _ in range(N):
    t, a, h = map(int, input().split())
    if (t == 1):
        battle(a, h)
    elif (t == 2):
        buff(a, h)

print(max_hp)