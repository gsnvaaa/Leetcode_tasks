class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        word_counter = {}
        banned_words = set()
        normal_str = ''.join(char.lower() if char.isalnum() else ' ' for char in paragraph)
        
        for word in normal_str.split():
            if word not in banned:
                word_counter[word] = word_counter.get(word,0) + 1
                
        curr_max = 0
        max_word = ''
        
        for word in word_counter:
            if word_counter[word] > curr_max:
                curr_max = word_counter[word]
                max_word = word
                
        return max_word