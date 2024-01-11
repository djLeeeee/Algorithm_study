import sys
sys.stdin = open('input.txt')

n = int(input())
h_lst = list(map(int, input().split()))

if sum(h_lst) % 3:
    print('NO')
    exit()

cnt = 0
for h in h_lst:
    cnt += h//2

# 2씩 자라게 할 수 있는 횟수가 전체 일수보다 작거나 같으면 불가능
if cnt <= sum(h_lst)//3:
    print('NO')
else:
    print('YES')