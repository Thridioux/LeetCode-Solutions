class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        def binary_search(l, r, target):
            # Return largest i,where nums[i] < target  
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            return r
            
        
        nums.sort()
        res = 0
        
        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]
            
            res +=(
                binary_search(i+1, len(nums)-1, up + 1) - binary_search(i+1, len(nums)-1, low)
            )
        
        return res