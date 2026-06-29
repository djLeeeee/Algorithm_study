import sys

def solution(cost, hint):
    n = len(cost)
    # i 번들 구매시, j번 스테이지 힌트권이 몇 장 증가하는지
    gain = [[0] * n for _ in range(n-1)]
    prices = [0] * (n-1)

    for i in range(n-1):
        prices[i] = hint[i][0]
        for ticket in hint[i][1:]:
            gain[i][ticket-1] += 1

    answer = sys.maxsize
    # mask: 구매 여부
    for mask in range(1 << (n-1)):
        hint_cnt = [0] * n
        total = 0
        # 구매 번들 반영
        for b in range(n-1):
            if mask & (1 << b):
                total += prices[b]
                for stage in range(n):
                    hint_cnt[stage] += gain[b][stage]
        for stage in range(n):
            usable = min(hint_cnt[stage], n-1)
            total += cost[stage][usable]
        answer = min(answer, total)
    return answer