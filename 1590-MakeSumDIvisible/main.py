class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums)
        remain = total % p
        if remain == 0:
            return 0
        
        res = len(nums) 
        cur_sum = 0
        
        # map the prefix sum to last index and handle the case when prefix sum is 0
        remain_to_idx = {0: -1}
        
        for i,num in enumerate(nums):
            # remain + x = cur_sum
            cur_sum = (cur_sum + num) % p
            prefix = (cur_sum - remain + p) % p
            if prefix in remain_to_idx:
                lenght = i - remain_to_idx[prefix]
                res = min(res, lenght)
            remain_to_idx[cur_sum] = i
        
        return -1 if res == len(nums) else res
        