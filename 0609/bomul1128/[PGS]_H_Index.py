def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations) - 1, -1, -1):
        if citations[i] >= i + 1:
            return i + 1
    return 0
