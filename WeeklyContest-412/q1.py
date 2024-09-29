class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        
        # nums is the list of integers, k is the integer of the operation count , multiplier is the intger
        # find the min value x in nums with first apperance, replace the x with x*multiplier
        # repeat k times, return the final state of nums
        
        for i in range(k):
            min_index = nums.index(min(nums))
            nums[min_index] = nums[min_index]*multiplier
            
        return nums
    
#test case
nums = [1,2]
k = 3
multiplier = 4
sol = Solution()
print(sol.getFinalState(nums, k, multiplier)) 
    