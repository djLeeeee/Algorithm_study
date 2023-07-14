def solution(stones, k):
    answer = 0
    L = len(stones)
    while True:
        i = -1
        while i < L:
            for j in range(1, k+1):
                i = i + 1
                if i == L:
                    answer += 1
                    break
                elif stones[i]:
                    stones[i] -= 1
                    break
            else:
                return answer


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))