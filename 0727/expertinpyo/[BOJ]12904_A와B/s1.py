S = input()
T = input()
ans = 0
while len(T) >= len(S):
    if T == S:
        ans = 1
        break
    last = T[-1]
    T = T[:len(T)-1]
    if last == 'B':
        T = T[::-1]


print(ans)
