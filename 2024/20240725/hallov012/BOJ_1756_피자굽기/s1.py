import sys
sys.stdin = open('input.txt')

d, n = map(int, input().split())
d_lst = list(map(int, input().split()))
p_lst = list(map(int, input().split()))

# 도우가 통과할 수 있는 지름으로 갱신
# 아래의 지름이 위보다 크면, 위의 지름으로 변경
for i in range(1, d):
    if d_lst[i] > d_lst[i-1]:
        d_lst[i] = d_lst[i-1]

p_idx = 0
for i in range(d-1, -1, -1):
    if d_lst[i] >= p_lst[p_idx]:
        p_idx += 1
        if p_idx == n:
            print(i+1)
            break
else:
    print(0)
