# https://www.acmicpc.net/problem/16935'
import sys
sys.stdin = open("./input/16935.txt")
input = sys.stdin.readline
# ----------------------------------------
def cal1(arr):
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        temp[i] = arr[N-1-i]
    return temp
 
def cal2(arr):
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            temp[i][j] = arr[i][M-1-j]
    return temp
 
def cal3(arr):
    temp = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            temp[i][j] = arr[N-1-j][i]
    return temp
 
def cal4(arr):
    temp = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            temp[i][j] = arr[j][M - 1 - i]
    return temp
 
def cal5(arr):
    temp = [[0] * M for _ in range(N)]
    for i in range(N // 2):
        for j in range(M // 2):
            temp[i][j + M // 2] = arr[i][j]
 
    for i in range(N // 2):
        for j in range(M // 2, M):
            temp[i + N // 2][j] = arr[i][j]
 
    for i in range(N // 2, N):
        for j in range(M // 2, M):
            temp[i][j - M // 2] = arr[i][j]
 
    for i in range(N // 2, N):
        for j in range(M // 2):
            temp[i - N // 2][j] = arr[i][j]
 
    return temp
 
def cal6(arr):
    temp = [[0] * M for _ in range(N)]
    for i in range(N // 2):
        for j in range(M // 2):
            temp[i + N // 2][j] = arr[i][j]
 
    for i in range(N // 2, N):
        for j in range(M // 2):
            temp[i][j + M // 2] = arr[i][j]
 
    for i in range(N // 2, N):
        for j in range(M // 2, M):
            temp[i - N // 2][j] = arr[i][j]
 
    for i in range(N // 2):
        for j in range(M // 2, M):
            temp[i][j - M // 2] = arr[i][j]
 
    return temp
 
N, M, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))
cals =  [0, cal1, cal2, cal3, cal4, cal5, cal6]

for cmd in cmds:
    arr = cals[cmd](arr)

    if (cmd == 3 or cmd == 4):
        N, M = M, N
 
for line in arr:
    print(*line)