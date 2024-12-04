class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        i = 0  # Pointer for str1
        j = 0  # Pointer for str2
        
        while i < len(str1) and j < len(str2):
            # Check if current characters match or if str1[i] can cyclically become str2[j]
            if str1[i] == str2[j] or (ord(str1[i]) - ord('a') + 1) % 26 == ord(str2[j]) - ord('a'):
                j += 1  # Move str2 pointer if there's a match
            i += 1  # Always move str1 pointer
        
        # If we've matched all characters of str2, return True
        return j == len(str2)
