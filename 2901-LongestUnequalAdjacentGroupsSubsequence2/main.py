class Solution:
    def getWordsInLongestSubsequence(self,words,groups):
        n = len(groups)
        dp =[]
        for x in words:
            dp.append([x])
        
        def hamming(a, b):
            n = len(a)
            count = 0
            for i in range(n):
                if a[i] != b[i]:
                    count += 1
                if count > 1:return False
            return count == 1
        
        max = 1
        res = [words[0]]
        
        for j in range(n):
            for i in range(0,j):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and hamming(words[i], words[j]) and len(dp[j]) < len(dp[i]) + 1:
                    dp[j] = dp[i] + [words[j]]
                    if len(dp[j]) > max:
                        max = len(dp[j])
                        res = dp[j]
        return res
        