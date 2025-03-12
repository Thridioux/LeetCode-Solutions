class Solution:
    def maximumCount(self, nums) -> int:
        neg = 0
        pos = 0
        for i in nums:
            if i < 0:
                neg += 1
            if i > 0:
                pos += 1
        return max(neg, pos)