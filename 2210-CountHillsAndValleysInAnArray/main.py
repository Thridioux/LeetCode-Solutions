from typing import List
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        # Remove consecutive duplicates
        nums = [nums[i] for i in range(n) if i == 0 or nums[i] != nums[i - 1]]
        
        # Count hills and valleys
        for i in range(1, len(nums) - 1):
            if (nums[i] > nums[i - 1] and nums[i] > nums[i + 1]) or (nums[i] < nums[i - 1] and nums[i] < nums[i + 1]):
                count += 1
        
        return count
        
        
        
        
        