class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        if not word:
            return ""
        
        comp = []
        i = 0
        while i < len(word):
            count = 1
            while i + 1 < len(word) and word[i] == word[i + 1]:
                count += 1
                i += 1
            
            # Append in chunks if count > 9
            while count > 9:
                comp.append("9" + word[i])
                count -= 9
            
            # Append the remaining count and character
            comp.append(str(count) + word[i])
            i += 1
        
        # Join list into a single string for optimized performance
        return ''.join(comp)
    
# test cases
print(Solution().compressedString('aaaaaaaaaaabcde')) # 1a1b2c3d4e