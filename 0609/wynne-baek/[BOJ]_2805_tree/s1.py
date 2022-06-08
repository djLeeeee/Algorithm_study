import sys
sys.stdin = open('input.txt')

def find_biggest_height(trees):
    global M
    start = 0
    end = max(trees)

    # 종료조건
    while start <= end:
        mid = (start + end) // 2

        firewood = 0
        for tree in trees:
            if tree > mid:
                firewood += (tree - mid)

        if firewood >= M:
            start = mid + 1
        elif firewood < M:
            end = mid - 1
    return end

N, M = map(int, input().split())
trees = sorted(list(map(int, sys.stdin.readline().split())))
print(find_biggest_height(trees))
"""
최대 높이
trees - 최대높이 >= M
"""