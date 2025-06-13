class Solution:
    def minimizeMax(self, nums, p: int) -> int:
        nums.sort()
        n = len(nums)
        
        def can_form_p_pairs(max_diff):
            count = 0
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2 # use this pair and skip next both elements
                else:
                    i += 1
            return count >= p
        
        left, right = 0, nums[-1] - nums[0]
        result = right
        while left <= right:
            mid = (left + right) // 2
            if can_form_p_pairs(mid):
                #this mid is a possible answer, try for even smaller one 
                result = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return result
        
        
        




        