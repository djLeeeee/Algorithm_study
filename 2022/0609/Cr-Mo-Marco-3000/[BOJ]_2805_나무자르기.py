import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().strip().split())
my_list = list(map(int, input().strip().split()))

def do(Height):
    total_H = 0
    total_Plus = 0

    for i in range(N-1, 0, -1):
        wood = my_list[i] - Height
        wood_plus = my_list[i] - (Height + 1)

        if wood <= 0:
            break
        else:
            total_H += wood
            total_Plus += wood_plus

    if total_H >= M and total_Plus < M:
        return 'ans'
    else:
        if total_H < M:
            return 'down'
        else:
            return 'up'

def binary_search(left, right):
    mid = (left + right) // 2
    ans = do(mid)
    if ans ==  'ans':
        return mid
    elif ans == 'up':
        return binary_search(mid+1, right)
    elif ans == 'down':
        return binary_search(left, mid-1)


my_list.sort()

min = my_list[0]
max = my_list[-1]

print(binary_search(min, max))

# 첫 번째 솔루션 => 바이너리 서치 => 실패