def power3(n, k):
    result = 1
    # 더 이상 곱할 것이 없을 때까지 진행하자.
    while k > 0:
        # 만약 k가 홀수라면, n을 곱하자.
        if k % 2:
            result *= n
        # 다음 과정을 위한 밑작업
        n *= n
        k //= 2
    return result