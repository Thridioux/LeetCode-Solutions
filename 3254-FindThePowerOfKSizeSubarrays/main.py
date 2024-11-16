class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        l = 0 
        consec_count = 1
        for r in range(len(nums)):
            if r>0 and nums[r-1] + 1 == nums[r]:
                consec_count += 1 
            
            if r - l + 1> k:
                if nums[l] + 1 == nums[l+1]:
                    consec_count -= 1
                l += 1
            
            if r - l + 1 == k:
                res.append(nums[r] if consec_count == k else -1)
            
        return res
    
                
                
                