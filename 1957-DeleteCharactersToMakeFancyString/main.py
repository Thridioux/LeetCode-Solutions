from typing import List, Dict
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        count = 0
        prev_char = ''
        for char in s:
            if char == prev_char:
                count += 1
            else:
                count = 1
                prev_char = char
            
            if count < 3:
                res.append(char)
        
        return ''.join(res)
        
        
        
        