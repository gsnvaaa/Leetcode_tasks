class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        m_dict = {}
        for c in magazine:
            if c not in m_dict:
                m_dict[c] = 1
            else:
                m_dict[c] += 1
        
        for ch in ransomNote:
            if ch not in m_dict or m_dict[ch] == 0:
                return False
            else:
                m_dict[ch] -= 1
        return True