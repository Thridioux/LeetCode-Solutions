class Solution:
    def minSwaps(self,nums):
        N = len(nums) #9
        total_ones = sum(nums)#5
        l = 0
        window_ones = max_window_ones  = 0
        for r in range(2*N):
            if nums[r%N] == 1: # if the element is 1, increment the window_ones
                window_ones += 1
            if r-l+1>total_ones:# if the window size is greater than total_ones, decrement the window_ones
                if nums[l%N] == 1:
                    window_ones -= 1
                l += 1
            max_window_ones = max(max_window_ones,window_ones)
        
        return total_ones-max_window_ones    
    
# [0,1,1,1,0,0,1,1,0] [0,1,1,1,0,0,1,1,0]