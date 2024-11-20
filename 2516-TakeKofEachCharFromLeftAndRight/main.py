class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #total counts
        count =[0,0,0]
        for c in s:
            count[ord(c)-ord('a')] += 1
            
        if min(count)<k:
            return -1
        
        #siliding window
        res = float('inf')
        l = 0
        for r in range(len(s)):
            count[ord(s[r])-ord('a')] -= 1
            
            while min(count)<k:
                count[ord(s[l])-ord('a')] += 1
                l += 1
                
            res = min(res, len(s) - (r-l+1))
            
        return res
                
                
        