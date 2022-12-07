from itertools import permutations

board = [list(input()) for _ in range(5)]
xy = [
    (0, 4), (1, 1), (1, 3), (1, 5), (1, 7), (2, 2),
    (2, 6), (3, 1), (3, 3), (3, 5), (3, 7), (4, 4)
]
empty = []
val = []
left = set(range(1, 13))
for i in range(12):
    x, y = xy[i]
    if board[x][y] == 'x':
        empty.append(i)
        val.append(0)
    else:
        v = ord(board[x][y]) - ord('A') + 1
        val.append(v)
        left.remove(v)
left = sorted(list(left))
l = len(left)
checker = [
    (0, 2, 5, 7), (0, 3, 6, 10), (7, 8, 9, 10),
    (1, 2, 3, 4), (1, 5, 8, 11), (4, 6, 9, 11)
]
for p in permutations(left):
    temp = val[:]
    for i in range(l):
        temp[empty[i]] = p[i]
    for c in checker:
        tot = 0
        for t in c:
            tot += temp[t]
        if tot != 26:
            break
    else:
        for i in range(12):
            x, y = xy[i]
            board[x][y] = chr(ord('A') + temp[i] - 1)
        for line in board:
            print(''.join(line))
        exit()
