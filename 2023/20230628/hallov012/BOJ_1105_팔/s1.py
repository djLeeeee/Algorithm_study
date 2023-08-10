import sys
sys.stdin = open('input.txt')

l, r = map(str, input().split())
if len(l) != len(r):
    print(0)
else:
    ans = 0
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == '8':
                ans += 1
        else:
            break
    print(ans)