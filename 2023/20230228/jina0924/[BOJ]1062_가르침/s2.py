# 백준 1067번 가르침

import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline
from itertools import combinations

N, K = map(int, input().split())
if K < 5:                               # 배울 수 있는게 없음(anta, tica도 못배움)
    print(0)
    sys.exit()
if K == 26:                             # 전부 다 배울 수 있음
    print(N)
    sys.exit()

words = [input().rstrip() for _ in range(N)]    # 배우려는 단어들
anta_words = []                         # 위에 있는 단어들을 비트 표현으로 저장할 배열
ans = 0
already = 'acint'

for word in words:
    bits = 0
    for c in word:                      # 단어에 있는 알파벳을 순회하면서 비트 표현 만듦
        bits |= 1 << ord(c) - 97        # ord('a') == 97
    anta_words.append(bits)

alpha = [1 << i for i in range(26)]     # 알파벳을 모두 비트 표현으로 저장
already_bits = 0                        # 'acint'를 비트식으로 저장할 변수
for c in already:
    alpha.remove(1 << ord(c) - 97)      # 'acint'를 combinations하지 않기 위해 미리 빼둠
    already_bits |= 1 << ord(c) - 97

for comb in combinations(alpha, K - 5):
    cnt, temp = 0, already_bits         # 배울 수 있는 단어 수, 알고 있는 알파벳들
    for c in comb:                      # 조합으로 얻은 결과물을 'anta'+'tica'와 합침
        temp |= c
    for anta_word in anta_words:
        if temp & anta_word == anta_word:   # 알고 있는 알파벳과 현재 살펴보는 단어의 교집합이 단어와 같다 = 배울 수 있다
            cnt += 1
    ans = max(ans, cnt)
print(ans)
