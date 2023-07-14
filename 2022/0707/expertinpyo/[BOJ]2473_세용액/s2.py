N = int(input())
arr = list(map(int, input().split()))
inf = float('inf')
numbers = [inf] * N
mins = inf
for i in range(N):
    first = inf
    idx1 = -1
    for j in range(N):
        if i != j:
            cal = arr[i] + arr[j]
            if abs(first) > abs(cal):
                idx1 = j
                first = cal
    second = inf
    idx2 = -1
    for k in range(N):
        if k not in [i, idx1]:
            cal2 = first + arr[k]
            if abs(second) > abs(cal2):
                second = cal2
                idx2 = k
    if mins > abs(second):
        mins = abs(second)
        numbers[i] = numbers[idx1] = numbers[idx2] = mins
        if not mins:
            break

ans = min(numbers)
ans_list = []
for i in range(N):
    if len(ans_list) == 3:
        break
    if numbers[i] == ans:
        ans_list.append(arr[i])
print(*sorted(ans_list))
