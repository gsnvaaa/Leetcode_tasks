class Solution(object):
    def checkIfPangram(self, sentence):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        mySentence = list(set(sentence))
        mySentence.sort()
        return "".join(mySentence) == alphabet