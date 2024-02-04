# Generated by make_my_study_record.py
# BOJ LINK : https://www.acmicpc.net/problem/17182
# My submission : https://www.acmicpc.net/status?option-status-pid=on&problem_id=17182&user_id=bomul1128&language_id=-1&result_id=-1&from_problem=1
n, k = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(n)]
for z in range(n):
    for x in range(n):
        for y in range(n):
            if dist[x][y] > dist[x][z] + dist[z][y]:
                dist[x][y] = dist[x][z] + dist[z][y]
dp = [[float('inf')] * n for _ in range(1 << n)]
q = [(1 << k, k)]
dp[1 << k][k] = 0
for bits, now in q:
    for adj in range(n):
        if bits & (1 << adj):
            continue
        new_bits = bits | (1 << adj)
        if dp[new_bits][adj] > dp[bits][now] + dist[now][adj]:
            dp[new_bits][adj] = dp[bits][now] + dist[now][adj]
            q.append((new_bits, adj))
print(min(dp[-1]))
