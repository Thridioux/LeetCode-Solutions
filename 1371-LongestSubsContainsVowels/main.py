class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = {'a':1,
                  'e':2,
                  'i':4,
                  'o':8,
                  'u':16
        }
        
        res = 0
        mask = 0
        mask_to_idx = [-1] * 32
        
        for i,c in enumerate(s):
            mask = mask ^ vowels.get(c,0) # get function returns 0 if c is not in vowels
            if mask_to_idx[mask] != -1 or mask == 0: 
                lenght = i - mask_to_idx[mask] 
                res = max(res,lenght)
            else:
                mask_to_idx[mask] = i
        return res
    
