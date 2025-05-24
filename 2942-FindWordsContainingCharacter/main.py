class Solution:
    def findWordsContaining(self, words, x):
        ans = []
        #returns words index if it contains x
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
        return ans
    
        