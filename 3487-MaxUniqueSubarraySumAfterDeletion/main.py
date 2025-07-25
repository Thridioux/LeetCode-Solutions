from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        #if the maximum element in the array is negative,the answer is the maximum element
        if max(nums) < 0:
            return max(nums)
        
        #otherwise the answer is the sum of all unique elements that are greater than or equal to zero
        unique_nums = set(nums)
        return sum(num for num in unique_nums if num >= 0)
    
    

