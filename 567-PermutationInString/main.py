class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        # calculate the frequency of each character in s1
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1 # get the value of c if not found return 0
            
        # initialize the window
        left = 0
        right = 0
        count = 0
        
        while right < len(s2):
            # if the character is in s1
            if s2[right] in freq:
                freq[s2[right]] -= 1
                if freq[s2[right]] == 0:
                    count += 1
            
            # if the window size is greater than s1
            if right - left + 1 > len(s1):
                if s2[left] in freq:
                    if freq[s2[left]] == 0:
                        count -= 1
                    freq[s2[left]] += 1
                left += 1
            
            # if the window size is equal to s1
            if right - left + 1 == len(s1):
                if count == len(freq):
                    return True
            right += 1
        return False


