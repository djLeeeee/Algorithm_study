from sys import stdin

input = stdin.readline

N = 10000
eratos = [1] * (N + 1)
eratos[0], eratos[1] = 0, 0

for i in range(2, 101):
    if eratos[i] == 1:
        for j in range(i * 2, N, i):
            eratos[j] = 0

for i in range(int(input())):
    a = int(input())
    b = a // 2
    while True:
        if eratos[b] * eratos[a - b]:
            print(b, a - b)
            break
        elif b % 2:
            b -= 2
        else:
            b -= 1
