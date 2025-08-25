import sys
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)

def insert(root, path):
    node = root
    for file in path:
        node = node.children[file]

def dfs(node, depth=0):
    for key in sorted(node.children):
        print(" " * depth + key)
        dfs(node.children[key], depth+1)

n = int(input())
root = TrieNode()
for _ in range(n):
    path = input().strip().split("\\")
    insert(root, path)

dfs(root)