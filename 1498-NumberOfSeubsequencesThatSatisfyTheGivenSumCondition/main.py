class Solution:
    def numSubseq(self, nums, target: int) -> int:
        MOD = 10**9 + 7
        #return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element in each subsequence is less than or equal to target.
        # Precompute powers of 2 up to the length of nums
        nums.sort()
        left, right = 0, len(nums) - 1
        
        power_of_2 = [1] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            power_of_2[i] = (power_of_2[i - 1] * 2) % MOD
            
        count = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                count = (count + power_of_2[right - left]) % MOD
                left += 1
            else:
                right -= 1
        return count
    