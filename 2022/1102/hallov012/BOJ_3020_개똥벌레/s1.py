import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, h = map(int, input().split())
top = [0] * (h+1)
bottom = [0] * (h+1)
ans = [n, 0]

for i in range(n):
    m = int(input())
    # 종유석
    if i % 2:
        top[m] += 1
    # 석순
    else:
        bottom[m] += 1

# 반대순서로 누적합 구하기
# 해당 높이로 개똥벌레가 지나갈 때 파괴해야할 장애물의 수
for i in range(h-1, 0, -1):
    top[i] += top[i+1]
    bottom[i] += bottom[i+1]

for i in range(1, h+1):
    num = top[i] + bottom[h-i+1]
    if num < ans[0]:
        ans[0] = num
        ans[1] = 1
    elif num == ans[0]:
        ans[1] += 1
print(*ans)