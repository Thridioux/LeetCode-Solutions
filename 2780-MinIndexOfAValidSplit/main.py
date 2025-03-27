class Solution:
    def minimumIndex(self, nums):
        majority = 0
        count = 0
        
        for n in nums:
            if count == 0:
                majority = n
            if n ==  majority:
                count += 1
            else:
                count -= 1
                
        left_cnt = 0
        right_cnt = nums.count(majority)
        
        for i in range(len(nums)):
            if nums[i] == majority:
                left_cnt += 1
                right_cnt -= 1
                
            left_len = i + 1
            right_len = len(nums) - left_len
            
            if 2* left_cnt > left_len and 2 * right_cnt > right_len:
                return i
        return -1 
                