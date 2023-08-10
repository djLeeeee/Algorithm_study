expr = input().split('-')
ans = 0
for i in expr[0].split('+'):
    ans += int(i)
for j in expr[1:]:
    x = 0
    for k in j.split('+'):
        x += int(k)
    ans -= x
print(ans)
