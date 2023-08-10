# https://www.acmicpc.net/problem/2258
import sys
sys.stdin = open("./input/2258.txt")
input = sys.stdin.readline
# ----------------------------------------

N, M = map(int, input().split())
DATA = [list(map(int, input().split())) for _ in range(N)]
DATA.sort(reverse=True)

