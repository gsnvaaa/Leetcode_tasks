class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            value = True
            for char in word:
                if char not in allowed:
                    value = False
            if value:
                count += 1
        return count