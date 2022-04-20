a, b = map(int, input().split())

eratos = [1] * (b + 1)
eratos[0], eratos[1] = 0, 0

for i in range(2, b + 1):
    if eratos[i] == 1:
        for j in range(i * 2, b + 1, i):
            eratos[j] = 0

for i in range(a, b + 1):
    if eratos[i]:
        print(i)
