# 세 용액을 혼합하여 특성 값이 0에 가장 가까운 용액 만들기
# 플로이드 와샬 - 거쳐가는 정점을 기준으로 최단거리를 구한다
import heapq

N = int(input())
arr = list(map(int, input().split()))
inf = float('inf')
heap = []
for i in range(N):
    mins = inf
    idx = -1
    for j in range(N):
        if i != j:
            cal = arr[i] + arr[j]
            if abs(mins) > abs(cal):
                idx = j
                mins = cal
    ans = inf
    idx2 = -1
    for k in range(N):
        if k not in (i, idx):
            cal2 = mins + arr[k]
            if abs(ans) > abs(cal2):
                ans = cal2
                idx2 = k
    if not ans:
        ans_list = [i, idx, idx2].sort()
        print(ans_list)
        break
    else:
        anss.append((abs(ans), i, idx, idx2))
if len(anss):
    li = sorted(anss)[0]
    ans = sorted([arr[li[1]], arr[li[2]], arr[li[3]]])
    print(*ans)
