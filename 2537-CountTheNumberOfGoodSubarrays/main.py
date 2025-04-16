class Solution:
    def countGood(self, nums, k):
        from collections import defaultdict
        n = len(nums)
        left = 0
        current_pairs = 0
        ans = 0
        counts = defaultdict(int)
        
        for right in range(n):
            current_pairs += counts[nums[right]]
            counts[nums[right]] += 1
            
            #while the window is good to slide 
            while current_pairs >=k:
                ans += n - right
                counts[nums[left]] -= 1
                current_pairs -= counts[nums[left]]
                left += 1
            
        return ans
                
                