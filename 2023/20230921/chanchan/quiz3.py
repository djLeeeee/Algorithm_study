# 센서
# https://www.acmicpc.net/problem/2212
import sys
sys.stdin = open("./input/quiz3.txt")
input = sys.stdin.readline
# 골5 ----------------------------------------

N = int(input())
K = int(input())

sensors = list(map(int, input().split(' ')))
sensors.sort()

dist = []
for idx in range(0, N-1):
    dist.append(sensors[idx+1] - sensors[idx])
    dist.sort()

min_sum = 0
for idx in range(0, N-K):
    min_sum += dist[idx]

print(min_sum)

# --------------------------------------------