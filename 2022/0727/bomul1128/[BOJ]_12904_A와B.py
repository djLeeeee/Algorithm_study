s = input()
t = input()
for _ in range(len(t) - len(s)):
    if t[-1] == 'B':
        t = t[:-1][::-1]
    else:
        t = t[:-1]
print(int(s == t))
