class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        i,j = 0,0
        res = []
        
        while i < len(s) and j < len(spaces):
            if i < spaces[j]:
                res.append(s[i])
                i += 1
                
            else:
                res.append(" ")
                j += 1
                
        if i < len(s):
            res.append(s[i:])
        
        return ''.join(res)