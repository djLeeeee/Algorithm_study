import sys
sys.stdin = open('input.txt')

n = int(input())
seq = list(map(int, input().split()))

s, e = 0, 0
visited = [0] * 100001
ans = 0
while s <= e and e < n:
    s_num, e_num = seq[s], seq[e]
    if not visited[e_num]:
        visited[e_num] = 1
        e += 1
        ans += e-s
    else:
        visited[s_num] = 0
        s += 1

print(ans)