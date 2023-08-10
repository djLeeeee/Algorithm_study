import sys
sys.stdin = open('input.txt')

exps = input().split('-')
cal = []
for exp in exps:
    this_sum = 0
    plus = exp.split('+')
    for num in plus:
        this_sum += int(num)
    cal.append(this_sum)
answer = cal[0]
for i in range(1, len(cal)):
    answer -= cal[i]
print(answer)


