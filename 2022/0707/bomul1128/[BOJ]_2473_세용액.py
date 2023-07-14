n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

combination = abs(sum(liquid[:3]))
result = [0, 1, 2]

for i in range(n - 2):
    x = i + 1
    y = n - 1
    while x != y:
        my_sum = liquid[i] + liquid[x] + liquid[y]
        if abs(my_sum) < combination:
            result = [i, x, y]
            combination = abs(my_sum)
        if my_sum < 0:
            x += 1
        elif my_sum > 0:
            y -= 1
        else:
            break
print(*[liquid[j] for j in result])
