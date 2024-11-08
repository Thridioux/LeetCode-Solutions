class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        xor = 0
        for n in nums:
            xor ^= n
            
        mask = (1 << maximumBit) - 1
        answer = []
        for n in reversed(nums):
            answer.append(mask ^ xor)
            xor ^= n
            
        return answer