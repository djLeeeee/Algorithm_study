def solution(alp, cop, problems):
    from heapq import heappop, heappush
    
    max_a = max([problem[0] for problem in problems])
    max_c = max([problem[1] for problem in problems])
    start = [(0, alp, cop)]
    check = [[] for _ in range(401)]
    da = [1, 0]
    dc = [0, 1]
    while True:
        t, a, c = heappop(start)
        if a >= max_a and c >= max_c:
            return t
        for d in range(2):
            na = a + da[d]
            nc = c + dc[d]
            flag = True
            for x, y in check[t + 1]:
                if x >= na and y >= nc:
                    flag = False
                    break
            if flag:
                check[t + 1].append((na, nc))
                heappush(start, (t + 1, na, nc))
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp_req <= a and cop_req <= c:
                flag = True
                for x, y in check[t + cost]:
                    if x >= a + alp_rwd and y >= c + cop_rwd:
                        flag = False
                        break
                if flag:
                    check[t + cost].append((a + alp_rwd, c + cop_rwd))
                    heappush(start, (t + cost, a + alp_rwd, c + cop_rwd))
