def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    for idx, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            i, _ = stack.pop()
            answer[i] = idx - i
        stack.append((idx, price))
    while stack:
        i, _ = stack.pop()
        answer[i] = idx - i
    return answer
