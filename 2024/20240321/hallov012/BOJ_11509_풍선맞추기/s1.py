import sys
sys.stdin = open('input.txt')

n = int(input())
h_lst = list(map(int, input().split()))
m = 1000000
# index 높이에 존재하는 화살의 수를 기록
arr = [0] * (m+1)

for h in h_lst:
    # 발사된 화살이 이미 있는 경우 높이를 감소시킴
    if arr[h]:
        arr[h] -= 1
        arr[h-1] += 1
    # 해당 높이에 화살이 없으면 하나 새로 쏜다
    else:
        arr[h-1] += 1

ans = sum(arr)
print(ans)