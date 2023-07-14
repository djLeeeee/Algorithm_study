s = input()
ans = []
ppap = list("PPAP")
for c in s:
    ans.append(c)
    if ans[-4:] == ppap:
        for _ in range(3):
            ans.pop()
print('PPAP' if ans == ['P'] else 'NP')
