class Solution:
    def maximumDifference(self, nums) -> int:
        #find the max difference between increasing elements
        max_diff = -1
        min_value = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > min_value:
                max_diff = max(max_diff, nums[i] - min_value)
            else:
                min_value = nums[i]
        
        return max_diff if max_diff > 0 else -1
        