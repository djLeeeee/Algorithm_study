while True:
    try:
        X = int(input()) * 10 ** 7
        N = int(input())
        distance = [int(input()) for _ in range(N)]
        distance.sort()
        left = 0
        right = N - 1
        l1 = l2 = -1
        while left < right:
            if distance[left] + distance[right] > X:
                right -= 1
            elif distance[left] + distance[right] < X:
                left += 1
            else:
                l1, l2 = distance[left], distance[right]
                break

        if l1 + l2 == X:
            print(f'yes {l1} {l2}')
        else:
            print('danger')
    except:
        break