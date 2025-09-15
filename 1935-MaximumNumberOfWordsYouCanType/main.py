from collections import defaultdict
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # return the number of words that can be typed using the keyboard 
        broken = set(brokenLetters)
        words = text.split()
        count = 0
        for word in words:
            if not any(char in broken for char in word):
                count += 1
        return count
        
        
        
        
        
        
        
        
        
        
        