for _ in range(int(input())):
    order = input()
    num = int(input())
    a = input()
    if num == 0:
        if 'D' in order:
            print('error')
        else:
            print('[]')
        continue
    my_list = list(map(int, a[1:-1].split(',')))
    init = 0
    end = num
    rev = False
    for i in order:
        if i == 'D':
            if rev:
                end -= 1
            else:
                init += 1
        else:
            rev = not rev
    if init <= end:
        result = list(reversed(my_list[init:end])) if rev else my_list[init:end]
        print('[', end='')
        print(*result, sep=',', end='')
        print(']')
    else:
        print('error')
