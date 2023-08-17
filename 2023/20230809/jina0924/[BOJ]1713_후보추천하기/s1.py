# 백준 1713번 후보 추천하기

import sys
sys.stdin = open('input.txt')

N = int(input())
C = int(input())
recs = list(map(int, input().split()))
candidates = []


def isRec(rec):
    for i in range(len(candidates)):
        if candidates[i][2] == rec:
            candidates[i][0] += 1
            return True
    return False


for j in range(C):
    rec = recs[j]
    if len(candidates) < N:
        if not isRec(rec):
            candidates.append([1, j, rec])
    else:
        if not isRec(rec):
            candidates.sort(reverse=True)
            candidates.pop()
            candidates.append([1, j, rec])
result = []
for _, _, s in candidates:
    result.append(s)
print(*sorted(result))