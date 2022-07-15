class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.as_prefix = 0
        self.as_word = 0

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            ord_char = ord(char) - ord("a")
            if not node.children[ord_char]:
                node.children[ord_char] = Trie()
            node = node.children[ord_char]
            node.as_prefix += 1
        node.as_word += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self
        for char in word:
            ord_char = ord(char) - ord("a")
            if node.children[ord_char] == None:
                return 0
            else:
                node = node.children[ord_char]
        return node.as_word

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self
        for char in prefix:
            ord_char = ord(char) - ord("a")
            if node.children[ord_char] == None:
                return 0
            else:
                node = node.children[ord_char]
        return node.as_prefix

    def erase(self, word: str) -> None:
        node = self
        for char in word:
            ord_char = ord(char) - ord("a")
            if node.children[ord_char] == None:
                return
            else:
                node = node.children[ord_char]
                node.as_prefix -= 1
        node.as_word -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
