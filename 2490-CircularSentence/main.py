class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        for i in range(len(sentence)):
            if sentence[i] == ' ' and sentence[i-1] != sentence[i+1]:
                return False
        return sentence[0] == sentence[-1]
                
        # or another solution
        # w = sentence.split()
        # for i in range(len(w)):
        #     if w[i][0] != w[i][-1]:
        #         return False
        # return True