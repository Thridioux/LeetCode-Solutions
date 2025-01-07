class Solution:
    def stringMatching(self, words):
        res = []
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                
                if words[i] in words[j]:
                    res.append(words[i])
                    break
                
        return res
        