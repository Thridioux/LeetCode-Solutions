class Solution:
    def countCompleteSubarrays(self, nums):
        from collections import Counter 
        n = len(nums)
        total_distinct = len(set(nums))
        count = 0
        left = 0
        window_counts = Counter()
        
        #sliding window
        for right in range(n):
            window_counts[nums[right]] += 1
            
            while len(window_counts) == total_distinct:
                #all subarrays starting from left to right are complete
                #or later are complete There are (n - right) such subarrays
                count += n - right
                #shrink the window from the left
                window_counts[nums[left]] -= 1
                #if count becomes 0, remove from the element key
                if window_counts[nums[left]] == 0:
                    del window_counts[nums[left]]
                    
                left += 1
        return count
            
        