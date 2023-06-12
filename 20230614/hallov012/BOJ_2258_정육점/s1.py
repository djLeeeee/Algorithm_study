import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
meet = [list(map(int, input().split())) for _ in range(n)]
meet.sort(key=lambda x: (x[1], -x[0]))
ans = sys.maxsize
cnt = 0
temp = 0
same_w_flag = False
for i in range(n):
    w, c = meet[i]
    cnt += w
    # 이전과 같은 가격인 고기가 있다면 그 수를 temp에 저장
    if i > 0 and c == meet[i-1][1]:
        temp += 1
    else:
        temp = 0
    if cnt >= m:
        cost_temp = c * (temp+1)
        ans = min(ans, cost_temp)
        # 같은 가격의 고기의 묶음 다음으로 나온 고기의 금액이 더 싸지는지만 확인하면 되니까...?
        if ans != sys.maxsize and ans > cost_temp:
            break

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)