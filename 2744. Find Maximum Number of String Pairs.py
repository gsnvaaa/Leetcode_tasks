class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        word_dict = {}
        pairs = 0
        for word in words:
            reversed_word = word[::-1]
            if reversed_word in word_dict:
                word_dict.pop(reversed_word)
                pairs += 1
            else:
                word_dict[word] = 1
        return pairs