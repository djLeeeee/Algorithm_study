def solution(stones, k):
    n = len(stones)
    left = 1
    right = 2 * (10 ** 8)
    while left <= right:
        mid = (left + right) // 2
        last_step = -1
        for i in range(n):
            if stones[i] - mid <= 0:
                if i - last_step >= k:
                    right = mid - 1
                    break
            else:
                last_step = i
        else:
            left = mid + 1
    answer = left
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))