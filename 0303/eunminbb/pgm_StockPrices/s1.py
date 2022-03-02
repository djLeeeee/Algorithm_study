def solution(prices):
    st_len = len(prices)
    answer = [0]*st_len
    for k in range(st_len):
        a = prices.pop(0)
        cnt = 0
        if prices:
            for j in range(len(prices)):
                if prices[j] >= a:
                    cnt += 1
                else:
                    cnt += 1
                    break

        answer[k] = cnt

    return answer