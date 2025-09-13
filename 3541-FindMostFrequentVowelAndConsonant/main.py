from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        # find the most frequent vowel and consonant in the string return their sum of frequencies
        vowels = 'aeiou'
        freq = Counter(s)
        max_vowel_freq = 0
        max_consonant_freq = 0
        for char, count in freq.items():
            if char in vowels:
                max_vowel_freq = max(max_vowel_freq, count)
            else:
                max_consonant_freq = max(max_consonant_freq, count)
        return max_vowel_freq + max_consonant_freq
        
        
        