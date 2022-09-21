from sys import stdin

input = stdin.readline

N = 10 ** 6
n = int(N ** 0.5)

prime = [1] * (N + 1)
prime[0], prime[1] = 0, 0
for i in range(n + 1):
    if prime[i]:
        for j in range(3 * i, N + 1, 2 * i):
            prime[j] = 0

while True:
    a = int(input())
    if a == 0:
        break
    for i in range(3, a // 2 + 1, 2):
        if prime[i] and prime[a - i]:
            print(f'{a} = {i} + {a - i}')
            break
    else:
        print('Goldbach\'s conjecture is wrong.')
