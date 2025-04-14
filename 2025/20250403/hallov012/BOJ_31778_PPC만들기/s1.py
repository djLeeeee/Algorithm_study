import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
S = list(map(str, input().strip()))
l, r = 0, n-1
while k > 0 and l < r:
    while l < n and S[l] == 'P':
        l += 1
    while r > 0 and S[r] == 'C':
        r -= 1
    if l < r:
        k -= 1
        S[l] = 'P'
        S[r] = 'C'

a, b, c = 0, 0, 0
for s in S:
    if s == 'P':
        # 앞에 나온 P의 수 만큼 생성 가능
        b += a
        a += 1
    else:
        c += b
print(c)