class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        prev_idx = {}
        cur_sum = 0
        
        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            
            i = prev_idx.get(nums[r], -1)
            
            while l<=i or r-l+1>k:
                cur_sum -= nums[l]
                l += 1
                
            if r-l+1==k:
                res = max(res, cur_sum)
                
            prev_idx[nums[r]] = r
            
        return res