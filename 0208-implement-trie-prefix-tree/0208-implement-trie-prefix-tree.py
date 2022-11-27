class Trie:
    class List:
        def __init__(self, val = None):
            self.val = val
            self.nexts = {}
            self.end = False

    def __init__(self):
        self.head = self.List()

    def insert(self, word: str) -> None:
        node = self.head
        for c in word:
            if c not in node.nexts:
                node.nexts[c] = self.List(c)
            node = node.nexts[c]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.head
        for c in word:
            if c not in node.nexts:
                return False
            node = node.nexts[c]
        return True if node.end else False

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for c in prefix:
            if c not in node.nexts:
                return False
            node = node.nexts[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)