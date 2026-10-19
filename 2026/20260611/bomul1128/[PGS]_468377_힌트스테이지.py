# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/468377
# Submission: 2026-06-11 17:04:55 Python3 정답 100 /
def solution(cost, hint):
    def cal(bits):
        arr = [0] * n
        val = cost[0][0]
        for idx in range(n - 1):
            if bits & 1:
                h, *vs = hint[idx]
                val += h
                for v in vs:
                    arr[v - 1] += 1
            bits >>= 1
            val += cost[idx + 1][min(arr[idx + 1], n - 1)]
            if val >= answer:
                return val
        return val
    
    n = len(cost)
    answer = float('inf')
    for b in range(1 << (n - 1)):
        tmp = cal(b)
        if tmp < answer:
            answer = tmp
    return answer
