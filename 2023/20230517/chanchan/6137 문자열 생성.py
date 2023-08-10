# https://www.acmicpc.net/problem/6137
import sys
sys.stdin = open("./input/6137.txt")
input = sys.stdin.readline
# ----------------------------------------

def get_fast_one(s, e, alp):
    c1, c2 = alp[s], alp[e]
    status = "front" if c1 < c2 else "back"
    
    if c1 == c2 and e - s > 2:
        status, _ = get_fast_one(s + 1, e - 1, alp)
    
    return(status, c1 if status == "front" else c2)
    
N = int(input())
alp = [input().rstrip() for _ in range(N)]
s, e = 0, N - 1
answer = []

while s <= e:
    status, char = get_fast_one(s, e, alp)
    answer.append(char)
    
    if status == "front":
        s += 1
    elif status == "back":
        e -= 1


for ind in range(len(answer) // 80 + 1):
    print(*answer[ind * 80: (ind + 1) * 80], sep="")