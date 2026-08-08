class TrieNode:

    def __init__(self, is_end):
        self.is_end = is_end
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(False)

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                new_node = TrieNode(False)
                curr.children[ch] = new_node

            curr = curr.children[ch]
        
        curr.is_end = True
        

    def search(self, word: str) -> bool:

        def dfs(i, curr):
            if i == len(word):
                return curr.is_end

            ch = word[i]
            if ch != '.':
                if ch not in curr.children:
                    return False
                return dfs(i + 1, curr.children[ch])
            else:
                res = False
                for child in curr.children.values():
                    res = res or dfs(i + 1, child)
                return res
        
        return dfs(0, self.root)