class Solution:
    def countSubarrays(self, nums):
        n = len(nums)
        count = 0
        # count the number of subarrays of length 3
        # the condition is that sum of the first and last element is half of the middle element
        for i in range(1, n - 1):
            if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                count += 1
        return count
    
