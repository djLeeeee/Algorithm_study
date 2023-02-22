from sys import stdin

input = stdin.readline

n = int(input())
leaf = {}
for _ in range(n):
    x, y, z = input().split()
    leaf[x] = (y, z)


def front(start):
    if start == '.':
        return ''
    return start + front(leaf[start][0]) + front(leaf[start][1])


def middle(start):
    if start == '.':
        return ''
    return middle(leaf[start][0]) + start + middle(leaf[start][1])


def back(start):
    if start == '.':
        return ''
    return back(leaf[start][0]) + back(leaf[start][1]) + start


print(front('A'))
print(middle('A'))
print(back('A'))
