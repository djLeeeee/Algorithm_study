
""" https://www.acmicpc.net/problem/1747
---------------------------------------------------------------------
메모리 (31,256 KB) | 시간 (2,012 ms) |
---------------------------------------------------------------------

- [itertools]   => combination 사용해서 학습할 문자 조합 리스트 활용
- 0b10001       => e _ _ _ a => (2 ** 4) _ _ _ (2 ** 0)

참고 자료: https://my-coding-notes.tistory.com/370
"""

import sys
import itertools as it
sys.stdin = open("input/1062.txt")
input = sys.stdin.readline

n, k = map(int, input().split())
if k < 5:
    print(0)
    sys.exit()

words = []
for _ in range(n):
    s = 0
    for i in list(input().rstrip()):
        s |= (2**(ord(i)-97))
    words.append(s)

base = 0
comb = [2**i for i in range(26)]
for i in [0, 2, 8, 13, 19]:
    base += 2 ** i
    comb.remove(2**i)

ans = 0
for c in it.combinations(comb, k-5):
    cnt, learned = 0, base
    for i in c:
        learned += i
    for word in words:
        if learned & word == word:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
