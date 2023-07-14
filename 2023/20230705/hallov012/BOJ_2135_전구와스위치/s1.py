import sys
sys.stdin = open('input.txt')

def change():
    temp = now[:]
    cnt = 0
    for i in range(1, n):
        if temp[i-1] == target[i-1]:
            continue
        else:
            cnt += 1
            for j in range(i-1, i+2):
                if j < n:
                    temp[j] = 1 - temp[j]
    if temp == target:
        return cnt
    else:
        return sys.maxsize

n = int(input())
now = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))


# 두번째 버튼부터 누른 경우
ans = change()

# 첫번째 버튼부터 누른 경우
now[0] = 1 - now[0]
now[1] = 1 - now[1]
ans = min(ans, change()+1)

print(ans if ans != sys.maxsize else -1)



