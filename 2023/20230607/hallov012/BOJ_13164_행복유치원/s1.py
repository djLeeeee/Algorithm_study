import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
h_lst = list(map(int, input().split()))
h_lst.sort()
gab = []
for i in range(1, n):
    gab.append(h_lst[i] - h_lst[i-1])
gab.sort()
# k개의 조로 나누니까 제일 차이가 큰 k개의 조합을 뺌
ans = sum(gab[:n-k])
print(ans)
