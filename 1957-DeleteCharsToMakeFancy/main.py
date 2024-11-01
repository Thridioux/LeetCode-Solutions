    class Solution(object):
        def makeFancyString(self, s):
            """
            :type s: str
            :rtype: str
            """
            # a fancy string is a string that has no 3 consecutive same characters
            
            streak = 1
            res = ''
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    streak += 1
                else:
                    streak = 1
                if streak < 3:
                    res += s[i-1]
                    
            res += s[-1] #add the last character
            return res    

#test cases
s = Solution()
print(s.makeFancyString("aab")) #leetcode    
       
        