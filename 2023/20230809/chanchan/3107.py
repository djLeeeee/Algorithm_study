# https://www.acmicpc.net/problem/3107'
import sys
sys.stdin = open("./input/3107.txt")
input = sys.stdin.readline
# ----------------------------------------

ip = input().rstrip().split(":")
ans = [] # "0000"
flag = 1

for i in ip:
    if flag and i == "":
        flag = 0
        for _ in range(8 - len(ip) + 1):
            ans.append("0000")
    else:
        # ans.append(i.zfill(4))
        ans.append(i.rjust(4, "0"))
    
print(":".join(ans))