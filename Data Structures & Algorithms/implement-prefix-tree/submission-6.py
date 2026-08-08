class Node:

    def __init__(self, is_end):
        self.is_end = is_end
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = Node(False)

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                child = Node(False)
                curr.children[char] = child
            curr = curr.children[char]
        
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return True
        