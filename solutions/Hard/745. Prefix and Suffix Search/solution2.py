class Trie:
    def __init__(self):
        self.children = dict()
        self.indices = []


class WordFilter:
    def __init__(self, words: List[str]):
        self.prefix_trie_root = Trie()
        self.suffix_trie_root = Trie()
        for i, word in enumerate(words):
            curr = self.prefix_trie_root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = Trie()
                curr = curr.children[ch]
                curr.indices.append(i)
            curr = self.suffix_trie_root
            for ch in word[::-1]:
                if ch not in curr.children:
                    curr.children[ch] = Trie()
                curr = curr.children[ch]
                curr.indices.append(i)

    def f(self, pref: str, suff: str) -> int:
        pref_indices_list = self.search(self.prefix_trie_root, pref, True)
        suff_indices_list = self.search(self.suffix_trie_root, suff, False)
        # Two pointers
        i, j = len(pref_indices_list) - 1, len(suff_indices_list) - 1
        while i >= 0 and j >= 0:
            if pref_indices_list[i] == suff_indices_list[j]:
                return pref_indices_list[i]
            elif pref_indices_list[i] > suff_indices_list[j]:
                i -= 1
            else:
                j -= 1
        return -1

    def search(self, root: Trie, s: str, is_prefix: bool) -> List[int]:
        curr = root
        if not is_prefix:
            s = s[::-1]
        for ch in s:
            if ch not in curr.children:
                return []
            curr = curr.children[ch]
        return curr.indices


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
