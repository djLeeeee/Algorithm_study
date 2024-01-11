import sys
from collections import defaultdict
sys.stdin = open('input.txt')

class Node:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, string):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node = current_node.children[char]
        nickname_dict[string] += 1
        current_node.word = True

    def search(self, string):
        current_node = self.head
        saved_nick = ''
        for char in string:
            saved_nick += char
            if char not in current_node.children:
                return saved_nick
            current_node = current_node.children[char]
        if current_node.word:
            saved_nick += str(nickname_dict[saved_nick]+1)
        return saved_nick


n = int(input())
nickname_dict = defaultdict(int)
trie = Trie()
for _ in range(n):
    nickname = input().rstrip()
    print(trie.search(nickname))
    trie.insert(nickname)

