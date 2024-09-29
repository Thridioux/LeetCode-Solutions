class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        # Given a string n representing a number, we need to find the closest palindrome to n
        
        if n == '1':
            return '0'
        
        length = len(n)
        candidates = set()
        
        # Edge case for numbers like 10, 1000, etc.
        if int(n) <= 10 or (n[0] == '1' and set(n[1:]) == {'0'}):
            return str(int(n) - 1) 
        
        # Edge case for numbers like 99, 999, etc.
        if n == '9' * length:
            return str(int(n) + 2)
        
        # Generate palindrome candidates by modifying the prefix
        prefix = n[:(length + 1) // 2]  # For example, if n = "12345", prefix = "123"
        
        # Create all possible palindromes by adjusting the prefix
        for i in (-1, 0, 1):
            new_prefix = str(int(prefix) + i)  # Adjust the prefix by -1, 0, or +1
            # Create the palindrome by mirroring the prefix
            candidate = new_prefix + (new_prefix[:-1] if length % 2 else new_prefix)[::-1]
            candidates.add(candidate)
        
        candidates.discard(n)  # Remove the original number from the candidates
        
        # Add extreme edge case palindromes: "999...999" and "100...001"
        candidates.add(str(10**(length - 1) - 1))  # "999...999"
        candidates.add(str(10**length + 1))        # "100...001"
        
        # Find the closest palindrome
        def diff(candidate):
            return abs(int(candidate) - int(n)), int(candidate)
        
        return min(candidates, key=diff)

