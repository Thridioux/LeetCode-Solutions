class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_cnt = 0
        res = 0
        
        for c in s:
            if c == '(':
                open_cnt += 1
            else:
                if open_cnt > 0:
                    open_cnt -= 1
                else:
                    res += 1 
                    
        return res + open_cnt
    
#test the solution
s = Solution()
print(s.minAddToMakeValid("())")) #1
print(s.minAddToMakeValid("(((")) #3
print(s.minAddToMakeValid("()")) #0
        