class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections
        res = float('inf')
        cur_sum = 0 
        q = collections.deque() # (prefix_sum, index)
        
        for r in range(len(nums)):
            cur_sum += nums[r]
            if cur_sum >= k:
                res = min(res, r+1)
                
            #find the minimum valid window ending at r
            while q and cur_sum - q[0][0] >= k:
                prefix, end_idx = q.popleft()
                res = min(res, r - end_idx)
                
            #validate the monotonic deque
            while q and q[-1][0] > cur_sum:
                q.pop()
            q.append((cur_sum, r))
            
        return res if res != float('inf') else -1
    
