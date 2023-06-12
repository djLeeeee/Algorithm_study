import sys
sys.stdin = open('input.txt')

def dfs(temp, idx, cnt):
    global ans
    if cnt == 3:
        ans = min(ans, check(temp))
        return
    for i in range(idx+1, n):
        temp.append(students[i])
        dfs(temp, i, cnt+1)
        temp.pop()

def check(temp):
    cnt = 0
    [a, b, c] = temp
    for i in range(4):
        if a[i] != b[i]:
            cnt += 1
        if b[i] != c[i]:
            cnt += 1
        if a[i] != c[i]:
            cnt += 1
    return cnt

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    students = list(map(str, input().rsplit()))
    # 총 16개의 유형이 있으므로 33명 이상이면 무조건 같은 유형이 3명은 있음
    m = 16 * 2 + 1
    if n >= m:
        print(0)
        continue
    visited = [0] * n
    ans = sys.maxsize
    dfs([], -1, 0)
    print(ans)