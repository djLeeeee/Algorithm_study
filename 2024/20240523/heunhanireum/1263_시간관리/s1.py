import sys
sys.stdin = open('input.txt')

N = int(input())
nlst = [tuple(map(int, input().split())) for _ in range(N)]
nlst.sort(key= lambda x : -x[1])
ans = nlst[0][1]-nlst[0][0]
for i in range(1, N):
    if ans <= nlst[i][1]:
        ans -= nlst[i][0]
    else:
        ans = nlst[i][1]-nlst[i][0]

print(-1 if ans < 0 else ans)