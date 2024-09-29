class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # target = max(nums)
        # size,res =0,0
        # for n in nums:
        #     if n == target:
        #         size +=1
        #     else:
        #         size = 0
        #     res = max(res,size)
        # return res
        
        
        
        #1. if n < cur_max, n & cur_max < cur_max 
        #2. if n == cur_max, n & cur_max == cur_max
        #3. if n > cur_max, n & cur_max < cur_max
        
        size,res = 0,0
        cur_max = 0
        for n in nums:
            if n > cur_max:
                cur_max = n
                size = 1
                res = 0
            elif n == cur_max:
                size +=1
            else:
                size = 0
            res = max(res,size)
        return res 
    
#testcases 
nums = [1,2,3,4]
sol = Solution()
print(sol.longestSubarray(nums)) 
