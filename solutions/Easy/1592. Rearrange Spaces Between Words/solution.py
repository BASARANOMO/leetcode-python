class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        space_cnt = text.count(" ")
        if len(words) == 1:
            return words[0] + " " * space_cnt
        per_space, rest_space = divmod(space_cnt, len(words) - 1)
        return (' ' * per_space).join(words) + ' ' * rest_space
        