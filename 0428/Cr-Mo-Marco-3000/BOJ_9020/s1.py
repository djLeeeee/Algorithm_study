from sys import stdin

T = int(stdin.readline().rstrip())

# 모든 소수
sosu = set()
sosu.add(2)
sosu.add(3)
sosu.add(5)
for i in range(7, 10001, 2):
    for j in range(i // 2, 2, -1):
        if not (i % j):
            break
    else:
        sosu.add(i)

for tc in range(1, T+1):
    a = int(stdin.readline().rstrip())
    for k in range(a//2, 1, -1):
        if k in sosu:
            b = a - k
            if b in sosu:
                print(f'{k} {b}')
                break
