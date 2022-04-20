def solution(stones, k):
    start = min(stones)
    end = max(stones)
    fin = len(stones)
    while start <= end:
        middle = (start + end) // 2
        previous = -1
        for idx, stone in enumerate(stones):
            if stone >= middle:
                if k < idx - previous:
                    end = middle - 1
                    break
                previous = idx
        else:
            if fin - previous > k:
                end = middle - 1
            else:
                answer = middle
                start = middle + 1
    return answer
