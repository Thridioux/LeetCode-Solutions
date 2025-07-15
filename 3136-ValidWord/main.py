from typing import List
class Solution:
    def isValid(self, word: str) -> bool:
        # word is considered valid if it includes only digits and english letters
        # must include at least one vowel and one consonant
        
        vowels = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False
        if len(word) < 3:
            return False
        
        for char in word:
            if char.isdigit():
                continue
            if char.isalpha():
                if char in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
            else:
                return False
        return has_vowel and has_consonant
            