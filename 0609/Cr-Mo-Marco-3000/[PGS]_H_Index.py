def solution(citations):
    ml = sorted(citations)
    N = len(ml)
    for i in range(N):
        if ml[i] > N - i:
            high = ml[i]
            low = ml[i-1]
            high_idx = i
            low_idx = i-1
            break
    else: # 만약 끝까지 순환할 경우, 조건에 맞는 경우가 없으므로 return 0
        return 0
    if N - low_idx == low:
        return low
    else:
        return N - high_idx