class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        #extract words from sentence
        words = sentence.split()
        
        #iterate through words
        for i in range(len(words)):
            #check if searchWord is a prefix of the word
            if words[i].startswith(searchWord):
                return i+1
        return -1
    