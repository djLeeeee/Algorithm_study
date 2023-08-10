from sys import stdin

input = stdin.readline

tc = 0
while True:
    tc += 1
    line = input().strip()
    ans = 0
    left = 0
    for c in line:
        if c == '{':
            left += 1
        elif c == '}':
            if not left:
                left += 1
                ans += 1
            else:
                left -= 1
        elif c == '-':
            exit()
    print(f'{tc}. {ans + left // 2}')
