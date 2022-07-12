class Trie:

    def __init__(self):
        self.is_finished = False
        self.children = [None] * 26

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            ord_char = ord(char) - ord("a")
            if not node.children[ord_char]:
                node.children[ord_char] = Trie()
            node = node.children[ord_char]
        node.is_finished = True

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for char in prefix:
            ord_char = ord(char) - ord("a")
            if not node.children[ord_char]:
                return None
            node = node.children[ord_char]
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.is_finished

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)