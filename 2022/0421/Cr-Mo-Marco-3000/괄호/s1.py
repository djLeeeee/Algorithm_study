import sys
T = int(sys.stdin.readline().rstrip())

for tc in range(1, T+1):
    g = tuple(map(str, sys.stdin.readline().rstrip()))
    G = len(g)
    stack = 0
    for i in range(G):
        if stack:
            if g[i] == '(':
                stack += 1
            else:
                stack -= 1
        else:
            if g[i] == ')':
                print('NO')
                break
            else:
                stack += 1
    else:
        if stack:
            print('NO')
        else:
            print('YES')




