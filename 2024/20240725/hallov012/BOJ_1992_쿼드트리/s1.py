import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def check(x, y, s,):
    val = data[x][y]
    for i in range(x, x+s):
        for j in range(y, y+s):
            if data[i][j] != val:
                return False
    return True

def find(x, y, s):
    global ans
    if not check(x, y, s):
        ans += '('
        ns = s // 2
        find(x, y, ns)
        find(x, y+ns, ns)
        find(x+ns, y, ns)
        find(x+ns, y+ns, ns)
        ans += ')'
    else:
        ans += str(data[x][y])

n = int(input())
data = [list(map(int, input().strip())) for _ in range(n)]
ans = ''
find(0, 0, n)
print(ans)