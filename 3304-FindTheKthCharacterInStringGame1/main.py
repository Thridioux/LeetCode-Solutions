class Solution:
    def kthCharacter(self, k: int) -> str:
        # Start with the initial string "a"
        word = "a"
        
        # Keep generating new strings until we have at least k characters
        while len(word) < k:
            # Generate the next character version of the current word
            next_chars = ""
            for char in word:
                if char == 'z':
                    next_chars += 'a'  # z wraps around to a
                else:
                    next_chars += chr(ord(char) + 1)  # next character in alphabet
            
            # Append the generated string to the original word
            word += next_chars
        
        # Return the kth character (1-indexed, so we use k-1 for 0-indexed)
        return word[k - 1]

        