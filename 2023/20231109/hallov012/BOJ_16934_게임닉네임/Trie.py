class Node(object):
    """
    key: 값으로 입력될 문자
    data: 문자의 종료를 알리는 flag
    children: 자식 노드
    """
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    """
    head를 빈 노드로 설정
    """
    def __init__(self):
        self.head = Node(None)

    """
    입력된 문자열의 문자 하나씩 children에 확인 후 저장
    문자열을 다 돌면 마지막 노드의 data에 문자열을 저장 
    """
    def insert(self, string):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    """
    문자열이 존재 여부를 리턴
    문자열을 하나씩 돌면서 확인 후, 마지막 노드에 data가 존재하면 True
    그렇지 않거나, 애초에 children이 존재하지 않다면 False
    """
    def search(self, string):
        current_node = self.head
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        if current_node.data:
            return True
        else:
            return False

    """
    prefix 단어로 시작하는 단어를 찾고 배열로 return
    prefix 단어까지 tree를 순회 후, 그 다움부터 data가 존재하는 것들만 배열에 저장해 return
    """
    def starts_with(self, prefix):
        current_node = self.head
        words = []
        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None
        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node):
                current_node = next_node
                next_node = []
            else:
                break
        return words