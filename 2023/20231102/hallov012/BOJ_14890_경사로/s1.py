import sys
sys.stdin = open('input.txt')

def check(line):
    visited = [False] * n
    h = line[0]
    i = 1
    while i < n:
        if line[i] == h:
            i += 1
        elif line[i] == h+1:
            if i-l < 0:
                return False
            for k in range(1, l+1):
                if line[i-k] != h or visited[i-k]:
                    return False
            else:
                for k in range(1, l+1):
                    visited[i-k] = True
                h += 1
                i += 1
        elif line[i] == h-1:
            if i+l > n:
                return False
            for k in range(l):
                if line[i+k] != h-1 or visited[i+k]:
                    return False
            else:
                for k in range(l):
                    visited[i+k] = True
                h -= 1
                i += l
        else:
            return False
    return True

input = sys.stdin.readline

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    if check(arr[i]):
        ans += 1

for j in range(n):
    if check([arr[i][j] for i in range(n)]):
        ans += 1

print(ans)