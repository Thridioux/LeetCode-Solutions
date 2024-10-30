class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        lis = [1] * N # Longest increasing subsequence,init with 1
        for i in range(N): # From left to right
            for j in range(i):  # From left to right
                if nums[j] < nums[i]: # Increasing
                    lis[i] = max(lis[i], lis[j] + 1) # Update lis[i]
                    
        lds = [1] * N # Longest decreasing subsequence,init with 1
        
        for i in reversed(range(N)): # From right to left
            for j in range(i+1, N): # From right to left
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], lds[j] + 1)
        
        res = N           
        for i in range(1, N-1): # go through all possible pivots
            if lis[i] > 1 and lds[i] > 1:
                res = min(res, N - lis[i] - lds[i] + 1)
            
        return res