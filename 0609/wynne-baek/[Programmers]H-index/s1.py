def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    for i in range(len(citations), 1, -1):
        tmp = i
        cnt = 0
        for num in citations:
            if num >= tmp:
                cnt += 1
            else:
                break
        if cnt >= tmp:
            answer = tmp
            break
    return answer

print(solution([3, 0, 6, 1, 5]))