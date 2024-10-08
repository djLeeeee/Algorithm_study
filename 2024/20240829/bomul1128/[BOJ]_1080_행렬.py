# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/1080
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=1080&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
from sys import stdin

input = stdin.readline

n, m = map(int, input().strip().split())
b1 = [list(map(int, input().strip())) for _ in range(n)]
b2 = [list(map(int, input().strip())) for _ in range(n)]
ans = 0
for i in range(n - 2):
    for j in range(m - 2):
        if b1[i][j] != b2[i][j]:
            ans += 1
            for di in range(3):
                for dj in range(3):
                    b1[i + di][j + dj] ^= 1
if b1 != b2:
    print(-1)
else:
    print(ans)
