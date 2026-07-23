from itertools import combinations

def solution(dice):
    n = len(dice)
    m = n // 2

    answer = []
    max_win = -1

    def make_sums(selected):
        sums = []
        def dfs(idx, tmp):
            if idx == len(selected):
                sums.append(tmp)
                return
            for num in dice[selected[idx]]:
                dfs(idx+1, tmp + num)
        dfs(0, 0)
        return sums

    dice_set = set(range(n))
    for case in combinations(range(n), m):
        a_dices = list(case)
        b_dices = list(dice_set - set(case))

        a_sum, b_sum = make_sums(a_dices), make_sums(b_dices)
        b_sum.sort()

        win = 0
        for target in a_sum:
            left, right = 0, len(b_sum)
            while left < right:
                mid = (left + right) // 2
                if b_sum[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            win += left

        if win > max_win:
            max_win = win
            answer = [i+1 for i in a_dices]
    return answer

input_lst = [
    [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]],
    [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]],
    [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
]