class Solution(object):
    def isIsomorphic(self, s, t):
       d = {}
       for indx in range(len(s)):
           char1, char2 = s[indx], t[indx]
           if char1 not in d:
              if char2 not in d.values():
                 return False
              d[char1] = char2
           elif d[char1] != char2:
                 return False
       return True