import sys
sys.stdin = open('input.txt')

N = int(input())
blst = list(map(int, input().split()))
if N < 3:           # 길이가 3 미만인 수열은 등차수열
    print(0)
else:               # 길이가 3 이상인 경우 0, 1, 2번째 숫자를 각각 연산해서 등차수열을 만들 수 있는 경우 res에 담기
    res = []
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            for k in (-1, 0, 1):
                if (blst[1]+j)-(blst[0]+i) == (blst[2]+k)-(blst[1]+j):
                    res.append((i, j, k))
    ans = 10**5+1
    for i, j, k in res:
        d = blst[1]+j-(blst[0]+i)                   # 0~2까지 연산 시 공차
        cnt = abs(i)+abs(j)+abs(k)                  # 0~2까지 등차수열로 만들때 연산횟수
        tmp = blst[2]+k                             # 연산 후 2번째 숫자의 값
        for idx in range(3, N):                     # 3번째 숫자부터
            if abs(blst[idx]-(tmp+d)) > 1:          # 연산을 해도 등차수열이 되지 않는 경우
                break
            else:                                   # 연산 하면 되는 경우
                cnt += abs(blst[idx]-tmp-d)         # 연산횟수 반영
                tmp += d
        else:
            if ans > cnt:
                ans = cnt

    if ans == 10**5+1:
        print(-1)
    else:
        print(ans)