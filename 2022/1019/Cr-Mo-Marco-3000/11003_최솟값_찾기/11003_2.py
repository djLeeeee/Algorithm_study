import sys, collections, heapq

input = sys.stdin.readline

N, L = map(int, input().strip().split())

my_list = list(map(int, input().strip().split()))

Q = collections.deque([])

for i in range(N):
    check_v = my_list[i]
    while Q and Q[-1][1] > check_v:
        Q.pop()
    Q.append((i, check_v))
    print(Q[0][1], end=' ')
    while Q and Q[0][0] <= i - L + 1:
        Q.popleft()

