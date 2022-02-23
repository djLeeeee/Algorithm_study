import sys
sys.stdin = open('input.txt')

t = int(input()) # 스위치
data = list(map(int, input().split()))
n = int(input()) # 학생 수
for _ in range(n):
    gender, num = map(int, input().split())
    num2 = num
    if gender == 1: # 남학생일 때, 주어진 num 의 배수를 바꿈
        while num-1 < t:
            if data[num-1]:
                data[num-1] = 0
            else:
                data[num-1] = 1
            num += num2
    if gender == 2: # 여학생일 때, 좌우 대칭인 구간을 바꿈
        i = 1
        chg_lst = [num-1]
        while num-1-i >= 0 and num-1+i < t:
            if data[num-1-i] != data[num-1+i]:
                break
            else:
                chg_lst = range(num-1-i, num+i)
            i += 1
        for i in chg_lst:
            if data[i]:
                data[i] = 0
            else:
                data[i] = 1
for i in range(t//20 + 1):
    print(*data[20*i: 20*(i+1)])