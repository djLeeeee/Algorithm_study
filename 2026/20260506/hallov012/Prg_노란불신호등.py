import math

def solution(signals):
    lcm = 1 # 최소공배수 구하기
    for signal in signals:
        cycle = sum(signal)
        lcm = lcm * cycle // math.gcd(lcm, cycle)

    for t in range(1, lcm+1):
        flag = True
        for i in range(len(signals)):
            g, y, r = signals[i]
            cycle = sum(signals[i])
            tmp = (t-1) % cycle + 1
            if not (g < tmp < g+y+1):
                flag = False
                break
        if flag:
            return t
    return -1

input_list = [
    [[2, 1, 2], [5, 1, 1]],
    [[2, 3, 2], [3, 1, 3], [2, 1, 1]],
    [[3, 3, 3], [5, 4, 2], [2, 1, 2]],
    [[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]]
]

for input in input_list:
    print(solution(input))