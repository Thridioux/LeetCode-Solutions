class Solution:
    def countSubarrays(self, nums, minK: int, maxK: int) -> int:
        valid_subarrays = 0
        invalid_idx = -1
        minK_idx = -1
        maxK_idx = -1

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                invalid_idx = i
            
            if nums[i] == minK:
                minK_idx = i
            if nums[i] == maxK:
                maxK_idx = i

            count = max(min(minK_idx, maxK_idx) - invalid_idx, 0)
            valid_subarrays += count

        return valid_subarrays