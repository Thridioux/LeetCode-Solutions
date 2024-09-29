class Solution(object):
    def minimumPushes(self, word):
        # Initialize a dictionary to store the frequency of each letter
        # word = "aabbccddeeffgghhiiiiii"
        freq = {}
        for char in word:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        # freq = {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 6}
        # Sort the frequencies in descending order
        sorted_freqs = sorted(freq.values(), reverse=True)
        # sorted_freqs = [6, 2, 2, 2, 2, 2, 2, 2, 2]

        
        # Calculate the minimum number of pushes needed
        min_pushes = 0
        for i, f in enumerate(sorted_freqs):
            # Each group of 8 characters will require 1 more push
            min_pushes += (i // 8 + 1) * f
            
        return min_pushes
