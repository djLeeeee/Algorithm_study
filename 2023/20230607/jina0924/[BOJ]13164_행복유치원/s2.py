# 백줕 13164번 행복 유치원

import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())        # 원생 수, 나누려는 조의 개수
h = list(map(int, input().split()))     # 원생 키(오름차순)
'''
조를 나누는 경계의 차이가 크면 클수록 비용이 최소가 됨
ex) K = 3이고 (a, b), (c, d), (e, f)로 조를 나눈다면
비용 = (f - e) + (d - c) + (b - a) = f - a + (b - c) + (d - e)
=> 처음과 끝 값은 고정되어 있으므로 (b - c)와 같은 값이 최소가 되도록 구하면 됨
'''
gap = [0] * N
for i in range(1, N):
    gap[i] = h[i - 1] - h[i]
gap.sort()
ans = h[N - 1] - h[0]
for i in range(K - 1):
    ans += gap[i]
print(ans)