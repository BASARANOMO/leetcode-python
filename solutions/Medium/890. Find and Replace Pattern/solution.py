class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word: str, pattern: str) -> bool:
            mp = {}
            for x, y in zip(word, pattern):
                if x not in mp:
                    mp[x] = y
                elif mp[x] != y:
                    return False
            return True
        
        return [word for word in words if match(word, pattern) and match(pattern, word)]