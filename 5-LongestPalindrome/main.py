class Solution:
    def LongestPalindrome(self,s):
        #Logic
        # start from the center and expand outwards
        # but we have a one edge case where the center is between two characters because "aa" is also a palindromic string  
        # so we need to check for that edge case

        res = ''
        resLen = 0 #max length of the palindromic string
        
        for i in range(len(s)):
            #odd length
            l,r = i,i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r -l+1
                l -= 1
                r += 1
            #even length

            l,r = i,i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r -l+1
                l -= 1
                r += 1

        return res

