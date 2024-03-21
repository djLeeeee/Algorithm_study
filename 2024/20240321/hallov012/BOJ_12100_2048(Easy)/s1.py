import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def move(arr, d):
    """
    0: 오른쪽
    1: 왼쪽
    2: 아래
    3: 위
    """
    new_arr = [[0] * n for _ in range(n)]
    if d == 0:
        for i in range(n):
            last = n-1
            new_arr[i][last] = arr[i][last]
            for j in range(n-2, -1, -1):
                if arr[i][j]:
                    val = arr[i][j]
                    if new_arr[i][last] == val:
                        new_arr[i][last] = val*2
                        last -= 1
                    else:
                        if new_arr[i][last]:
                            last -= 1
                        new_arr[i][last] = val
    elif d == 1:
        for i in range(n):
            last = 0
            new_arr[i][last] = arr[i][last]
            for j in range(1, n):
                if arr[i][j]:
                    val = arr[i][j]
                    if new_arr[i][last] == val:
                        new_arr[i][last] = val*2
                        last += 1
                    else:
                        if new_arr[i][last]:
                            last += 1
                        new_arr[i][last] = val

    elif d == 2:
        for j in range(n):
            last = n-1
            new_arr[last][j] = arr[last][j]
            for i in range(n-2, -1, -1):
                if arr[i][j]:
                    val = arr[i][j]
                    if new_arr[last][j] == val:
                        new_arr[last][j] = 2*val
                        last -= 1
                    else:
                        if new_arr[last][j]:
                            last -= 1
                        new_arr[last][j] = val
    else:
        for j in range(n):
            last = 0
            new_arr[last][j] = arr[last][j]
            for i in range(1, n):
                if arr[i][j]:
                    val = arr[i][j]
                    if new_arr[last][j] == val:
                        new_arr[last][j] = val*2
                        last += 1
                    else:
                        if new_arr[last][j]:
                            last += 1
                        new_arr[last][j] = val
    return new_arr

def find(arr, cnt):
    global ans
    if cnt == 5:
        for line in arr:
            ans = max(ans, max(line))
        return
    for d in range(4):
        tmp = move(arr, d)
        find(tmp, cnt+1)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
find(arr, 0)
print(ans)

