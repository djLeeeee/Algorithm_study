import sys
sys.stdin = open('input.txt')

N = int(input())
solution = sorted(list(map(int, input().split())))
# print(solution)

min_sum = 1000000000000

for i in range(N-2):
    start = i + 1
    end = N-1
    while start < end:
        temp = solution[i] + solution[start] + solution[end]
        if abs(temp) < min_sum:
            min_sum = abs(temp)
            result = [solution[i], solution[start], solution[end]]
        if temp < 0:
            start = start + 1
        elif temp > 0:
            end = end -1
        else:
            break
print(*result)

