import sys
sys.stdin = open('input.txt')

def preOrder(root):
    if root != '.':
        print(root, end='')
        preOrder(tree[root][0])
        preOrder(tree[root][1])

def inOrder(root):
    if root != '.':
        inOrder(tree[root][0])
        print(root, end='')
        inOrder(tree[root][1])

def postOrder(root):
    if root != '.':
        postOrder(tree[root][0])
        postOrder(tree[root][1])
        print(root, end='')

input = sys.stdin.readline

n = int(input())
tree = {}
for _ in range(n):
    a, b, c = map(str, input().split())
    tree[a] = [b, c]

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')