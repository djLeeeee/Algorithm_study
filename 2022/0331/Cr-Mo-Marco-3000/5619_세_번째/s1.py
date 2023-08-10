import sys
import heapq
from itertools import permutations

sys.stdin = open('input.txt')

def search(string):
    l = len(string)
    global cnt
    for i in range(1, l):
        a = int(string[0:i])
        b = int(string[i:l])
        if a in binary and b in binary:
            cnt += 1
        if cnt == 3:
            return string
    return string


my_list = []
binary = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    temp = int(sys.stdin.readline().rstrip())
    heapq.heappush(my_list, temp)
    heapq.heappush(binary, temp)

asdf = []

while my_list and len(asdf) < 4:
    asdf.append(heapq.heappop(my_list))

asdf = list(permutations(map(str, asdf), 2))

# 작은 수 숫자는 이 정도 안에서 다 걸리지 않을까?
# 여기서 안 걸리면 포기해야징
# 이거 왜 맞았지?

fdsa = []
for i in range(len(asdf)):
    fdsa.append(int(asdf[i][0] + asdf[i][1]))

fdsa.sort()
cnt = 0
ans = 0
# s1 나눠서 검색
ans = search(str(fdsa[0]))
# s2 나눠서 검색
if cnt < 3:
    ans = search(str(fdsa[1]))
# s3
if cnt < 3:
    ans = search(str(fdsa[2]))
print(int(ans))