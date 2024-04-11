from collections import deque

def solution(coin, cards):
    """
    코인을 안쓰고 가져올 수 있다면 안쓰고 해결
    안된다면 1개 => 2개 사용
    최대한 코인을 적게 쓰면서 한 턴을 마치기
    """
    def check(a_lst, b_lst):
        for a in a_lst:
            if t-a in b_lst:
                a_lst.remove(a)
                b_lst.remove(t-a)
                return True
        return False

    answer = 1
    n = len(cards)
    m = n // 3
    t = n+1

    have, left, pend = cards[:m], deque(cards[m:]), []

    while coin >= 0 and left:
        x, y = left.popleft(), left.popleft()
        pend.append(x)
        pend.append(y)
        if check(have, have):
            pass
        elif coin >= 1 and check(have, pend):
            coin -= 1
        elif coin >= 2 and check(pend, pend):
            coin -= 2
        else:
            break
        answer += 1
    return answer


data = [
    # [4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]],
    # [3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]],
    # [2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]],
    [10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]
]

for coin, cards in data:
    print(solution(coin, cards))