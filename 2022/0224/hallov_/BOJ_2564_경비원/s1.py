import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
n = int(input())
shop = [list(map(int, input().split())) for _ in range(n)]
now = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if now[0] == 1:
        if shop[i][0] == 1:
            cnt += abs(now[1] - shop[i][1])
        elif shop[i][0] == 2:
            cnt += min(h + now[1] + shop[i][1], h + 2 * w - now[1] - shop[i][1])
        elif shop[i][0] == 3:
            cnt += now[1] + shop[i][1]
        else:
            cnt += (w - now[1]) + shop[i][1]
    if now[0] == 2:
        if shop[i][0] == 1:
            cnt += min(h + now[1] + shop[i][1], h + 2 * w - now[1] - shop[i][1])
        if shop[i][0] == 2:
            cnt += abs(now[1] - shop[i][1])
        elif shop[i][0] == 3:
            cnt += now[1] + (h - shop[i][1])
        elif shop[i][0] == 4:
            cnt += (w - now[1]) + (h - shop[i][1])
    if now[0] == 3:
        if shop[i][0] == 1:
            cnt += now[1] + shop[i][1]
        elif shop[i][0] == 2:
            cnt += (h - now[1]) + shop[i][1]
        if shop[i][0] == 3:
            cnt += abs(now[1] - shop[i][1])
        else:
            cnt += min(w + now[1] + shop[i][1], w + 2 * h - now[1] - shop[i][1])
    if now[0] == 4:
        if shop[i][0] == 1:
            cnt += now[1] + (w - shop[i][1])
        elif shop[i][0] == 2:
            cnt += (h - now[1]) + (w - shop[i][1])
        elif shop[i][0] == 3:
            cnt += min(w + now[1] + shop[i][1], w + 2 * h - now[1] - shop[i][1])
        else:
            cnt += abs(now[1] - shop[i][1])
print(cnt)