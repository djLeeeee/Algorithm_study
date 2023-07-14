# 백준 1067번 가르침

import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline
from itertools import combinations

N, K = map(int, input().split())
if K < 5:
    print(0)
    sys.exit()
if K == 26:
    print(N)
    sys.exit()

# K - 5 = 추가로 가르칠 수 있는 글자 수
# 글자수 만큼 조합 돌려서 가르칠 수 있는 단어 개수 출력
words = [input().rstrip() for _ in range(N)]
alpha = {'b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z'}
already = 'acint'
ans = 0
for comb in combinations(alpha, K - 5):
    cnt = 0
    for word in words:
        isKnown = True
        for i in range(4, len(word) - 4):
            if word[i] not in comb and word[i] not in already:
                isKnown = False
                break
        if isKnown:
            cnt += 1
    ans = max(ans, cnt)
print(ans)