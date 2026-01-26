import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

# 최대 공약수
def get_gcd(a, b):
    if a % b == 0:
        return b
    return get_gcd(b, a % b)

def dfs(start):
    visited[start] = 1
    for next, p, q in ratio[start]:
        if not visited[next]:
            amount[next] = amount[start] * q // p
            dfs(next)

n = int(input())
ratio = [[] for _ in range(n)]
lcm = 1 # 최소 공배수
for _ in range(n-1):
    a, b, p, q = map(int, input().split())
    ratio[a].append((b, p, q)) # a가 p일 때, b는 q
    ratio[b].append((a, q, p)) # b가 q일 때, a는 p
    lcm = lcm * p * q // get_gcd(p, q)

visited = [0] * n
amount = [0] * n
amount[0] = lcm
dfs(0)

gcd = amount[0]
for m in amount[1:]:
    gcd = get_gcd(gcd, m)

print(*[m // gcd for m in amount])
