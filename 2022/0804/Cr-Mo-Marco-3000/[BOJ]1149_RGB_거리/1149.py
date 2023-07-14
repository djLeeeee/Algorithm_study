import sys

input = sys.stdin.readline

N = int(input().strip())

my_list = []
memoization = [0, 0, 0] * N
min_v = 1000 * 1000

for i in range(N):
    temp = list(map(int, input().strip().split()))
    my_list.append(temp)

def do(cnt, all, before):
    global min_v
    if all > min_v:
        return
    elif cnt == N:
        if all < min_v:
            min_v = all
    else:
        for i in range(3):
            if i != before:
                do(cnt+1, all + my_list[cnt][i], i)

do(0, 0, 3)

print(min_v)

