def solution(prices):
    N = len(prices)
    counts = []
    for i in range(N): # 0부터
        for j in range(i, N):
            if prices[i] > prices[j] or j == N-1:
                    counts.append(j-i)
                    break
    return counts
