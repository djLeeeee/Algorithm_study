N = int(input())
arr = list(map(int, input().split()))
inf = float('inf')
numbers = [inf] * N
mins = inf
for i in range(N):
    for j in range(N):
        for k in range(N):
            if numbers[i] == numbers[j] == numbers[k] and numbers[i] != inf:
                continue
            elif i != j and j != k and k != i:
                cal = arr[i] + arr[j] + arr[k]
                if abs(mins) > abs(cal):
                    mins = cal
                    numbers[i] = numbers[j] = numbers[k] = abs(mins)
ans = min(numbers)
ans_list = []
for i in range(N):
    if len(ans_list) == 3:
        break
    if numbers[i] == ans:
        ans_list.append(arr[i])
print(*sorted(ans_list))
