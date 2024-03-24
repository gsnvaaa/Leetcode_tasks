class Solution(object):
    def isAnagram(self, s, t):
       dict_value = {}

       for letter in s:
           if letter not in dict_value:
              dict_value[letter] = 1
           else:
                dict_value[letter] += 1
        
       for letter in t:
            if letter not in dict_value:
                return False
            else:
                dict_value[letter] -= 1

       for value in dict_value.values():
            if value != 0:
                return False
       return True