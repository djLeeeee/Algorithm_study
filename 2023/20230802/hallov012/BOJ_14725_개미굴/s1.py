import sys
sys.stdin = open('input.txt')

def tree_add(dic, data):
    if data[0] not in dic:
        dic[data[0]] = {}
    if len(data) > 1:
        tree_add(dic[data[0]], data[1:])

def tree_print(dic, depth):
    keys = sorted(dic.keys())
    for k in keys:
        print(space * depth + k)
        tree_print(dic[k], depth + 1)

input = sys.stdin.readline

N = int(input())
tree = {}
for _ in range(N):
    n, *foods = input().split()
    tree_add(tree, foods)

space = '--'
tree_print(tree, 0)


