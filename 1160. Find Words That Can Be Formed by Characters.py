class Solution(object):
    def countCharacters(self, words, chars):
        counts = [0] * 26

        for ch in chars:
            counts[ord(ch) - ord('a')] += 1

        result = 0

        for word in words:
            if self.canForm(word, counts):
                result += len(word)

        return result

    def canForm(self, word, counts):
        c = [0] * 26
        for ch in word:
            x = ord(ch) - ord('a')
            c[x] += 1
            if c[x] > counts[x]:
                return False

        return True