import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
time = sorted(list(int(sys.stdin.readline()) for _ in range(N)))
left, right = 0, time[-1]*M
ans = right

while left <= right:
    mid = (left+right)//2
    res = 0
    for t in time:
        res += mid//t       # mid초 동안 t 심사대에서 심사할 수 있는 사람 수를 더해줌

    if res >= M:
        right = mid-1
        ans = min(ans, mid)
    elif res < M:
        left = mid+1

print(ans)