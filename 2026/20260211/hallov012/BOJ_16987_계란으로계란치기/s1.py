import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(idx):
    global ans
    if idx == n:
        cnt = 0
        for s, _ in eggs:
            cnt += 1 if s < 0 else 0
        ans = max(ans, cnt)
        return
    if eggs[idx][0] <= 0:
        find(idx+1)
    else:
        flag = False
        _, w_1 = eggs[idx]
        for i in range(n):
            s_2, w_2 = eggs[i]
            if idx != i and s_2 > 0:
                flag = True
                eggs[idx][0] -= w_2
                eggs[i][0] -= w_1
                find(idx+1)
                eggs[idx][0] += w_2
                eggs[i][0] += w_1
        if not flag:
            find(n)

n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
ans = 0
find(0)
print(ans)
