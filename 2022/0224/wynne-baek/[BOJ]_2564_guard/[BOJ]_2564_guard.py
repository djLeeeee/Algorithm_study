import sys
sys.stdin = open('input.txt')

def how_long(x1, y1, x2, y2):
    if x1 == 1:
        if x2 == 1:
            return abs(y1 - y2)
        if x2 == 2:
            return min((c + y1 + y2), ((2 * r) - y1 - y2 + c))
        if x2 == 3:
            return y1 + y2
        if x2 == 4:
            return y1 + r - y2
    if x1 == 2:
        if x2 == 1:
            return min((c + y1 + y2), ((2 * r) - y1 - y2 + c))
        if x2 == 2:
            return abs(y1 - y2)
        if x2 == 3:
            return c - y2 + y1
        if x2 == 4:
            return r + c - y1 - y2
    if x1 == 3:
        if x2 == 1:
            return y1 + y2
        if x2 == 2:
            return c - y1 + y2
        if x2 == 3:
            return abs(y1 - y2)
        if x2 == 4:
            return min((y1 + y2 + r), ((2 * c) + r - y1 - y2))
    if x1 == 4:
        if x2 == 1:
            return r + y1 - y2
        if x2 == 2:
            return c - y2 + r - y1
        if x2 == 3:
            return min((y1 + y2 + r), ((2 * c) + r - y1 - y2))
        if x2 == 4:
            return abs(y1 - y2)



r, c = map(int, input().split())
how_many = int(input())

store = []
for _ in range(how_many):
    x, y = map(int, input().split())
    store.append([x, y])
dx, dy = map(int, input().split())
result = 0
for spot in store:
    result += how_long(dx, dy, spot[0], spot[1])
print(result)

