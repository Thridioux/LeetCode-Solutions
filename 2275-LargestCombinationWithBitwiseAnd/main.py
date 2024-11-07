class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        count = [0] * 32
        
        for n in candidates:
            i = 0
            while n > 0:
                count[i] += n & 1
                n >>= 1
                i += 1
        return max(count)