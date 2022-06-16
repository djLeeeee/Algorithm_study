import sys
from heapq import heappush,heappop
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
testCase = 1

while True:
    N = int(input())
    if N == 0:
        break
    board = [list(map(int,input().split())) for _ in range(N)]
    visited = [[-1 for _ in range(N)]for _ in range(N)]
    heap = []
    heappush(heap,[board[0][0],0,0])
    visited[0][0] = 0
    while heap:
        cost,x,y = heappop(heap)
        if [x,y] == [N-1,N-1]:
            print("Problem",testCase,end = "")
            print(":",cost)
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0<= ax < N and 0 <= ay < N:
                if visited[ax][ay] == -1:
                    heappush(heap, [cost+board[ax][ay],ax,ay])
                    visited[ax][ay] = 0
    testCase += 1
