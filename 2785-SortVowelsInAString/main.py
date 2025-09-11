from typing import List
class Solution:
    def sortVowels(self, s: str) -> str:
        # vowels must be sorted according to their ASCII values,and consanants must be in their original positions.
        vowels = sorted([c for c in s if c in 'aeiouAEIOU'])
        res = []
        for c in s:
            if c in 'aeiouAEIOU':
                res.append(vowels.pop(0))
            else:
                res.append(c)
        return ''.join(res)
    
        
        