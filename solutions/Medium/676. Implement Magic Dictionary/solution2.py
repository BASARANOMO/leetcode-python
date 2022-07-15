class Trie:
    def __init__(self):
        self.is_finished = False
        self.children = dict()


class MagicDictionary:
    def __init__(self):
        self.root = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            curr = self.root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = Trie()
                curr = curr.children[ch]
            curr.is_finished = True

    def search(self, searchWord: str) -> bool:
        def dfs(node: Trie, pos: int, modified: bool) -> bool:
            if pos == len(searchWord):
                return modified and node.is_finished

            ch = searchWord[pos]
            if ch in node.children:
                if dfs(node.children[ch], pos + 1, modified):
                    return True

            if not modified:
                for char_next in node.children:
                    if ch != char_next:
                        if dfs(node.children[char_next], pos + 1, True):
                            return True

            return False

        return dfs(self.root, 0, False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
