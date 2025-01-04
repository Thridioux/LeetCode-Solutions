class Solution:
    def countPalindromicSubsequence(self, s):
        from collections import Counter
        res = set() # (mid_char, outer_char)
        left = set()
        right = Counter(s)# this creates a hash map counting the occurences of each character in the string
        
        for m in s: # for middle character
            right[m] -= 1
            
            for c in left:
                if right[c] > 0:
                    res.add((m, c))
            left.add(m)
            
        return len(res)
    