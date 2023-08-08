# https://www.acmicpc.net/problem/3107'
import sys
sys.stdin = open("./input/3107.txt")
input = sys.stdin.readline
# ----------------------------------------

ip = input().rstrip().split(":")
ans = []
flag = 1

for i in ip:
    if flag and i == "":
        flag = 0
        for _ in range(8 - len(ip) + 1):
            ans.append("0000")
    else:
        ans.append(i.zfill(4))
    

print(":".join(ans))