class Solution:
    def longestNiceSubarray(self, nums):
        res = 0
        cur = 0 # bitmask
        l = 0 
        for r in range(len(nums)):
            while cur & nums[r]:
                cur ^= nums[l] #unset bit
                l += 1
            res = max(res, r - l + 1)
            cur |= nums[r]
        return res
            
        
        