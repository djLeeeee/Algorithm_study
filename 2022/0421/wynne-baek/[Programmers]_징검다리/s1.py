stones1 = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
stones2 = [3, 4, 5, 7, 4, 1, 2, 3]
stones3 = [1, 1, 1, 1, 1, 1, 1]
k = 3
stones4 = [3333, 0, 3333, 3333, 3333]

#정확성 잡았고...

def findzero(stones, k):
    cnt = 0
    for stone in stones:
        if stone == 0:
            cnt += 1
            if cnt == k:
                return False
        elif stone != 0:
            cnt = 0
    return True

def minus_stone(stones, num):
    for i in range(len(stones)):
        if stones[i] > 0:
            stones[i] -= num

def solution(stones, k):
    answer = min(stones)
    flag = True
    minus_stone(stones, answer)
    while flag:
        if not findzero(stones, k):
            return answer
        answer += 1
        minus_stone(stones, 1)

print(solution(stones1, 3))