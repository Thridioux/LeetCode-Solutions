class Solution:
    def countSubarrays(self, nums, k: int) -> int:
        N = len(nums)
        total = 0
        left = 0
        ans = 0
        for right in range(N):
            total += nums[right]
            
            while total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            ans += right - left + 1
        return ans
        
        