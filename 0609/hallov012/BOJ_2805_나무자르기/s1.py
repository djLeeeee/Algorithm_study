# 이전에 풀었으나 알고리즘 스터디를 위해 재풀이
# binary search를 이용한 시간 단축
import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 0, max(trees)
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for tree in trees:
        if mid < tree:
            cnt += tree - mid
    if cnt >= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)
