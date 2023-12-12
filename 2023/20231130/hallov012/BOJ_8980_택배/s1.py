import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
delivery = [list(map(int, input().split())) for _ in range(m)]
# 박스를 받는 마을 순으로 오름차순 정렬
delivery.sort(key=lambda x: x[1])

capacity = [c] * (n+1)
cnt = 0
for s, e, b in delivery:
    # 가져갈 수 있는 박스의 수는 (구간 내에서 적재 가능한 박스의 양 + 현재 가져야 할 박스의 수)의 최솟값
    min_num = min(b, c)
    for i in range(s, e):
        min_num = min(min_num, capacity[i])
    # min_num 만큼 가져갈거니까 해당 구간의 수용 가능 양에서 마이너스
    for i in range(s, e):
        capacity[i] -= min_num
    cnt += min_num

print(cnt)