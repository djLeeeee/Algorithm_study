# Problem: https://school.programmers.co.kr/learn/courses/30/lessons/258709
# Submission: 2026-07-23 22:29:22 Python3 오답 50 / 100
def solution(dice):
    from itertools import combinations, product
    
    def compare(a, b):
        ac = []
        bc = []
        pros = list(product(range(6), repeat=len(a)))
        for pro in pros:
            at = 0
            bt = 0
            for i, k in enumerate(pro):
                at += dice[a[i]][k]
                bt += dice[b[i]][k]
            ac.append(at)
            bc.append(bt)
        win = lose = 0
        for i in ac:
            for j in bc:
                if i > j:
                    win += 1
                elif i < j:
                    lose += 1
        return win, lose
    
    answer = []
    vals = 0
    n = len(dice)
    cases = list(combinations(range(1, n), n // 2 - 1))
    for case in cases:
        a_side = [0] + list(case)
        b_side = list(set(range(n)) - set(a_side))
        tw, tl = compare(a_side, b_side)
        if tw > vals:
            vals = tw
            answer = a_side
        if tl > vals:
            vals = tl
            answer = b_side
    return [i + 1 for i in answer]
