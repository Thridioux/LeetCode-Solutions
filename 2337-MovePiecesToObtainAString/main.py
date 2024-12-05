class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        n = len(start)
        i, j = 0, 0
        
        while i < n or j < n:
            # Skip underscores in both strings
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1

            # Check if we've reached the end of both strings
            if i == n and j == n:
                return True
            if i == n or j == n:
                return False
            
            # Characters must match
            if start[i] != target[j]:
                return False

            # Movement rules for 'L' and 'R'
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            
            i += 1
            j += 1
        
        return True
