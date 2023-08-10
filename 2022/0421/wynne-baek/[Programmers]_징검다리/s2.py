def solutions(stones, k):
    left = 0
    right = 200000000
    while left <= right:
        temp = stones[:]
        mid = (left + right) // 2
        cnt = 0
        for stone in temp:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left

stones1 = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
stones2 = [3, 4, 5, 7, 4, 1, 2, 3]
stones3 = [1, 1, 1, 1, 1, 1, 1]
k = 3

# print(solutions(stones1, 3))