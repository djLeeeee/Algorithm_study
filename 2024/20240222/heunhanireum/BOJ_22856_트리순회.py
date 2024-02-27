import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
mt = [0]*(N+1)
visited = [0]*(N+1)
cnt = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    mt[a] = (b, c)

def total(num):
    global cnt
    l, r = mt[num]
    visited[num] = 1
    if l > 0 and visited[l] == 0:
        total(l)
        cnt += 1
    if r > 0 and visited[r] == 0:
        total(r)
        cnt += 1


def right(num):
    global cnt
    r = mt[num][1]
    visited[num] = 1
    if r > 0 and visited[r] == 0:
        right(r)
        cnt -= 1


total(1)
cnt *= 2
visited = [0]*(N+1)
right(1)
print(cnt)