# https://www.acmicpc.net/problem/1991

import sys
sys.stdin = open("1991.txt")
input = sys.stdin.readline


def preorder(n):
    if n:
        sol.append(chr(n + 64))
        preorder(c1[n])
        preorder(c2[n])


def inorder(n):
    if n:
        inorder(c1[n])
        sol.append(chr(n + 64))
        inorder(c2[n])


def postorder(n):
    if n:
        postorder(c1[n])
        postorder(c2[n])
        sol.append(chr(n + 64))


N = int(input())
c1 = [0] * (N + 1)
c2 = [0] * (N + 1)
for _ in range(N):
    p, *data = [ord(x) - 64 if x.isalpha() else 0 for x in input().split()]
    c1[p], c2[p] = data

sol = []
preorder(1)
print(''.join(sol))

sol = []
inorder(1)
print(''.join(sol))

sol = []
postorder(1)
print(''.join(sol))
