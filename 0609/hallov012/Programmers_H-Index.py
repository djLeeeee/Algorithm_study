def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)
    max_num = max(citations)
    cnt = [0] * (max_num + 1)
    for num in citations:
        cnt[num] += 1
    for i in range(n, -1, -1):
        if sum(cnt[:i]) <= i <= sum(cnt[i:]):
            answer = i
            break
    return answer

print(solution([3, 0, 6, 1, 5]))
