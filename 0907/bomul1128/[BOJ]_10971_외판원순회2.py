"""
비트마스킹 DP 메모이제이션 사용
숫자를 2진법으로 표현해, visited 역할을 대신 수행하도록 하는 방법
ex) 25 = 11001(2) : 1번, 4번, 5번 방을 방문했다! (역순 주의)
[장점]
일반적으로 가지치기가 거의 최대로 된 형태 -> 매우 빠름
[단점]
탐색해야하는 지점의 갯수가 커지면 활용 불가 (최대 25 정도)
"""
from sys import stdin

input = stdin.readline


def tour(now, path):
    if dp[now][path]:
        return dp[now][path]
    # 1 << (n - 1) - 1 :  모든 비트가 1이다 -> 모든 도시를 방문했다
    if path + 1 == 1 << (n - 1):
        if costs[now][0]:
            return costs[now][0]
        return INF
    result = INF
    for adj in range(1, n):
        if not costs[now][adj]:
            continue
        if path & 1 << adj - 1:
            continue
        total = costs[now][adj] + tour(adj, path | 1 << (adj - 1))
        result = min(result, total)
    dp[now][path] = result
    return result


n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
# dp[x][bit] = x번째 마을에 현재 있고 방문한 도시가 bit 로 표현됐을 때 최소 비용
dp = [[0] * (1 << n - 1) for _ in range(n)]
INF = float('inf')
print(tour(0, 0))
