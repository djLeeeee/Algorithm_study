from collections import deque


def solution(coin, cards):
    n = len(cards)
    m = n // 3
    target = n+1
    have, left, pend = cards[:m], deque(cards[m:]), []
    round = 1

    def check(lst_a, lst_b):
        for a in lst_a:
            diff = target - a
            if diff in lst_b:
                lst_a.remove(a)
                lst_b.remove(diff)
                return True
        return False

    while left and coin >= 0:
        a, b = left.popleft(), left.popleft()
        pend.extend([a, b])
        if check(have, have):
            pass
        elif coin > 0 and check(have, pend):
            coin -= 1
        elif coin > 1 and check(pend, pend):
            coin -= 2
        else:
            break
        round += 1
    return round
