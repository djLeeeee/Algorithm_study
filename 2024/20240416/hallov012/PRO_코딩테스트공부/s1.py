import sys

def solution(alp, cop, problems):
    answer = 0
    max_alp, max_cop = 0, 0
    for p in problems:
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])

    if alp > max_alp and cop > max_cop:
        return answer

    dp = [[sys.maxsize] * (max_cop + 1) for _ in range(max_alp + 1)]
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    dp[alp][cop] = 0

    for i in range(alp, max_alp +1):
        for j in range(cop, max_cop + 1):
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    n_alp = min(i + alp_rwd, max_alp)
                    n_cop = min(j + cop_rwd, max_cop)
                    dp[n_alp][n_cop] = min(dp[n_alp][n_cop], dp[i][j] + cost)

    answer = dp[max_alp][max_cop]
    return answer

datas = [
    (10, 10, [[10,15,2,1,2],[20,20,3,3,4]]),
    (0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])
]

for alp, cop, problems in datas:
    print(solution(alp, cop, problems))