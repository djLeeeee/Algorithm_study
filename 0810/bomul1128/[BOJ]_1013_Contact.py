from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    target = input()
    l = len(target) - 1
    p = 0
    ans = 'YES'
    while p < l:
        if target[p] == '0':
            p += 1
            if target[p] == '1':
                p += 1
            else:
                ans = 'NO'
                break
        else:
            ex = 0
            while target[p + ex + 1] == '0':
                ex += 1
            if ex < 2:
                ans = 'NO'
                break
            p += ex + 1
            if target[p] != '1':
                ans = 'NO'
                break
            else:
                while target[p] == '1':
                    p += 1
                if p + 1 < l and target[p + 1] == '0':
                    p -= 1
                    if target[p - 1] == '0':
                        ans = 'NO'
                        break
    print(ans)
